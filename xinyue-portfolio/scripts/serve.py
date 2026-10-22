from http.server import ThreadingHTTPServer,SimpleHTTPRequestHandler
from pathlib import Path
import argparse
from urllib.parse import urlsplit,unquote
ROOT=Path(__file__).resolve().parents[1]
class Handler(SimpleHTTPRequestHandler):
 def translate_path(self,path):
  path=unquote(urlsplit(path).path)
  if path=='/preview.html':return str(ROOT/('preview.html' if FULL else 'public-preview.html'))
  base=SERVE_ROOT
  if path.startswith('/dist/'):path=path[5:]
  if path.startswith('/public/'):path=path[7:]
  target=(base/path.lstrip('/')).resolve()
  try:target.relative_to(base)
  except ValueError:return str(base/'not-found')
  if any(part.startswith('.') for part in target.relative_to(base).parts):return str(base/'not-found')
  if target.is_file() and target.suffix.lower() not in ['.html','.css','.js','.json','.svg','.png','.jpg','.webp','.woff2']:
   return str(base/'not-found')
  return str(target)
 def list_directory(self,path):
  self.send_error(404,'Not found')
  return None
FULL=False;SERVE_ROOT=ROOT/'public'
if __name__=='__main__':
 parser=argparse.ArgumentParser();parser.add_argument('--full',action='store_true');FULL=parser.parse_args().full;SERVE_ROOT=ROOT/('dist' if FULL else 'public')
 print('Local: http://127.0.0.1:8765/\nOffline package preview: http://127.0.0.1:8765/preview.html',flush=True)
 ThreadingHTTPServer(('127.0.0.1',8765),Handler).serve_forever()
