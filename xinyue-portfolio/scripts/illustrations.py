"""Code-native illustrations: diagrams summarize supplied project content, not new data."""
from pathlib import Path
from html import escape
import textwrap
# Node: short Chinese label, English label, Chinese note, English note, icon.
DIAGRAMS={
'xpeng':dict(kind='branch',title=('价值如何形成？','Where does value come from?'),caption=('行业、业务与现金流的研究框架','A framework connecting the industry, businesses and cash flow'),nodes=[('整车业务','Vehicle business','产品、销量与盈利基础','Products, sales and operating foundations','car'),('技术变现','Technology monetization','技术授权与服务收入','Licensing and service revenue','chip'),('新业务','New businesses','Robotaxi、机器人与飞行汽车','Robotaxi, robotics and flying cars','network')],output=('现金流与估值','Cash flow & valuation','结合现金约束、业务兑现与股权归属','Cash constraints, commercialization and attributable ownership','chart')),
'ai-compute':dict(kind='flow',title=('从产业链走向需求判断','From the value chain to demand'),caption=('AI 算力专题研究框架','AI computing research framework'),nodes=[('产业链梳理','Map the value chain','系统梳理 AI 算力全产业链','Map the AI computing ecosystem','layers'),('竞争格局','Competitive landscape','分析国产芯片竞争格局','Analyze domestic chip competition','chip'),('需求变化','Changing demand','建设 → 消纳与场景；关注 Agent 工作流','Build-out → utilization and use cases; Agent workloads','search')]),
'sanxie':dict(kind='branch',title=('模型回报依赖哪些条件？','What underpins the modeled return?'),caption=('经营、融资与退出共同决定股东现金流；数值为案例测算','Operating, financing and exit assumptions drive case-model cash flows'),nodes=[('经营假设','Operating assumptions','收入、毛利率、资本开支与营运资金','Revenue, margins, capex and working capital','chart'),('融资安排','Financing','债务摊还、最低现金与追加股本','Debt service, minimum cash and follow-on equity','layers'),('退出假设','Exit assumptions','退出 EBITDA 与估值倍数','Exit EBITDA and valuation multiple','search')],output=('股东现金流 → IRR / MOIC','Sponsor cash flows → IRR / MOIC','基准情景：28.63% IRR · 3.40× MOIC','Base case: 28.63% IRR · 3.40× MOIC','chart')),
'ai-leads':dict(kind='flow',title=('从分散信号到商机推荐','From scattered signals to leads'),caption=('商机识别工作流示意','Sales intelligence workflow'),nodes=[('多源数据','Multiple sources','备案、融资、招聘等 9 路数据','Nine sources, including filings, funding and hiring','layers'),('信息融合','Data integration','实体匹配与 CRM 校验','Entity matching and CRM validation','network'),('评分 Agent','Scoring Agent','识别企业商机，生成推荐路径','Identify opportunities and recommended paths','chip'),('业务使用','Business use','定期推送、前后端与持续运维','Regular recommendations and full-stack maintenance','document')]),
'real-assets':dict(kind='branch',title=('把资产放回现金流','Underwriting the cash flows'),caption=('不动产项目分析与估值框架','Real-asset analysis and valuation framework'),nodes=[('资产基本面','Asset fundamentals','行业、区位、需求与运营表现','Industry, location, demand and operations','building'),('交易结构','Transaction structure','ABS / REITs、夹层与资金分配','ABS / REITs, mezzanine and distributions','layers'),('持有与退出','Holding & exit','运营、融资和退出假设','Operating, financing and exit assumptions','chart')],output=('现金流与杠杆收益','Cash flow & leveraged returns','现金流测算 · IRR · 敏感性分析','Cash-flow modeling · IRR · Sensitivities','chart')),
'industry-research':dict(kind='parallel',title=('三条独立的研究线','Three distinct research tracks'),caption=('行业判断与公司估值分别展开，不构成先后因果关系','Separate sector and company analyses, rather than a sequential causal chain'),nodes=[('SAF 行业','SAF industry','政策、技术壁垒与原料供给','Policy, technological barriers and feedstock','globe'),('中科曙光','Sugon','算力业务拆分与 SOTP 估值','Computing segments and SOTP valuation','chip'),('嘉澳股份','Jiaao Environmental','双业务布局与 PB 估值','Business mix and PB valuation','chart')]),
'ai-research':dict(kind='components',title=('研究系统的组成','Components of the research system'),caption=('系统组成示意，展示各技术在项目中的角色','A component overview showing the role of each technology'),nodes=[('Python','Python','工具与工作流','Tools and workflows','document'),('OpenAI GPT','OpenAI GPT','语言模型能力','Language-model capabilities','chip'),('RAG + 向量数据库','RAG + vector database','知识检索','Knowledge retrieval','search'),('记忆架构','Memory architecture','组织研究上下文','Organize research context','layers')],output=('金融研报生成系统','Financial research system','大语言模型应用项目','An LLM application project','network')),
'academic':dict(kind='lanes',title=('两篇论文，两条分析路径','Two papers, two analytical paths'),caption=('研究问题、方法与发现一一对应','Research questions, methods and findings remain distinct'),lanes=[
 [('AI 转型与 ROA','AI transformation & ROA','研究企业转型的隐性成本','Study the hidden costs of transformation','search'),('实证方法','Empirical methods','机器学习词典 + 固定效应面板回归','ML dictionary + fixed-effects panel regression','layers'),('研究发现','Research finding','对 ROA 的抑制效应，并进行稳健性检验','Negative ROA relationship and robustness checks','chart')],
 [('房价稳定性','Housing stability','基本面与政策有效性','Fundamentals and policy effectiveness','building'),('机器学习方法','Machine-learning methods','爬虫数据 + 决策树','Web-scraped data + decision trees','network'),('研究产出','Research output','稳定性预测模型；入选 APNHR 论坛','Stability prediction model; accepted by APNHR','document')]])}

def icon(name,x,y,color='#82926d'):
 paths={
 'layers':'<path d="M0 -10L15 -3L0 4L-15 -3Z M-15 4L0 11L15 4 M-15 11L0 18L15 11"/>',
 'chip':'<rect x="-11" y="-11" width="22" height="22" rx="3"/><rect x="-5" y="-5" width="10" height="10" rx="1"/><path d="M-17 -7h6M-17 0h6M-17 7h6M11 -7h6M11 0h6M11 7h6M-7 -17v6M0 -17v6M7 -17v6M-7 11v6M0 11v6M7 11v6"/>',
 'chart':'<path d="M-15 -13v28h31M-9 9V0M0 9V-6M9 9V-14"/>',
 'search':'<circle cx="-3" cy="-3" r="10"/><path d="M5 5l11 11"/>',
 'network':'<circle cx="0" cy="0" r="5"/><circle cx="-14" cy="-12" r="3"/><circle cx="14" cy="-12" r="3"/><circle cx="-14" cy="12" r="3"/><circle cx="14" cy="12" r="3"/><path d="M-11 -10l7 6M11 -10l-7 6M-11 10l7 -6M11 10l-7 -6"/>',
 'document':'<path d="M-11 -16H5l8 8v24h-24Z M5 -16v8h8 M-5 -2h12M-5 5h12M-5 12h8"/>',
 'building':'<path d="M-12 16v-30h24v30M-17 16h34M-6 -7h3M4 -7h3M-6 0h3M4 0h3M-6 7h3M4 7h3M-3 16v-5h6v5"/>',
 'car':'<path d="M-17 8v-9l5 -9h24l5 9v9H-17M-13 -1h26M-10 -10l-3 9M10 -10l3 9M-17 8v6h6V8M11 8v6h6V8M-12 4h4M8 4h4"/>',
 'globe':'<circle r="16"/><ellipse rx="7" ry="16"/><path d="M-15 -5h30M-15 5h30"/>'}
 return f'<g transform="translate({x} {y})" fill="none" stroke="{color}" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round">{paths.get(name,paths["document"])}</g>'
def lines(text,limit):
 result=[];line='';weight=0
 for word in text.split(' ') if ' ' in text and not any('\u4e00'<=c<='\u9fff' for c in text) else list(text):
  w=sum(1 if ord(c)>255 else .53 for c in word)+(0.53 if line and ' ' in text and not any('\u4e00'<=c<='\u9fff' for c in text) else 0)
  if line and weight+w>limit:result.append(line);line='';weight=0
  if line and ' ' in text and not any('\u4e00'<=c<='\u9fff' for c in text):line+=' '
  line+=word;weight+=w
 if line:result.append(line)
 return result

def textnode(x,y,text,size=14,color='#64765a',limit=22,weight=400,center=False):
 ls=lines(text,limit)
 return '<text x="%s" y="%s" font-size="%s" font-weight="%s" fill="%s"%s>'%(x,y,size,weight,color,' text-anchor="middle"' if center else '')+''.join(f'<tspan x="{x}" dy="{0 if i==0 else round(size*1.55,1)}">{escape(line)}</tspan>' for i,line in enumerate(ls))+'</text>'
def box(node,x,y,w,h,lang,index=0,highlight=False):
 label=node[0 if lang=='zh' else 1];note=node[2 if lang=='zh' else 3];color='#9680ac' if highlight else '#879b70'
 result=f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="14" fill="{"#eae2f2" if highlight else "#f9faf2"}" stroke="{"#cec0db" if highlight else "#d1dcc3"}"/>'
 result+=f'<circle cx="{x+30}" cy="{y+31}" r="19" fill="{"#d9cbe6" if highlight else "#e9efd9"}"/>'+icon(node[4],x+30,y+30,color)
 if w<200:
  result+=textnode(x+17,y+73,label,12.5,'#4f6047',(w-34)/12.5,500)
  result+=textnode(x+17,y+116,note,10.5,'#8a957d',(w-34)/10.5)
 else:
  result+=textnode(x+58,y+36,label,14,'#4f6047',max(4,(w-76)/14),500)
  result+=textnode(x+20,y+76,note,11.5,'#8a957d',max(13,(w-40)/11.5))
 return result

def arrow(x1,y1,x2,y2,dash=False):return f'<path d="M{x1} {y1} L{x2} {y2}" fill="none" stroke="#b4a1c8" stroke-width="1.5" {"stroke-dasharray=\"4 5\"" if dash else ""} marker-end="url(#arr)"/>'

def make(prid,spec,lang,mobile=False):
 kind=spec['kind'];W=380 if mobile else 960;H=600 if mobile else 360
 if kind=='flow':H=(len(spec['nodes'])*136+95) if mobile else 340
 if kind=='parallel':H=515 if mobile else 340
 if kind=='lanes':H=990 if mobile else 465
 if kind=='components':H=655 if mobile else 460
 parts=[]
 parts.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-labelledby="title desc"><title id="title">{escape(spec["title"][lang=="en"])}</title><desc id="desc">{escape(spec["caption"][lang=="en"])}</desc><defs><linearGradient id="bg" x2="1" y2="1"><stop stop-color="#eef1e4"/><stop offset="1" stop-color="#ebe5f2"/></linearGradient><marker id="arr" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M1 1L7 4L1 7" fill="none" stroke="#b4a1c8" stroke-width="1.2"/></marker><pattern id="dots" width="16" height="16" patternUnits="userSpaceOnUse"><circle cx="1" cy="1" r=".55" fill="#a9b699" opacity=".25"/></pattern></defs><rect width="{W}" height="{H}" rx="20" fill="url(#bg)"/><rect width="{W}" height="{H}" rx="20" fill="url(#dots)"/><g font-family="Arial, PingFang SC, Microsoft YaHei, sans-serif">')
 parts.append(textnode(25 if mobile else 35,31 if mobile else 35,'RESEARCH NOTES / '+prid.upper(),8.5,'#9c8eaa',60))
 if kind=='flow':
  n=len(spec['nodes'])
  if mobile:
   for i,node in enumerate(spec['nodes']):
    y=60+i*136;parts.append(box(node,30,y,320,112,lang,i,i==n-1))
    if i<n-1:parts.append(arrow(190,y+112,190,y+130))
  else:
   gap=24;w=(890-gap*(n-1))/n
   for i,node in enumerate(spec['nodes']):
    x=35+i*(w+gap);parts.append(box(node,x,92,w,150,lang,i,i==n-1))
    if i<n-1:parts.append(arrow(x+w+3,166,x+w+gap-3,166))
 elif kind=='branch':
  if mobile:
   for i,node in enumerate(spec['nodes']):
    y=57+i*128;parts.append(box(node,25,y,296,108,lang,i));parts.append(f'<path d="M321 {y+54}H349" stroke="#b4a1c8" fill="none" stroke-width="1.4"/>')
   parts.append('<path d="M349 111V462H190V477" fill="none" stroke="#b4a1c8" stroke-width="1.5" marker-end="url(#arr)"/>');parts.append(box(spec['output'],25,485,330,91,lang,highlight=True))
  else:
   for i,node in enumerate(spec['nodes']):
    x=35+i*303;parts.append(box(node,x,63,284,127,lang,i));parts.append(f'<path d="M{x+142} 190V214H480" stroke="#b4a1c8" fill="none" stroke-width="1.4"/>')
   parts.append(arrow(480,214,480,237));parts.append(box(spec['output'],260,245,440,91,lang,highlight=True))
 elif kind=='parallel':
  for i,node in enumerate(spec['nodes']):parts.append(box(node,25 if mobile else 35+i*303,58+i*143 if mobile else 80,330 if mobile else 284,126 if mobile else 175,lang,i,i==1))
 elif kind=='components':
  boxes=[];connectors=[]
  if mobile:
   boxes.append(box(spec['output'],25,60,330,112,lang,highlight=True))
   for i,node in enumerate(spec['nodes']):
    x=25+(i%2)*173;y=221+(i//2)*181;boxes.append(box(node,x,y,157,157,lang,i))
    if i<2:path=f'M190 172V197H{x+78}V{y}'
    else:
     edge=14 if i%2==0 else 366;target=25 if i%2==0 else 355
     path=f'M190 172V196H{edge}V{y+78}H{target}'
    connectors.append(f'<path d="{path}" fill="none" stroke="#c4b5d1" stroke-width="1.2" stroke-dasharray="4 4"/>')
  else:
   boxes.append(box(spec['output'],310,175,340,107,lang,highlight=True))
   for i,node in enumerate(spec['nodes']):
    x=35 if i%2==0 else 710;y=65 if i<2 else 283;boxes.append(box(node,x,y,215,133,lang,i));sx=x+215 if i%2==0 else x;tx=310 if i%2==0 else 650
    connectors.append(f'<path d="M{sx} {y+65}H{(sx+tx)/2}V228H{tx}" fill="none" stroke="#c4b5d1" stroke-width="1.3" stroke-dasharray="4 5"/>')
  parts.extend(connectors);parts.extend(boxes)
 elif kind=='lanes':
  for j,lane in enumerate(spec['lanes']):
   if mobile:
    top=50+j*465;parts.append(textnode(25,top+13,('论文 ' if lang=='zh' else 'PAPER ')+str(j+1),9,'#9c86ad',40))
    for i,node in enumerate(lane):
     y=top+28+i*135;parts.append(box(node,30,y,320,112,lang,i,j==1))
     if i<2:parts.append(arrow(190,y+112,190,y+129))
   else:
    top=60+j*192;parts.append(textnode(35,top+5,('论文 ' if lang=='zh' else 'PAPER ')+str(j+1),9,'#9c86ad',40))
    for i,node in enumerate(lane):
     x=35+i*303;parts.append(box(node,x,top+20,284,141,lang,i,j==1))
     if i<2:parts.append(arrow(x+287,top+89,x+300,top+89))
 parts.append('</g><defs><pattern id="signature" width="380" height="145" patternUnits="userSpaceOnUse" patternTransform="rotate(-19)"><text x="14" y="68" fill="#5b5268" opacity=".13" font-size="14" font-family="Arial, sans-serif">谢欣玥 Xinyue Xie · READ ONLY</text></pattern></defs>')
 parts.append(f'<rect width="{W}" height="{H}" fill="url(#signature)" pointer-events="none"/><text x="{W-20}" y="{H-12}" text-anchor="end" font-family="Arial, sans-serif" font-size="8" fill="#8f8298">© Xinyue Xie · 仅供阅读 / READ ONLY</text></svg>');return ''.join(parts)

def generate(directory):
 directory.mkdir(parents=True,exist_ok=True)
 for id,spec in DIAGRAMS.items():
  for lang in ['zh','en']:
   for mobile in [False,True]:
    (directory/f'{id}-{lang}{"-mobile" if mobile else ""}.svg').write_text(make(id,spec,lang,mobile))
