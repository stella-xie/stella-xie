# 个人网站

谢欣玥 / Xinyue Xie（Stella）的双语个人网站。包含完整简历、分类作品集、研究逻辑图示、可展开正文及经历与作品的双向链接。

## 公开展示版

本仓库提交个人介绍、完整双语履历、项目介绍、研究摘要、逻辑图，以及带水印的逻辑图。**不提交 PDF/Excel 原件、客户及报价等内部材料、完整模型、单元格数据或公式导出。** 现有 GitHub 个人主页 README 保留。网站的公开发布目录为仓库根目录的 `docs/`，由 GitHub Pages 托管。

2026-10-22 更新：沿用原有深色首页和作品卡片，加入简历／作品集两个大球及八个可点击的小球、可拖动视角、分类星图与作品预览弹窗。六段详细实习与景林、字节两段已有记录分别呈现；两次中信实习分开。本地准备了小鹏 26 页、三协备忘录 10 页、算力节选 6 页及 Quick LBO 模型关键页 2 页的水印阅读副本。报告阅读副本仅用于本地，公开站点继续采用研究展示版。算力节选排除了客户、报价和内部竞争分析，第 17 原页的供应链细节已烘焙遮蔽。

- 直接打开 `public-preview.html`，支持离线页面切换、双语、项目分类与搜索。
- 运行 `python3 scripts/serve.py` 后访问 `http://127.0.0.1:8765/`。服务器仅监听本机，默认服务 `public/`。
- 网站静态输出在 `public/`，每次构建同步到根目录 `docs/`，供 GitHub Pages 发布。
- 网站地址：<https://stella-xie.github.io/stella-xie/>。仓库 Pages 设置使用 **Deploy from a branch → main → /docs**。
- 后续修改后运行构建与检查，再提交源码和 `docs/`；GitHub Pages 会自动更新。页面使用相对路径，支持仓库子目录托管。

## 修改与构建

需要 Python 3.12+。常规构建仅使用标准库，不依赖原始报告、Excel 或私有图片。

```sh
python3 scripts/build.py
python3 scripts/check.py
```

- 内容：`scripts/content.py`；分类与经历关联：`scripts/connections.py`；逻辑图：`scripts/illustrations.py`。
- 样式与交互：`assets/style.css`、`assets/main.js`、`assets/constellations.css`、`assets/explore.js`；星图结构：`scripts/constellations.py`；离线路由：`assets/preview-router.js`；标识：`assets/logos/`。
- 修改这些源文件，再构建更新 `public/` 和 `public-preview.html`，不要只修改生成文件。
- 页面：`/`、`/resume/`、`/portfolio/` 和 14 个独立项目详情页；此前的两个合并项目 URL 继续可用，共 19 条路由。
- 全局和区块均可切换中英；作品可归入多个分类。目录直接打开对应分析，简历与作品互相连接。

## 本地完整版（不进入 Git）

本地保留 `preview.html`、`dist/` 与 `private-sources/`。它们全部被 Git 忽略。

完整阅读副本包括小鹏报告 26 页、三协备忘录 10 页，以及模型 9 个工作表、889 个非空行的计算值。报告页面和模型图片直接写入署名水印，原始 PDF/XLSX、提取全文和公式数据留在私有资料目录。宽表按列分组，保留工作表名、行号和列标；阅读副本不会在线重算。

只有本机拥有这些私有材料时，才可运行：

```sh
python3 scripts/build.py --full
python3 scripts/check.py --full
python3 scripts/serve.py --full
```

从 GitHub 克隆的展示版无需也无法生成完整阅读副本。请勿将本地完整版加入公开提交。

如原始报告更新，可选运行 `scripts/prepare_readers.py` 重新制作阅读图片，再构建 `--full`。此步骤读取私有原件，依赖 Pillow、pypdf、openpyxl、Poppler 和 macOS Arial Unicode 字体；不改写原件、不生成新 PDF/Excel。其他系统需要配置字体路径。

## 内容与权利

中英文履历按提供材料保留并统一口径。弘毅采用 2025.09—2026.01，百度覆盖企业采用 3700+；中信能源化工采用本次补充的 2025.02—2025.07，嘉澳估值采用用户确认的 4.6 倍 PB。版本核对、审批与聊天备注仅留在被 Git 忽略的本地目录，不出现在网站。未提供原报告的项目只展示已提供的经历与方法，不伪造附件。

小鹏研究保留原报告时点；三协为笔试条件性案例，模型测算不代表实际投资业绩。组织 Logo 来源见 `LOGO-SOURCES.md`。所有研究内容保留作者权利，第三方标识权利归原所有者。

水印及移除下载入口不能阻止截图、保存图片或手动抄录。即使有水印，公开仓库中的阅读图片也可被保存，因此本次不公开报告图片。原件、完整模型与内部研究材料留在本地；进一步的访问控制需要私有存储、登录与服务端鉴权。`private-sources/reading-copies/manifest.json` 记录本地阅读资源。可选的 `scripts/prepare_local_readings.py` 从本机原件与已签名图片制作该集合，常规公开构建不需原件。

## 验证

`check.py` 检查页面链接、锚点、目录目标、水印标记和原件隔离，并确认公开输出不含报告图片、完整模型或审批备注。`--full` 核对本地 44 张新增阅读图片的尺寸与无 EXIF 元数据。`--full` 额外检查本地阅读页数与图片。

静态检查与 JavaScript 语法检查通过后，在浏览器复核星球入口、分类筛选、双语、预览弹窗、经历关联与报告翻页。阅读图片另外抽样检查水印和遮蔽效果。
