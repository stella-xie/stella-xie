"""Small, linked navigation constellations within the original dark visual style."""
from math import cos, sin, radians
from html import escape

def home(t):
    hubs=[('resume',250,310,'简历','Resume','经历、教育与技能，连接到我做过的具体工作。','Experience, education and skills, connected to the work.','/resume/'),
          ('portfolio',655,290,'作品集','Portfolio','从一个领域出发，探索报告、模型与项目。','Start with a field and explore reports, models and projects.','/portfolio/')]
    satellites=[
        ('resume',-145,'教育背景','Education','/resume/#education','从交大的公共管理，到清华的管理学学习。','Public administration at SJTU and management at Tsinghua.'),
        ('resume',-93,'实习经历','Experience','/resume/#experience-full','在产业研究、投资分析和业务工具中积累判断。','Research, investment analysis and practical business tools.'),
        ('resume',-30,'技能与实践','Skills & practice','/resume/#practice','数据分析、AI 工具与研究之外的实践。','Data analysis, AI tools and experience beyond research.'),
        ('resume',120,'竞赛奖项','Awards','/resume/#awards','数学建模、商业案例与公共治理中的尝试。','Work in mathematical modeling, business cases and governance.'),
        ('portfolio',-93,'行业研究','Industry','/portfolio/#category-industry','理解算力、能源与新材料的商业逻辑。','Explore the business logic of computing, energy and materials.'),
        ('portfolio',-25,'估值建模','Valuation','/portfolio/#category-model','从经营假设走到现金流与公司价值。','Follow operating assumptions into cash flow and value.'),
        ('portfolio',40,'学术研究','Academic','/portfolio/#category-academic','用数据研究 AI 转型与房价稳定性。','Study AI transformation and housing stability with data.'),
        ('portfolio',100,'AI 应用','AI tools','/portfolio/#category-ai','让检索、分析和业务信息变成可用的工具。','Turn retrieval, analysis and business information into useful tools.')]
    nodes='';paths=''
    centers={h[0]:(h[1],h[2]) for h in hubs}
    for id,x,y,zh,en,hz,he,href in hubs:
        nodes+=f'<a class="sphere-node sphere-hub hub-{id}" data-orbit-hub="{id}" data-cluster="{id}" data-hint-zh="{escape(hz)}" data-hint-en="{escape(he)}" href="{href}" style="left:{x/9}%;top:{y/5.9}%"><span class="sphere-surface"><small>{"01 / EXPERIENCE" if id=="resume" else "02 / THE WORK"}</small><strong>{t(zh,en)}</strong><i aria-hidden="true">↗</i></span></a>'
    for i,(cluster,angle,zh,en,href,hz,he) in enumerate(satellites):
        cx,cy=centers[cluster];rx,ry=(178,198) if cluster=='resume' else (171,197)
        x=cx+rx*cos(radians(angle));y=cy+ry*sin(radians(angle))
        nodes+=f'<a class="sphere-node satellite satellite-{cluster}" data-orbit-node data-cluster="{cluster}" data-cx="{cx}" data-cy="{cy}" data-rx="{rx}" data-ry="{ry}" data-angle="{angle}" data-path="orbit-path-{i}" data-hint-zh="{escape(hz)}" data-hint-en="{escape(he)}" href="{href}" style="left:{x/9}%;top:{y/5.9}%"><span class="sphere-dot" aria-hidden="true"></span><span class="satellite-label">{t(zh,en)}</span></a>'
        paths+=f'<path id="orbit-path-{i}" data-cluster="{cluster}" d="M{cx} {cy}L{x} {y}"/>'
    return f'<div class="constellation" data-constellation><div class="constellation-toolbar"><span>{t("沿着兴趣，发现联系。","Follow a question. Find connections.")}</span><button data-orbit-reset aria-label="重置星图 / Reset constellation">↺</button></div><div class="constellation-canvas"><svg viewBox="0 0 900 590" preserveAspectRatio="none" aria-hidden="true"><g class="orbit-rings"><ellipse cx="250" cy="310" rx="195" ry="215"/><ellipse cx="655" cy="290" rx="187" ry="215"/><path d="M250 310C370 240 525 390 655 290"/></g><g class="orbit-rays">{paths}</g><g class="sky-marks"><path d="M455 55v12m-6-6h12M454 521v10m-5-5h10M48 380v8m-4-4h8"/></g></svg>{nodes}</div><p class="constellation-caption" data-constellation-hint>{t("点击星球进入内容，也可以拖动空白处，换一个角度探索。","Select a planet to explore, or drag the space to shift the view.")}</p></div>'

def portfolio(t,categories,projects,meta):
    coords=[(130,135),(275,307),(760,135),(625,307),(450,49)]
    planets='';lines='';groups=''
    for (id,zh,en),(x,y) in zip(categories,coords):
        related=[p for p in projects if id in meta[p['id']]['categories']]
        planets+=f'<button class="field-orbit" data-filter="{id}" aria-pressed="false" style="left:{x/9}%;top:{y/4.05}%"><span class="field-dot" aria-hidden="true"></span><strong>{t(zh,en)}</strong><small>{len(related)} {t("项作品","works")}</small></button>'
        lines+=f'<path data-field-line="{id}" d="M450 193L{x} {y}"/>'
        groups+=f'<div data-map-work="{id}" hidden>'+''.join(f'<button data-work-trigger="{p["id"]}">{t(p["name"][0].split("：")[0],p["name"][1].split(":")[0])} <span aria-hidden="true">↗</span></button>' for p in related)+'</div>'
    return f'<section class="portfolio-sky" aria-label="作品星图 / Portfolio constellation"><div class="portfolio-sky-head"><span class="eyebrow">THE WORK / CONNECTED</span><p>{t("选择一个小球，沿着作品看见研究方法。","Choose a field to explore the work and its methods.")}</p></div><div class="field-canvas"><svg viewBox="0 0 900 405" preserveAspectRatio="none" aria-hidden="true"><ellipse cx="450" cy="193" rx="325" ry="140"/>{lines}</svg><button class="field-center" data-filter="all" aria-pressed="true"><small>PORTFOLIO</small><strong>{t("作品集","The work")}</strong><span>{t("查看全部","View all")} ↗</span></button>{planets}</div><div class="map-work-list"><div data-map-work="all">'+''.join(f'<button data-work-trigger="{p["id"]}">{t(p["name"][0].split("：")[0],p["name"][1].split(":")[0])} <span aria-hidden="true">↗</span></button>' for p in projects[:4])+f'</div>{groups}</div></section>'
