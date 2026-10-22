# -*- coding: utf-8 -*-
"""Visitor-facing bilingual content. Private review notes are never imported."""
COMPANIES = [{'id': 'baidu',
  'logo': 'baidu',
  'zh': '百度',
  'en': 'Baidu',
  'role': ['AI 战略实习生', 'AI Strategy Intern'],
  'date': '2026.03 — 2026.07',
  'focus': ['算力研究 · 政府资金 · 商机 Agent', 'AI infrastructure · Government funding · Sales intelligence'],
  'bullets': [('算力产业与商业化研究：系统梳理 AI 算力产业链及国产芯片竞争格局，结合芯片性能、软件生态、系统交付和客户需求分析商业化条件。研究关注国产算力需求从建设走向消纳与应用场景的变化，以及 Agent 工作流中 CPU '
               '承担调度、工具调用等任务的重要性。',
               'Mapped the AI computing value chain and domestic chip competition, examining hardware, software ecosystems, delivery and '
               'customer needs. Studied the shift from construction toward utilization and use cases, and the importance of CPUs for '
               'orchestration and tool calls in Agent workflows.'),
              ('政府资金与竞争研究：完成政府资金专题研究，梳理政府四本账及专项债等资金工具的核心逻辑，分析资金扩容背景下的项目要求；通过访谈研究科大讯飞等友商的业务模式，为政务、交通等领域的战略分析提供支持。',
               'Studied government funding, including the four budget accounts and special-purpose bonds, and examined project '
               'requirements alongside funding expansion. Used competitor interviews, including iFlytek, to support government and '
               'transportation strategy research.'),
              ('销售线索库与 Agent 搭建：从零搭建 Token 销售线索库，整合备案、融资、招聘等九路数据，通过多源信息融合、企业实体匹配与 CRM 校验形成企业记录；构建商机识别评分 Agent 和推荐路径，覆盖 3700 '
               '余家企业，并完成前后端搭建、优质线索定期推送及持续运维。',
               'Built a Token sales intelligence database from scratch, integrating nine sources including filings, funding and hiring. '
               'Combined entity matching and CRM validation with an opportunity-scoring Agent and recommended paths, covering more than '
               '3,700 companies. Built and maintained the frontend and backend and delivered regular lead recommendations.'),
              ('战略规划支持：参与公司战略规划，开展政务、交通及宏观等领域的战略刷新，整理政策、市场和竞争信息，支持业务判断。',
               'Contributed to corporate strategic planning and strategy refreshes in government, transportation and macroeconomic themes, '
               'organizing policy, market and competitive information to support business decisions.')],
  'links': [('ai-compute', '算力产业研究', 'AI computing research'),
            ('government-funding', '政府资金专题', 'Government funding'),
            ('ai-leads', '商机识别 Agent', 'Sales intelligence Agent')]},
 {'id': 'hony',
  'logo': 'hony',
  'zh': '弘毅投资',
  'en': 'Hony Capital',
  'role': ['不动产投资实习生', 'Real Estate Investment Intern'],
  'date': '2025.09 — 2026.01',
  'focus': ['资产研究 · 交易结构 · 现金流', 'Asset research · Transaction structures · Cash flow'],
  'bullets': [('资产研究与交易分析：参与 ABS 与 REITs 项目研究，从行业、区位、需求和运营表现等维度分析资产，梳理交易架构与夹层结构，并搭建估值和现金流模型，测算持有期间的投资收益及现金分配。',
               'Contributed to ABS and REITs research, analyzing industry, location, demand and operations. Assessed transaction and '
               'mezzanine structures and built valuation and cash-flow models for interim investment returns and cash distributions.'),
              ('杠杆回报与情景测算：结合运营、融资和退出假设，测算项目运营六年及持有至到期两种情景下的内部收益率（IRR），并开展敏感性分析；参与筛选长三角、西南地区物流资产及上海、北京商改住项目，所筛选项目的资本化率高于 7%，模型 IRR 高于 10%。',
               'Combined operating, financing and exit assumptions to calculate leveraged IRRs for six-year and hold-to-maturity scenarios '
               'and ran sensitivities. Screened logistics assets in the Yangtze River Delta and southwestern China and '
               'commercial-to-residential projects in Shanghai and Beijing, with screened cap rates above 7% and modeled IRRs above 10%.'),
              ('投资材料与尽调支持：整理行业研究、投资备忘录和交易材料，协助对接外部机构，推进保密协议签署及尽调资料准备。',
               'Prepared industry research, investment memoranda and transaction materials, coordinating with external parties on '
               'confidentiality agreements and due-diligence materials.')],
  'links': [('real-assets', '不动产投资与建模', 'Real asset investment & modeling')]},
 {'id': 'citic',
  'logo': 'citic',
  'zh': '中信证券',
  'en': 'CITIC Securities',
  'role': ['能源化工行业研究实习生', 'Energy & Chemicals Research Intern'],
  'date': '2025.02 — 2025.07',
  'focus': ['SAF · 能源转型 · 公司研究', 'SAF · Energy transition · Company research'],
  'bullets': [('可持续航空燃料行业研究：以欧盟对生物柴油加征关税为背景，研究可持续航空燃料（SAF）的技术壁垒、产品附加值和碳减排价值，结合双重碳积分属性及中国餐厨废油资源条件分析产业机会；原研究测算 2030 年全球市场规模为 2266 亿元。',
               'Studied sustainable aviation fuel (SAF) in the context of EU tariffs on biodiesel, examining technology barriers, '
               'value-added economics, carbon-credit attributes and China’s waste cooking oil resources. The historical research estimated '
               'a RMB 226.6 billion global market for 2030.'),
              ('嘉澳股份公司研究：分析嘉澳股份（603822.SH）生物质能源与环保增塑剂的双业务布局，评估其战略转型中的潜在竞争力；结合 100 万吨在建项目、政策支持、实控人增持及大客户参与等因素形成公司判断，并在当时的研究框架下给予 4.6 '
               '倍市净率（PB）估值。',
               'Analyzed Jiaao Environmental (603822.SH), considering biomass energy and eco-friendly plasticizers, a million-tonne '
               'project under construction, policy support, controlling-shareholder purchases and major-customer participation. Applied a '
               '4.6x price-to-book multiple in the historical research framework.')],
  'links': [('saf', 'SAF 行业研究', 'SAF industry research'), ('jiaao', '嘉澳股份研究', 'Jiaao Environmental')]},
 {'id': 'fosun',
  'logo': 'fosun',
  'zh': '复星创富',
  'en': 'Fosun Capital',
  'role': ['新材料投资实习生', 'Advanced Materials Investment Intern'],
  'date': '2024.10 — 2025.02',
  'focus': ['新材料产业链 · 招商研究 · 品牌出海', 'Advanced materials · Investment attraction · Overseas expansion'],
  'bullets': [('品牌出海战略研究：撰写集团旗下日化品牌出海战略报告，聚焦东南亚与中东两大市场，分析市场进入和合作路径，为海外业务拓展提供研究支持。',
               'Wrote an overseas expansion strategy report for a group-owned personal-care brand, focusing on Southeast Asia and the '
               'Middle East and examining market-entry and partnership routes.'),
              ('新材料产业链与招商研究：围绕武汉某区新材料全产业链布局，提出“光谷＋车谷”双核驱动战略，构建“链主企业＋反向配套”招商模型，完成 100 余页深度研究报告；研究成果为争取数十万元专项资金提供支持。',
               'Researched the advanced-materials value chain for a district in Wuhan. Proposed an Optics Valley–Auto Valley dual-engine '
               'strategy and an anchor-company-led, backward-supply-chain investment-attraction model. Completed a report of more than 100 '
               'pages; the research supported efforts to secure dedicated funding of several hundred thousand renminbi.')],
  'links': [('materials', '新材料产业链与招商', 'Advanced materials & investment attraction'),
            ('overseas', '日化品牌出海战略', 'Personal-care brand expansion')]},
 {'id': 'citic-ipo',
  'logo': 'citic',
  'zh': '中信证券',
  'en': 'CITIC Securities',
  'role': ['生物医药组 IPO 实习生', 'Healthcare IPO Intern'],
  'date': '2024.02 — 2024.05',
  'focus': ['IPO 底稿 · 可比公司 · 财务核查', 'IPO working papers · Comparables · Financial review'],
  'bullets': [('可比公司与申报资料整理：搜集国内外可比公司的基本情况、产品、财务数据和销售渠道，提炼核心竞争优势并制作展示材料，整理和更新招股说明书底稿；完成 ABS 项目底稿包制作，归类整合 70 余项细分文件。',
               'Researched domestic and international comparable companies, covering products, financials and sales channels; distilled '
               'competitive advantages into presentations and updated prospectus working papers. Prepared an ABS project working-paper '
               'package, classifying and integrating more than 70 detailed files.'),
              ('财务报表与指标更新：根据公司会计提供的资料更新三张财务报表，计算扣除非经常性损益后的归母净利润、复合年增长率（CAGR）等指标，为项目分析和材料更新提供支持。',
               'Updated the three financial statements using materials provided by the company’s accounting team and calculated recurring '
               'net profit attributable to the parent and compound annual growth rates.'),
              ('核查与项目执行支持：整理函证及银行回单，使用 Excel 的 VLOOKUP 等工具制作 15 余份控制表，并协助开展存货盘点。',
               'Organized confirmations and bank receipts, built more than 15 control schedules using Excel tools such as VLOOKUP, and '
               'assisted with inventory counts.')],
  'links': []},
 {'id': 'qingtong',
  'logo': 'qingtong',
  'zh': '青桐资本',
  'en': 'PhoenixTree Capital',
  'role': ['硬科技投资助理实习生', 'Hard Technology Investment Assistant Intern'],
  'date': '2023.07 — 2023.09',
  'focus': ['商业计划书 · 路演 · 项目资料', 'Business plans · Roadshows · Project data'],
  'bullets': [('商业计划书制作：参与光伏、柔性智能工厂等领域硬科技企业的商业计划书制作，梳理投资亮点、市场规模、核心产品与技术及可比公司，完成三份商业计划书并以 PPT 进行可视化呈现。',
               'Contributed to three business plans for hard-technology companies, including photovoltaics and flexible smart factories. '
               'Organized investment highlights, market sizing, products and technology, and comparable-company analysis into visual '
               'presentations.'),
              ('路演与融资支持：参与八个项目的路演支持，提出展示与沟通建议并获采纳；参与支持的项目中，四个完成融资，融资总额达 3 亿元。',
               'Supported roadshows for eight projects and provided presentation and communication recommendations that were adopted. Four '
               'of the supported projects completed financings totaling RMB 300 million.'),
              ('项目资料整合：整理企业股权架构、财务及专利信息，形成项目资料包（Datapack），并梳理关键股权变动时点的信息。',
               'Compiled ownership, financial and patent information into project data packs and organized information around key '
               'ownership changes.')],
  'links': []}]

EXTRA = [('greenwoods', '景林资本', 'Greenwoods', '有色组', 'Metals & Mining'), ('bytedance', '字节跳动', 'ByteDance', '电商运营', 'E-commerce Operations')]

EDU = [('清华大学（保研）· 经济与管理学院',
  'Tsinghua University · School of Economics and Management',
  '2026.08 — 2028.06',
  '工商管理硕士 MiM',
  'Master in Management · Recommended admission'),
 ('上海交通大学 · 国际与公共事务学院',
  'Shanghai Jiao Tong University · School of International and Public Affairs',
  '2022.09 — 2026.06',
  '行政管理（城市管理）',
  'Bachelor of Public Administration · Urban Management')]

COURSES = [('微积分基础', 'Calculus', 100),
 ('因果推断', 'Causal Inference', 100),
 ('大数据分析', 'Big Data Analysis', 100),
 ('微观经济学', 'Microeconomics', 97),
 ('宏观经济学', 'Macroeconomics', 96),
 ('管理学原理', 'Principles of Management', 96),
 ('定性研究方法', 'Qualitative Research Methods', 95),
 ('多元统计分析', 'Multivariate Statistics', 94)]

AWARDS = [('第 14 届全国大学生数学竞赛三等奖', 'Third Prize · 14th National College Mathematics Competition'),
 ('华数杯国际大学生数学建模大赛全国二等奖', 'National Second Prize · Huashu Cup International Mathematical Modeling Competition'),
 ('美赛 H 奖', 'Honorable Mention · Mathematical Contest in Modeling / ICM'),
 ('第 6 届复旦国际万花筒挑战赛冠军', 'Champion · 6th Fudan International Case Competition'),
 ('第 12 届北大光华管理案例大赛全国九强', 'National Top 9 · 12th PKU Guanghua Management Case Competition'),
 ('高金峰会三等奖', 'Third Prize · SAIF Summit'),
 ('国际大学生创新大赛上海赛区金奖', 'Shanghai Gold Prize · International College Innovation Competition'),
 ('上证杯决赛三等奖', 'Third Prize in Finals · Shanghai Securities Cup'),
 ('第 4 届美团商业分析精英大赛优秀案例', 'Outstanding Case · 4th Meituan Business Analytics Elite Competition'),
 ('第 9 届全国大学生城市治理案例挑战大赛一等奖', 'First Prize · 9th National College Urban Governance Case Challenge'),
 ('全国公共治理人工智能提示词邀请赛一等奖', 'First Prize · National Public Governance AI Prompting Invitational')]

PROJECTS = [{'id': 'xpeng',
  'category': 'industry',
  'type': ['公司研究 · 26 页', 'Company research · 26 pages'],
  'year': '2026',
  'name': ['小鹏汽车：超越整车的价值', 'XPeng: Beyond the vehicle'],
  'sub': ['技术优势怎样转化为利润与股东价值？', 'How do technical advantages become profit and shareholder value?'],
  'desc': ['把技术、销量、利润和现金流分开检验，才能判断哪些增长真正属于股东。',
           'Technology, sales, profit and cash flow must be examined separately to understand which growth creates shareholder value.'],
  'cover': 'xpeng',
  'tags': ['26-page report', 'FCFF / FCFE', 'SOTP'],
  'files': [],
  'sections': [('核心判断',
                'Core argument',
                '小鹏的研究不能停留在技术领先或销量增长上。我把整车业务、技术服务和新业务分别放回各自的盈利与现金流条件中分析：整车需要检验产品结构和毛利率，技术服务需要区分项目收入与可持续收入，机器人等新业务则需要核对商业化阶段、实际持股与融资稀释。估值部分用现金流模型和分业务估值相互核对，关注技术优势在什么条件下才能转化为上市公司股东可获得的价值。',
                'The XPeng study goes beyond technology leadership and sales growth. I examine vehicles, technology services and new '
                'ventures against their own profitability and cash-flow requirements. Vehicles require scrutiny of product mix and '
                'margins; services require a distinction between project revenue and recurring income; emerging ventures require checks on '
                'commercialization, ownership and dilution. Cash-flow and segment valuations then test the conditions under which '
                'technical strengths can create value attributable to listed shareholders.'),
               ('分析过程',
                'Analytical process',
                '从行业需求和产品位置开始，区分销量的短期驱动与技术能力的长期兑现，避免把技术领先直接等同于商业成功。\n'
                '\n'
                '拆开利润来源，检查整车与高毛利技术服务各自的贡献，以及项目收入能否持续。\n'
                '\n'
                '对新业务分别判断商业化、资金需求和实际权益，不把技术共用理解成商业化同步，也不直接把全部业务估值相加。\n'
                '\n'
                '以一致的口径连接经营假设、现金流和分部估值，最后列出需要持续跟踪的验证条件。',
                'Locate the company within demand and product segments, separating near-term sales drivers from long-term technical '
                'monetization.\n'
                '\n'
                'Separate vehicle and high-margin service contributions, and examine whether project-based revenue can continue.\n'
                '\n'
                'Assess each venture’s commercialization, funding and ownership separately; shared technology does not imply equal '
                'commercial readiness or fully attributable value.\n'
                '\n'
                'Link operating assumptions, cash flow and segment values on consistent terms, then identify what must be monitored.'),
               ('关键证据',
                'Supporting evidence',
                '报告做了一个条件情景：整车毛利率不变时，技术服务收入占比从 13.7% 降到 8%，综合毛利率约从 20.7% 降至 17.1%。这个差异说明，高毛利服务收入的持续性会明显影响对盈利质量的判断，不能只看整车销量。见原报告第 18–19 '
                '页；这是原报告的情景分析，并非本轮更新后的业绩预测。',
                'In a report scenario holding vehicle margins constant, a reduction in the service revenue share from 13.7% to 8% lowers '
                'the blended gross margin from about 20.7% to 17.1%. The comparison shows why service continuity matters to earnings '
                'quality beyond vehicle volume. Source: report pp. 18–19; this is an original scenario, not an updated forecast.')],
  'capabilities': [('理解商业',
                    'Understand a business',
                    '区分整车、技术服务和新业务各自的盈利条件。',
                    'Distinguish the economics of vehicles, services and new ventures.'),
                   ('建立模型', 'Build a model', '把现金流、业务边界和实际权益放进估值。', 'Bring cash flow, business boundaries and ownership into valuation.'),
                   ('检验证据',
                    'Evaluate evidence',
                    '用服务收入占比的条件情景，检验综合毛利率判断。',
                    'Use a conditional service-mix scenario to test the margin thesis.')],
  'reading': 'xpeng'},
 {'id': 'ai-compute',
  'category': 'industry',
  'type': ['算力产业认知报告 · 42 页', 'Computing industry report · 42 pages'],
  'year': '2026',
  'name': ['算力产业：从芯片到商业化', 'AI computing: From chips to commercialization'],
  'sub': ['客户购买的，是芯片，还是可用的计算能力？', 'Are customers buying chips, or usable computing capacity?'],
  'desc': ['算力的商业价值，需要从芯片参数一路追踪到系统效率、交付方式和客户的实际约束。',
           'The commercial value of computing must be traced from chip specifications to system efficiency, delivery models and customer '
           'constraints.'],
  'cover': 'compute',
  'tags': ['AI Infrastructure', 'Domestic Chips', 'Agent Workflows'],
  'files': [],
  'sections': [('核心判断',
                'Core argument',
                '这份研究从一个具体问题出发：为什么单卡性能更强，并不必然意味着客户会选择它？报告先区分训练与推理的任务需求，再比较显存、互联、软件适配和供应链，随后把单卡放进服务器、集群及服务模式中讨论。最后，研究回到客户的预算、技术团队和准入要求，解释同一套算力为什么可能以设备、租赁资源或模型调用服务的形式成交。它呈现的是一条从技术条件走向商业选择的分析路径。',
                'This report starts with a practical question: why does a more powerful chip not necessarily win the customer? It '
                'distinguishes training from inference, then examines memory, interconnects, software adaptation and supply constraints. '
                'It places chips within servers, clusters and service offerings before returning to customers’ budgets, engineering '
                'resources and procurement requirements. The result is a framework for understanding why the same computing resources may '
                'be sold as equipment, rented capacity or model services.'),
               ('分析过程',
                'Analytical process',
                '先看任务：训练与推理对计算、显存、通信和稳定性的要求不同，因此不能只凭一个峰值算力数字比较产品。\n'
                '\n'
                '再看能否交付：芯片性能需要通过供给、封装、软件适配和多卡协同，才能变成可持续使用的系统能力。\n'
                '\n'
                '然后看如何赚钱：卖设备、租算力和提供模型调用服务，对收入持续性、运营责任和利用率的要求并不相同。\n'
                '\n'
                '最后回到客户：预算来源、技术消化能力和合规要求，会筛选出真正可采购的方案；技术上可行只是其中一个条件。',
                'Start with the workload: training and inference have different requirements, so peak compute alone is not a sufficient '
                'comparison.\n'
                '\n'
                'Test deliverability: supply, packaging, software and multi-chip coordination turn chip performance into usable system '
                'capacity.\n'
                '\n'
                'Examine the business model: equipment sales, capacity rental and model services imply different revenue patterns, '
                'operating responsibilities and utilization needs.\n'
                '\n'
                'Return to the customer: funding, engineering capability and procurement constraints determine which technically feasible '
                'options can actually be purchased.'),
               ('关键证据',
                'Supporting evidence',
                '以客户选型为例，报告把“需要什么算力”与“最终买什么”分开：预算及其使用条件、工程团队的适配能力、合规与准入要求，会共同改变采购方案。因此，比较芯片不能停在参数表，还需要比较交付与使用成本。见原报告第 33–36 '
                '页；具体客户与交易信息不进入这段摘要。',
                'The customer framework separates required computing from actual procurement. Budget conditions, engineering resources and '
                'admission requirements can change the final choice. Product comparison therefore needs to consider delivery and use, '
                'beyond specifications. Source: report pp. 33–36; customer and transaction details are excluded from this summary.')],
  'capabilities': [('理解商业',
                    'Understand a business',
                    '把芯片与系统能力连接到交付方式和客户采购。',
                    'Connect chip and system capabilities with delivery and procurement.'),
                   ('检验证据',
                    'Evaluate evidence',
                    '按任务比较性能，避免把一个参数当成完整竞争力。',
                    'Compare performance by workload rather than one headline specification.')],
  'reading': 'ai-compute'},
 {'id': 'sanxie',
  'category': 'model',
  'type': ['收购笔试案例 · 10 页备忘录及配套模型', 'Acquisition test case · 10-page memo and model'],
  'year': '2026',
  'name': ['三协电机：回报背后的条件', 'Sanxie Motor: Conditions behind the returns'],
  'sub': ['增长能否支持一笔杠杆收购？', 'Can business growth support a leveraged acquisition?'],
  'desc': ['模型回报依赖经营改善，也依赖股东能否承担利润兑现前的现金缺口。',
           'Modeled returns depend both on operating improvement and on shareholders funding the cash shortfall before that improvement '
           'materializes.'],
  'cover': 'lbo',
  'tags': ['28.63% modeled IRR', '3.40× MOIC', '10-page memo'],
  'files': [],
  'sections': [('核心判断',
                'Core argument',
                '在三协电机收购案例中，我没有只把模型算出的回报率作为结论，而是继续追问：增长来自哪里，毛利为什么变化，利润能否变成偿债所需的现金？研究将设备需求拆到电机价值量、供货份额和价格，并把产品毛利、应收账款、资本开支及追加股本连进收购模型。案例得到 '
                '28.63% 的模型年化股东回报，但前三年还需追加约 1.03 亿元股本，因此备忘录的判断是先验证经营恢复与融资条件，再决定是否推进交易。',
                'In this acquisition case, I treat the model’s return as the beginning of the analysis: where does growth come from, why '
                'are margins changing, and can profit become cash available for debt service? The study connects equipment demand with '
                'motor content, supplier share and pricing, then brings margins, receivables, capex and follow-on equity into the buyout '
                'model. The case produces a modeled annualized equity return of 28.63%, but requires roughly RMB 103 million of additional '
                'equity in the first three years. The memo therefore calls for targeted diligence on operating recovery and financing '
                'before advancing the transaction.'),
               ('分析过程',
                'Analytical process',
                '先检验收入逻辑：下游设备增长，必须经过单机电机价值量、公司供货份额和售价，才能转化为公司收入；机器人是待验证的增量。\n'
                '\n'
                '再解释利润变化：把产品结构变化与同类产品自身毛利下滑分开，识别放量是否伴随盈利质量改善。\n'
                '\n'
                '把利润转成现金：连接应收、资本开支、债务偿还、最低现金和股本追加，按每期真实股东现金流计算回报。\n'
                '\n'
                '再形成投资判断：在进入和退出倍数相同的案例中，回报主要依赖经营改善，因此尽调需要验证利润恢复和融资可得性。',
                'Test revenue transmission: equipment growth reaches company revenue through motor content, sourcing share and price; '
                'robotics remains conditional upside.\n'
                '\n'
                'Explain margin changes by separating product mix from within-product profitability, and test whether volume growth '
                'improves earnings quality.\n'
                '\n'
                'Translate profit into cash by linking receivables, capex, debt service, minimum cash and equity calls, using complete '
                'sponsor cash flows.\n'
                '\n'
                'Form a conditional investment view: with unchanged entry and exit multiples, operating improvement and funding '
                'availability must be verified.'),
               ('关键证据',
                'Supporting evidence',
                '毛利桥分析显示，约 81% 的集团毛利率下降来自同类产品内部盈利变化，而非仅由产品结构改变解释。收购模型还显示，前三年需追加 102.56 '
                '百万元股本。把这两点与回报放在一起，尽调问题就更明确：经营恢复能否兑现，股东又能否承担现金缺口？见备忘录第 6、8–10 页及配套模型；均为案例条件下的分析。',
                'The margin bridge attributes approximately 81% of the group margin decline to within-product economics rather than '
                'product mix alone. The buyout model also requires RMB 102.56 million of follow-on equity in the first three years. '
                'Together these sharpen the diligence questions: can operations recover, and can shareholders fund the shortfall? Source: '
                'memo p. 6, pp. 8–10 and accompanying model; these are conditional case analyses.')],
  'capabilities': [('理解商业',
                    'Understand a business',
                    '把下游增长拆到公司能实际获得的收入与毛利。',
                    'Trace end-market growth to the revenue and margins available to the company.'),
                   ('建立模型',
                    'Build a model',
                    '联动经营、偿债与追加股本，计算完整股东现金流回报。',
                    'Link operations, debt service and equity calls in sponsor returns.'),
                   ('检验证据',
                    'Evaluate evidence',
                    '用毛利桥与现金缺口，确定尽调需要验证的问题。',
                    'Use margin bridges and funding gaps to identify diligence questions.')],
  'reading': 'sanxie'},
 {'id': 'ai-leads',
  'category': 'ai',
  'type': ['百度 · 工具项目', 'Baidu · tool project'],
  'year': '2026',
  'name': ['Token 商机识别 Agent', 'Token sales intelligence Agent'],
  'sub': ['怎样把分散的企业信号，变成可跟进的线索？', 'How can scattered company signals become actionable leads?'],
  'desc': ['将信息采集、企业识别、商机判断与持续推送连成一条流程。', 'Connect collection, entity identification, opportunity assessment and regular delivery.'],
  'cover': 'agent',
  'tags': ['9 data sources', '3,700+ companies', '0 → 1'],
  'files': [],
  'sections': [('核心判断',
                'Core argument',
                '我从零搭建 Token 销售线索库，将备案、融资、招聘等九路数据整合到企业层面，并结合实体匹配与 CRM 校验减少信息割裂。在此基础上，我构建商机识别评分 Agent '
                '和推荐路径，将分散信号整理为销售可以继续跟进的线索，并完成前后端搭建与持续运维。线索库覆盖 3700 多家企业；项目的重点是把资料整理做成可以反复使用的工作流程。',
                'I built a Token sales intelligence database from scratch, bringing nine sources—including filings, financing and '
                'hiring—together at the company level, with entity matching and CRM validation. An opportunity-scoring Agent and '
                'recommended paths turned fragmented signals into leads for follow-up. I also built and maintained the frontend and '
                'backend. The database covers more than 3,700 companies. The project’s emphasis is a repeatable workflow rather than a '
                'one-off information exercise.'),
               ('分析过程',
                'Analytical process',
                '先收集多源信号，再匹配到同一家企业，形成统一记录。\n\n通过评分和推荐路径，帮助识别值得跟进的商机。\n\n通过前后端与定期推送，让流程持续可用。',
                'Collect signals and match them into unified company records.\n'
                '\n'
                'Use scoring and recommended paths to identify opportunities for follow-up.\n'
                '\n'
                'Support continuing use through the frontend, backend and regular delivery.')],
  'capabilities': [('理解商业',
                    'Understand a business',
                    '把企业信号整理成商机评分与跟进路径。',
                    'Turn company signals into opportunity assessments and follow-up paths.'),
                   ('做成工具',
                    'Make it usable',
                    '从多源采集、实体匹配延伸到前后端与定期推送。',
                    'Connect collection and entity matching with a frontend, backend and regular delivery.')]},
 {'id': 'materials',
  'category': 'industry',
  'type': ['复星创富 · 投资专题研究', 'Fosun Capital · Investment research'],
  'year': '2024–2025',
  'name': ['新材料产业链与招商研究', 'Advanced materials & investment attraction'],
  'sub': ['从产业布局，到企业引进的具体路径。', 'From an industry map to a company-attraction strategy.'],
  'desc': ['围绕武汉某区新材料全产业链布局，我梳理产业协同与招商路径，提出“光谷＋车谷”双核驱动战略，并构建“链主企业＋反向配套”招商模型。研究希望先识别能够带动产业链的关键企业，再从其上下游需求反推配套企业的引进方向。我完成了 100 '
           '余页深度研究报告，研究成果为争取数十万元专项资金提供支持。',
           'For a district in Wuhan, I examined the advanced-materials value chain and proposed an Optics Valley–Auto Valley dual-engine '
           'strategy. An anchor-company-led model works backward from key companies’ supplier and customer needs to identify supporting '
           'businesses to attract. I completed a report of more than 100 pages; the research supported dedicated-funding efforts of '
           'several hundred thousand renminbi.'],
  'cover': 'assets',
  'tags': ['Advanced Materials'],
  'files': [],
  'sections': [('研究内容',
                'The work',
                '围绕武汉某区新材料全产业链布局，我梳理产业协同与招商路径，提出“光谷＋车谷”双核驱动战略，并构建“链主企业＋反向配套”招商模型。研究希望先识别能够带动产业链的关键企业，再从其上下游需求反推配套企业的引进方向。我完成了 100 '
                '余页深度研究报告，研究成果为争取数十万元专项资金提供支持。',
                'For a district in Wuhan, I examined the advanced-materials value chain and proposed an Optics Valley–Auto Valley '
                'dual-engine strategy. An anchor-company-led model works backward from key companies’ supplier and customer needs to '
                'identify supporting businesses to attract. I completed a report of more than 100 pages; the research supported '
                'dedicated-funding efforts of several hundred thousand renminbi.'),
               ('分析过程',
                'Analytical process',
                '梳理新材料产业链及区域协同关系，明确产业布局要解决的问题。\n\n以链主企业为起点，从上下游需求反推配套企业的招商方向。\n\n以“光谷＋车谷”双核驱动战略连接产业研究、招商模型与资金支持。',
                'Map the materials value chain and regional links to define the planning question.\n'
                '\n'
                'Work backward from anchor companies’ upstream and downstream needs to identify supporting businesses.\n'
                '\n'
                'Connect research, the attraction model and funding support through a dual-engine regional strategy.')],
  'capabilities': [('商业研究', 'Business research', '将产业或区域选择与实际进入路径相联系。', 'Connect industry or geography choices with execution paths.')]},
 {'id': 'overseas',
  'category': 'strategy',
  'type': ['复星创富 · 投资专题研究', 'Fosun Capital · Investment research'],
  'year': '2024–2025',
  'name': ['日化品牌出海战略', 'Personal-care brand expansion'],
  'sub': ['东南亚与中东：怎样选择进入与合作路径？', 'Southeast Asia and the Middle East: How should a brand enter?'],
  'desc': ['在复星创富实习期间，我撰写集团旗下日化品牌的出海战略报告，聚焦东南亚与中东两大市场，分析进入与合作路径。项目将区域选择与合作方式放在一起讨论：选择一个市场之后，还需要考虑品牌通过什么方式进入，并与当地合作方形成怎样的关系。',
           'At Fosun Capital, I wrote an overseas expansion strategy report for a group-owned personal-care brand, focusing on Southeast '
           'Asia and the Middle East. The research considers market choice alongside entry and partnership routes: choosing a geography '
           'also requires deciding how the brand will enter and work with local partners.'],
  'cover': 'industry',
  'tags': ['Overseas Strategy'],
  'files': [],
  'sections': [('研究内容',
                'The work',
                '在复星创富实习期间，我撰写集团旗下日化品牌的出海战略报告，聚焦东南亚与中东两大市场，分析进入与合作路径。项目将区域选择与合作方式放在一起讨论：选择一个市场之后，还需要考虑品牌通过什么方式进入，并与当地合作方形成怎样的关系。',
                'At Fosun Capital, I wrote an overseas expansion strategy report for a group-owned personal-care brand, focusing on '
                'Southeast Asia and the Middle East. The research considers market choice alongside entry and partnership routes: choosing '
                'a geography also requires deciding how the brand will enter and work with local partners.'),
               ('分析过程',
                'Analytical process',
                '聚焦东南亚与中东两大区域，明确战略报告的研究范围。\n\n围绕品牌出海问题，分析进入目标市场的路径。\n\n将市场选择与合作路径联系起来，形成战略报告。',
                'Focus the strategy on Southeast Asia and the Middle East.\n'
                '\n'
                'Examine routes for entering the target markets.\n'
                '\n'
                'Connect market choice and partnership routes in the strategy report.')],
  'capabilities': [('商业研究', 'Business research', '将产业或区域选择与实际进入路径相联系。', 'Connect industry or geography choices with execution paths.')]},
 {'id': 'real-assets',
  'category': 'model',
  'type': ['弘毅投资 · 实习项目', 'Hony Capital · internship work'],
  'year': '2025–2026',
  'name': ['不动产：把资产放回现金流', 'Real assets: Underwriting the cash flows'],
  'sub': ['一项资产的吸引力，如何落实到现金分配？', 'How does an asset’s appeal translate into cash distributions?'],
  'desc': ['资产、交易结构、融资与退出，需要在同一套现金流中衔接。', 'Assets, transaction structure, financing and exit need to connect in one cash-flow framework.'],
  'cover': 'assets',
  'tags': ['ABS / REITs', 'Cap rate >7%', 'IRR >10%'],
  'files': [],
  'sections': [('核心判断',
                'Core argument',
                '在不动产投资实习中，我从行业、区位和需求分析进入具体项目，并将运营与退出假设、融资条件及夹层结构连接到现金流模型。工作覆盖物流资产和商改住项目，既测算持有期间的分配，也比较不同持有期限下的杠杆回报。这个项目体现的是把资产判断转化为交易层面的收益测算，并通过敏感性分析理解结果依赖哪些条件。',
                'In the real assets internship, I connected industry, location and demand analysis with operating and exit assumptions, '
                'financing and mezzanine structures in cash-flow models. The work covered logistics and commercial-to-residential '
                'projects, considering interim distributions and leveraged returns under different holding periods. It shows how asset '
                'analysis translates into transaction-level returns and how sensitivity analysis makes the assumptions visible.'),
               ('分析过程',
                'Analytical process',
                '从行业、区位、需求与运营表现分析资产质量。\n\n把交易结构和融资条件放进期间现金流与分配安排。\n\n比较运营六年与持有至到期的测算，并检验运营、融资和退出假设。',
                'Assess assets through industry, location, demand and operating performance.\n'
                '\n'
                'Connect structure and financing with interim cash flows and distributions.\n'
                '\n'
                'Compare six-year and hold-to-maturity scenarios and test operating, financing and exit assumptions.')],
  'capabilities': [('理解商业',
                    'Understand a business',
                    '将区位、需求和运营表现转成具体资产判断。',
                    'Translate location, demand and operations into asset judgments.'),
                   ('建立模型',
                    'Build a model',
                    '连接交易结构、融资、分配和退出情景。',
                    'Connect transaction structure, financing, distributions and exit scenarios.')]},
 {'id': 'saf',
  'category': 'industry',
  'type': ['中信证券 · 研究经历', 'CITIC Securities · research'],
  'year': '2025',
  'name': ['SAF：航空减排背后的产业机会', 'SAF: An industry opportunity in aviation decarbonization'],
  'sub': ['航空减排需求，怎样变成一门可实现的生意？', 'How can aviation decarbonization become a viable business?'],
  'desc': ['需求空间需要与技术门槛、原料供给和政策条件一起分析。', 'Market potential must be considered alongside technology, feedstock and policy.'],
  'cover': 'industry',
  'tags': ['Sustainable aviation fuel'],
  'files': [],
  'sections': [('核心判断',
                'Core argument',
                '在可持续航空燃料研究中，我以欧盟对生物柴油加征关税的背景为起点，关注航空燃料的技术门槛、附加值与碳减排属性，并分析中国餐厨废油资源能够带来的供给条件。研究将政策推动的需求与产业实际供给连接起来，当时测算的 2030 年全球市场规模为 2266 '
                '亿元。这一测算属于原研究时点的判断；理解产业机会，仍需要同时看需求为什么增长，以及技术和原料能否支持供给。',
                'This study began with EU tariffs on biodiesel and examined the technology barriers, value-added economics and '
                'carbon-reduction attributes of sustainable aviation fuel, alongside China’s waste cooking oil resources. Connecting '
                'policy-driven demand with supply conditions, the historical research estimated a RMB 226.6 billion global market for '
                '2030. That estimate belongs to the original research period. Understanding the opportunity also requires examining '
                'whether technology and feedstock can support the demand.'),
               ('分析过程',
                'Analytical process',
                '以政策和下游需求变化界定研究问题。\n\n结合技术门槛、产品价值和原料供给分析产业条件。\n\n将政策、技术与原料条件连接到当时的市场规模测算。',
                'Define the question through policy and end-market changes.\n'
                '\n'
                'Examine technology, product economics and feedstock availability.\n'
                '\n'
                'Connect policy, technology and feedstock conditions with the historical market estimate.')],
  'capabilities': [('理解商业',
                    'Understand a business',
                    '将政策、需求、技术门槛与原料供给放在一起分析。',
                    'Study policy, demand, technology barriers and feedstock together.'),
                   ('检验证据',
                    'Evaluate evidence',
                    '市场规模判断需要回到测算口径与供给条件。',
                    'Ground market-size estimates in their definitions and supply conditions.')]},
 {'id': 'jiaao',
  'category': 'model',
  'type': ['中信证券 · 公司研究', 'CITIC Securities · company research'],
  'year': '2025',
  'name': ['嘉澳股份：转型与产能的价值判断', 'Jiaao: Valuing transformation and capacity'],
  'sub': ['产能与政策预期，怎样落到公司价值？', 'How do capacity and policy expectations translate into value?'],
  'desc': ['把业务布局、在建产能和估值依据放在同一套分析中讨论。', 'Connect the business mix, planned capacity and valuation basis.'],
  'cover': 'industry',
  'tags': ['Jiaao Environmental'],
  'files': [],
  'sections': [('核心判断',
                'Core argument',
                '嘉澳股份研究围绕生物质能源与环保增塑剂两条业务展开。我结合百万吨在建产能、政策变化、实控人增持及大客户参与等因素形成当时的公司判断，并以 4.6 '
                '倍市净率表达估值。产能和政策提供了理解未来增长的线索，但预期与经营结果之间仍有距离：在建产能并不是已经实现的利润，估值判断也需要后续经营兑现来验证。',
                'This study considers Jiaao’s biomass energy and eco-friendly plasticizer businesses, including million-tonne capacity '
                'under construction, policy changes, controlling-shareholder purchases and large-customer participation. A 4.6x '
                'price-to-book multiple expressed the historical valuation view. Capacity and policy offer clues to potential growth, but '
                'planned capacity is not realized profit, and the valuation thesis still requires operating delivery.'),
               ('分析过程',
                'Analytical process',
                '先理解两条业务各自的经营特征。\n\n区分在建产能、政策信号与实际兑现的经营结果。\n\n解释当时采用市净率估值的思路及其限制。',
                'Understand the two businesses and their operating characteristics.\n'
                '\n'
                'Separate planned capacity and policy signals from realized results.\n'
                '\n'
                'Explain the historical price-to-book approach and its limitations.')],
  'capabilities': [('理解商业', 'Understand a business', '同时分析两条业务、产能预期和政策影响。', 'Consider both businesses, capacity expectations and policy.'),
                   ('建立模型', 'Build a model', '以当时的市净率框架表达公司判断。', 'Express the historical company view through a price-to-book framework.'),
                   ('检验证据', 'Evaluate evidence', '区分在建产能与已兑现的经营结果。', 'Distinguish planned capacity from realized operating results.')]},
 {'id': 'sugon',
  'category': 'model',
  'type': ['中信证券 · 公司研究', 'CITIC Securities · company research'],
  'year': '2025',
  'name': ['中科曙光：业务拆分与估值', 'Sugon: Business segments and valuation'],
  'sub': ['不同业务，为什么需要分别估值？', 'Why value different businesses separately?'],
  'desc': ['先看懂业务与权益，再选择估值方法，而不是只给公司套一个倍数。', 'Understand businesses and ownership before choosing valuation methods.'],
  'cover': 'compute',
  'tags': ['Sugon'],
  'files': [],
  'sections': [('核心判断',
                'Core argument',
                '在中科曙光研究中，我采用分部估值的思路，将子公司价值与主业经营价值分别讨论，再形成整体判断。研究关注全栈自主可控能力与算力整合模式如何影响盈利质量，并在当时的估值框架下对主业采用 29 '
                '倍市盈率。原研究认为这一整合模式的价值尚未被充分反映；分开讨论各项业务，是为了让公司判断与估值依据之间的关系更清楚。',
                'The Sugon study separates subsidiary value from the core business before forming an overall view. It considers how '
                'proprietary technology and integrated computing affect profitability, and applied a 29x earnings multiple to the core '
                'business in the historical research framework. The original thesis was that the integrated model’s value was not fully '
                'reflected. Segment valuation helps make the relationship between that business judgment and valuation explicit.'),
               ('分析过程',
                'Analytical process',
                '识别主业与子公司的业务边界和权益关系。\n\n采用分部估值，将子公司与主业经营价值分别讨论。\n\n解释当时主业估值倍数与商业判断之间的关系。',
                'Identify business boundaries and ownership.\n'
                '\n'
                'Use a segment valuation to examine subsidiaries and core operations separately.\n'
                '\n'
                'Explain how the historical core-business multiple relates to the business thesis.'),
               ('研究时点与估值口径',
                'Historical research context',
                '原研究采用分部估值，对子公司单独估值，主业给予 29 倍市盈率，关注全栈自主可控与约 30% 毛利率的算力整合模式。上述口径用于说明当时的研究思路。',
                'The historical study valued subsidiaries separately and applied 29x earnings to core operations, examining proprietary '
                'technology and an integrated computing model with approximately 30% gross margin. These assumptions describe the original '
                'research framework.')],
  'capabilities': [('理解商业', 'Understand a business', '从业务模式理解盈利，而后讨论公司价值。', 'Understand the business model before discussing value.'),
                   ('建立模型', 'Build a model', '区分主业和子公司价值，采用分部估值。', 'Separate core operations and subsidiaries in a segment valuation.')]},
 {'id': 'government-funding',
  'category': 'industry',
  'type': ['百度 · 专题研究', 'Baidu · thematic research'],
  'year': '2026',
  'name': ['政府资金：从需求到项目落地', 'Government funding: From demand to execution'],
  'sub': ['有项目需求，为什么仍然未必能成交？', 'Why does project demand not always lead to a transaction?'],
  'desc': ['需求能否落地，还取决于资金从哪里来、按什么条件使用。', 'Demand becomes actionable only when funding sources and spending conditions also fit.'],
  'cover': 'industry',
  'tags': ['Government funding'],
  'files': [],
  'sections': [('核心判断',
                'Core argument',
                '在政府资金专题中，我梳理政府四本账及专项债等资金工具，关注资金规模扩大与项目要求趋严之间的关系，并结合友商访谈理解业务落地方式。这段研究帮助我把客户需求与资金条件放在一起看：政策方向能够解释为什么要做一个项目，预算和采购路径则影响项目能否真正推进。',
                'This research mapped the four government budget accounts and funding instruments such as special-purpose bonds, examining '
                'stricter project conditions alongside funding expansion. Competitor interviews added a view of how projects were '
                'executed. The work connects customer demand with financing: policy may explain why a project is desired, while budgets '
                'and procurement pathways affect whether it can proceed.'),
               ('分析过程',
                'Analytical process',
                '区分预算与资金工具，避免把政策支持等同于可立即使用的资金。\n\n梳理项目要求与采购路径，理解资金和方案能否匹配。\n\n通过访谈补充业务模式的理解，将政策、资金和竞争条件连接起来。',
                'Distinguish budgets and funding instruments from immediately available funding.\n'
                '\n'
                'Consider project requirements and procurement pathways.\n'
                '\n'
                'Use interviews to connect business models with policy, funding and competition.')],
  'capabilities': [('理解商业',
                    'Understand a business',
                    '把项目需求与资金来源、使用条件和采购路径连接。',
                    'Connect project demand with funding, spending conditions and procurement.'),
                   ('检验证据',
                    'Evaluate evidence',
                    '结合资料梳理与访谈理解业务落地条件。',
                    'Combine desk research and interviews to understand execution conditions.')]},
 {'id': 'ai-transformation',
  'category': 'academic',
  'type': ['实证论文', 'empirical paper'],
  'year': 'RESEARCH',
  'name': ['AI 转型的隐性成本', 'The hidden costs of AI transformation'],
  'sub': ['企业采用 AI，短期回报一定会提高吗？', 'Does AI adoption necessarily improve near-term returns?'],
  'desc': ['将 AI 转型与财务表现之间的关系，作为一个需要数据检验的问题。',
           'Treat the relationship between AI transformation and financial performance as an empirical question.'],
  'cover': 'academic',
  'tags': ['AI transformation & ROA'],
  'files': [],
  'sections': [('核心判断',
                'Core argument',
                '这篇实证论文研究企业 AI 转型与资产回报率的关系。我使用机器学习方法构建文本词典，并结合固定效应面板回归分析企业数据。研究结果显示，在研究样本与模型设定下，AI '
                '转型与资产回报率之间存在稳健的负向关系。这项研究提醒我：技术投入的价值并不会自动、即时地表现为财务回报，判断需要结合研究条件与证据。',
                'This empirical paper studies AI transformation and return on assets using a machine-learning-based text dictionary and '
                'fixed-effects panel regressions. The study finds a robust negative relationship within its sample and model '
                'specifications. The project treats financial returns from technology adoption as a question to investigate rather than an '
                'automatic outcome, while keeping the finding within its evidential limits.'),
               ('分析过程',
                'Analytical process',
                '将企业 AI 转型转化为可以研究的文本指标。\n\n用固定效应面板回归检验它与资产回报率的关系。\n\n把结果限制在样本与识别条件内，不把相关关系直接写成普遍因果结论。',
                'Construct a text-based measure of AI transformation.\n'
                '\n'
                'Examine its relationship with ROA using fixed-effects panel regressions.\n'
                '\n'
                'Keep the result within the sample and identification limits, without claiming universal causality.'),
               ('论文与项目题名',
                'Paper or project title',
                '《人工智能转型的隐性成本——对企业资产回报率（ROA）的抑制效应的实证研究》',
                'The Hidden Costs of AI Transformation: An Empirical Study of Its Negative Relationship with Corporate ROA')],
  'capabilities': [('检验证据',
                    'Evaluate evidence',
                    '用文本指标与面板回归研究问题，并区分关系与因果。',
                    'Use text measures and panel regressions while distinguishing association from causality.')]},
 {'id': 'housing',
  'category': 'academic',
  'type': ['机器学习论文 · APNHR 论坛', 'ML paper · APNHR forum'],
  'year': 'RESEARCH',
  'name': ['房价稳定性：数据与政策', 'Housing stability: Data and policy'],
  'sub': ['房价稳定性，可以从哪些因素理解？', 'What factors help explain housing-price stability?'],
  'desc': ['将基本面与政策因素一起纳入数据分析，探索稳定性的预测。', 'Study fundamentals and policy together to explore the prediction of housing stability.'],
  'cover': 'academic',
  'tags': ['Housing stability'],
  'files': [],
  'sections': [('核心判断',
                'Core argument',
                '这项研究使用爬虫采集的数据与决策树等机器学习方法，从基本面和政策有效性两个角度研究房价稳定性，并构建预测模型。研究将城市治理中的实际问题转化为数据分析任务，尝试从多种因素之间的关系理解房价表现。论文入选 APNHR '
                '论坛；预测模型描述的是数据中的关系，不能单凭预测结果认定政策具有因果效果。',
                'This study uses web-scraped data and decision-tree methods to examine housing-price stability through fundamentals and '
                'policy effectiveness, and builds a prediction model. It translates a real urban-governance question into a data-analysis '
                'task, exploring relationships among factors that shape housing-price behavior. The paper was accepted by the APNHR forum. '
                'Predictive relationships alone do not establish causal policy effects.'),
               ('分析过程',
                'Analytical process',
                '收集并组织与房价稳定性相关的数据。\n\n结合基本面和政策因素构建决策树等预测模型。\n\n将预测关系与政策因果效果区分，明确模型解释的范围。',
                'Collect and organize data relevant to housing stability.\n'
                '\n'
                'Build predictive models using fundamentals and policy-related factors.\n'
                '\n'
                'Distinguish predictive relationships from causal policy effects and define the model’s scope.'),
               ('论文与项目题名',
                'Paper or project title',
                '《房价稳定性影响因素决策树模型：基于基本面和政策有效性的双重实证》',
                'A Decision-Tree Model of Housing-Price Stability: Evidence from Fundamentals and Policy Effectiveness')],
  'capabilities': [('检验证据', 'Evaluate evidence', '将基本面与政策因素共同纳入研究问题。', 'Study fundamentals and policy factors together.'),
                   ('做成工具', 'Make it usable', '用爬虫组织数据，再应用决策树构建预测模型。', 'Organize scraped data and apply decision trees to prediction.')]},
 {'id': 'ai-research',
  'category': 'ai',
  'type': [' AI 应用项目', 'AI application'],
  'year': 'PROJECT',
  'name': ['智能金融研报生成系统', 'AI-powered financial research system'],
  'sub': ['让资料检索进入研报写作流程。', 'Bring source retrieval into research writing.'],
  'desc': ['先从已有资料中找到相关信息，再借助模型组织文本，并保留上下文。',
           'Retrieve relevant information before using a model to organize text, while retaining context.'],
  'cover': 'rag',
  'tags': ['Python', 'RAG / GPT', 'Vector database'],
  'files': [],
  'sections': [('核心判断',
                'Core argument',
                '这个项目尝试把金融研报写作中的资料检索与文本组织连接起来。我使用 Python、大语言模型和向量数据库搭建系统，通过检索增强生成，让系统先查找相关资料，再辅助生成内容，并用记忆架构保留研究上下文。它展示的是我把 AI '
                '能力接入具体研究流程的尝试；生成结果仍需要研究者核对资料与判断。',
                'This project connects source retrieval with the organization of financial research. Using Python, a language model and a '
                'vector database, it retrieves relevant material before assisting with drafting, while a memory architecture retains '
                'context. It demonstrates an attempt to apply AI within a concrete research workflow; researchers still need to verify the '
                'sources and judgments in generated text.'),
               ('分析过程',
                'Analytical process',
                '用向量数据库组织资料，支持相关信息检索。\n\n把检索结果交给模型，辅助组织研究文本。\n\n用记忆架构保留上下文，人工核对事实和推理。',
                'Organize source material in a vector database for retrieval.\n'
                '\n'
                'Provide retrieved material to the model to support drafting.\n'
                '\n'
                'Retain context through memory and review facts and reasoning manually.'),
               ('论文与项目题名', 'Paper or project title', '基于大语言模型的智能金融研报生成系统', 'An LLM-Based Financial Research Report Generation System')],
  'capabilities': [('做成工具',
                    'Make it usable',
                    '将资料检索、语言模型与记忆架构接入写作流程。',
                    'Bring retrieval, a language model and memory into a writing workflow.')]}]
