"""Optional local preprocessing. Originals remain outside dist and Git history.

Produces watermarked raster reading copies, never PDFs/XLSX or cell data exports.
Normal site builds use the already prepared images and need no private sources.
"""
from pathlib import Path
from tempfile import TemporaryDirectory
import datetime, json, re, shutil, subprocess
from PIL import Image, ImageDraw, ImageFont
from pypdf import PdfReader
from openpyxl import load_workbook
from openpyxl.utils import get_column_letter

ROOT = Path(__file__).resolve().parents[1]
PRIVATE = ROOT / 'private-sources'
OUT = PRIVATE / 'readers'
FONT = '/System/Library/Fonts/Supplemental/Arial Unicode.ttf'

def font(size):
    return ImageFont.truetype(FONT, size)

def watermark(image):
    original = image.convert('RGBA')
    # Append a footer instead of covering the original report's bottom edge.
    image = Image.new('RGBA', (original.width, original.height+37), 'white')
    image.alpha_composite(original)
    layer = Image.new('RGBA', image.size)
    tile = Image.new('RGBA', (600, 180))
    draw = ImageDraw.Draw(tile)
    draw.text((20, 48), '谢欣玥 Xinyue Xie · 仅供阅读', font=font(27), fill=(66, 69, 85, 44))
    draw.text((22, 88), 'PERSONAL PORTFOLIO / READ ONLY', font=font(17), fill=(66, 69, 85, 44))
    tile = tile.rotate(24, expand=True)
    for y in range(-120, image.height, 310):
        for x in range(-220, image.width, 570):
            layer.alpha_composite(tile, (x, y))
    image = Image.alpha_composite(image, layer)
    draw = ImageDraw.Draw(image)
    draw.rectangle((0, image.height-37, image.width, image.height), fill=(242, 244, 236, 245))
    draw.text((20, image.height-29), '© Xinyue Xie / 谢欣玥 · 仅供阅读 / READ ONLY', font=font(18), fill='#68745c')
    return image.convert('RGB')

def save(image, path):
    image = watermark(image)
    image.save(path, 'WEBP', quality=88, method=6)
    return {'src': '/assets/readers/'+path.name, 'width': image.width, 'height': image.height}

def render_pdf(key, source):
    count = len(PdfReader(source).pages)
    pages = []
    with TemporaryDirectory(prefix='portfolio-readers-') as temp:
        # Raster only; no new PDF is authored or shipped.
        subprocess.run(['pdftoppm', '-r', '140', '-png', str(source), str(Path(temp)/'page')], check=True, stdout=subprocess.DEVNULL)
        raw = sorted(Path(temp).glob('page-*.png'), key=lambda f: int(f.stem.split('-')[-1]))
        assert len(raw) == count
        for i, path in enumerate(raw, 1):
            with Image.open(path) as image:
                pages.append(save(image, OUT/f'{key}-{i:03}.webp'))
    return {'pages': pages, 'page_count': count}

def display(cell):
    value = cell.value
    if value is None: return ''
    if isinstance(value, (datetime.datetime, datetime.date)): return value.strftime('%Y-%m-%d')
    if isinstance(value, bool): return str(value)
    if not isinstance(value, (int, float)): return str(value)
    sections = cell.number_format.split(';')
    index = 1 if value < 0 and len(sections)>1 else 2 if value == 0 and len(sections)>2 else 0
    fmt = re.sub(r'\[[^]]*\]', '', sections[index]).replace('\\','')
    if fmt == 'General': return str(value) if isinstance(value,int) else f'{value:.12g}'
    if not re.search(r'[0#]',fmt):return fmt.replace('"','').strip()
    magnitude = abs(value) if index==1 else value
    match = re.search(r'\.([0#]+)',fmt);places=len(match.group(1)) if match else 0
    result = format(magnitude, (',' if ',' in fmt else '')+'.'+str(places)+('f' if '%' not in fmt else '%'))
    literals = re.findall(r'"([^"]*)"',fmt)
    if literals:result+=''.join(literals)
    if '(' in fmt and ')' in fmt:result='('+result+')'
    elif fmt.startswith('+'):result='+'+result
    elif index==1 and fmt.startswith('-'):result='-'+result
    return result

def wrap(value, width, face):
    lines = []
    for paragraph in value.split('\n'):
        line = ''
        for char in paragraph:
            if line and face.getlength(line+char) > width:
                lines.append(line); line = ''
            line += char
        lines.append(line)
    return lines

def render_model(source):
    values = load_workbook(source, data_only=True)
    formulas = load_workbook(source, data_only=False)
    sheets = []
    for si, sheet in enumerate(values):
        original = formulas[sheet.title]
        rows = [r for r in range(1, sheet.max_row+1) if any(original.cell(r,c).value is not None for c in range(1, sheet.max_column+1))]
        columns = [c for c in range(1, sheet.max_column+1) if any(original.cell(r,c).value is not None for r in rows)]
        pages = []; accounted = set()
        groups = [[columns[0]]+columns[start:start+7] for start in range(1,len(columns),7)] or [columns]
        for start in range(0, len(rows), 26):
            block = rows[start:start+26]
            for gi, cols in enumerate(groups):
                widths = [440]+[185]*(len(cols)-1)
                face = font(19); small = font(17)
                layouts = []; heights = []
                for r in block:
                    cells = [wrap(display(sheet.cell(r,c)), width-24, face) for c,width in zip(cols,widths)]
                    heights.append(max(38, max(map(len,cells))*27+20))
                    layouts.append(cells)
                    accounted.update((r,c) for c in cols if original.cell(r,c).value is not None)
                width = sum(widths)+80; height = sum(heights)+190
                image = Image.new('RGB', (width,height), '#fafbf6'); d = ImageDraw.Draw(image)
                d.rectangle((0,0,width,92), fill='#24372e')
                d.text((26,19), 'SANXIE MOTOR / MODEL READING COPY', font=font(21), fill='#d8e6c3')
                d.text((26,52), sheet.title, font=font(19), fill='#e5dcef')
                y = 132; x = 66
                for c,w in zip(cols,widths):
                    d.text((x+12,103), get_column_letter(c), font=small, fill='#78856e'); x += w
                for r,cells,h in zip(block,layouts,heights):
                    x=66
                    d.text((9,y+10), str(r), font=small, fill='#88947b')
                    for w,ls in zip(widths,cells):
                        d.rectangle((x,y,x+w,y+h), fill=('#f0f3e9' if r%2 else '#fafbf6'), outline='#d9dfcf')
                        for li,line in enumerate(ls):d.text((x+12,y+10+li*27),line,font=face,fill='#354331')
                        x+=w
                    y+=h
                item=save(image, OUT/f'model-{si+1:02}-{len(pages)+1:03}.webp')
                item.update(rows=f'{block[0]}–{block[-1]}', columns=', '.join(get_column_letter(c) for c in cols))
                pages.append(item)
        expected={(r,c) for r in rows for c in columns if original.cell(r,c).value is not None}
        assert accounted == expected, sheet.title
        sheets.append({'name':sheet.title, 'rows':len(rows), 'pages':pages})
    return {'sheets':sheets, 'nonempty_rows':sum(s['rows'] for s in sheets)}

def main():
    PRIVATE.mkdir(exist_ok=True); OUT.mkdir(parents=True,exist_ok=True)
    assets = ROOT/'dist/assets'
    # Migrate legacy copies out of the serving root; originals stay intact locally.
    for name in ['xpeng-research.pdf','sanxie-memo.pdf','sanxie-model.xlsx','xinyue-xie-resume.pdf','original-resume.txt','workbook.json','xpeng-source.jpg']:
        old=assets/name; new=PRIVATE/name
        if old.exists():
            if new.exists():
                assert old.read_bytes()==new.read_bytes(), f'Conflicting local source: {name}'
                old.unlink()
            else:shutil.move(str(old),str(new))
    manifest={
        'xpeng':render_pdf('xpeng',PRIVATE/'xpeng-research.pdf'),
        'sanxie':render_pdf('sanxie',PRIVATE/'sanxie-memo.pdf'),
        'model':render_model(PRIVATE/'sanxie-model.xlsx'),
    }
    with Image.open(PRIVATE/'xpeng-source.jpg') as image:
        # Protected card cover too: the unmarked source image stays private.
        save(image,OUT/'xpeng-cover.webp')
    (OUT/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2))
    print('Prepared',36,'report pages;',len(manifest['model']['sheets']),'model sheets;',manifest['model']['nonempty_rows'],'nonempty model rows. Originals retained privately.')

if __name__=='__main__':main()
