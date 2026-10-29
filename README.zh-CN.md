# 用 AI 画好科研图

**从研究思路到论文配图** · TopLocalAI 开源双语书籍

[English](README.md) · [中文 PDF](pdf/ai-scientific-figures-zh.pdf) · [English PDF](pdf/ai-scientific-figures-en.pdf)

围绕科研表达讲清如何确定绘图任务、使用 AI、核验内容并完成可追溯交付。全书统一以 **SciDraw AI** 组织实践，AI 融入各类图片的构思、制作、修改与检查。

**当前为 v0.1.0 工作稿，日期 2026-10-29。** 中英文均包含前言、第一章、第二章、十三章规划、练习与参考资料。第三至十三章仍在计划中。

## 阅读与构建

LaTeX 是正式编辑源：main.tex 为中文，main-en.tex 为英文；正文分别位于 chapters/zh/、chapters/en/。两版共用案例数据与来源记录，图注和数据图标签分别本地化。

安装包含 XeLaTeX、latexmk、中文支持、Fandol 字体和常用扩展包的 TeX Live 后：

    make check
    make          # 编译中英文
    make zh       # 只编译中文
    make en       # 只编译英文

PDF 输出到 pdf/，临时编译文件保存在忽略的 build/。无需商业字体或 shell escape。仓库中的 PDF 是当前工作稿的阅读副本。

复现数据图时，先在虚拟环境安装 requirements.txt，运行 make figures，再编译。只有这一步需要 Python/Matplotlib；直接编译可使用已经保存的图版。

## 已写内容

- **第一章：建立 AI 科研绘图工作流。** 图片的问题、材料分类、路线选择与资料保存。
- **第二章：把研究内容变成绘图任务书。** 对象、关系、证据状态、数据约束和验收条件。
- **后续规划：** 构图、视觉语言、数据图、方法图、机制图、实验图像、组图与图注、图形摘要、修改、汇报与交付。

## 案例来源

配对数据是人工编制的模拟教学数据：8 个虚构对象、16 个观测值。数据图由 Codex 编写的确定性脚本绘制。机制图是 Codex 内置图像生成的实际输出，附完整输入与核验记录。二者均不代表真实研究结果，也不冒充 SciDraw AI 的生成结果。

界面截图来自本地开发版，/figure-workflow 是开发中的配套入口；截图不意味着该功能已经公开上线。

见 [图版清单](ASSETS.md)、[数据说明](data/README.md)、[案例来源记录](provenance/README.md)。阅读和编译不需要任何 API 密钥。

## 参与和许可

欢迎修订表达、报告问题和补充经过核验的案例，详见 [贡献说明](CONTRIBUTING.md)。正文、原创教学数据及图版采用 **CC BY 4.0**，构建与绘图代码采用 **MIT**。许可范围、AI 素材及商标说明见 [LICENSE](LICENSE)。
