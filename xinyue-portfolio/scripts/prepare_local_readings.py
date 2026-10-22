"""Make local watermarked reading images; never publish original documents.

Optional local preprocessing. Normal builds only need the prepared assets.
Private customer/transaction material in the computing report is not published.
"""
from pathlib import Path
from tempfile import TemporaryDirectory
import json, re, shutil, subprocess
from PIL import Image, ImageDraw
from pypdf import PdfReader
import pdfplumber
from prepare_readers import watermark, font

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'private-sources/reading-copies'
PRIVATE = ROOT / 'private-sources'

def main():
    OUT.mkdir(parents=True, exist_ok=True)
    private_manifest = json.loads((PRIVATE/'readers/manifest.json').read_text())
    manifest = {}
    for key, filename in [('xpeng','xpeng-research.pdf'), ('sanxie','sanxie-memo.pdf')]:
        reader=PdfReader(PRIVATE/filename)
        # Catch contact details in the text layer before accepting a reading copy.
        for page in reader.pages:
            text=page.extract_text() or ''
            assert not re.search(r'(?<!\d)1[3-9]\d{9}(?!\d)|[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}',text), 'Contact details require redaction'
        pages=[]
        for index,item in enumerate(private_manifest[key]['pages'],1):
            source=PRIVATE/'readers'/Path(item['src']).name
            target=OUT/f'{key}-{index:03}.webp'
            shutil.copyfile(source,target)
            pages.append(dict(src='/assets/reading/'+target.name,width=item['width'],height=item['height'],original_page=index))
        manifest[key]=dict(kind='report',pages=pages,total_pages=len(reader.pages),excerpt=False,
                           label=['小鹏汽车研究报告','XPeng research report'] if key=='xpeng' else ['三协电机投资备忘录','Sanxie investment memo'])

    source=ROOT.parent/'算力报告/算力产业认知报告.pdf'
    selected=[3,6,9,16,17,18]
    pages=[]
    with pdfplumber.open(source) as pdf, TemporaryDirectory(prefix='public-compute-') as tmp:
        for number in selected:
            target_prefix=Path(tmp)/f'page-{number}'
            subprocess.run(['pdftoppm','-f',str(number),'-l',str(number),'-r','140','-png','-singlefile',str(source),str(target_prefix)],check=True,stdout=subprocess.DEVNULL)
            with Image.open(str(target_prefix)+'.png') as raw:
                image=raw.convert('RGB')
            if number==17:
                page=pdf.pages[number-1]
                matches=page.search('代工格局高度集中')
                assert len(matches)==1
                y=matches[0]['top']-6
                box=(int(25/page.width*image.width),int(y/page.height*image.height),int((page.width-25)/page.width*image.width),int((page.height-34)/page.height*image.height))
                draw=ImageDraw.Draw(image)
                draw.rectangle(box,fill='#f0f1ec')
                draw.text((box[0]+20,box[1]+14),'产品与供应链细节已隐去',font=font(19),fill='#6b7468')
            image=watermark(image)
            target=OUT/f'ai-compute-{number:03}.webp'
            image.save(target,'WEBP',quality=88,method=6)
            pages.append(dict(src='/assets/reading/'+target.name,width=image.width,height=image.height,original_page=number))
    manifest['ai-compute']=dict(kind='report',pages=pages,total_pages=42,excerpt=True,label=['算力产业认知报告 · 公开节选','AI computing report · Public excerpts'])

    # Two pages from the Quick LBO sheet, not the original workbook or its data.
    pages=[]
    sheet=next(s for s in private_manifest['model']['sheets'] if s['name']=='Part 1 - Quick LBO')
    for index,item in enumerate(sheet['pages'],1):
        target=OUT/f'sanxie-model-{index:03}.webp'
        shutil.copyfile(PRIVATE/'readers'/Path(item['src']).name,target)
        pages.append(dict(src='/assets/reading/'+target.name,width=item['width'],height=item['height'],original_page=index))
    manifest['sanxie-model']=dict(kind='model',pages=pages,total_pages=len(pages),excerpt=True,label=['三协电机模型 · Quick LBO 关键页','Sanxie model · Quick LBO pages'])
    (OUT/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2))
    print('Prepared',sum(len(m['pages']) for m in manifest.values()),'watermarked reading pages; original documents and complete model remain private.')

if __name__=='__main__': main()
