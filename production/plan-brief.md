# 给章节规划者的任务说明

你负责为《用 AI 画好科研图》写指定章节的**详细制作规划**（不是正文）。规划会被直接用来：(1) 派 Codex 生成图、派脚本作者写 Matplotlib/TikZ 图；(2) 派写作者写中英文正文。所以必须具体、可执行。

先读：
- BOOK/production/book-spec.md（全书规范，必须遵守）
- (SciDraw product notes, not public) 13 章大纲，可在质量需要时调整）
- BOOK/chapters/zh/01-workflow.tex、02-brief.tex（已有文风样例）
- BOOK/cases/ch07-insulin-glut4/case-plan.md（一个合格案例脚本的样例：关系表、任务书、逐版提示词、检查清单）
- SciDraw AI 能力事实：(SciDraw product notes, not public)

BOOK = .

每章输出一个文件 BOOK/production/plans/chNN.md（先建文件，每写完一部分就写入），包含：

1. **章标题**（中英）与本章读完能做到的 3–5 件事。
2. **小节大纲**：每节标题（中英）、要讲的要点、预计字数、对应哪幅图。总字数 9,000–13,000（中文）。
3. **主案例**：学科、研究情境（真实、教科书级、保守），原始材料是什么、来源/许可；完整走一遍：任务书 → 提示词/代码 → 初稿 → 问题 → 修改指令 → 修订 → 终稿 → 图注 → 核验。写出任务书全文和关键提示词全文。
4. **图清单**（5–8 幅），每幅用这个格式：
   ```
   ### FIG chNN-MM short-name
   - kind: codex-image | python | tikz | sourced | reuse
   - file: figures/chNN/chNN-MM-short-name.png（python/tikz 写 -zh/-en 两个）
   - 教学目的：
   - 画面内容：（逐项）
   - prompt（codex-image，英文全文，除反例外要求 no text, no letters, no labels；给出宽高比）：
   - spec（python：数据集名称、下载 URL、许可、字段、要画什么、好/坏两版的差别、轴与单位；tikz：结构）：
   - 叠加标签（若需要）：中英文标签 + 0–1 相对坐标
   - 图注-中 / caption-en：
   - 核验要点：
   ```
   正反对比图要成对列出。数据图只能用真实公开数据（写明数据集、URL、许可、引用）或明确标注的模拟数据。
5. **「AI 能做 / 不能做 / 作者要核对」表**的内容。
6. **本章检查清单**与 **3 道练习**。
7. **参考文献**：只列你用 Crossref 或出版商页面核对过 DOI 的真实文献；也可引用官方指南（期刊作者指南、ColorBrewer 等），写 URL。

约束：只描述 SciDraw AI 已有能力（见 book-spec 第 8 节）；不写价格积分；不编造数据。完成后用几句话汇报：文件路径、每章图数与 kind 分布、需要外部数据/图像的地方、你不确定的科学点。
