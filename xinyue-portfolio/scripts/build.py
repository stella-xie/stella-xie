from pathlib import Path
import html,json,re,base64,argparse,shutil,posixpath
from content import COMPANIES,EXTRA,EDU,COURSES,AWARDS,PROJECTS
from connections import CATEGORIES,META,CAPABILITIES
from illustrations import DIAGRAMS,generate
from constellations import home as home_constellation, portfolio as portfolio_constellation
parser=argparse.ArgumentParser();parser.add_argument('--full',action='store_true',help='Local full reading edition; requires private-sources/readers. Never commit this output.')
FULL=parser.parse_args().full
ROOT=Path(__file__).resolve().parents[1];D=ROOT/('dist' if FULL else 'public');A=D/'assets'
D.mkdir(exist_ok=True);shutil.copytree(ROOT/'assets',A,dirs_exist_ok=True)
generate(A/'diagrams')
READING_COPIES={}
if FULL:
 shutil.copytree(ROOT/'private-sources/reading-copies',A/'reading',dirs_exist_ok=True)
 READING_COPIES=json.loads((A/'reading/manifest.json').read_text())
elif (A/'reading').exists():
 shutil.rmtree(A/'reading')
if FULL:
 shutil.copytree(ROOT/'private-sources/readers',A/'readers',dirs_exist_ok=True)
 READERS=json.loads((A/'readers/manifest.json').read_text())
else:
 assert not (A/'readers').exists(),'Public output must not contain full reading copies'
def e(x):return html.escape(str(x),quote=True)
def t(zh,en):return f'<span data-copy data-zh="{e(zh)}" data-en="{e(en)}">{e(zh)}</span>'
def p(zh,en,cls=''):return f'<p class="{cls}">{t(zh,en)}</p>'
def switch(global_=False):return '<div class="lang-switch'+(' global-lang' if global_ else '')+'" '+('data-global' if global_ else '')+' role="group" aria-label="Language / 语言"><button data-lang="zh" class="active" aria-pressed="true">中文</button><button data-lang="en" aria-pressed="false">EN</button></div>'
MARK='<svg viewBox="0 0 40 40" fill="none" aria-hidden="true"><path d="M20 2v36M2 20h36M7.3 7.3l25.4 25.4M7.3 32.7L32.7 7.3" stroke="currentColor" stroke-width="2.4"/></svg>'
def header(active='home'):
 return f'<header class="site-header"><a class="brand" href="/" aria-label="Xinyue Xie / 谢欣玥">{MARK}xinyue<small>谢欣玥 / STELLA</small></a><nav class="nav" aria-label="主导航 / Navigation"><a href="/portfolio/" {"aria-current=page" if active=="portfolio" else ""}>{t("作品集","Portfolio")}</a><a href="/#experience">{t("经历","Experience")}</a><a href="/resume/" {"aria-current=page" if active=="resume" else ""}>{t("简历","Resume")} ↗</a><a href="/#contact" class="nav-contact">{t("聊一聊","Let’s talk")}<i>↗</i></a>{switch(True)}</nav></header>'
def footer():return f'<footer class="footer"><span>© 2026 XINYUE XIE · {t("保持好奇，持续探索。","Always curious. Always building.")}</span><span><a href="/portfolio/">{t("作品集","PORTFOLIO")} ↗</a><a href="/resume/">{t("完整简历","RESUME")} ↗</a><a href="/#contact">{t("联系我","CONTACT")} ↗</a></span></footer>'
def page(zh,en,body,slug='home',home=False):
 return f'<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="description" content="谢欣玥 Xinyue Xie (Stella) · Research, strategy and AI. 投资研究、AI 应用与完整个人经历。"><meta name="theme-color" content="#111b17"><meta name="page-title" content="{e(zh)}" data-zh="{e(zh)}" data-en="{e(en)}"><title>{e(zh)} · Xinyue Xie</title><link rel="icon" href="/assets/favicon.svg"><link rel="stylesheet" href="/assets/style.css"><link rel="stylesheet" href="/assets/constellations.css"><script src="/assets/main.js" defer></script><script src="/assets/explore.js" defer></script></head><body data-page="{slug}"><div class="progress" aria-hidden="true"></div>{body if home else "<div class=wrap>"+header(slug)+"<main>"+body+"</main>"+footer()+"</div>"}{preview_dialog()}<button class="to-top" aria-label="回到顶部 / Back to top">↑</button></body></html>'
def logo(id):
 icon=' icon-logo' if id in ['bytedance','hony','qingtong'] else ''
 return f'<span class="logo-box"><img class="{icon}" src="/assets/logos/{id}.png" alt="{id} logo" loading="lazy"></span>'
def bullets(items):return '<ul class="full-bullets">'+''.join('<li>'+t(*x)+'</li>' for x in items)+'</ul>'
def cover(pr,index=1):
 c=pr['cover'];label=f'<div class="cover-label">{e(pr["tags"][0])}</div><div class="cover-no">0{index}</div>'
 if c=='xpeng':inner='<div class="xpeng-outline" aria-hidden="true"><svg viewBox="0 0 480 160" fill="none"><path d="M45 104l24-31 88-10 62-35h105l57 40 43 9 20 27v22h-37m-50 0H146m-50 0H45v-22Z" stroke="currentColor" stroke-width="2"/><circle cx="121" cy="123" r="24" stroke="currentColor" stroke-width="2"/><circle cx="381" cy="123" r="24" stroke="currentColor" stroke-width="2"/><path d="M173 62h183l-42-25h-89Z" stroke="currentColor" stroke-width="1.5"/></svg></div><div class="cover-word"><strong>Beyond the vehicle.</strong><small>XPENG / STRUCTURAL OPPORTUNITIES</small></div>'
 elif c=='compute':inner='<div class="chip"><span>AI</span></div><div class="chip-note">CHIPS<br>COMPUTE<br>UTILIZATION</div><div class="compute-flow">INFRASTRUCTURE → APPLICATIONS</div>'
 elif c=='lbo':inner='<div class="lbo-sheet"><div class="sheet-label">SANXIE MOTOR / QUICK LBO</div><div class="sheet-name">Behind the returns.</div><div class="sheet-values"><div>28.63%<small>MODELED IRR</small></div><div>3.40×<small>MOIC</small></div></div><div class="sheet-line"></div></div>'
 elif c in ['agent','rag']:
  inner='<div class="system"><div class="system-node">'+('9 SOURCES' if c=='agent' else 'KNOWLEDGE')+'<small>COLLECT</small></div><div class="system-node core">'+('LEAD AGENT' if c=='agent' else 'RESEARCH AI')+'<small>'+('SCORE + MATCH' if c=='agent' else 'RAG + MEMORY')+'</small></div><div class="system-node">'+('3,700+' if c=='agent' else 'INSIGHTS')+'<small>'+('COMPANIES' if c=='agent' else 'GENERATE')+'</small></div></div><div class="agent-foot">INFORMATION → INTELLIGENCE → ACTION</div>'
 elif c=='assets':inner='<div class="buildings"><i></i><i></i><i></i></div><div class="cover-word"><small>OPERATIONS / FINANCING / EXIT</small></div>'
 elif c=='industry':inner='<div class="industry-orbit"></div><div class="cover-word"><small>ENERGY TRANSITION × DOMESTIC COMPUTING</small></div>'
 else:inner='<div class="academic-word">Why<em>→ What</em></div>'
 return f'<div class="cover cover-{c}"><div class="cover-inner">{label}{inner}</div></div>'
def compact_logic(pr):
 return '<ol class="compact-logic">'+''.join(f'<li><span class="logic-index">{i+1:02}</span><div><strong>{t(zh,en)}</strong>{p(txt,txten)}</div></li>' for i,(zh,en,txt,txten) in enumerate(META[pr['id']]['steps']))+'</ol>'
def origin(pr,cls='origin-link'):
 zh,en,anchor=META[pr['id']]['source']
 return f'<a class="{cls}" href="/resume/#{anchor}"><span class="connection-dot"></span>{t(zh,en)} <span aria-hidden="true">↗</span></a>'
def project_links(ids):
 result='<div class="linked-work-list">'
 for id in ids:
  pr=next(p for p in PROJECTS if p['id']==id)
  result+=f'<a class="linked-work" href="/projects/{id}/#logic"><span class="work-symbol work-symbol-{pr["cover"]}">↗</span><div><small>{t(*pr["type"])}</small><strong>{t(*pr["name"])}</strong></div><span class="linked-arrow">↗</span></a>'
 return result+'</div>'
def card(pr,i):
 id=pr['id'];meta=META[id]
 search=' '.join(pr['name']+pr['type']+pr['desc']+pr['tags'])
 preview=f'<div class="hover-preview" id="preview-{pr['id']}"><div class="preview-eyebrow">{t("内容速览","AT A GLANCE")} / 0{i}</div><h4>{t(*pr["name"])}</h4>{p(*pr["desc"])}<div class="preview-footer">{t("点击查看研究逻辑","Explore the reasoning")} <span>↗</span></div></div>'
 return f'<article class="project" data-category="{meta["categories"][0]}" data-categories="{" ".join(meta["categories"])}" data-search="{e(search)}"><a class="project-visual" href="/projects/{id}/#logic" aria-label="{e(pr["name"][0])} / {e(pr["name"][1])}">{cover(pr,i)}{preview}</a><div class="project-meta">{t(*pr["type"])} · {pr["year"]}</div><h3 class="project-title"><a href="/projects/{id}/">{t(*pr["name"])}</a><i aria-hidden="true">↗</i></h3>{p(*pr["desc"],"project-desc")}<div class="project-actions"><button class="preview-toggle" data-work-trigger="{id}" aria-controls="work-preview" aria-haspopup="dialog">{t("点开预览","Preview the work")} <span aria-hidden="true">◉</span></button>{origin(pr)}</div><details class="card-logic"><summary>{t("展开核心逻辑","Unpack the core logic")}<span class="expand-mark" aria-hidden="true">+</span></summary>{compact_logic(pr)}<a class="logic-read-link" href="/projects/{id}/#logic">{t("进入完整分析","Read the full analysis")} ↗</a></details>{preview_template(pr)}</article>'
def sectionhead(no,zh,en,extra=''):
 return f'<div class="section-head"><div class="section-heading"><div><div class="eyebrow">{no}</div><h2>{t(zh,en)}</h2></div>{switch()}</div>{extra}</div>'
def capability_section(scope='capabilities'):
 cards=''.join(f'<a class="capability-card" href="/projects/{id}/#logic"><span class="capability-number">0{i+1} / {tag}</span><h3>{t(zh,en)} <span>↗</span></h3>{p(txt,txten)}<div class="capability-bottom">{t("查看对应作品与研究逻辑","See the work and reasoning")} ↗</div></a>' for i,(id,zh,en,txt,txten,tag) in enumerate(CAPABILITIES))
 return f'<section class="capability-section" id="ai-capabilities" data-scope="{scope}">{sectionhead("AI / CAPABILITIES IN CONTEXT","AI 能力，让作品来说明。","AI skills, backed by the work.")}<div class="capability-grid">{cards}</div></section>'
def journey_hub():
 resume_branches=''.join(f'<a href="/resume/#experience-{c["id"]}"><span>{t(c["zh"],c["en"])}</span><small>{t(*c["role"])}</small><span>↗</span></a>' for c in COMPANIES)
 categories=''.join(f'<a href="/portfolio/#category-{id}"><span>{t(zh,en)}</span><span>↗</span></a>' for id,zh,en in CATEGORIES)
 return f'<section class="journey-section" id="explore" data-scope="journey">{sectionhead("TWO WAYS IN / ONE CONNECTED STORY","从经历出发，沿作品深入。","A journey. A body of work.")}<div class="journey-grid"><details class="journey-box resume-journey"><summary><div class="journey-label"><span>01 / THE JOURNEY</span><span class="expand-mark">+</span></div><div class="folder-art" aria-hidden="true"><i></i><i></i><i></i></div><h3>{t("简历与经历","Resume & Experience")}</h3>{p("打开每段经历，找到能力背后的具体作品。","Open an experience and find the work behind the skills.")}<span class="journey-prompt">{t("展开经历索引","Explore the experience")} <span>↘</span></span></summary><div class="journey-content">{resume_branches}<a href="/resume/#research"><span>{t("科研与 AI 项目","Academic & AI projects")}</span><span>↗</span></a><a class="journey-primary" href="/resume/">{t("查看完整简历","Open the complete resume")} ↗</a></div></details><details class="journey-box portfolio-journey"><summary><div class="journey-label"><span>02 / THE EVIDENCE</span><span class="expand-mark">+</span></div><div class="folder-art" aria-hidden="true"><i></i><i></i><i></i></div><h3>{t("分类作品集","The Portfolio")}</h3>{p("按行业、模型、学术与 AI 探索，再回到相关经历。","Explore industries, models, academic work and AI—and connect them to my experience.")}<span class="journey-prompt">{t("展开作品分类","Explore the categories")} <span>↘</span></span></summary><div class="journey-content">{categories}<a class="journey-primary" href="/portfolio/">{t("浏览全部作品","Explore all the work")} ↗</a></div></details></div><div class="journey-connection"><span></span><b>RESUME</b><i>↔</i><b>PORTFOLIO</b><span></span></div></section>'
def logic_section(pr):
 id=pr['id'];spec=DIAGRAMS[id]
 diagram=f'<figure class="project-illustration"><picture><source media="(max-width:600px)" data-diagram-mobile data-zh="/assets/diagrams/{id}-zh-mobile.svg" data-en="/assets/diagrams/{id}-en-mobile.svg" srcset="/assets/diagrams/{id}-zh-mobile.svg"><img data-diagram data-zh="/assets/diagrams/{id}-zh.svg" data-en="/assets/diagrams/{id}-en.svg" src="/assets/diagrams/{id}-zh.svg" data-alt-zh="{e(spec["title"][0])}" data-alt-en="{e(spec["title"][1])}" alt="{e(spec["title"][0])}"></picture><figcaption>{t(*spec["caption"])}</figcaption></figure>'
 outline='';notes=''
 for i,(zh,en,txt,txten) in enumerate(pr['sections']):
  target=f'analysis-{id}-{i}'
  outline+=f'<button class="analysis-jump" data-open-analysis="{target}" aria-controls="{target}"><span>{i+1:02}</span>{t(zh,en)}<i>↘</i></button>'
  if False:
   notes+=f'<div class="related-topic-label">{t("同岗位的其他研究与工作","Other research and responsibilities in the same role")}</div>'
  notes+=f'<details class="analysis-note" id="{target}" data-analysis-index="{i}" {"open" if i==0 else ""}><summary><span class="analysis-no">{i+1:02}</span><h3>{t(zh,en)}</h3><span class="expand-mark">+</span></summary><div class="analysis-body">{p(txt,txten)}</div></details>'
 heading=('项目思路','Project overview') if id in ['ai-leads','ai-research'] else ('研究思路','Research overview')
 if id=='academic':heading=('问题、方法与发现','Questions, methods & findings')
 return f'<section class="project-narrative" id="logic" data-scope="analysis">{sectionhead("PROJECT NOTES / THE BIG PICTURE",*heading)}{diagram}<div class="analysis-layout"><nav class="analysis-outline" aria-label="项目内容 / Project contents"><div class="eyebrow">{t("内容导航","CONTENTS")}</div>{outline}</nav><div class="analysis-stack">{notes}</div></div><div class="context-connection"><span>{t("相关经历","Related experience")}</span>{origin(pr)}</div></section>'
def preview_dialog():
 return f'<dialog id="work-preview" class="work-preview" aria-labelledby="work-preview-heading" data-scope="preview"><div class="work-preview-top"><h2 id="work-preview-heading">{t("作品预览","Work preview")}</h2><form method="dialog"><button aria-label="关闭预览 / Close preview">×</button></form></div><div class="work-preview-content" data-preview-content></div></dialog>'
def preview_template(pr):
 key=pr.get('reading');reading=READING_COPIES.get(key);paper=''
 if reading:
  image=reading['pages'][0]
  paper=f'<div class="preview-paper"><img src="{image["src"]}" width="{image["width"]}" height="{image["height"]}" alt="{e(reading["label"][0])} / {e(reading["label"][1])}" loading="lazy" draggable="false"></div>'
 readlink=f'<a href="/projects/{pr["id"]}/#documents">{t("阅读报告","Read the report")} ↗</a>' if reading else ''
 return f'<template id="quick-{pr["id"]}" data-work-template="{pr["id"]}"><div class="preview-layout {"" if paper else "no-page"}"><div><div class="preview-source">{t(*pr["type"])}</div><h3>{t(*pr["name"])}</h3>{p(*pr["sections"][0][2:])}{compact_logic(pr)}<div class="preview-read-links"><a href="/projects/{pr["id"]}/#logic">{t("研究逻辑与详情","Reasoning & details")} ↗</a>{readlink}</div></div>{paper}</div></template>'
def reading_section(key,anchor='documents'):
 reading=READING_COPIES[key];pages=reading['pages'];label=reading['label'];figures='';options=''
 for i,item in enumerate(pages):
  oz='原报告第 '+str(item['original_page'])+' 页' if reading['kind']=='report' else '模型第 '+str(item['original_page'])+' 页'
  oe=('Original page ' if reading['kind']=='report' else 'Model page ')+str(item['original_page'])
  options+=f'<option value="{i}" data-copy data-zh="{e(oz)}" data-en="{e(oe)}">{oz}</option>'
  figures+=f'<figure class="reader-figure" data-reading-page="{i}" {"hidden" if i else ""}><img class="reading-image" src="{item["src"]}" width="{item["width"]}" height="{item["height"]}" alt="{e(label[0])} / {e(label[1])} · {item["original_page"]}" loading="lazy" decoding="async" draggable="false"><figcaption>{t(oz,oe)}</figcaption></figure>'
 if key=='ai-compute':notice=('公开节选包含芯片分工、训练推理及制造流程；客户、报价与内部竞争分析未纳入，部分供应链细节已隐去。','Public excerpts cover chip roles, training/inference and manufacturing. Customer, pricing and internal competitive material are excluded, and selected supply details are redacted.')
 elif reading['kind']=='model':notice=('Quick LBO 工作表的水印阅读页，展示案例假设与测算。','Watermarked pages from the Quick LBO sheet, showing case assumptions and calculations.')
 else:notice=('研究保留原报告时点与条件假设，仅供作品展示与阅读。','The original research date and conditional assumptions are retained for portfolio reading.')
 count=(str(len(pages))+' 页公开节选' if reading['excerpt'] else str(len(pages))+' 页研究报告',str(len(pages))+' public excerpt pages' if reading['excerpt'] else str(len(pages))+' report pages')
 return f'<section class="reader-section reading-disclosure" data-scope="reading-{key}"><details class="document-disclosure" id="{anchor}"><summary><span class="document-icon">↗</span><div><h2>{t(*label)}</h2><span>{t(*count)} · {t("署名水印","Watermarked")}</span></div><span class="expand-mark">+</span></summary><div class="document-content" data-reading-viewer><div class="reader-heading">{switch()}</div>{p(*notice,"read-only-copy")}<div class="project-reader-controls"><button data-reading-prev aria-label="上一页 / Previous page">←</button><label class="reader-position">{t("页码","Page")} <select data-reading-select aria-label="选择阅读页 / Choose a page">{options}</select></label><button data-reading-next aria-label="下一页 / Next page">→</button><button data-reading-zoom aria-pressed="false">{t("放大","Zoom")}</button></div><div class="reader-frame" data-reading-frame>{figures}</div></div></details></section>'
def project_abilities(pr):
 return '<div class="project-abilities">'+''.join(f'<div class="project-ability"><h3>{t(zh,en)}</h3>{p(txt,txten)}</div>' for zh,en,txt,txten in pr.get('capabilities',[]))+'</div>'
HERO=f'''<div class="hero-shell"><div class="wrap">{header()}<section class="hero hero-explore" id="explore" data-scope="hero"><div><div style="display:flex;align-items:center;gap:22px"><div class="eyebrow"><span class="dot"></span>XINYUE XIE / STELLA</div>{switch()}</div><h1>{t('保持好奇。','Stay curious.')}<em>{t('向深处探索。','Go beyond.')}</em></h1><div class="hero-lede"><b>{t('你好，我是谢欣玥。','Hi, I’m Xinyue Xie.')}</b>{t('在投资研究、AI 与商业战略的交汇处，\n用数据理解变化，把想法变成可落地的作品。','Exploring the intersection of investment research, AI and business strategy.\nTurning complex questions into insight—and ideas into things that work.')}</div><div class="hero-actions"><a class="btn" href="/portfolio/">{t('进入我的作品集','Explore my work')} <span>↗</span></a><a class="text-link" href="/resume/">{t('查看完整简历','The full story')} <span>↗</span></a></div></div>{home_constellation(t)}</section><div class="hero-bottom"><span><b>{t('清华大学 · 经管学院 MiM','Tsinghua SEM · Master in Management')}</b><span class="divider">/</span>2026 — 2028</span><span><b>{t('上海交通大学 · 行政管理','Shanghai Jiao Tong · Public Administration')}</b><span class="divider">/</span>2022 — 2026</span><span>RESEARCH MIND. BUILDER SPIRIT.</span></div></div></div><div class="ticker"><div class="ticker-track"><span>AI INFRASTRUCTURE</span><i>✳</i><span>INVESTMENT RESEARCH</span><i>✳</i><span>FINANCIAL MODELING</span><i>✳</i><span>AGENTS & RAG</span><i>✳</i><span>BUSINESS STRATEGY</span></div></div>'''
featured_extra='<div class="section-right"><a class="text-link" href="/portfolio/">'+t('全部作品','All projects')+' <span>↗</span></a></div>'
featured='<section class="section" id="work" data-scope="work">'+sectionhead('01 / SELECTED WORK','让思考，有迹可循。','Thinking, made tangible.',featured_extra)+'<div class="projects">'+''.join(card(pr,i+1) for i,pr in enumerate(PROJECTS[:4]))+'</div></section>' 
# Full internship descriptions remain in each company tab, with the same complete content in the resume.
tabs='';panels=''
for i,c in enumerate(COMPANIES):
 tabs+=f'<button class="company-tab" id="tab-{c["id"]}" role="tab" aria-controls="panel-{c["id"]}" aria-selected="{str(i==0).lower()}" tabindex="{0 if i==0 else -1}" data-company-tab="{c["id"]}">{logo(c.get("logo",c["id"]))}<span><strong>{t(c["zh"],c["en"])}</strong><small>{t(*c["role"])}</small></span></button>'
 panels+=f'<div class="experience-panel" id="panel-{c["id"]}" role="tabpanel" aria-labelledby="tab-{c["id"]}" data-company-panel="{c["id"]}" {"hidden" if i else ""}><div class="panel-top"><div><h3>{t(*c["role"])}</h3><p>{t(*c["focus"])}</p></div><time>{c["date"]}</time></div>{bullets(c["bullets"])}<div class="panel-links">'+''.join(f'<a href="/projects/{id}/">{t(zh,en)} ↗</a>' for id,zh,en in c['links'])+f'<a class="panel-resume-link" href="/resume/#experience-{c["id"]}">{t("在简历中查看这段经历","See this experience in the resume")} ↗</a></div></div>'
additional='<div class="additional">'+''.join(f'<div class="mini-company">{logo(id)}<div><strong>{t(zh,en)}</strong><small>{t(role,roleen)}</small></div></div>' for id,zh,en,role,roleen in EXTRA)+'</div>'
experience=f'<section class="experience-section" id="experience" data-scope="experience">{sectionhead("02 / EXPERIENCE","在真实问题中，积累判断。","Learning in the real world.")}<div class="experience-shell"><div class="company-tabs" role="tablist" aria-label="实习单位 / Internship company">{tabs}</div><div>{panels}</div></div>{additional}</section>'
about=f'''<section class="about" id="about" data-scope="about"><div><div class="about-title-row"><div class="eyebrow">03 / THE PERSON BEHIND THE WORK</div>{switch()}</div><h2>{t('认真研究，也保持\n对世界的好奇。','A research mind.\nAn open, curious world.')}</h2>{p('从交大的公共管理，到清华的工商管理，我始终对同一个问题感兴趣：变化如何发生，又如何创造价值？','From public administration at Shanghai Jiao Tong to management at Tsinghua, one question keeps me curious: how does change happen, and how does it create value?')}{p('我喜欢在数据中寻找逻辑，也喜欢把想法做成工具。这里记录我的研究、尝试，以及还在继续的问题。','I look for logic in data and enjoy turning ideas into tools. This space collects my research, experiments and questions that are still unfolding.')}<a class="text-link" href="/resume/">{t('我的完整经历','My complete journey')} ↗</a></div><div class="about-right"><div class="interest"><span class="no">01</span><div><h3>{t('研究与构建','Research & build')}</h3>{p('行业研究、财务建模、AI 算力、Agent 与 RAG。','Sector research, financial modeling, AI infrastructure, Agents and RAG.')}</div></div><div class="interest"><span class="no">02</span><div><h3>{t('走进更大的世界','A wider world')}</h3>{p('牛津大学暑期学校；与 OECD 合作赴卢旺达开展数据处理与 AI 能力建设。','Oxford summer school; collaboration with OECD in Rwanda on data processing and AI capabilities.')}</div></div><div class="interest"><span class="no">03</span><div><h3>{t('屏幕之外','Beyond the screen')}</h3>{p('琵琶、素描、国画、健身、历史、旅行与写小说。','Pipa, sketching, Chinese painting, fitness, history, travel and writing fiction.')}</div></div></div></section>'''
contact=f'<section class="contact" id="contact" data-scope="contact"><div><div class="about-title-row"><div class="eyebrow">04 / LET’S CONNECT</div>{switch()}</div><h2>{t("好想法，", "Good ideas start")}<br><em>{t("从一次对话开始。", "with a conversation.")}</em></h2>{p("关于研究、AI，或一个值得探索的新想法。","About research, AI, or a new idea worth exploring.")}</div><a class="email-link" href="mailto:1918621456@qq.com">1918621456@qq.com <span>↗</span></a></section>'
(D/'index.html').write_text(page('谢欣玥 · 研究、战略与 AI','Research, Strategy & AI',HERO+'<main class="wrap">'+featured+experience+capability_section()+about+contact+footer()+'</main>',home=True))
portfolio=f'<section class="page-top" data-scope="intro"><div class="top-line"><span class="eyebrow">THE WORK / 14 PROJECTS</span>{switch()}</div><h1>{t("作品，是思考的另一种语言。","Ideas deserve a tangible form.")}</h1>{p("从行业研究与估值建模，到 AI 应用和实证分析。这里记录问题如何被拆解，以及判断如何形成。","From industry research and valuation to AI applications and empirical analysis. A collection of questions, methods and the thinking behind each conclusion.","lede")}</section>{portfolio_constellation(t,CATEGORIES,PROJECTS,META)}<section data-scope="portfolio"><div class="portfolio-tools"><div class="filters">'+''.join(f'<button data-filter="{id}" class="filter {"active" if id=="all" else ""}" aria-pressed="{str(id=="all").lower()}">{t(zh,en)}</button>' for id,zh,en in [('all','全部','All')]+CATEGORIES)+f'</div><div style="display:flex;gap:20px;align-items:center"><label class="search-wrap">⌕ <input data-project-search aria-label="搜索项目 / Search projects" data-placeholder-zh="搜索项目、方法、关键词" data-placeholder-en="Search work, methods, ideas" placeholder="搜索项目、方法、关键词"></label>{switch()}</div></div><div class="result-count" data-result-count aria-live="polite"></div><div class="projects portfolio-grid">'+''.join(card(pr,i+1) for i,pr in enumerate(PROJECTS))+f'</div><div class="empty-state" data-empty hidden>{t("暂未找到匹配项目，试试其他关键词。","No matching projects. Try another keyword.")}</div></section>'
(D/'portfolio').mkdir(exist_ok=True);(D/'portfolio/index.html').write_text(page('作品集','Portfolio',portfolio,'portfolio'))
# Complete, structured resume with faithful, equally detailed translations.
resume=f'<section class="page-top" data-scope="identity"><div class="top-line"><span class="eyebrow">THE FULL STORY / RESUME</span>{switch()}</div><h1>{t("谢欣玥","Xinyue Xie")} <span class="page-deco">Xinyue Xie / Stella</span></h1>{p("清华大学经管学院 MiM · 上海交通大学行政管理学士","Tsinghua SEM MiM · Shanghai Jiao Tong University, Public Administration","lede")}{p("1918621456@qq.com","1918621456@qq.com","source-note")}<a class="btn secondary" href="/portfolio/">{t("浏览作品集","Explore the portfolio")} ↗</a></section><div class="content-grid"><aside class="sidebar">'+''.join(f'<a href="#{id}">{n} / {t(zh,en)}</a>' for n,id,zh,en in [('01','education','教育背景','Education'),('02','experience-full','实习经历','Experience'),('03','research','科研与项目','Research & Projects'),('04','awards','竞赛奖项','Awards'),('05','practice','实践与技能','Practice & Skills'),('AI','ai-capabilities','AI 能力','AI Capabilities')])+'</aside><div class="prose">'
education=f'<section id="education" data-scope="education">{sectionhead("01 / EDUCATION","教育背景","Education")}'
for zh,en,date,deg,degen in EDU:education+=f'<div class="edu-item"><h3>{t(zh,en)}</h3><div class="edu-date">{date}</div>{p(deg,degen)}</div>'
education+='<div class="academic-stats"><div class="stat"><b>95.28</b><small>'+t('平均学积分 / 100','Average score / 100')+'</small></div><div class="stat"><b>4.19</b><small>GPA / 4.30</small></div><div class="stat"><b>1 / 24</b><small>'+t('专业排名','Major ranking')+'</small></div></div>'
education+=p('荣誉经历：2022—2023、2023—2024 学年国家奖学金（1/50）、上海市奖学金、上海交大校三好学生。','Honors: National Scholarship in both 2022–2023 and 2023–2024 (1/50), Shanghai Municipal Scholarship, and SJTU Three-Good Student recognition.')
education+=f'<h3>{t("专业核心课程","Core courses")}</h3><div class="course-grid">'+''.join('<div>'+t(zh,en)+f'<b>{score}</b></div>' for zh,en,score in COURSES)+'</div>'
education+=p('英语水平：CET-6 628；CET-4 635；全国高校创新英语挑战活动英语翻译赛二等奖。','English: CET-6 628; CET-4 635; Second Prize in the English Translation track of the National College Innovative English Challenge.')+'</section>'
res_exp=f'<section id="experience-full" data-scope="experience">{sectionhead("02 / EXPERIENCE","实习经历","Internships")}'
for c in COMPANIES:
 res_exp+=f'<details class="resume-box" id="experience-{c["id"]}" {"open" if c["id"]=="baidu" else ""}><summary><div class="resume-box-heading">{logo(c.get("logo",c["id"]))}<div><h3>{t(c["zh"],c["en"])}</h3><span>{t(*c["role"])}</span></div><time>{c["date"]}</time><b class="expand-mark">+</b></div></summary><div class="resume-box-content">{bullets(c["bullets"])}<div class="linked-work-heading">{t("这段经历，对应这些作品","The work connected to this experience")} ↗</div>{project_links([link[0] for link in c["links"]])}</div></details>'
res_exp+=f'<h3>{t("其他实习经历","Additional internships")}</h3>'+additional+'</section>'

research=f'<section id="research" data-scope="research">{sectionhead("03 / RESEARCH","科研及项目经历","Research & Projects")}'
research+='<div id="research-academic">'
for prid in ['ai-transformation','housing','ai-research']:
 pr=next(x for x in PROJECTS if x['id']==prid);anchor='research-ai' if prid=='ai-research' else 'research-'+prid
 if prid=='ai-research':research+='</div>'
 research+=f'<details class="resume-box" id="{anchor}"><summary><div class="resume-box-heading"><span class="research-symbol">✳</span><div><h3>{t(*pr["name"])}</h3><span>{t(*pr["type"])}</span></div><b class="expand-mark">+</b></div></summary><div class="resume-box-content">'+p(*pr['sections'][0][2:])+project_links([prid])+'</div></details>'
research+=f'<details class="resume-box" id="research-independent"><summary><div class="resume-box-heading"><span class="research-symbol">↗</span><div><h3>{t("公司研究与案例作品","Company research & case work")}</h3><span>{t("小鹏与中科曙光公司研究 · 三协 LBO 案例","XPeng & Sugon research · Sanxie LBO case")}</span></div><b class="expand-mark">+</b></div></summary><div class="resume-box-content">'+p('作品包括小鹏汽车、中科曙光公司研究，以及三协电机杠杆收购案例。','The work includes XPeng and Sugon company research and the Sanxie Motor leveraged-buyout case.')+project_links(['xpeng','sugon','sanxie'])+'</div></details></section>'
awards=f'<section id="awards" data-scope="awards">{sectionhead("04 / AWARDS","竞赛奖项","Awards & Competitions")}<ul class="award-list">'+''.join(f'<li><span class="award-no">{i+1:02}</span>{t(zh,en)}</li>' for i,(zh,en) in enumerate(AWARDS))+'</ul></section>'
practice=f'<section id="practice" data-scope="practice">{sectionhead("05 / BEYOND THE WORK","实践、技能与兴趣","Practice, Skills & Interests")}<h3>{t("学生工作","Student leadership")}</h3>'+p('任院学生会外联部部长，承担对外联络工作并参与筹办大型活动；任学习委员。','Served as Head of External Relations in the school student union, responsible for external liaison and supporting major events; also served as class academic representative.')+f'<h3>{t("国际实践","International experience")}</h3>'+p('参加牛津大学暑期学校，获学校奖学金支持，任小组长并完成电影拍摄和结业展示；与经合组织（OECD）合作，赴卢旺达协助当地统计局提升数据处理及 AI 应用能力，助力跨国知识共享。','Attended Oxford University summer school with school scholarship support, led a group, and completed a film project and final presentation. Collaborated with OECD in Rwanda to support the local statistics office’s data processing and AI capabilities and cross-border knowledge sharing.')+f'<h3>{t("技能与资格","Skills & certification")}</h3><div class="skills">'+''.join(f'<span>{x}</span>' for x in ['Python','SQL','R','Docker','Git','LangChain','HTML','Dify','Microsoft Office','Wind','iFind'])+'</div>'+p('基金从业资格。','Fund Practitioner Certification.')+f'<h3>{t("爱好","Interests")}</h3>'+p('琵琶、素描、国画、健身、历史、旅行与写小说。','Pipa, sketching, Chinese painting, fitness, history, sightseeing and writing fiction.')+'</section>'
original=''
(D/'resume').mkdir(exist_ok=True)
(D/'resume/index.html').write_text(page('完整简历','Complete Resume',resume+education+res_exp+research+capability_section()+awards+practice+original+'</div></div>','resume'))
# Full-page watermarked reading copies; original files never enter the serving root.
def report_reader(pr):
 zh,en=('小鹏汽车研究报告','XPeng research report') if pr['id']=='xpeng' else ('三协电机投资备忘录','Sanxie investment memorandum')
 pages=READERS[pr['id']]['pages']
 images=''.join(f'<figure class="report-page"><figcaption>{t("第 "+str(i)+" / "+str(len(pages))+" 页","Page "+str(i)+" / "+str(len(pages)))}</figcaption><img src="{item["src"]}" width="{item["width"]}" height="{item["height"]}" alt="{e(zh)} / {e(en)} · {i}" loading="lazy" decoding="async" draggable="false"></figure>' for i,item in enumerate(pages,1))
 return f'<section class="reader-section" data-scope="report"><details class="document-disclosure" id="documents"><summary><span class="document-icon">↗</span><div><h2>{t(zh,en)}</h2><span>{t(str(len(pages))+" 页 · 带水印在线阅读",str(len(pages))+" pages · Watermarked reading copy")}</span></div><span class="expand-mark">+</span></summary><div class="document-content">{p("仅供个人作品展示与在线阅读，未经许可请勿转载。","For portfolio viewing and online reading. Please do not redistribute without permission.","reader-notice")}<div class="report-pages">{images}</div></div></details></section>'
def workbook_reader():
 sheets=READERS['model']['sheets'];options='';panels=''
 for i,sheet in enumerate(sheets):
  options+=f'<option value="{i}" {"selected" if i==2 else ""}>{e(sheet["name"])}</option>'
  figures=''
  for j,item in enumerate(sheet['pages'],1):
   caption=f'{sheet["name"]} · {j} / {len(sheet["pages"])} · {item["rows"]} · {item["columns"]}'
   figures+=f'<figure class="model-page"><figcaption>{e(caption)}</figcaption><div class="model-image-scroll" tabindex="0" role="region" aria-label="{e(caption)}"><img src="{item["src"]}" width="{item["width"]}" height="{item["height"]}" alt="{e(caption)}" loading="lazy" decoding="async" draggable="false"></div></figure>'
  panels+=f'<div data-model-panel="{i}" {"hidden" if i!=2 else ""}>{figures}</div>'
 return f'<section class="reader-section" data-scope="model"><details class="document-disclosure" id="model"><summary><span class="document-icon">↗</span><div><h2>{t("三协电机 LBO 模型","Sanxie Motor LBO Model")}</h2><span>{t("9 个工作表 · 带水印静态阅读","9 worksheets · Watermarked static reading")}</span></div><span class="expand-mark">+</span></summary><div class="document-content"><div class="reader-heading">{p("原模型的计算值按工作表展示；宽表可横向滑动。静态阅读页不提供公式与原件下载。","Browse cached model results by worksheet; scroll horizontally for wide tables. This static reading copy does not provide formulas or the original workbook.","reader-notice")}{switch()}</div><label class="model-sheet-label">{t("选择工作表","Choose a worksheet")}<select data-model-sheet aria-label="工作表 / Worksheet">{options}</select></label>{panels}</div></details></section>'
for pr in PROJECTS:
 id=pr['id'];buttons=''
 if pr.get('reading') in READING_COPIES:buttons=f'<a class="btn" href="#documents">{t("在线阅读报告","Read the report")} ↘</a>'
 if FULL and id=='sanxie':buttons+=f'<a class="btn secondary" href="#model">{t("浏览模型","Explore the model")} ↘</a>'
 body=f'<section class="page-top" data-scope="intro"><div class="top-line"><a class="breadcrumb" href="/portfolio/">← {t("返回作品集","BACK TO PORTFOLIO")}</a>{switch()}</div><div class="project-context-label">{t(*pr["type"])}</div><h1>{t(*pr["name"])}</h1>{p(*pr["sub"],"lede")}{buttons}</section>'+logic_section(pr)+project_abilities(pr)
 if FULL and pr.get('reading'):
  body+=report_reader(pr) if FULL and id in ['xpeng','sanxie'] else reading_section(pr['reading'])
 if FULL and id=='sanxie':body+=workbook_reader() if FULL else reading_section('sanxie-model','model')
 body+=p('谢欣玥 Xinyue Xie · 研究作品仅供在线阅读','Xinyue Xie · Research work for online reading only','print-readonly')
 body+='<a class="back-link" href="/portfolio/">← '+t('返回全部作品','Back to all work')+'</a>'
 target=D/'projects'/id;target.mkdir(exist_ok=True,parents=True);(target/'index.html').write_text(page(*pr['name'],body,'project-'+id))
# Compatibility for previously shared report URLs.
for alias,target,related in [('industry-research','saf',['saf','jiaao','sugon']),('academic','ai-transformation',['ai-transformation','housing'])]:
 targetpage=(D/'projects'/target/'index.html').read_text()
 extra='<section class="legacy-related">'+sectionhead('RELATED WORK','相关作品','Related work')+project_links(related)+'</section>'
 targetpage=targetpage.replace('<a class="back-link"',extra+'<a class="back-link"',1)
 location=D/'projects'/alias;location.mkdir(parents=True,exist_ok=True);(location/'index.html').write_text(targetpage)
# Single-entry file preview. Inline all visuals, fonts fallback locally, routes stay in the frame.
pages={};css=(A/'style.css').read_text();js=(A/'main.js').read_text()
for f in D.rglob('index.html'):
 route='/'+f.parent.relative_to(D).as_posix().strip('.')+'/';route=re.sub('/+','/',route)
 s=f.read_text()
 for stylesheet in ['style.css','constellations.css']:
  s=s.replace('<link rel="stylesheet" href="/assets/'+stylesheet+'">','<style>'+(A/stylesheet).read_text()+'</style>')
 for script in ['main.js','explore.js']:
  s=s.replace('<script src="/assets/'+script+'" defer></script>','<script>document.addEventListener("DOMContentLoaded",()=>{'+(A/script).read_text()+'});</script>')
 for asset in A.rglob('*'):
  if not asset.is_file() or asset.suffix in ['.css','.js','.json']:continue
  old='/assets/'+asset.relative_to(A).as_posix()
  if old not in s:continue
  if not FULL and 'reading' in asset.relative_to(A).parts:
   s=s.replace(old,'./public/assets/'+asset.relative_to(A).as_posix());continue
  if asset.suffix in ['.png','.jpg','.svg','.webp']:
   mime={'.png':'image/png','.jpg':'image/jpeg','.svg':'image/svg+xml','.webp':'image/webp'}[asset.suffix];new='data:'+mime+';base64,'+base64.b64encode(asset.read_bytes()).decode()
  else:new='./dist/assets/'+asset.relative_to(A).as_posix()
  s=s.replace(old,new)
 pages[route]=s
router=(A/'preview-router.js').read_text()
preview='<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>谢欣玥 · 个人网站</title><style>html,body{margin:0;width:100%;height:100%;background:#111b17}iframe#site{display:block;width:100%;height:100%;border:0}</style></head><body><iframe title="谢欣玥个人网站 / Xinyue Xie portfolio" id="site"></iframe><script>const pages='+json.dumps(pages,ensure_ascii=False,separators=(',',':')).replace('</script>','<\\/script>')+';'+router+'</script></body></html>'
(ROOT/('preview.html' if FULL else 'public-preview.html')).write_text(preview)
if not FULL:
 # Relative URLs work both at a domain root and GitHub Pages' /repository/ path.
 # The offline preview above keeps its own absolute-route map unchanged.
 for f in D.rglob('index.html'):
  parent=f.parent.relative_to(D).as_posix()
  def relative_url(match):
   attr,url=match.group(1),match.group(2)
   path,fragment=(url.split('#',1)+[''])[:2] if '#' in url else (url,'')
   relative=posixpath.relpath(path.lstrip('/') or '.',parent)
   if path.endswith('/'):relative=('./' if relative=='.' else relative+'/')
   return attr+'="'+relative+('#'+fragment if fragment else '')+'"'
  markup=re.sub(r'\b(href|src|srcset|data-zh|data-en)="(/(?!/)[^"]*)"',relative_url,f.read_text())
  f.write_text(markup)
 (D/'.nojekyll').write_text('')
 # GitHub's branch publisher serves only this audited public static directory.
 docs=ROOT.parent/'docs'
 if docs.exists():shutil.rmtree(docs)
 shutil.copytree(D,docs)
print('Built',len(pages),'routes;',('local full reading edition' if FULL else 'public showcase edition'),'; preview',round(len(preview)/1024),'KB')
