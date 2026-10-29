# 第 7 章案例脚本：胰岛素刺激的 GLUT4 转位

> 案例编号：ch07-insulin-glut4
> 章节：第七章 机制图与结构示意图 / Mechanisms and Structures
> 状态：案例脚本（待生成图像、待专业核验）
> 撰写日期：2026-10-29


## 使用说明（给执行生图与排版的人）

- 本文件是一个完整教学案例的“剧本”：每一版图都有目的、给图像模型的英文提示词、预期问题、检查清单和下一版修改指令。
- 图像由 Codex 内置图像生成按本文提示词制作。正文按第 2 章约定，可把这些图作为 SciDraw AI 工作流示例讲解；但 `provenance/` 与 `ASSETS.md` 中必须如实记录每张图的实际生成工具、提交的完整提示词、生成次数和人工修改。
- **除 V1 外，所有底图都不得包含任何可读文字、字母、数字或符号标签。** 文字一律在 LaTeX/TikZ 中叠加。V1 中出现伪文字是有意展示的失败。
- 每次生成后，先用第 3 节的关系表和第 6 节的核验表检查科学内容，再看美观。生成结果有随机性，同一提示词不保证一次满足全部条件；不满足时可重试，但要在 provenance 记录重试次数，并保留一张有代表性的失败稿用于正文。
- 本案例只表达教科书和综述层面已确立的机制，不涉及任何实验数据、样本量或统计结果。

---

## 1. 案例目标

### 1.1 这张图要回答的问题

用一张示意图回答：**胰岛素与细胞表面受体结合后，信号如何经过一条有序的激酶级联，最终让细胞内储存的 GLUT4 转运到质膜，从而增加葡萄糖进入细胞？**

按第 1 章的句式：

> 看完这张图，读者应该能够理解**胰岛素信号从质膜受体经 IRS-1、PI3K、Akt 到 AS160 的传递顺序，以及 AS160 被抑制后 GLUT4 储存囊泡转位并与质膜融合的结果**，并能从图中找到**每一条关系的方向和类型（激活、抑制、酶促转化、囊泡转位、葡萄糖跨膜流动）**。

### 1.2 读者能核查什么

读者应能在图中逐项找到并核对：

1. 胰岛素位于胞外，与跨膜的胰岛素受体结合（结合用“接触”表示，不画箭头）。
2. 受体胞内段发生酪氨酸自身磷酸化（磷酸化标记）。
3. 受体 → IRS-1 → PI3K 的激活顺序。
4. PI3K 在质膜内侧把 PIP2 转化为 PIP3（酶促转化，与“激活”线型不同）。
5. PIP3 招募 PDK1 与 Akt 至质膜；PDK1 与 mTORC2 分别磷酸化激活 Akt。
6. Akt 磷酸化 AS160，**抑制**其 Rab-GAP 活性（抑制线型）。
7. AS160 原本抑制 Rab（把 Rab-GTP 转为 Rab-GDP）；抑制被解除后 Rab-GTP 增多（“抑制的抑制”在图上可追溯为两条 T 形线串联）。
8. GLUT4 储存囊泡（GSV）沿转位箭头移向质膜并融合，GLUT4 出现在质膜上。
9. 葡萄糖从胞外经质膜上的 GLUT4 进入胞质（物质流动线型，与信号线型不同）。
10. 图例说明全部五种线型；图注说明省略了哪些分支。

### 1.3 用途与尺寸

- 用途：一篇代谢/细胞生物学论文的 **Figure 1 机制示意图**（引言或讨论中用来交代背景机制），读者为了解基础细胞生物学的同行。
- 版面：**双栏通栏宽约 174 mm**，建议高度 95–105 mm（宽高比约 16:9 至 7:4）。
- 最终字号：叠加标签在印刷尺寸下不小于 6–7 pt，主要对象名称 7–8 pt。
- 交付：底图 PNG（≥ 300 dpi 等效，宽 ≥ 2400 px）+ TikZ 叠加层 → PDF 矢量文字 + 位图底图。

### 1.4 本案例在章中承担的教学点

- 从第 2 章的“关系表”直接驱动绘图，而不是从名词清单出发。
- 线型语义：激活、抑制、酶促转化、转位、物质流动必须各有一种线型，并在图例中定义。
- “抑制的抑制”这类双重否定关系如何画得可核对。
- 空间分区（胞外 / 质膜 / 胞质）本身就是信息，不是装饰。
- 为什么终稿采用“无字底图 + LaTeX 叠加标签”：图像模型的拼写和位置不可靠。
- 证据状态：哪些是确立关系、哪些是为了可读性做的简化，并在图注中写明。

---

## 2. 研究情境与依据

### 2.1 情境设定

设想一位研究骨骼肌或脂肪细胞葡萄糖摄取的研究生，要在论文 Figure 1 中交代“经典胰岛素—GLUT4 通路”这一背景，以便后续图中说明自己研究的是哪一环。Figure 1 本身**不报告任何新发现**，只总结已确立的知识，因此每条关系都应能指向综述或经典文献。作者自己的研究假设（如果有）应在后续图中以“假设”线型单独表示，不混入本图。

### 2.2 机制逐步关系与证据状态

“确立”指在主流教科书和下列综述中作为共识表述的关系；“简化”指关系本身确立，但为了单图可读而省略了细节、并列分支或中间步骤，需在图注中说明。

| # | 起点 | 终点 / 结果 | 关系 | 位置 | 证据状态 | 简化说明 |
|---|---|---|---|---|---|---|
| R1 | 胰岛素 | 胰岛素受体（IR）α 亚基 | 结合 | 胞外 | 确立 | 不画 α2β2 异四聚体的完整结构，只画为一个跨膜二聚体轮廓 |
| R2 | 胰岛素结合 | IR β 亚基胞内酪氨酸激酶域 | 自身磷酸化（激活） | 质膜胞内侧 | 确立 | 不标具体酪氨酸位点 |
| R3 | 活化 IR | IRS-1 | 酪氨酸磷酸化（激活） | 质膜下胞质 | 确立 | 肌肉/脂肪中 IRS-1 与 IRS-2 均有作用，本图只画 IRS-1 |
| R4 | 磷酸化 IRS-1 | I A 类 PI3K（p85/p110） | 招募并激活 | 质膜下 | 确立 | 不画 p85 调节亚基与 p110 催化亚基的分别结构 |
| R5 | PI3K | PI(4,5)P2 → PI(3,4,5)P3 | 酶促转化 | 质膜内叶 | 确立 | 不画 PTEN/SHIP2 的反向去磷酸化 |
| R6 | PIP3 | PDK1、Akt 招募至质膜 | 招募（经 PH 结构域） | 质膜内叶 | 确立 | 用“靠近膜”表示，不单独设箭头；或用短接触线表示 |
| R7 | PDK1 | Akt（Thr308） | 磷酸化激活 | 质膜内侧 | 确立 | 不标位点数字 |
| R8 | mTORC2 | Akt（Ser473） | 磷酸化激活 | 质膜内侧 | 确立（Sarbassov 等 2005） | mTORC2 自身如何被胰岛素激活仍有细节争议，本图**不画**任何指向 mTORC2 的上游箭头 |
| R9 | Akt | AS160（TBC1D4） | 磷酸化 → 抑制其 Rab-GAP 活性 | 胞质 | 确立（Sano 等 2003） | 不画 14-3-3 结合；骨骼肌中 TBC1D1 也参与，本图只画 AS160；Akt 有多个亚型，以 Akt2 为主，图中写作“Akt” |
| R10 | AS160（未被抑制时） | Rab（GTP → GDP） | GAP 作用，即抑制 Rab 活性 | GSV 表面 | 确立 | 不指名具体 Rab（脂肪细胞中常提 Rab10，肌肉中 Rab8A/Rab13），图中写作“Rab” |
| R11 | Rab-GTP | GSV 向质膜移动、停靠 | 促进转位 | 胞质 → 质膜 | 确立（机制细节仍在研究中） | 不画微管、马达蛋白、肌动蛋白重构 |
| R12 | GSV | 与质膜融合，GLUT4 插入质膜 | 膜融合 | 质膜 | 确立 | 不画 SNARE 复合物（VAMP2/syntaxin-4/SNAP23/Munc18c） |
| R13 | 胞外葡萄糖 | 胞内葡萄糖 | 经 GLUT4 的易化扩散（物质流动） | 跨质膜 | 确立 | 不画后续己糖激酶磷酸化及代谢去路 |

**明确不画的内容（并在图注中声明省略）：**

- Grb2–SOS–Ras–MAPK 分支（与本图问题无关）。
- CAP–Cbl–TC10 分支（其在生理条件下的必要性存在争议，不作为确立关系表达）。
- GLUT4 的内吞与再循环、受体内化与降解、负反馈（如 S6K 对 IRS-1 的丝氨酸磷酸化）。
- 运动/肌肉收缩引起的、不依赖胰岛素的 GLUT4 转位通路（AMPK 等）。
- 任何定量信息：转位倍数、摄取速率、时间常数。

**“抑制的抑制”说明（R9 + R10）：** Akt 并不直接“激活”转位。Akt 抑制 AS160，AS160 原本抑制 Rab；两次抑制串联的净效应是 Rab-GTP 增多。图中应保留两条 T 形线，而不是把 Akt 直接画成指向 GSV 的激活箭头——后者虽然净效应方向正确，却抹去了可核对的中间环节。

### 2.3 参考文献

以下文献的作者、年份、期刊、卷页与 DOI 已于 2026-10-29 通过 Crossref API 查询核对存在且元数据一致；正文引用前仍建议作者阅读原文确认具体表述。

1. Saltiel AR, Kahn CR. Insulin signalling and the regulation of glucose and lipid metabolism. *Nature*. 2001;414(6865):799–806. doi:10.1038/414799a —— 胰岛素受体、IRS、PI3K–Akt 主干的经典综述（R1–R7）。
2. Leto D, Saltiel AR. Regulation of glucose transport by insulin: traffic control of GLUT4. *Nature Reviews Molecular Cell Biology*. 2012;13(6):383–396. doi:10.1038/nrm3351 —— GLUT4 储存囊泡、AS160/Rab、停靠与融合（R9–R13）。
3. Klip A, McGraw TE, James DE. Thirty sweet years of GLUT4. *Journal of Biological Chemistry*. 2019;294(30):11369–11381. doi:10.1074/jbc.REV119.008351 —— GLUT4 研究的较新综述，可用于核对肌肉与脂肪细胞间差异及仍未解决的问题。
4. （原始研究，R9）Sano H, Kane S, Sano E, Mîinea CP, Asara JM, Lane WS, Garner CW, Lienhard GE. Insulin-stimulated phosphorylation of a Rab GTPase-activating protein regulates GLUT4 translocation. *Journal of Biological Chemistry*. 2003;278(17):14599–14602. doi:10.1074/jbc.C300063200 —— 首个报道 Akt 磷酸化 AS160 调控 GLUT4 转位的研究。
5. （原始研究，R8）Sarbassov DD, Guertin DA, Ali SM, Sabatini DM. Phosphorylation and regulation of Akt/PKB by the Rictor-mTOR complex. *Science*. 2005;307(5712):1098–1101. doi:10.1126/science.1106148。

> 全部五条的作者名单、卷（期）、页码、年份和 DOI 均已与 Crossref 元数据逐项比对一致。排版进 BibTeX 时以 Crossref 导出的条目为准。

---

## 3. 绘图任务书（完整版）

格式沿用第 2 章的十个填写项。正文中可展示为 `Prompt` 环境；SciDraw AI 中的操作是：在**科研绘图向导**（`/zh/figure-workflow`）选择“机制图与流程图”路线，把默认任务书替换为下面内容并下载副本，再从路线中的机制图入口进入绘图（提示词生成图片）。向导只负责组织任务书和串联工具，不会自动检查科学关系。

### 3.1 任务书正文

```
【用途与读者】论文 Figure 1 背景机制示意图，双栏通栏宽约 174 mm、高约 100 mm；
读者为了解基础细胞生物学的代谢/细胞生物学同行。

【目标】让读者看清：胰岛素经 IR → IRS-1 → PI3K → PIP3 → Akt 的信号顺序；
Akt 抑制 AS160、AS160 抑制 Rab 这一“抑制的抑制”；以及由此引起的 GLUT4 储存
囊泡转位、与质膜融合和葡萄糖进入细胞。

【材料】教科书与综述层面的已确立关系：Saltiel & Kahn 2001；Leto & Saltiel 2012；
Klip, McGraw & James 2019。本图不含作者的新发现、假设或任何实验数据。

【对象】（每个对象只出现一次，GLUT4 除外——见下）
胞外：胰岛素（小分子簇）、葡萄糖（3–5 个小六边形）。
质膜：脂双层；胰岛素受体（跨膜二聚体）；PIP2 与 PIP3（内叶上的脂质头基）；
      融合后插入质膜的 GLUT4（1 个）。
胞质：IRS-1、PI3K、PDK1、Akt、mTORC2、AS160、Rab（结合在囊泡表面）、
      GLUT4 储存囊泡（GSV，2–3 个小囊泡成簇，囊泡膜上嵌 GLUT4）。
GLUT4 允许出现两处：囊泡膜上（储存态）和质膜上（转位后），二者形状一致。
磷酸化：受体胞内段、IRS-1、Akt、AS160 上各有小圆点标记，不写字母。

【关系】（线型定义见 3.2）
R1 胰岛素—受体：直接接触，无箭头。
R2 受体自身磷酸化：受体胞内段上的磷酸化圆点，无箭头。
R3 受体 → IRS-1：激活箭头。
R4 IRS-1 → PI3K：激活箭头。
R5 PI3K 催化 PIP2 → PIP3：酶促转化线（细线、空心箭头，PI3K 以短线接触弧线中点）。
R6 PIP3 招募 PDK1 与 Akt：PDK1、Akt 紧贴质膜内叶 PIP3 处，无箭头。
R7 PDK1 → Akt：激活箭头。
R8 mTORC2 → Akt：激活箭头；mTORC2 不画任何上游箭头。
R9 Akt ⊣ AS160：抑制线（T 形端）。
R10 AS160 ⊣ Rab：抑制线（T 形端）。
R11 Rab → GSV 转位：从囊泡簇出发、向上指向质膜的转位箭头。
R12 GSV 与质膜融合：转位箭头终点即质膜上的 GLUT4。
R13 葡萄糖经质膜 GLUT4 进入胞质：物质流动线，从胞外穿过 GLUT4 到胞质。

【布局】横向长方形（16:9）。上方 20% 为胞外，水平质膜位于高度约 20–28%，
下方为胞质；底部 10% 留空给图例。信号主线从左到右沿质膜下方推进：
受体在最左侧，IRS-1、PI3K、PDK1、Akt 依次向右；mTORC2 在 Akt 下方；
AS160 在 Akt 右下方；GSV 簇在右下部胞质深处；转位箭头从 GSV 向上到右侧质膜；
葡萄糖在右上方胞外，经质膜 GLUT4 进入。阅读路径呈“左→右，再右下→右上”。

【视觉】白底、扁平二维、矢量插画风格，无渐变、无阴影、无高光、无 3D。
颜色角色：信号蛋白统一中等蓝；AS160 与 Rab 为低饱和灰蓝；
GLUT4、GSV 与葡萄糖为柔和橙色；膜为浅暖灰；磷酸化为小琥珀色圆点；
线条深灰。全图不超过 3 个色相加灰色。对象之间留足空白，以便叠加标签。

【限制】图中不出现任何文字、字母、数字或符号标签；不画细胞核、线粒体、
内质网、微管、肌动蛋白或任何未列出的分子；不画 MAPK、CAP/Cbl/TC10 分支；
不画 GLUT4 内吞；不画实验数据、图表、比例尺；不画装饰性背景。

【图例】（在 LaTeX 中制作）解释：激活箭头、抑制线、酶促转化、囊泡转位、
物质流动、磷酸化圆点；注明“已省略的分支见图注”。

【验收】对象齐全且不重复（GLUT4 两处例外）；13 条关系逐条对应，方向与线型正确；
Akt 与 GSV 之间没有直接激活箭头；三个空间分区清楚；底图无任何文字；
在 174 mm 宽下叠加标签后可读。
```

### 3.2 关系与箭头语义（线型规范）

| 关系类型 | 用于 | 线型 | 端点 | 颜色 / 粗细（印刷尺寸） | 备注 |
|---|---|---|---|---|---|
| 结合 / 招募 | R1、R6 | 无线，对象直接接触 | — | — | 用空间接触表达，避免箭头泛滥 |
| 激活 / 促进 | R3、R4、R7、R8 | 实线 | 实心三角箭头 | 深灰 #3A3A3A，0.8 pt | 全图唯一的“实线 + 实心头” |
| 抑制 | R9、R10 | 实线 | 平头 T 形端 | 深灰 #3A3A3A，0.8 pt | T 形端必须垂直于线并紧贴靶标 |
| 酶促转化 | R5 | 细实线弧 | 空心 V 形箭头 | 中灰 #7A7A7A，0.5 pt | 酶以短垂线接触弧线中点，酶本身不是起点 |
| 囊泡转位 | R11–R12 | 粗虚线 | 大号空心箭头 | 柔和橙 #E39B5B，1.5 pt | 唯一的粗虚线；表示“空间移动”而非“信号” |
| 物质流动 | R13 | 点线 | 小实心箭头 | 深橙 #C46A2A，0.8 pt | 唯一的点线；穿过 GLUT4 |
| 磷酸化 | R2、R3、R7–R9 | 小圆点 | — | 琥珀 #E3B23C | 不写“P”，图例解释 |

注意：图像模型无法保证精确的色值和粗细。色值写入提示词作为方向；终稿若偏差明显，在 V3/V4 中逐项要求修正，或在 TikZ 叠加层中重画箭头（见 V4 方案 B）。

### 3.3 空间布局草案（相对坐标，x 向右、y 向下，0–1）

| 区域 / 对象 | 中心或范围 |
|---|---|
| 胞外区 | y 0.00–0.20 |
| 质膜（脂双层） | y 0.20–0.28，横贯全宽 |
| 胞质区 | y 0.28–0.88 |
| 图例留空 | y 0.88–1.00 |
| 胰岛素 | (0.12, 0.10) |
| 胰岛素受体 | x 0.12，y 0.12–0.36 |
| IRS-1 | (0.20, 0.46) |
| PI3K | (0.30, 0.37) |
| PIP2 → PIP3 | 内叶 x 0.33–0.41，y ≈ 0.28 |
| PDK1 | (0.42, 0.36) |
| Akt | (0.53, 0.37) |
| mTORC2 | (0.53, 0.57) |
| AS160 | (0.63, 0.52) |
| Rab（囊泡表面） | (0.71, 0.64) |
| GSV 簇 | x 0.70–0.82，y 0.66–0.80 |
| 质膜上 GLUT4 | (0.87, 0.24) |
| 葡萄糖 | x 0.82–0.92，y 0.05–0.14 |

### 3.4 必须出现的标签（在 LaTeX 中叠加）

对象名：Insulin、Insulin receptor、IRS-1、PI3K、PIP2、PIP3、PDK1、Akt、mTORC2、AS160 (TBC1D4)、Rab-GTP、GLUT4 storage vesicles、GLUT4、Glucose。
分区名：Extracellular、Plasma membrane、Cytoplasm。
（可选）关系标注：translocation & fusion。
中文版对应：胰岛素、胰岛素受体、IRS-1、PI3K、PIP2、PIP3、PDK1、Akt、mTORC2、AS160（TBC1D4）、Rab-GTP、GLUT4 储存囊泡、GLUT4、葡萄糖；胞外、质膜、胞质；转位与融合。
分子名缩写保持英文，不译。

### 3.5 禁止出现的内容

- 底图中的任何文字、伪文字、字母、数字、“P”字样。
- 3D 渲染、光泽、渐变、投影、玻璃质感、发光、景深。
- 未列出的细胞器和细胞骨架；整细胞轮廓以外的“细胞写实背景”。
- 未列出的分子或分支（MAPK、CAP/Cbl/TC10、AMPK、胰岛素降解、受体内化）。
- 重复对象（例如出现两个 Akt、两个受体）。
- 从 Akt 直接指向 GSV 或 GLUT4 的激活箭头。
- 任何数据元素：坐标轴、柱状图、数值、星号、比例尺。
- 用颜色或箭头暗示未经确立的关系（例如从 mTORC2 上游连到受体）。

---

## 4. 版本序列

文件命名建议：`figures/ch07/glut4-v0-sketch.png`、`glut4-v1-vague.png`、`glut4-v2-brief.png`、`glut4-v3-revised.png`、`glut4-v4-base.png`（底图）与 `glut4-v4-final.pdf`（叠加后），对比图 `glut4-pairA-mixed.png` / `glut4-pairA-unified.png`、`glut4-pairB-many.png` / `glut4-pairB-restrained.png`。每张图在 `provenance/ch07/` 下保存同名 `.txt`，记录实际提交的提示词、工具、日期、生成次数与人工修改。

各版统一的画布要求：横向 16:9（如 1920×1080 或更高），白底。

---

### V0 手绘构思草图

**目的。** 展示作者在动笔前用铅笔把关系表“摆”到纸上的过程：只确定分区、对象的大致位置和阅读路径，不追求美观。这一版说明：草图是给自己和 AI 看的布局意图，后续可以作为 SciDraw AI 草图模式（草图生成图片）的输入之一。

> 来源说明：本书中 V0 由图像模型模拟“作者的铅笔草图”，provenance 中必须注明这是模拟草图，而非真实手稿扫描。若作者愿意提供真实手绘，优先使用真实手绘。

**提示词（英文，交给图像模型）：**

```
A rough pencil sketch on slightly off-white sketchbook paper, photographed flat
from directly above, evenly lit, no hands, no pencils, no objects on the paper.
Landscape 16:9. It is a researcher's quick planning sketch of a cell signaling
diagram, drawn with a single graphite pencil, loose confident lines, some
construction lines and small erasure marks.

Layout of the sketch:
- A long horizontal double line across the upper fifth of the page, representing
  a cell membrane (two parallel lines with short tick marks between them).
- Above the membrane, near the left edge, a small cluster of dots touching the
  top of a Y-shaped receptor that crosses the membrane.
- Below the membrane, a left-to-right chain of five simple rounded blobs of
  different sizes, connected by short arrows with filled heads, running parallel
  to the membrane.
- Between the second and third blob, a small curved arrow drawn along the
  underside of the membrane line.
- One extra rounded blob below the fourth blob, with an arrow pointing up into it.
- To the lower right, a blob connected by a line ending in a short flat bar
  (a T-shaped end), then a second line with a flat bar end touching a small
  circle on the surface of a cluster of three small circles (vesicles).
- From the vesicle cluster, a long dashed arrow curving upward to the membrane on
  the right side, where a small rectangle sits inside the membrane.
- Above the membrane on the right, three tiny hexagons with a dotted arrow
  passing down through the small rectangle.
- Bottom tenth of the page left blank.

Strictly no writing of any kind: no letters, no words, no numbers, no labels,
no annotations, no title. Only lines, blobs, arrows and shapes. Pencil gray only,
no color.
```

**预期问题 / 故意暴露的问题：**

- 草图本身没有名字，读者看不出哪个团块是哪个分子 —— 这正是要说明的：草图只承担布局，含义由任务书承担。正文中用 LaTeX 在草图上加编号圆圈（①–⑬）对应关系表。
- 模型可能自作主张加文字或涂鸦式“标注”，或者把团块画成写实细胞。
- 可能缺少 T 形端，或者把所有连线都画成同一种箭头。

**作者检查清单：**

- [ ] 质膜在上方约 1/5 处，三个分区可辨。
- [ ] 受体在最左，信号链沿膜下从左到右。
- [ ] 存在两条 T 形端线，串联在“第四团块下游”与“囊泡”之间。
- [ ] 存在一条虚线转位箭头和一条穿膜的点线。
- [ ] 无任何文字、数字。
- [ ] 底部留空。

**下一版修改指令（→ V1/V2）：** V0 不直接修改。它用于两种后续路径的对照：（a）V1 故意不用草图也不用任务书，只给一句话；（b）V2 使用完整任务书。正文可提示读者：也可以把 V0 上传到 SciDraw AI 的草图模式，同时附上任务书文字，比较“草图 + 任务书”与“只有任务书”的差别。草图约束不等于对象锁定或硬性布局保持，生成后仍需逐条核对。

---

### V1 一句模糊提示词的初稿

**目的。** 复现常见的第一次尝试，让读者看到“看起来很专业”的图在科学上如何不可用。这是全书唯一允许底图出现文字的版本——伪文字正是要展示的失败。

**提示词（英文，交给图像模型，原样一句）：**

```
Make a beautiful, professional scientific illustration of insulin signaling and
GLUT4 translocation for a top journal.
```

**预期会出现 / 故意暴露的问题（逐项在正文中用红色编号圈出）：**

1. **过度装饰：** 写实或卡通细胞、细胞核、线粒体、渐变背景、发光粒子。
2. **3D 与光泽：** 蛋白画成带高光的玻璃球或软糖质感，阴影和景深让对象边界不清。
3. **伪文字：** 标签像英文却拼错（如 “Insluin”“GLUT-A”“PI3KK”），或是不可读字符串；位置与对象不对应。
4. **箭头语义混乱：** 所有关系都用同一种发光箭头；抑制被画成激活；箭头方向倒置；箭头“漂浮”不连接任何对象。
5. **对象缺失或重复：** 缺 AS160、Rab、mTORC2 或 PIP2/PIP3；出现两个受体；GLUT4 只画在囊泡里或只画在膜上，缺少“转位”过程。
6. **空间错误：** 胰岛素画在胞内；PI3K 漂在胞质中央与膜无关；受体不跨膜。
7. **未要求的内容：** MAPK 分支、细胞核内的基因表达、血管或器官插图。
8. **捷径式因果：** 从 Akt 或受体直接画一支大箭头到 GLUT4，抹去 AS160/Rab 环节。

**作者检查清单（用第 6 节核验表打分）：**

- [ ] 13 条关系各自是否能找到？记录“缺失 / 错误 / 正确”。
- [ ] 所有文字是否拼写正确、位置正确？（预期：否）
- [ ] 线型数量与含义是否可由读者推断？（预期：否）
- [ ] 是否有未列出的对象？逐个列出。
- [ ] 在 174 mm 宽时，细节和文字是否可读？

**下一版修改指令（→ V2）：** 不要在 V1 基础上“修修补补”，也不要只追加“更简洁、更准确”。改为从第 3 节任务书重新生成：明确对象清单、13 条关系与线型、三分区布局，并要求底图无文字。正文要点：V1 的问题不是“不够漂亮”，而是输入里没有关系、没有线型定义、没有空间约束，模型只能自己补。

---

### V2 用完整任务书得到的结构正确稿

**目的。** 证明结构正确主要来自输入的完整度：对象、关系、线型、布局全部写明后，初稿就能在科学结构上基本可核对。允许风格尚未统一。

**提示词（英文，交给图像模型）：**

```
Flat 2D scientific schematic for a journal figure, landscape 16:9, pure white
background. Style: clean vector illustration, flat fills, thin dark outlines,
no gradients, no shadows, no highlights, no 3D, no glow, no texture.

ABSOLUTELY NO TEXT: no letters, no words, no numbers, no symbols, no labels,
no legend text, no title. Labels will be added later by the author.

SPACE (top to bottom):
- Top 20% = extracellular space, white.
- A horizontal lipid bilayer plasma membrane spanning the full width at 20-28% of
  the image height, drawn as two rows of small round light warm-gray head groups
  with short tails between them.
- 28-88% = cytoplasm, white or very faint gray.
- Bottom 12% left completely empty (reserved for a legend).

OBJECTS (each appears exactly once unless stated):
1. Insulin: a small cluster of 3 dark blue round beads in the extracellular
   space at the far left (about 12% from the left), touching the top of the
   receptor.
2. Insulin receptor: a symmetric two-armed transmembrane receptor (like a
   rounded "Y" pair) crossing the membrane at about 12% from the left, medium
   blue, its intracellular part extending below the membrane. Two small amber
   dots on its intracellular part (phosphorylation).
3. IRS-1: a medium-blue rounded elongated shape in the cytoplasm just right of
   and below the receptor (about 20% from left, 46% from top), with one small
   amber dot.
4. PI3K: a medium-blue two-lobed shape just under the membrane at about 30% from
   left.
5. PIP2 and PIP3: on the inner leaflet of the membrane between 33% and 41% from
   left, a few lipid head groups; the ones on the left plain gray (PIP2), the ones
   on the right slightly larger with a small extra bump (PIP3).
6. PDK1: a small medium-blue oval touching the inner leaflet at about 42% from
   left.
7. Akt: a medium-blue oval touching the inner leaflet at about 53% from left,
   with two small amber dots.
8. mTORC2: a medium-blue compact cluster of three joined circles below Akt
   (about 53% from left, 57% from top).
9. AS160: a desaturated gray-blue rounded shape at about 63% from left, 52% from
   top, with one small amber dot.
10. GLUT4 storage vesicles: a cluster of three small round vesicles with pale
   orange membranes in the lower right cytoplasm (70-82% from left, 66-80% from
   top). Each vesicle has one small orange GLUT4 transporter (a short
   barrel shape) embedded in its membrane.
11. Rab: a small gray-blue bead attached to the surface of the upper-left vesicle
   of the cluster.
12. GLUT4 in the plasma membrane: one orange barrel-shaped transporter embedded
   in the plasma membrane at about 87% from left, same shape as on the vesicles.
13. Glucose: four small orange hexagons in the extracellular space above the
   membrane GLUT4 (82-92% from left).

RELATIONS (draw exactly these, nothing else):
- Activation = solid dark gray line with a filled triangular arrowhead:
  receptor -> IRS-1; IRS-1 -> PI3K; PDK1 -> Akt; mTORC2 -> Akt (pointing up).
- Inhibition = solid dark gray line ending in a short flat perpendicular bar
  (T-bar) touching the target: Akt -| AS160; AS160 -| Rab.
- Enzymatic conversion = a thin mid-gray curved arc running along the inner
  leaflet from the PIP2 head groups to the PIP3 head groups, ending in an open
  V-shaped arrowhead; PI3K touches the middle of this arc with a short stub.
- Translocation = one thick dashed pale-orange arrow with a large open arrowhead,
  starting at the vesicle cluster and curving upward to the GLUT4 in the
  plasma membrane.
- Substance flow = a dotted dark-orange line with a small filled arrowhead from
  the glucose hexagons down through the membrane GLUT4 into the cytoplasm.
- Insulin touches the receptor directly with no arrow. PDK1 and Akt sit
  directly on the membrane with no arrow from PIP3.

DO NOT DRAW: nucleus, mitochondria, endoplasmic reticulum, microtubules, actin,
other organelles, any other proteins, any other arrows, any arrow from Akt
directly to the vesicles or to GLUT4, any upstream arrow into mTORC2, charts,
numbers, scale bars, decorative backgrounds, glowing particles.
```

**预期会出现的问题（留给 V3 修）：**

- 颜色倾向接近但不统一（蓝色深浅不一、橙色偏红或偏黄；膜颜色太重）。
- 线条粗细不一，T 形端偶尔画成小箭头或圆头；酶促转化弧线与激活箭头区分不明显。
- 对象大小层级混乱：小分子（胰岛素、葡萄糖）过大，或 GSV 太小不易辨认。
- 部分对象拥挤，缺乏标签留白；底部留空可能被占用。
- 可能残留少量伪文字或类似字母的符号（即使要求无文字）——一旦出现必须重生成或手工去除，不能保留到终稿。
- 偶发：多一个对象（第二个 Akt），或缺一条关系（mTORC2 → Akt）。

**作者检查清单：**

- [ ] 用第 6 节核验表逐条核对 R1–R13，记录每条“正确 / 方向错 / 线型错 / 缺失”。
- [ ] 对象计数：受体 1、IRS-1 1、PI3K 1、PDK1 1、Akt 1、mTORC2 1、AS160 1、Rab 1、GSV 簇 1、质膜 GLUT4 1。
- [ ] Akt 与 GSV/GLUT4 之间没有直接箭头。
- [ ] mTORC2 没有上游箭头。
- [ ] 三分区、阅读路径与 3.3 的布局草案大致一致（偏差 < 0.05 可接受）。
- [ ] 底图无文字。
- [ ] 记录风格问题清单，交给 V3。

**下一版修改指令（→ V3，示例，按实际 V2 结果替换括号内内容）：**

```
保持所有对象、位置和 13 条关系不变，只做以下修改：
1. 全部信号蛋白（受体、IRS-1、PI3K、PDK1、Akt、mTORC2）改为同一种中等蓝填充、同一深灰描边；
   AS160 与 Rab 改为同一种低饱和灰蓝。
2. 所有激活箭头与抑制线统一为同一粗细；抑制端统一为垂直短横线（当前 [AS160 ⊣ Rab] 画成了箭头）。
3. 酶促转化弧线改细、改为中灰，与激活箭头明显区分。
4. 胰岛素与葡萄糖缩小到蛋白的约 1/3；GSV 簇放大约 1.3 倍。
5. 每个对象四周留出至少一个对象宽度的空白；底部 12% 清空。
6. 删除 [描述多余对象或伪字符的位置]。
```

---

### V3 针对 V2 问题的修订稿（统一配色、线型、层级、留白）

**目的。** 展示“把‘再好看一点’变成可核对的修改”：只改表达，不改科学结构。同时说明图像修改可能影响整张图，所以改风格后必须重新核对关系。

**操作方式。** 两种都可以，正文选一种实际执行并记录：
（a）在 SciDraw AI 中以 V2 作为参考图，输入上方修改指令进行修改；
（b）用下面的完整提示词重新生成（当参考图修改漂移过大时采用）。

**提示词（英文，完整重生成版本）：**

```
Redraw the same flat 2D scientific schematic with identical content and layout,
landscape 16:9, pure white background, clean vector style, flat fills, uniform
1.5 px dark gray (#3A3A3A) outlines, no gradients, no shadows, no highlights,
no 3D, no texture.

ABSOLUTELY NO TEXT: no letters, words, numbers, symbols or labels anywhere.

STRICT COLOR PALETTE (use only these):
- Signaling proteins (receptor, IRS-1, PI3K, PDK1, Akt, mTORC2): one medium blue
  fill #A9C4E0 with #4C78A8 accents. Same blue for all of them.
- Insulin beads: dark blue #2F5D8C.
- AS160 and Rab: one desaturated gray-blue #B8C2CC.
- GLUT4 transporters, vesicle membranes and glucose hexagons: soft orange family
  only (#F2C49B fill, #E39B5B lines, #C46A2A for glucose).
- Plasma membrane head groups: light warm gray #D9D6D0; tails #BDB8AF.
- Phosphorylation dots: amber #E3B23C, all the same size.
- All signaling lines: dark gray #3A3A3A.
No other hues.

HIERARCHY AND SIZE:
- Proteins are the largest objects and similar in size to each other; the
  receptor may be slightly larger.
- Insulin beads and glucose hexagons are small, about one third of a protein.
- The vesicle cluster is clearly visible, roughly the size of two proteins.
- The plasma membrane band is thin and calm, not visually dominant.

LINE SEMANTICS (exactly five line types, consistent everywhere):
- Activation: solid #3A3A3A line, uniform weight, filled triangular head.
  Receptor -> IRS-1, IRS-1 -> PI3K, PDK1 -> Akt, mTORC2 -> Akt.
- Inhibition: solid #3A3A3A line, same weight, ending in a perpendicular flat bar
  touching the target. Akt -| AS160, AS160 -| Rab.
- Enzymatic conversion: thinner mid-gray (#7A7A7A) arc along the inner leaflet
  from PIP2 to PIP3 with an open V head; PI3K touches its midpoint.
- Translocation: one thick dashed #E39B5B arrow with a large open head from the
  vesicle cluster up to the GLUT4 in the plasma membrane.
- Substance flow: dotted #C46A2A line with a small filled head from glucose down
  through the membrane GLUT4 into the cytoplasm.
Lines never cross objects; lines never cross each other.

SAME LAYOUT AS BEFORE (x from left, y from top, as fraction of the image):
insulin (0.12, 0.10); receptor x 0.12 spanning y 0.12-0.36; membrane y 0.20-0.28;
IRS-1 (0.20, 0.46); PI3K (0.30, 0.37); PIP2->PIP3 along inner leaflet x 0.33-0.41;
PDK1 (0.42, 0.36); Akt (0.53, 0.37); mTORC2 (0.53, 0.57); AS160 (0.63, 0.52);
Rab on the upper-left vesicle near (0.71, 0.64); vesicle cluster x 0.70-0.82,
y 0.66-0.80; membrane GLUT4 (0.87, 0.24); glucose x 0.82-0.92, y 0.05-0.14.

WHITESPACE: keep clear empty space of at least one protein width around every
object for labels; keep the bottom 12% completely empty; keep a 4% empty margin
on all sides.

DO NOT DRAW anything not listed: no organelles, cytoskeleton, extra proteins,
extra arrows, no arrow from Akt directly to vesicles or GLUT4, no arrow into
mTORC2, no data elements, no decoration.
```

**预期问题：**

- 修改可能“顺手”改动了布局或删掉一条关系（尤其 mTORC2 → Akt、PIP2→PIP3 弧线）。
- 色值无法逐像素保证；蓝和灰蓝可能难以区分。
- 仍可能出现字母状细节（如在膜 GLUT4 上出现条纹被误读为文字）。

**作者检查清单：**

- [ ] 重新完整执行 R1–R13 核验（不是只看改过的地方）。
- [ ] 颜色：只出现蓝、灰蓝、橙三个色相加灰；同类对象同色。
- [ ] 线型恰为五种，且与 3.2 一一对应；同类线粗细一致。
- [ ] 尺寸层级：蛋白 > 囊泡簇 ≈ 两个蛋白 > 小分子。
- [ ] 每个对象周围有标签空间；底部 12% 为空。
- [ ] 灰度打印测试：转灰度后线型仍可区分（不依赖颜色区分关系）。
- [ ] 与 V2 并排比较，记录“意外变化”。

**下一版修改指令（→ V4）：** V3 若已满足全部科学与风格条件，即以 V3 的提示词作为 V4 底图提示词的基础，追加“为标签预留的具体空白位置”和“精确对齐”要求，并决定箭头由图像模型画（方案 A）还是在 TikZ 中画（方案 B）。

---

### V4 终稿：无字底图 + LaTeX/TikZ 精确叠加标签

**为什么这样做。** 图像模型生成文字时会拼错字母、混用大小写（如把 “PIP3” 写成 “PIP”“P1P3”）、随意改变字号，并且同一提示词每次给出的标签位置不同。科研图的标签是科学内容的一部分，一个字母错误（如 Akt 写成 Act）就构成错误陈述。把文字移到 LaTeX/TikZ 中：拼写可复制、可检索、可校对；字体与正文一致；字号在印刷尺寸下可控；中英文两版共用一张底图，只换标签层。代价是需要手工确定坐标，并在底图更换后重新对位。

**两种方案（正文推荐 A，B 作为底图箭头不可靠时的备选）：**

- **方案 A：** 底图含对象和全部箭头，TikZ 只叠加文字与图例。
- **方案 B：** 底图只含分区、膜和对象，不含任何箭头；箭头、T 形端、虚线和点线全部在 TikZ 中绘制。线型 100% 可控，适合审稿要求严格时。下面提示词中的 `[ARROWS]` 段在方案 B 中替换为 “Do not draw any arrows or connecting lines.”

**V4 底图提示词（英文）：**

```
Final base artwork for a journal Figure 1, flat 2D vector-style scientific
schematic, landscape 16:9, at least 2400 px wide, pure white background,
uniform thin dark gray (#3A3A3A) outlines, flat fills, no gradients, no shadows,
no highlights, no 3D, no texture, crisp edges.

THIS IMAGE MUST CONTAIN NO TEXT AT ALL: no letters, no words, no numbers,
no symbols such as "P", no labels, no legend, no title, no watermark. All text
will be typeset later on top of this image, so leave the specified label areas
empty.

PALETTE (only these): signaling proteins #A9C4E0 fill with #4C78A8 accents;
insulin #2F5D8C; AS160 and Rab #B8C2CC; GLUT4, vesicle membranes #F2C49B /
#E39B5B; glucose #C46A2A; membrane heads #D9D6D0, tails #BDB8AF; phosphorylation
dots #E3B23C; lines #3A3A3A and #7A7A7A.

LAYOUT (x from left, y from top, fractions of the image):
- Extracellular y 0.00-0.20; plasma membrane bilayer y 0.20-0.28 full width;
  cytoplasm y 0.28-0.88; bottom band y 0.88-1.00 completely empty.
- Insulin: 3 small beads at (0.12, 0.10) touching the receptor top.
- Insulin receptor: two-armed transmembrane receptor at x 0.12, y 0.12-0.36,
  two amber dots on its intracellular part.
- IRS-1 (0.20, 0.47) with one amber dot.
- PI3K (0.30, 0.38) just under the membrane.
- PIP2 head groups x 0.33-0.36 and PIP3 head groups (with an extra small bump)
  x 0.38-0.41 on the inner leaflet at y 0.28.
- PDK1 (0.43, 0.36) touching the inner leaflet.
- Akt (0.54, 0.36) touching the inner leaflet, two amber dots.
- mTORC2 (0.54, 0.58), three joined circles.
- AS160 (0.65, 0.52), one amber dot.
- Vesicle cluster of three pale-orange vesicles, each with one GLUT4 barrel, at
  x 0.72-0.82, y 0.67-0.81; Rab bead on the upper-left vesicle at (0.72, 0.65).
- One GLUT4 barrel embedded in the plasma membrane at (0.88, 0.24).
- Four glucose hexagons at x 0.83-0.93, y 0.05-0.14.

[ARROWS]
- Activation, solid #3A3A3A, filled triangular heads: receptor -> IRS-1,
  IRS-1 -> PI3K, PDK1 -> Akt, mTORC2 -> Akt (upward).
- Inhibition, solid #3A3A3A, perpendicular flat bar at the target: Akt -| AS160,
  AS160 -| Rab.
- Enzymatic conversion, thin #7A7A7A arc along the inner leaflet from PIP2 to
  PIP3 with an open V head; PI3K touches the arc midpoint.
- Translocation, one thick dashed #E39B5B arrow with a large open head from the
  vesicle cluster (0.80, 0.66) curving up to the membrane GLUT4 (0.88, 0.29).
- Substance flow, dotted #C46A2A line with small filled head from the glucose
  (0.88, 0.15) straight down through the membrane GLUT4 to (0.88, 0.42).
- No other lines.

KEEP THESE LABEL AREAS EMPTY (plain white, nothing drawn):
(0.02-0.10, 0.02-0.07), (0.17-0.26, 0.05-0.09), (0.17-0.33, 0.12-0.17), (0.16-0.26, 0.52-0.57),
(0.24-0.36, 0.41-0.46), (0.33-0.45, 0.30-0.34) just below the leaflet,
(0.40-0.48, 0.41-0.45), (0.57-0.62, 0.39-0.44), (0.58-0.66, 0.60-0.64),
(0.68-0.80, 0.47-0.51), (0.62-0.70, 0.66-0.70), (0.83-0.97, 0.82-0.86),
(0.90-0.99, 0.30-0.35), (0.92-0.99, 0.08-0.12), (0.02-0.12, 0.80-0.85),
(0.60-0.78, 0.15-0.19).

DO NOT DRAW: organelles, cytoskeleton, any unlisted molecule, any arrow from Akt
to vesicles or GLUT4, any arrow into mTORC2, any data element, any decoration.
```

**V4 标签表（相对坐标 0–1，x 向右、y 向下，为标签文字中心；生成后按实际底图微调）：**

| # | 英文标签 | 中文标签 | 位置 (x, y) | 对齐 | 字号 / 样式 |
|---|---|---|---|---|---|
| L1 | Extracellular | 胞外 | (0.06, 0.045) | 左 | 7 pt，斜体，灰 #6B6B6B |
| L2 | Plasma membrane | 质膜 | (0.69, 0.17) | 中 | 7 pt，斜体，灰 |
| L3 | Cytoplasm | 胞质 | (0.07, 0.825) | 左 | 7 pt，斜体，灰 |
| L4 | Insulin | 胰岛素 | (0.21, 0.07)，短引线指向 (0.13, 0.10) | 左 | 8 pt |
| L5 | Insulin receptor | 胰岛素受体 | (0.25, 0.145)，短引线指向受体胞外臂 (0.14, 0.16) | 左 | 8 pt |
| L6 | IRS-1 | IRS-1 | (0.21, 0.545)，IRS-1 正下方 | 中 | 8 pt |
| L7 | PI3K | PI3K | (0.30, 0.435)，PI3K 正下方 | 中 | 8 pt |
| L8 | PIP2 → PIP3 | PIP2 → PIP3 | (0.38, 0.32) | 中 | 7 pt |
| L9 | PDK1 | PDK1 | (0.44, 0.43) | 中 | 8 pt |
| L10 | Akt | Akt | (0.595, 0.415) | 中 | 8 pt，粗体（主线枢纽） |
| L11 | mTORC2 | mTORC2 | (0.62, 0.62) | 中 | 8 pt |
| L12 | AS160 (TBC1D4) | AS160（TBC1D4） | (0.74, 0.49) | 中 | 8 pt |
| L13 | Rab-GTP | Rab-GTP | (0.66, 0.68) | 中 | 7 pt |
| L14 | GLUT4 storage vesicles | GLUT4 储存囊泡 | (0.90, 0.84) | 中 | 8 pt |
| L15 | GLUT4 | GLUT4 | (0.945, 0.325) | 中 | 8 pt，粗体 |
| L16 | Glucose | 葡萄糖 | (0.955, 0.10) | 中 | 8 pt |
| L17 | translocation & fusion | 转位与融合 | (0.90, 0.52)，沿虚线箭头旁 | 左 | 7 pt，斜体，橙 #C46A2A |

> 坐标是起点，不是结论：底图出来后先测量各对象实际中心，再整体平移或微调标签；确定版坐标写入 provenance。若标签与箭头冲突，优先移动标签，其次缩短引线，最后才考虑重生成底图。

**图例（TikZ 绘制，位于 y 0.90–0.98 的底部空白带，横排）：** 激活（实线实心箭头）｜抑制（T 形端）｜酶促转化（细弧空心头）｜囊泡转位（粗虚线）｜葡萄糖流动（点线）｜磷酸化（琥珀圆点）。英文：Activation｜Inhibition｜Enzymatic conversion｜Vesicle translocation｜Glucose flux｜Phosphorylation。

**TikZ 叠加骨架（示意，排版时放入 `figures/ch07/glut4-v4-final.tex`）：**

```latex
\begin{tikzpicture}
  \node[anchor=south west,inner sep=0] (img)
    {\includegraphics[width=174mm]{figures/ch07/glut4-v4-base.png}};
  \begin{scope}[x={(img.south east)},y={(img.north west)},
                font=\sffamily\fontsize{8}{9}\selectfont]
    % 坐标换算：TikZ y 向上，表中 y 向下，故使用 (x, 1-y)
    \node at (0.595, 1-0.415) {\textbf{Akt}};
    \node at (0.74, 1-0.49) {AS160 (TBC1D4)};
    \node[align=center] at (0.90, 1-0.84) {GLUT4 storage vesicles};
    % ……其余标签按上表
    % 方案 B：在此绘制箭头，例如抑制线
    % \draw[line width=0.8pt, -{Bar[width=6pt]}] (0.58,1-0.40) -- (0.62,1-0.49);
  \end{scope}
\end{tikzpicture}
```

**预期问题：**

- 底图实际坐标与提示词有偏差（常见 ±0.03–0.08）——这是预期内的，按实际调整标签，不为对位反复重生成。
- 留空区域偶尔被小装饰填充，需要重生成或在位图编辑中清白。
- 叠加后可能出现引线与箭头交叉；优先移动标签而非加引线。

**作者检查清单（终稿验收）：**

- [ ] 底图放大到 200% 检查：无任何文字、伪字母、水印。
- [ ] R1–R13 全部正确（第 6 节表格全部打勾，并由一位领域同行复核签字）。
- [ ] 17 个标签拼写逐字核对（与 3.4 清单复制比对，不手打）。
- [ ] 每个标签指向唯一对象，无歧义；引线不穿过其他对象。
- [ ] 174 mm 宽打印预览：最小字 ≥ 6 pt，线型可分辨；灰度下仍可区分。
- [ ] 图例覆盖全部五种线型 + 磷酸化标记。
- [ ] 中英文两版仅标签层不同，底图为同一文件（核对文件哈希）。
- [ ] 图注中写明简化与省略（见第 5 节）。

**下一步：** 终稿进入第 9 章组图流程时，可在 SciDraw AI 的组图（panel assembly）中与其他面板排版；图注草稿可用图注辅助生成，但只作为草稿，样本量、统计方法、实验条件不得由工具补写（本图为纯背景示意，本就不应出现这些内容）。

---

### 对比组 A：箭头语义混用 vs 统一

用同一段简化通路（Akt → AS160 → Rab → 囊泡转位 → 质膜 GLUT4）做两张小图，正文并排放置，宽各约 80 mm。两张图都不含文字；正文用 TikZ 在两图下方各加一行说明。

**A-1 混用（反例）提示词：**

```
Small flat 2D schematic, landscape 4:3, white background, no text, no letters,
no numbers, no labels. A horizontal gray lipid membrane across the top quarter
with one orange barrel-shaped transporter embedded at the right. Below it, from
left to right: a blue oval, a gray-blue rounded shape, a small gray-blue bead on
a cluster of three pale-orange vesicles at lower right.
Connect them with deliberately inconsistent arrows: blue oval to gray-blue shape
with a thick curved red arrow with a filled head; gray-blue shape to the bead
with a thin green dashed arrow with an open head; vesicle cluster to the membrane
transporter with a solid black arrow with a filled head identical in style to a
plain activation arrow; add one extra double-headed purple arrow between the
blue oval and the membrane. Arrow weights all different. Flat colors, no
gradients, no 3D.
```

**A-2 统一（正例）提示词：**

```
Small flat 2D schematic, landscape 4:3, white background, no text, no letters,
no numbers, no labels. A horizontal light warm-gray lipid membrane across the
top quarter with one soft-orange barrel-shaped transporter embedded at the
right. Below it, from left to right: a medium-blue oval, a desaturated gray-blue
rounded shape, a small gray-blue bead attached to a cluster of three pale-orange
vesicles at lower right.
Line semantics, consistent weights:
- blue oval to gray-blue shape: solid dark gray line ending in a perpendicular
  flat bar (inhibition).
- gray-blue shape to the bead: solid dark gray line ending in a perpendicular
  flat bar (inhibition), same weight as the first.
- vesicle cluster to the membrane transporter: one thick dashed soft-orange arrow
  with a large open head, curving upward (translocation).
No other lines. Flat colors, thin dark gray outlines, no gradients, no shadows,
no 3D.
```

**教学要点 / 检查：** A-1 中读者无法判断哪条是抑制、哪条是空间移动，且多出一条无定义的双向箭头；转位箭头与激活箭头同型，误导读者以为“囊泡激活了 GLUT4”。A-2 中两条 T 形线串联可直接读出“抑制的抑制”，转位是唯一的粗虚线。检查：A-2 恰好三条线、两种线型；A-1 的“错误”必须正好是提示词所设计的那几处，便于正文逐一指出。

### 对比组 B：配色过多 vs 克制

使用同一张 V3 结构（完整通路），各约 80 mm 宽并排。

**B-1 配色过多（反例）提示词：**

```
Flat 2D scientific schematic of a cell signaling pathway, landscape 16:9, white
background, no text, no letters, no numbers, no labels. Same layout as follows:
a horizontal lipid membrane across the top fifth; a transmembrane receptor at
the far left with small beads above it; a left-to-right chain of six rounded
protein shapes under the membrane; a cluster of three vesicles at the lower
right; one transporter in the membrane at the right; small hexagons above it.
Give EVERY protein a different saturated color (red, lime green, purple, cyan,
magenta, yellow, navy), make the membrane rainbow-striped, the vesicles bright
pink, the hexagons teal, and use a different color for every arrow. Keep the
shapes flat, no gradients, no 3D, no text.
```

**B-2 克制（正例）：** 直接复用 V3 提示词（即“STRICT COLOR PALETTE”版本）。若需要单独生成小图，在 V3 提示词前加一句 “Small version for a side-by-side comparison, landscape 16:9.”。

**教学要点 / 检查：** B-1 中颜色不承担任何含义，读者会试图从颜色找分组却找不到；红/绿同时出现对色觉差异读者不友好；彩虹膜抢走视觉中心。B-2 中颜色只编码三类角色（信号蛋白 / 运输调控 / 运输物质与载体），图例无需解释颜色本身。检查：B-2 色相 ≤ 3 + 灰；把两图转灰度，B-2 仍可读、B-1 层级混乱。

### 版本与提示词汇总

| 编号 | 图 | 提示词数 | 允许文字 |
|---|---|---|---|
| V0 | 手绘构思草图 | 1 | 否 |
| V1 | 一句话初稿 | 1 | 是（失败展示） |
| V2 | 任务书结构稿 | 1 + 1 条修改指令 | 否 |
| V3 | 修订稿 | 1（完整重生成版）+ 修改指令版 | 否 |
| V4 | 终稿底图 | 1（方案 A/B 共用，B 替换箭头段） | 否 |
| A-1 / A-2 | 箭头语义对比 | 2 | 否 |
| B-1 / B-2 | 配色对比 | 1 + 复用 V3 | 否 |

---

## 5. 图注草稿

本图为背景机制示意，不报告实验结果，因此图注中不出现样本量、统计方法或任何数值。若使用 SciDraw AI 的图注辅助起草，应把下面的“简化与省略”信息一并提供；工具起草的图注只是草稿，不能让它补写样本量、统计或实验条件，作者需逐句对照第 2 节关系表和参考文献核对。

### 5.1 中文图注

> **图 1　胰岛素刺激 GLUT4 转位的经典信号通路示意。** 胰岛素与质膜上的胰岛素受体结合，引起受体胞内段酪氨酸自身磷酸化，进而磷酸化 IRS-1 并招募 I A 类 PI3K。PI3K 在质膜内叶将 PIP2 转化为 PIP3，后者招募 PDK1 与 Akt；Akt 由 PDK1 和 mTORC2 磷酸化而激活。活化的 Akt 磷酸化 AS160（TBC1D4），抑制其 Rab-GAP 活性，使 GLUT4 储存囊泡上的 Rab 维持 GTP 结合状态，促进囊泡向质膜转位并融合，GLUT4 由此增加于质膜，葡萄糖经其易化扩散进入细胞。实线实心箭头表示激活，T 形端表示抑制，细弧线表示酶促转化，粗虚线表示囊泡转位，点线表示葡萄糖流动，琥珀色圆点表示磷酸化。为便于阅读，图中省略了 MAPK 与 CAP–Cbl–TC10 分支、GLUT4 内吞与再循环、负反馈调节、SNARE 融合机器及细胞骨架运输；Rab 未区分具体亚型，Akt 未区分亚型，骨骼肌中并行的 TBC1D1 未画出；mTORC2 的上游激活方式未表示。依据 Saltiel 与 Kahn（2001）、Leto 与 Saltiel（2012）、Klip 等（2019）的综述整理。

### 5.2 English caption

> **Figure 1 | Schematic of the canonical insulin signaling pathway leading to GLUT4 translocation.** Insulin binding to the insulin receptor at the plasma membrane triggers tyrosine autophosphorylation of the receptor's intracellular domain, which phosphorylates IRS-1 and recruits class IA PI3K. PI3K converts PIP2 to PIP3 in the inner leaflet; PIP3 recruits PDK1 and Akt, and Akt is activated by phosphorylation by PDK1 and mTORC2. Active Akt phosphorylates AS160 (TBC1D4), inhibiting its Rab-GAP activity. Rab proteins on GLUT4 storage vesicles therefore remain GTP-bound, promoting vesicle translocation to and fusion with the plasma membrane. The resulting increase in surface GLUT4 allows facilitated diffusion of glucose into the cell. Solid lines with filled heads, activation; T-bars, inhibition; thin arc, enzymatic conversion; thick dashed arrow, vesicle translocation; dotted arrow, glucose flux; amber dots, phosphorylation. For clarity, the MAPK and CAP–Cbl–TC10 branches, GLUT4 endocytosis and recycling, negative feedback, the SNARE fusion machinery and cytoskeletal transport are omitted; Rab and Akt isoforms are not distinguished, the parallel role of TBC1D1 in skeletal muscle is not shown, and upstream regulation of mTORC2 is not depicted. Based on reviews by Saltiel and Kahn (2001), Leto and Saltiel (2012) and Klip et al. (2019).

### 5.3 图注自查

- [ ] 每一句都能在第 2 节关系表中找到对应行（R1–R13）。
- [ ] 线型说明与图例完全一致。
- [ ] 未出现“显著”“增加 X 倍”“n =”等任何数据或统计词。
- [ ] “简化与省略”与第 2.2 节列表一致，没有漏项也没有多出未讨论的内容。
- [ ] 中英文各自独立通顺，不是逐字直译。

---

## 6. 核验记录模板

每生成一版（V1–V4）复制一份填写。结论栏：✓ 正确｜✗ 错误（写明错在哪）｜— 缺失｜? 无法判断。第 3 列“图中应见”以第 3 节任务书为准。

**版本：____　文件：____　生成工具：____　日期：____　核验人：____　复核人（领域同行）：____**

### 6.1 科学关系逐条核对

| # | 关系 | 图中应见 | 方向正确 | 线型正确 | 位置/分区正确 | 结论 | 备注 / 依据 |
|---|---|---|---|---|---|---|---|
| R1 | 胰岛素结合受体 | 胞外配体接触受体胞外段，无箭头 | — | ☐ | ☐ 胞外 | | Saltiel & Kahn 2001 |
| R2 | 受体自身磷酸化 | 受体胞内段磷酸化圆点 | — | ☐ | ☐ 胞内侧 | | 同上 |
| R3 | 受体 → IRS-1 | 激活箭头 | ☐ | ☐ | ☐ | | 同上 |
| R4 | IRS-1 → PI3K | 激活箭头 | ☐ | ☐ | ☐ 膜下 | | 同上 |
| R5 | PI3K：PIP2 → PIP3 | 内叶上的酶促转化弧线 | ☐ | ☐ | ☐ 内叶 | | 同上 |
| R6 | PIP3 招募 PDK1、Akt | PDK1、Akt 贴膜，无箭头 | — | ☐ | ☐ | | 同上 |
| R7 | PDK1 → Akt | 激活箭头 | ☐ | ☐ | ☐ | | 同上 |
| R8 | mTORC2 → Akt | 激活箭头；mTORC2 无上游箭头 | ☐ | ☐ | ☐ | | Sarbassov 等 2005 |
| R9 | Akt ⊣ AS160 | 抑制线 + AS160 磷酸化圆点 | ☐ | ☐ | ☐ 胞质 | | Sano 等 2003；Leto & Saltiel 2012 |
| R10 | AS160 ⊣ Rab | 抑制线，终点在囊泡表面 Rab | ☐ | ☐ | ☐ | | Leto & Saltiel 2012 |
| R11 | Rab-GTP → GSV 转位 | 粗虚线从囊泡簇指向质膜 | ☐ | ☐ | ☐ 胞质→膜 | | 同上 |
| R12 | GSV 与质膜融合 | 转位终点为质膜中的 GLUT4 | ☐ | ☐ | ☐ 膜内 | | 同上 |
| R13 | 葡萄糖经 GLUT4 进入 | 点线自胞外穿过 GLUT4 到胞质 | ☐ | ☐ | ☐ 跨膜 | | Klip 等 2019 |

### 6.2 对象与禁止项

| 检查项 | 期望 | 实际 | 结论 |
|---|---|---|---|
| 对象计数 | 受体、IRS-1、PI3K、PDK1、Akt、mTORC2、AS160、Rab、GSV 簇、质膜 GLUT4 各 1；胰岛素 1 簇；葡萄糖 3–5 个 | | |
| GLUT4 出现位置 | 仅囊泡膜与质膜两处 | | |
| 多余对象 | 无（细胞器、骨架、MAPK 等） | | |
| 捷径箭头 | Akt/受体到 GSV 或 GLUT4 无直接箭头 | | |
| 底图文字 | 无（V1 除外） | | |
| 三分区 | 胞外 / 质膜 / 胞质清楚，质膜横贯全宽 | | |

### 6.3 表达质量

| 检查项 | 期望 | 结论 |
|---|---|---|
| 线型数 | 恰为 5 种 + 磷酸化圆点，与图例一致 | |
| 色相 | ≤ 3 个色相 + 灰；同类对象同色 | |
| 灰度测试 | 转灰度后关系仍可区分 | |
| 尺寸层级 | 蛋白 > 囊泡簇 > 小分子 | |
| 留白 | 各标签位与底部图例带为空 | |
| 印刷尺寸 | 174 mm 宽时最小字 ≥ 6 pt | |

### 6.4 意外变化记录

| 与上一版相比，未要求却发生的变化 | 是否影响科学内容 | 处理（保留 / 下一版修正 / 重生成） |
|---|---|---|
| | | |

---

## 7. 本章练习

**练习 1：把一条“捷径箭头”拆回可核对的环节。** 下面这句话来自一张常见的教学图：“Akt → GLUT4 translocation”。（a）写出它省略的中间环节，并为每一环指定第 3.2 节中的线型；（b）解释为什么 Akt 与 AS160 之间用抑制线，而整条通路的净效应却是促进转位；（c）把你的结果写成一份三行的关系表（起点、终点、关系、线型、依据），并说明你查阅了哪篇综述的哪一部分来确认。

**练习 2：为自己的机制写任务书并预判失败。** 选择你研究领域中一条教科书已确立的机制（不超过 8 个对象）。（a）按第 2 章的十个填写项写任务书，其中必须包括空间分区和每种线型的定义；（b）先只用一句话提示词生成一张图，按第 6 节模板记录至少 5 处问题；（c）再用完整任务书生成一张无文字底图，比较两份核验表，指出哪些问题因输入补全而消失、哪些仍然存在。提交两张图、两份核验表和修改记录。

**练习 3：标签与图例分层。** 使用本案例的 V4 底图（或你在练习 2 中得到的底图）：（a）测量各对象的实际中心，修订第 4 节的标签坐标表；（b）在 TikZ 中叠加中文和英文两套标签与图例，保证底图为同一文件；（c）在 174 mm 宽下打印或导出 PDF，检查最小字号、引线是否穿过对象、灰度下线型是否可辨；（d）写出一句话，说明在你的期刊目标中，为什么不应让图像模型直接生成标签。
