# 全书制作规范（所有写作者、出图者必须遵守）

书名：《用 AI 画好科研图：从研究思路到论文配图》/ *Use AI to Make Better Scientific Figures: From Research Ideas to Paper Figures*。
读者：研究生、博士后、青年研究人员。实践平台统一称 **SciDraw AI**（拼写固定）。AI 贯穿每一章：每章都要具体说明 AI 在这一环节能做什么、不能做什么、作者要核对什么。

仓库：`.`（下称 BOOK）。

## 1. 体量

- 每章正文（中文）9,000–13,000 字，排版后约 14–20 页；5–8 幅有教学作用的图。全书目标约 200 页/版。
- 不靠空话凑字。每节都要有：具体情境 → 原理 → AI 怎么做（给出可复制的提示词或操作） → 实际结果图 → 问题与修改 → 核对要点。

## 2. 每章结构（LaTeX `\section` 级）

1. 开篇情境（一个具体研究者遇到的具体问题，半页内）
2. 3–5 节核心内容，每节带图
3. 一个**贯穿本章的完整案例**：原始材料 → 任务书 → 提示词/代码 → 初稿 → 问题 → 修改指令 → 修订稿 → 终稿 → 图注 → 核验
4. 「AI 在这一步能做什么 / 不能做什么」对照表（`tabularx`，每章一张）
5. 本章检查清单（`itemize`）
6. 练习 3 道（含一道用 SciDraw AI 实际操作的）

## 3. 学科多样性

全书案例跨学科：生物医学、材料/化学、工程、地球与环境、计算机/数据科学。每章的主案例学科在各章规划中指定，避免全书只有细胞图。

科学内容必须正确、保守、达到教科书水平。只用确立的关系；简化要明说。引用文献必须真实存在（用 Crossref 核对 DOI），不确定就不引。

## 4. 图片的四种来源（每幅图标明 kind）

| kind | 由谁做 | 用于 | 要求 |
|---|---|---|---|
| `codex-image` | Codex 内置图像生成 | 示意图、机制图、草图、正反例、版式示意 | 除"故意展示伪文字"的反例外，**底图不含任何文字**；需要标签时在 LaTeX 中用 TikZ 叠加（见第 6 节） |
| `python` | Matplotlib 脚本（`scripts/`） | 一切数据图 | 数据来自真实公开数据集（写明许可与引用）或明确标注的模拟数据；生成中英两版；中文版走 PGF/XeLaTeX 输出（照 `scripts/plot_paired.py`），避免 Fandol 空白字问题 |
| `tikz` | 写在 `figures/chNN/*.tex` | 流程框图、对照表式图、布局线框 | 中英文各一份或用宏切换 |
| `sourced` | 外部开放许可图像 | 实验原图（第 8 章等） | 仅 CC0 / CC BY / 公有领域；在 `ASSETS.md` 记录来源 URL、作者、许可、改动 |

图像生成由 Codex 完成。正文可以把这些图当作 SciDraw AI 工作流的示例来讲解（两者底层生成能力相当），**不必逐图声明"非 SciDraw 生成"**；但 `provenance/` 必须如实记录实际工具、提示词与修改过程。

## 5. 文件与编号

- 图：`BOOK/figures/chNN/chNN-MM-short-name.{png,pdf,tex}`，中英不同时加 `-zh`/`-en`。
- 图标签：`\label{fig:chNN-MM}`；表 `\label{tab:chNN-MM}`。两版编号完全一致。
- 章节文件：`BOOK/chapters/zh/NN-slug.tex`、`BOOK/chapters/en/NN-slug.tex`。
- 每章规划：`BOOK/production/plans/chNN.md`；出图记录：`BOOK/provenance/chNN/`。

## 6. LaTeX 约定

- 只写章节正文（从 `\chapter{...}` 开始），不改 `main.tex`、`shared/preamble.tex`（需要新宏写在规划里提出）。
- 插图：
  ```latex
  \begin{figure}[htbp]\centering
  \includegraphics[width=\linewidth]{figures/ch07/ch07-04-v4-final.png}
  \caption{...}\label{fig:ch07-04}
  \end{figure}
  ```
- 叠加标签：
  ```latex
  \begin{tikzpicture}
  \node[anchor=south west,inner sep=0] (img) at (0,0) {\includegraphics[width=\linewidth]{...}};
  \begin{scope}[x={(img.south east)},y={(img.north west)}]
    \node[font=\small] at (0.42,0.81) {胰岛素受体};
  \end{scope}
  \end{tikzpicture}
  ```
- 提示词用现有 `Prompt` 环境（`\begin{Prompt}...\end{Prompt}`）；提示框用 `BookNote`。
- 交叉引用用 `图~\ref{fig:...}` / `Figure~\ref{fig:...}`。参考文献：每章末尾 `\section*{参考文献}` + `itemize`（不要用 `\cite`，统一的参考文献表之后整理）。
- 特殊字符要转义（`%`、`&`、`_`、`#`）。

## 7. 中英两版

- 中文版先写，英文版据中文版**用地道英文重写**，而不是逐句翻译；章节、图、表、编号一一对应。
- 图注中英分别维护。

## 8. SciDraw AI 功能描述必须真实

只描述已存在的能力，参照 `(SciDraw product notes, not public)` 第「当前实现中必须准确描述的事实」一节。要点：

- 有：提示词绘图（`/ai-drawing`）、草图模式（草图不等于布局锁定）、参考图修改、机制图生成（`/mechanism-figure-generator`）、流程图（`/workflow-diagram-generator`）、图形摘要（`/graphical-abstract-maker`）、数据可视化（`/sci-vis`：上传数据、对话生成与修改、历史版本）、组图（`/multi-panel-figure-maker`：网格、裁剪、编号、导出 TIFF/PNG/PDF/PPTX）、图注辅助（`/figure-legend`，不得编造样本量/统计）、图片检查（`/figure-checker`：技术检查，不代表科学审核）、科研绘图向导（`/figure-workflow`）。
- 不能写：对象锁定、自动理解整篇论文、所有导出都是可编辑矢量、跨工具自动传图、云端项目系统。
- 不写具体价格和积分数。

## 9. 诚信底线

- 不生成假实验结果；模拟数据、模型生成的"实验图样"必须在图注中标明。
- 实验原始图像不做生成式美化。
- 不说某张 AI 图"可直接投稿"；始终强调作者核验。
