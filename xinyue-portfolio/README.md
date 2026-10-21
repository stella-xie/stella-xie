# 个人网站

谢欣玥 / Xinyue Xie（Stella）的双语个人网站。包含完整简历、分类作品集、研究逻辑图示、可展开正文及经历与作品的双向链接。

## 公开展示版

本仓库只提交展示版：个人介绍、完整双语履历、项目介绍、研究摘要和带水印的逻辑图。**不提交完整报告、模型阅读图片、原件、单元格数据或公式导出。** 现有 GitHub 个人主页 README 保留。本次仅上传代码，没有开通网站托管。

- 直接打开 `public-preview.html`，支持离线页面切换、双语、项目分类与搜索。
- 运行 `python3 scripts/serve.py` 后访问 `http://127.0.0.1:8765/`。服务器仅监听本机，默认服务 `public/`。
- 网站静态输出在 `public/`，可作为后续托管的目录。

## 修改与构建

需要 Python 3.12+。常规构建仅使用标准库，不依赖原始报告、Excel 或私有图片。

```sh
python3 scripts/build.py
python3 scripts/check.py
```

- 内容：`scripts/content.py`；分类与经历关联：`scripts/connections.py`；逻辑图：`scripts/illustrations.py`。
- 样式与交互：`assets/style.css`、`assets/main.js`；离线路由：`assets/preview-router.js`；标识：`assets/logos/`。
- 修改这些源文件，再构建更新 `public/` 和 `public-preview.html`，不要只修改生成文件。
- 页面：`/`、`/resume/`、`/portfolio/` 和 8 个 `/projects/…/` 项目详情页。
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

中英文履历细节按提供材料保留。简历中英版本差异：弘毅日期分别为 2025.09—2026.01 与 2025.10—2025.12；百度企业数分别为 3700+ 与 3300+。展示采用中文版口径，并在简历页说明。未提供独立报告的项目只展示已提供的履历与思路，不伪造附件。

小鹏研究保留原报告时点；三协为笔试条件性案例，模型测算不代表实际投资业绩。组织 Logo 来源见 `LOGO-SOURCES.md`。所有研究内容保留作者权利，第三方标识权利归原所有者。

水印及移除下载入口不能阻止截图、保存图片或手动抄录。公开仓库里的摘要、逻辑图和代码本身可以被读取与保存，因此完整报告和模型不在仓库中。进一步的全文访问控制应使用私有存储、登录与服务端鉴权。

## 验证

`check.py` 检查页面链接、锚点、目录目标、水印标记和原件隔离，并确认公开输出没有完整报告与模型阅读资源。`--full` 额外检查本地阅读页数与图片。

本轮通过静态检查、JavaScript 语法、离线路由及服务器路径隔离检查。水印图片已抽样检查清晰度与版式；本轮未完成完整网站的浏览器视觉复核。
