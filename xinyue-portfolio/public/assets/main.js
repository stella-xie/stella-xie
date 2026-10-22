(()=>{
let memory={};try{const owner=window.parent!==window?window.parent:window;owner.XINYUE_PREFERENCES=owner.XINYUE_PREFERENCES||{};memory=owner.XINYUE_PREFERENCES}catch{}
const store={get(k){try{return localStorage.getItem(k)||memory[k]||null}catch{return memory[k]||null}},set(k,v){memory[k]=v;try{localStorage.setItem(k,v)}catch{}},remove(k){delete memory[k];try{localStorage.removeItem(k)}catch{}}};
let globalLang=store.get('xinyue-language')||'zh';
const scopes=[...document.querySelectorAll('[data-scope]')],page=document.body.dataset.page||'home';
function key(scope){return 'xinyue-scope-'+page+'-'+scope.dataset.scope}
function langFor(element){const scope=element.closest('[data-scope]');return scope?(scope.dataset.locale||globalLang):globalLang}
function apply(){
 document.documentElement.lang=globalLang==='zh'?'zh-CN':'en';
 document.querySelectorAll('[data-copy]').forEach(el=>{const lang=langFor(el);el.textContent=el.dataset[lang]||'';el.dataset.render=lang});
 document.querySelectorAll('[data-placeholder-zh]').forEach(el=>el.placeholder=el.dataset[langFor(el)==='zh'?'placeholderZh':'placeholderEn']);
 document.querySelectorAll('.lang-switch').forEach(control=>{const lang=control.hasAttribute('data-global')?globalLang:langFor(control);control.querySelectorAll('button').forEach(b=>{const active=b.dataset.lang===lang;b.classList.toggle('active',active);b.setAttribute('aria-pressed',String(active))})});
 document.querySelectorAll('[data-language]').forEach(el=>el.hidden=el.dataset.language!==langFor(el));
 document.querySelectorAll('[data-diagram]').forEach(el=>{const lang=langFor(el);el.src=el.dataset[lang];el.alt=el.dataset[lang==='zh'?'altZh':'altEn']||''});
 document.querySelectorAll('[data-diagram-mobile]').forEach(el=>el.srcset=el.dataset[langFor(el)]);

 const title=document.querySelector('meta[name="page-title"]');if(title)document.title=(title.dataset[globalLang]||title.content)+' · Xinyue Xie';document.dispatchEvent(new CustomEvent('site:language'));
}
scopes.forEach(s=>{const saved=store.get(key(s));if(saved)s.dataset.locale=saved});
document.querySelectorAll('.lang-switch button').forEach(b=>b.addEventListener('click',()=>{const control=b.closest('.lang-switch');if(control.hasAttribute('data-global')){globalLang=b.dataset.lang;store.set('xinyue-language',globalLang);Object.keys(memory).filter(k=>k.startsWith('xinyue-scope-')).forEach(k=>delete memory[k]);scopes.forEach(s=>{delete s.dataset.locale;store.remove(key(s))});try{Object.keys(localStorage).filter(k=>k.startsWith('xinyue-scope-')).forEach(k=>localStorage.removeItem(k))}catch{}}else{const scope=control.closest('[data-scope]');if(scope){scope.dataset.locale=b.dataset.lang;store.set(key(scope),b.dataset.lang)}}apply();updateCount();}));
apply();
let category='all';const search=document.querySelector('[data-project-search]');
function updateCount(){const output=document.querySelector('[data-result-count]');if(output){const cards=[...document.querySelectorAll('[data-category]')];const n=cards.filter(c=>!c.hidden).length;output.textContent=langFor(output)==='zh'?`${n} / ${cards.length} 个项目`:`${n} / ${cards.length} projects`}}
function filter(){const q=(search?.value||'').toLowerCase().trim();document.querySelectorAll('[data-category]').forEach(card=>card.hidden=!(category==='all'||(card.dataset.categories||card.dataset.category).split(/\s+/).includes(category))||!!q&&!card.dataset.search.toLowerCase().includes(q));document.querySelectorAll('[data-filter]').forEach(b=>{b.classList.toggle('active',b.dataset.filter===category);b.setAttribute('aria-pressed',String(b.dataset.filter===category))});updateCount();const empty=document.querySelector('[data-empty]');if(empty)empty.hidden=[...document.querySelectorAll('[data-category]')].some(c=>!c.hidden);document.dispatchEvent(new CustomEvent('portfolio:changed',{detail:{category}}))}
document.querySelectorAll('[data-filter]').forEach(b=>b.addEventListener('click',()=>{category=b.dataset.filter;filter();if(document.body.dataset.page==='portfolio'&&window.parent===window)history.replaceState(null,'','#category-'+category)}));search?.addEventListener('input',filter);
function selectCategory(id){if(![...document.querySelectorAll('[data-filter]')].some(b=>b.dataset.filter===id))return;category=id;filter()}
document.addEventListener('portfolio:filter',e=>selectCategory(String(e.detail?.category||'')));
function revealAnchor(){let id=location.hash.slice(1);try{id=decodeURIComponent(id)}catch{}if(id.startsWith('category-')){selectCategory(id.slice(9));return}const target=document.getElementById(id);if(!target)return;let node=target;while(node){if(node.tagName==='DETAILS')node.open=true;node=node.parentElement}requestAnimationFrame(()=>target.scrollIntoView({block:'start'}))}
addEventListener('hashchange',revealAnchor);filter();revealAnchor();
document.querySelectorAll('[data-open-analysis]').forEach(button=>button.addEventListener('click',()=>{const target=document.getElementById(button.dataset.openAnalysis);if(!target)return;target.open=true;target.scrollIntoView({block:'start',behavior:matchMedia('(prefers-reduced-motion: reduce)').matches?'instant':'smooth'});target.querySelector('summary')?.focus({preventScroll:true})}));

document.addEventListener('keydown',e=>{if(e.key==='Escape'){document.querySelectorAll('.project.preview-pinned').forEach(p=>{p.classList.remove('preview-pinned');p.querySelector('[data-preview-toggle]')?.setAttribute('aria-expanded','false')})}});

const tabs=[...document.querySelectorAll('[data-company-tab]')];function selectCompany(id){tabs.forEach(b=>{const active=b.dataset.companyTab===id;b.setAttribute('aria-selected',String(active));b.tabIndex=active?0:-1});document.querySelectorAll('[data-company-panel]').forEach(p=>p.hidden=p.dataset.companyPanel!==id)}tabs.forEach((b,i)=>{b.addEventListener('click',()=>selectCompany(b.dataset.companyTab));b.addEventListener('keydown',e=>{if(!['ArrowRight','ArrowLeft','ArrowUp','ArrowDown','Home','End'].includes(e.key))return;e.preventDefault();let n=e.key==='Home'?0:e.key==='End'?tabs.length-1:(i+(['ArrowRight','ArrowDown'].includes(e.key)?1:-1)+tabs.length)%tabs.length;selectCompany(tabs[n].dataset.companyTab);tabs[n].focus()})});
const progress=document.querySelector('.progress');function scrollUpdate(){const h=document.documentElement.scrollHeight-innerHeight;if(progress)progress.style.width=(h>0?scrollY/h*100:0)+'%'}addEventListener('scroll',scrollUpdate,{passive:true});scrollUpdate();document.querySelector('.to-top')?.addEventListener('click',()=>scrollTo({top:0,behavior:matchMedia('(prefers-reduced-motion: reduce)').matches?'instant':'smooth'}));
const art=document.querySelector('.hero-art'),stage=document.querySelector('.orbit-stage');if(art&&stage&&!matchMedia('(prefers-reduced-motion: reduce)').matches){art.addEventListener('pointermove',e=>{if(e.pointerType==='touch')return;const r=art.getBoundingClientRect();stage.style.transform=`rotateY(${(e.clientX-r.left-r.width/2)/r.width*8}deg) rotateX(${-(e.clientY-r.top-r.height/2)/r.height*6}deg)`});art.addEventListener('pointerleave',()=>stage.style.transform='')}
const modelSelect=document.querySelector('[data-model-sheet]');
function selectModel(){if(!modelSelect)return;document.querySelectorAll('[data-model-panel]').forEach(panel=>panel.hidden=panel.dataset.modelPanel!==modelSelect.value)}
modelSelect?.addEventListener('change',selectModel);selectModel();
})();
