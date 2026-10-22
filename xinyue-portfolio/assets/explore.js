/* Linked planets, real work previews and watermarked report-page navigation. */
(()=>{
 const langFor=el=>el?.closest('[data-scope]')?.dataset.locale||document.documentElement.lang.split('-')[0]||'zh';
 const scene=document.querySelector('[data-constellation]');
 if(scene){
  const canvas=scene.querySelector('.constellation-canvas'),hint=scene.querySelector('[data-constellation-hint]');
  let rotation=0,drag=null,focused=null;
  const defaultHint=()=>{const copy=hint.querySelector('[data-copy]');if(copy)copy.textContent=copy.dataset[langFor(scene)]||copy.dataset.zh};
  function draw(){
   scene.querySelectorAll('[data-orbit-node]').forEach(node=>{
    const angle=(Number(node.dataset.angle)+rotation)*Math.PI/180,cx=Number(node.dataset.cx),cy=Number(node.dataset.cy);
    const x=cx+Number(node.dataset.rx)*Math.cos(angle),y=cy+Number(node.dataset.ry)*Math.sin(angle);
    node.style.left=x/9+'%';node.style.top=y/5.9+'%';
    scene.querySelector('#'+node.dataset.path)?.setAttribute('d',`M${cx} ${cy}L${x} ${y}`);
   });
  }
  function focus(node){focused=node;scene.dataset.focus=node.dataset.cluster;const copy=hint.querySelector('[data-copy]');if(copy)copy.textContent=node.dataset[langFor(scene)==='zh'?'hintZh':'hintEn']||''}
  function clear(){focused=null;delete scene.dataset.focus;defaultHint()}
  scene.querySelectorAll('.sphere-node').forEach(node=>{
   node.addEventListener('pointerenter',()=>{if(!drag)focus(node)});
   node.addEventListener('pointerleave',()=>{if(!node.matches(':focus-visible'))clear()});
   node.addEventListener('focus',()=>focus(node));node.addEventListener('blur',clear);
  });
  canvas.addEventListener('pointerdown',event=>{
   if(event.target.closest('a,button'))return;
   drag={x:event.clientX,rotation};canvas.setPointerCapture(event.pointerId);canvas.classList.add('is-dragging');
  });
  canvas.addEventListener('pointermove',event=>{if(!drag)return;rotation=Math.max(-14,Math.min(14,drag.rotation+(event.clientX-drag.x)/10));draw()});
  const stop=()=>{drag=null;canvas.classList.remove('is-dragging')};canvas.addEventListener('pointerup',stop);canvas.addEventListener('pointercancel',stop);
  scene.querySelector('[data-orbit-reset]').addEventListener('click',()=>{rotation=0;draw();clear()});
  document.addEventListener('site:language',()=>focused?focus(focused):defaultHint());draw();
 }

 function selectField(category){
  document.querySelectorAll('[data-map-work]').forEach(group=>group.hidden=group.dataset.mapWork!==category);
  document.querySelectorAll('[data-field-line]').forEach(path=>path.classList.toggle('active',path.dataset.fieldLine===category));
 }
 document.addEventListener('portfolio:changed',event=>selectField(event.detail.category));
 selectField(location.hash.startsWith('#category-')?location.hash.slice(10):'all');

 const dialog=document.getElementById('work-preview');let returnFocus=null;
 function applyPreviewLanguage(){
  if(!dialog)return;const lang=langFor(dialog);
  dialog.querySelectorAll('[data-copy]').forEach(copy=>copy.textContent=copy.dataset[lang]||copy.dataset.zh||'');
 }
 function openPreview(id,trigger){
  const template=document.querySelector(`[data-work-template="${id}"]`);
  if(!template||!dialog)return;
  returnFocus=trigger;dialog.dataset.locale=langFor(trigger);
  dialog.querySelector('[data-preview-content]').replaceChildren(template.content.cloneNode(true));
  applyPreviewLanguage();dialog.showModal();dialog.scrollTop=0;
 }
 document.addEventListener('click',event=>{const trigger=event.target.closest('[data-work-trigger]');if(trigger)openPreview(trigger.dataset.workTrigger,trigger)});
 dialog?.addEventListener('close',()=>returnFocus?.focus({preventScroll:true}));
 dialog?.addEventListener('click',event=>{if(event.target!==dialog)return;const rect=dialog.getBoundingClientRect();if(event.clientX<rect.left||event.clientX>rect.right||event.clientY<rect.top||event.clientY>rect.bottom)dialog.close()});
 document.addEventListener('site:language',()=>{if(dialog?.open)applyPreviewLanguage()});

 document.querySelectorAll('[data-reading-viewer]').forEach(viewer=>{
  const pages=[...viewer.querySelectorAll('[data-reading-page]')],select=viewer.querySelector('[data-reading-select]');
  const prev=viewer.querySelector('[data-reading-prev]'),next=viewer.querySelector('[data-reading-next]'),zoom=viewer.querySelector('[data-reading-zoom]'),frame=viewer.querySelector('[data-reading-frame]');
  function show(index){const n=Math.max(0,Math.min(pages.length-1,index));select.value=String(n);pages.forEach((page,i)=>page.hidden=i!==n);prev.disabled=n===0;next.disabled=n===pages.length-1;frame.scrollTo({left:0,top:0})}
  prev.addEventListener('click',()=>show(Number(select.value)-1));next.addEventListener('click',()=>show(Number(select.value)+1));select.addEventListener('change',()=>show(Number(select.value)));
  zoom.addEventListener('click',()=>{const enlarged=frame.classList.toggle('zoomed');zoom.setAttribute('aria-pressed',String(enlarged))});
  // Keep the image interaction focused on reading. Raster watermarks carry attribution.
  frame.addEventListener('dragstart',event=>event.preventDefault());
  frame.addEventListener('contextmenu',event=>{if(event.target.tagName==='IMG')event.preventDefault()});
  show(0);
 });
})();
