/* Offline preview: internal anchors stay in the current document. */
const frame=document.getElementById('site');
let currentPath=null;
function parseRoute(route){
 const at=route.indexOf('#');
 const path=at<0?route:route.slice(0,at);
 let anchor=at<0?'':route.slice(at+1);
 try{anchor=decodeURIComponent(anchor)}catch{}
 return {path:path||currentPath||'/',anchor};
}
function routeAddress(path,anchor){return path+(anchor?'#'+anchor:'')}
function openAnchor(doc,anchor){
 if(!anchor){frame.contentWindow?.scrollTo?.(0,0);return true}
 if(anchor.startsWith('category-')){
  doc.dispatchEvent(new CustomEvent('portfolio:filter',{detail:{category:anchor.slice(9)}}));
  return true;
 }
 const target=doc.getElementById(anchor);
 if(!target)return false;
 let node=target;
 while(node){if(node.tagName==='DETAILS')node.open=true;node=node.parentElement}
 target.scrollIntoView({block:'start'});
 return true;
}
function render(route,update=true){
 const parsed=parseRoute(route);
 if(!pages[parsed.path])return false;
 const address=routeAddress(parsed.path,parsed.anchor);
 if(parsed.path===currentPath&&frame.contentDocument?.body){
  openAnchor(frame.contentDocument,parsed.anchor);
 }else{
  currentPath=parsed.path;
  frame.onload=()=>{
   const doc=frame.contentDocument;
   if(!doc)return;
   openAnchor(doc,parsed.anchor);
   doc.addEventListener('click',event=>{
    const link=event.target.closest('a');
    if(!link||link.hasAttribute('download'))return;
    const href=link.getAttribute('href')||'';
    if(href.startsWith('#')||href.startsWith('/')&&pages[parseRoute(href).path]){
     event.preventDefault();render(href);
    }
   });
  };
  frame.srcdoc=pages[parsed.path];
 }
 if(update)history.pushState({route:address},'','#!'+address);
 return true;
}
addEventListener('popstate',()=>render(location.hash.startsWith('#!')?location.hash.slice(2):'/',false));
render(location.hash.startsWith('#!')?location.hash.slice(2):'/',false);
