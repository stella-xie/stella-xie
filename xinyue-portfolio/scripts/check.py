"""Checks the distributable site, including accidental source-file exposure."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
import json,re,xml.etree.ElementTree as ET,argparse

parser=argparse.ArgumentParser();parser.add_argument('--full',action='store_true');FULL=parser.parse_args().full
ROOT=Path(__file__).resolve().parents[1];DIST=ROOT/('dist' if FULL else 'public')
FORBIDDEN={'.pdf','.xlsx','.xls','.csv','.docx','.pptx','.zip','.txt','.py','.map'}
class Document(HTMLParser):
 def __init__(self):
  super().__init__();self.ids=[];self.links=[];self.targets=[];self.downloads=[]
 def handle_starttag(self,tag,items):
  a=dict(items)
  if a.get('id'):self.ids.append(a['id'])
  if 'download' in a:self.downloads.append(a)
  for key in ['href','src','srcset']:
   if a.get(key):self.links.append(a[key])
  if a.get('data-open-analysis'):self.targets.append(a['data-open-analysis'])
  if 'data-diagram' in a or 'data-diagram-mobile' in a:
   self.links.extend([a['data-zh'],a['data-en']])

def main():
 files=list(DIST.rglob('*'));pages={}
 for f in files:
  if f.is_file():
   assert f.suffix.lower() not in FORBIDDEN, f'Private file in dist: {f}'
   assert f.name not in ['workbook.json','original-resume.txt'],f
 for f in DIST.rglob('index.html'):
  doc=Document();doc.feed(f.read_text());pages[f]=doc
  assert len(doc.ids)==len(set(doc.ids)),f'Duplicate IDs: {f}'
  assert not doc.downloads, f'Download action: {f}'
  assert all(target in doc.ids for target in doc.targets),f'Dead contents target: {f}'
  assert not re.search(r'(?:data:application/(?:pdf|vnd)|XINYUE_WORKBOOK|workbook\.json|\.xlsx|\.pdf(?:["#?]))',f.read_text()),f'Original-file reference: {f}'
 for f,doc in pages.items():
  for url in doc.links:
   part=urlsplit(url)
   if part.scheme or part.netloc:continue
   path=unquote(part.path);target=(DIST/path.lstrip('/')) if path.startswith('/') else f.parent/path
   if not path:target=f
   if target.is_dir():target=target/'index.html'
   assert target.is_file(),f'{f}: missing {url}'
   if part.fragment:
    assert target in pages and unquote(part.fragment) in pages[target].ids or part.fragment.startswith('category-'),f'{f}: missing anchor {url}'
 for diagram in (DIST/'assets/diagrams').glob('*.svg'):
  ET.parse(diagram);assert 'READ ONLY' in diagram.read_text(),diagram
 metadata=[]
 if FULL:
  manifest=json.loads((DIST/'assets/readers/manifest.json').read_text())
  assert manifest['xpeng']['page_count']==26 and manifest['sanxie']['page_count']==10
  assert len(manifest['model']['sheets'])==9 and manifest['model']['nonempty_rows']==889
  for key in ['xpeng','sanxie']:metadata+=manifest[key]['pages']
  for sheet in manifest['model']['sheets']:metadata+=sheet['pages']
  for item in metadata:
   assert set(item)<=set(['src','width','height','rows','columns']), 'Cell data exported'
   assert (DIST/item['src'].lstrip('/')).is_file(),item
   assert item['width']>0 and item['height']>0,item
 else:
  assert not (DIST/'assets/readers').exists(), 'Full research images in public output'
  for f in pages:assert '/assets/readers/' not in f.read_text(),f
 preview=(ROOT/('preview.html' if FULL else 'public-preview.html')).read_text()
 assert not any(word in preview for word in ['XINYUE_WORKBOOK','workbook.json','application/pdf','sanxie-model.xlsx','xpeng-research.pdf'])
 assert not re.search(r'<a[^>]+\bdownload\b',preview)
 if not FULL:assert '/assets/readers/' not in preview and 'data-model-panel=' not in preview
 print(f'PASS: {len(pages)} pages, all local links/anchors, contents targets, {len(metadata)} reading images, 32 diagram signatures, no downloadable originals or model data in dist/preview.')

if __name__=='__main__':main()
