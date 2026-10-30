# 用 AI 画好科研图

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23794693.svg)](https://doi.org/10.5281/zenodo.23794693)

**从研究思路到论文配图** · TopLocalAI 开源双语书籍

[English](README.md)

**v1.0.0，2026-10-30 发布。** 全书已完成：前言、13 章正文、附录 A–G 和封面。中文版 442 页，英文版 421 页（170 × 240 mm）。

## 下载

- **[中文 PDF](https://github.com/TopLocalAI/ai-scientific-figures-book/releases/latest/download/ai-scientific-figures-zh.pdf)**
- **[English PDF](https://github.com/TopLocalAI/ai-scientific-figures-book/releases/latest/download/ai-scientific-figures-en.pdf)**

以上链接始终指向最新版本，每个 PDF 约 78 MB。历史版本见 [全部发布](https://github.com/TopLocalAI/ai-scientific-figures-book/releases)。

## 这本书讲什么

本书写给需要为论文、汇报和海报作图的研究生、博士后和科研人员。书中讲清楚：一张图要表达什么，怎样把研究内容写成绘图任务书，怎样借助 AI 推演构图、绘制数据图、处理实验图像和示意图，怎样逐项核对科学内容，以及怎样交付数据、提示词和修改过程都可追溯的图。案例覆盖生物医学、材料与能源、工程、地球与环境科学和数据科学。

## 目录

1. 建立你的 AI 科研绘图工作流
2. 把研究内容变成一份绘图任务书
3. 与 AI 一起推演构图和草图
4. 建立整篇论文的视觉语言
5. 用 AI 辅助数据可视化
6. 方法图与实验流程图
7. 机制图与结构示意图
8. 实验图像的科学呈现
9. 把多张图组织成论文组图
10. 图形摘要：用一张图表达研究贡献
11. 把“再好看一点”变成可执行的修改
12. 从论文配图到汇报与海报
13. 检查、导出与可追溯交付

附录 A–G：绘图任务书模板、提示词与修改指令改写表、图注核对表、交付清单、术语表（中英对照）、案例与素材来源、尺寸与字号速查。

## 用 SciDraw AI 练习

全书以 [SciDraw AI](https://sci-draw.com) 作为练习平台，PDF 中提到的每个工具都可以直接点击打开。
[科研绘图流程向导](https://sci-draw.com/zh/figure-workflow) 可以先选图的类型，再按 3–4 步的工具路线完成。

## 阅读与编译

LaTeX 是编辑源：`main.tex` 为中文版，`main-en.tex` 为英文版，正文分别在 `chapters/zh/` 和 `chapters/en/`。安装含 XeLaTeX、latexmk、中文支持和 Fandol 字体的 TeX Live 即可编译，不需要商业字体或 shell escape。

    make check    # 检查书稿与案例完整性
    make          # 编译中英文
    make zh       # 只编译中文
    make en       # 只编译英文

PDF 输出到 `pdf/`，中间文件在 `build/`，两者都不纳入 git。Ubuntu 上 CI 安装的包为 texlive-xetex、texlive-lang-chinese、texlive-latex-extra、texlive-fonts-recommended、tex-gyre、fonts-texgyre、fonts-lmodern 和 latexmk。GitHub Actions 工作流 “Build bilingual PDFs” 可在 Actions 页面点 Run workflow 手动运行，编译出的两个 PDF 作为 artifact 上传。

仓库已保存全部图版，直接编译即可。需要重新生成图时：

    python3 -m venv .venv
    . .venv/bin/activate
    python3 -m pip install -r requirements.txt
    make figures  # 重新生成配对数据示例图
    make

`requirements.txt` 只覆盖配对数据示例；各章脚本（`scripts/chNN_*.py`）还需要 numpy、Pillow、pandas、SciPy、colorspacious 和 openpyxl。

## 案例、数据与来源记录

书中的图有四类：图像生成模型出底图、再用 LaTeX/TikZ 加标注；用 matplotlib 基于公开数据或明确标注的模拟数据绘制的数据图；TikZ 绘制的示意图；开放许可的外部图像。案例包括 USGS 河流硝酸盐监测、胰岛素–GLUT4 信号通路、锂离子电池、基于模拟数据的钙钛矿太阳能电池组图、山火主题图形摘要和 BBBC022 显微图像。

每张生成图所用的工具、提示词和修改过程记录在 [provenance/](provenance/README.md)；第三方素材的来源与许可见 [ASSETS.md](ASSETS.md)；数据说明见 [data/README.md](data/README.md)。HOT 和 Global Carbon Budget 的原始数据不随仓库分发，可用 `scripts/fetch_ch04_data.py` 下载。阅读和编译都不需要 API 密钥。

## 参与、许可与引用

欢迎修订表达、报告问题、补充经过核验的案例，详见 [贡献说明](CONTRIBUTING.md)。请保持中英文含义一致，保留来源记录，并把模拟数据、教学假设与真实研究证据区分清楚。

正文、图版和原创数据采用 [CC BY 4.0](LICENSES/CC-BY-4.0.txt)，代码采用 [MIT](LICENSES/MIT.txt)；第三方素材遵循各自的许可（见 [ASSETS.md](ASSETS.md)）。许可的具体范围、AI 生成素材和商标说明见 [LICENSE](LICENSE)。

本书已在 Zenodo 存档：[10.5281/zenodo.23794693](https://doi.org/10.5281/zenodo.23794693)（指向所有版本；v1.0.0 为 [10.5281/zenodo.23794694](https://doi.org/10.5281/zenodo.23794694)）。引用格式：

> TopLocalAI. (2026). *Use AI to Make Better Scientific Figures: From Research Ideas to Paper Figures* (Version 1.0.0). Zenodo. https://doi.org/10.5281/zenodo.23794694

引用信息见 [CITATION.cff](CITATION.cff)。
