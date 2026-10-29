# 第 6 章 Codex 图像生成与看图核验

日期：2026-10-29。依据：production/plans/ch06.md（§3.6、§4）及 production/book-spec.md（§4、§5）。

## 交付状态与边界

生成 V1、V2、12 图标表，以及 icon 08 局部修正版；保留 V1/V2 各 1 张落选图。总计调用内置图像工具 6 次：V1 2 次、V2 2 次、图标表 1 次、icon 08 局部编辑 1 次。任何图均未超过 3 次。

所有本轮主动写入均在 figures/ch06/ 或 provenance/ch06/ 内；工具自动缓存路径在下方如实记录。未启动子 agent，未 commit/push，未操作账户，未运行 SciDraw AI，未生成或修改 TikZ/标签/截图。没有使用模拟截图冒充实测结果。

**尚未达标：V1/V2 选用原图均只有 1672 × 941，未达到规划 ≥2400 px 宽；图标表的 08 原图像打印机，已有单独修正版但未替换并行流程的标准名切片；图标与 V2 仍有渐变/透视。** 没有把插值放大宣称为原生高清，也没有把这些缺口记为通过。工具参数未提供独立尺寸字段；V1/V2 各重试一次追加尺寸要求后仍返回同样的原生尺寸，因而保留原始图并明确报告缺口。

## 来源真实性与完整提示词

实际工具：**image_gen.imagegen**（调用名 tools.image_gen__imagegen）。具体模型：**不知道，返回结果未提供**。六次工具输出均先原样复制到授权目录，缓存原文件保留。缓存目录：codex-output/。

第一轮 V1/V2/V3 的 prompt 均逐字提取规划中相应代码块，保留换行。V1/V2 第二轮仅在完整原文后追加技术尺寸要求，具体改动理由与实际全文逐份列在下面。08 的局部修改按规划许可另写修改指令。所有生成与衍生文件的完整 prompt 也逐文件保存在 codex-images.json（不是摘要）。

## 1. figures/ch06/ch06-01-v1-vague.png

- 工具：image_gen.imagegen (tools.image_gen__imagegen)；模型：不知道；工具返回未提供具体模型名称。
- 次数：第 1 次；选用/保留的输出。
- 原始缓存文件：exec-22adb2e7-1fe9-4d59-a08a-3c173ca28a97.png。
- 实测尺寸：1672 × 941 px。
- 提示词修改：无，逐字使用规划 §3.6 V1。

实际使用的完整 prompt：

```text
Create a professional, colorful flowchart of a single-cell RNA sequencing experiment and
data analysis workflow, from tissue to cell type annotation. Landscape 16:9.
```

看图核验：

- 画面内容：原样保留模型自由生成的 11 个彩色分区；组织、解离、捕获/建库、测序、原始数据和计算分析均可辨。
- 教学目的：可用于讨论“一句话提示词产出的图还需核验”，但不支持规划预写的全部失败情节。
- 文字：V1 是唯一允许文字的反例。此次大多数英文可读；未确认明显伪文字。不得套用“①伪文字”的预写图注。
- 顺序：捕获在测序之前；没有明确的 UMAP → 聚类箭头。不得声称出现这两种指定错误。
- 湿/干区分：图中实际写出了 Experimental workflow (wet lab) 和 Computational analysis (bioinformatics)，不能声称湿干完全未区分。
- 确认的问题 1：Quality control and filtering 只是普通面板，没有通过/不通过出口、回退箭头（下排第 2 面板）。
- 确认的问题 2：Dimensionality reduction and clustering 合并成一个面板；未显式画出 k 近邻图分叉到聚类与 UMAP（下排第 4 面板）。这是关系未表达，不能改写成“已有反向箭头”。
- 确认的问题 3：没有呈现主案例两个样本的并行处理及文库/矩阵合并点。
- 确认的问题 4：渐变、阴影、立体仪器和大量文字同时出现，终稿尺寸下负担较重；这是可直接观察的视觉问题。
- 案例差异：左上是肾脏图标，并非规划的小鼠肺组织；V1 原提示词并未指定器官，不能把这个差异归咎于违反 V1 提示词。
- 其他预写问题：没有确认显微镜/齿轮装饰；重复组织图形也可能表示步骤交接，不认定为无意义重复。
- 选用理由：首张已足以如实展示未显式表达的分支、质控出口与样本合并，且原提示词完全未改。没有为制造坏例而改坏图像。
- 尺寸：1672 × 941，约 16:9（整数像素取整），宽度低于 2400 px；未达标。

## 2. figures/ch06/ch06-01-v1-vague-alt1.png

- 工具：image_gen.imagegen (tools.image_gen__imagegen)；模型：不知道；工具返回未提供具体模型名称。
- 次数：第 2 次；落选，作为 alt 保留。
- 原始缓存文件：exec-f1b04b60-2adc-4a17-91dc-fc2cbdf904a9.png。
- 实测尺寸：1672 × 941 px。
- 提示词修改：保留原提示词全文，仅追加原生 2560×1440/至少2400宽要求；首轮尺寸不达标。第二轮仍不达标。

实际使用的完整 prompt：

```text
Create a professional, colorful flowchart of a single-cell RNA sequencing experiment and
data analysis workflow, from tissue to cell type annotation. Landscape 16:9.

Technical output requirement: render a native 2560 × 1440 pixel PNG canvas, exact 16:9 landscape aspect ratio, at least 2400 pixels wide. Keep the entire illustration within this canvas. This is a pixel-dimension requirement, not text to draw.
```

看图核验：

- 画面内容：原样保留 10 个分区，展示组织、单细胞捕获、逆转录、建库、测序及计算分析。
- 文字：允许文字；大多数英文可读，未确认明显伪文字。
- 顺序：捕获、逆转录、建库、测序大体有序；没有可作为“UMAP 指向聚类”证据的独立箭头。
- 质控：文库质控埋在文字项目中；计算质控仍没有明确通过/不通过出口。
- 分支：PCA、UMAP、t-SNE 和 Clustering 放在同一面板，未显式画近邻图的两条平行输出；没有两个样本的合并点。
- 视觉：有渐变、阴影、立体仪器；组织在左上呈整块器官样，而非限定的肺组织案例。
- 落选理由：追加输出尺寸要求后仍为 1672 × 941，没有解决首轮最明确的技术缺口；首轮的湿/干阶段标识更清晰，因此沿用首轮。
- 尺寸：约 16:9；低于 2400 px。

## 3. figures/ch06/ch06-05-v2-brief-alt1.png

- 工具：image_gen.imagegen (tools.image_gen__imagegen)；模型：不知道；工具返回未提供具体模型名称。
- 次数：第 1 次；落选，作为 alt 保留。
- 原始缓存文件：exec-acf7aedf-119a-4cd7-92a5-5099b563b7b7.png。
- 实测尺寸：1983 × 793 px。
- 提示词修改：无，逐字使用规划 §3.6 V2。

实际使用的完整 prompt：

```text
A clean, flat, vector-style scientific workflow diagram on a pure white background,
landscape 16:9. Two horizontal swim lanes separated by a thin light-grey line.
Top lane (very light warm beige background): a left-to-right sequence of nine small
rounded-rectangle steps, each with one simple icon inside: (1) a small piece of pink
soft tissue on a dish, (2) a conical tube with tiny enzyme droplets, (3) a cell strainer
mesh over a tube, (4) a diamond-shaped checkpoint containing a counting grid with a few
round cells, (5) a microfluidic chip whose channel forms droplets, each droplet holding
one cell and one bead, (6) a small PCR tube, (7) short double-stranded DNA fragments
with coloured end caps, (8) a second diamond-shaped checkpoint containing a small
fragment-size curve, (9) a benchtop sequencer box. Between steps 1 and 8, every step
is drawn as a stack of two slightly offset cards (two samples processed in parallel);
the two stacks merge into the single sequencer at step 9. A dashed curved arrow returns
from checkpoint 4 back to step 2, and from checkpoint 8 back to step 7.
A small circle connector at the right end of the top lane, and an identical circle at
the left end of the bottom lane.
Bottom lane (very light cool blue-grey background): a left-to-right sequence: a monitor
with aligned reads, a grid matrix of small squares, a diamond checkpoint with a filter
funnel (with two small optional dashed boxes above it, joined back into it), a bar-like
normalisation symbol, a short list of highlighted rows, a scatter of points with two
perpendicular axes arrows (PCA), a network graph of dots and edges; from the network
graph the path splits into two branches: upper branch to a set of coloured point
clusters, lower branch to a two-dimensional point embedding; only the upper branch
continues to a heat-map-like marker table and then to a final cluster map with blank
tag shapes. A dashed curved arrow returns from the final map back to the checkpoint.
Warm muted orange-brown accents in the top lane, muted teal-blue accents in the bottom
lane, dark slate arrows of uniform weight with solid triangular heads. Generous white
space. No text, no letters, no numbers, no labels, no symbols, no logos. No 3D, no
gradients, no shadows, no microscope, no DNA double helix, no gears, no people.
```

看图核验：

- 画面内容：暖色湿实验、冷色计算两泳道；上排 9 个主体图标，下排 11 个，共 20 个，另有 2 个可选小框。
- 无文字：目视未见文字、字母、数字或伪文字；网格、轴线和条形图属于提示词要求的图形内容。
- 主链：组织→管→滤网→计数菱形→微滴→管→短 DNA→文库质控→测序仪的顺序可辨。
- 分叉：近邻网络分成上方聚类和下方嵌入两支；只有上支继续至热图与终点。没有观察到 UMAP → 聚类或 UMAP → 注释的错误箭头。
- 反馈：上排两个反馈分别指向解离管和文库片段，方向符合提示词；下排的反馈弧在质控端和终点端都出现箭头，形成双向关系，不符合“终点返回质控”的单向要求。
- 双样本：6 个操作卡有偏移叠卡；两处菱形没有叠卡。没有清晰的两条文库线汇入测序仪。
- 可选框：两个虚线小框位于质控上方并指回质控，符合 V2 的位置描述。
- 终点：有空白标签形状，未见文字。
- 风格：仪器和容器仍有明暗与立体感，没有完全满足 no gradients/no 3D。
- 落选理由：1983 × 793，约 2.50:1，明显偏离 16:9；反馈弧双向也较差。
- 尺寸：宽度低于 2400 px。

## 4. figures/ch06/ch06-05-v2-brief.png

- 工具：image_gen.imagegen (tools.image_gen__imagegen)；模型：不知道；工具返回未提供具体模型名称。
- 次数：第 2 次；选用/保留的输出。
- 原始缓存文件：exec-575f70d4-3649-4473-8106-9cb4735cf772.png。
- 实测尺寸：1672 × 941 px。
- 提示词修改：保留原提示词全文，仅追加原生2560×1440/至少2400宽及不裁为全景的要求；首轮画幅与尺寸不达标。第二轮画幅恢复，宽度仍不达标。

实际使用的完整 prompt：

```text
A clean, flat, vector-style scientific workflow diagram on a pure white background,
landscape 16:9. Two horizontal swim lanes separated by a thin light-grey line.
Top lane (very light warm beige background): a left-to-right sequence of nine small
rounded-rectangle steps, each with one simple icon inside: (1) a small piece of pink
soft tissue on a dish, (2) a conical tube with tiny enzyme droplets, (3) a cell strainer
mesh over a tube, (4) a diamond-shaped checkpoint containing a counting grid with a few
round cells, (5) a microfluidic chip whose channel forms droplets, each droplet holding
one cell and one bead, (6) a small PCR tube, (7) short double-stranded DNA fragments
with coloured end caps, (8) a second diamond-shaped checkpoint containing a small
fragment-size curve, (9) a benchtop sequencer box. Between steps 1 and 8, every step
is drawn as a stack of two slightly offset cards (two samples processed in parallel);
the two stacks merge into the single sequencer at step 9. A dashed curved arrow returns
from checkpoint 4 back to step 2, and from checkpoint 8 back to step 7.
A small circle connector at the right end of the top lane, and an identical circle at
the left end of the bottom lane.
Bottom lane (very light cool blue-grey background): a left-to-right sequence: a monitor
with aligned reads, a grid matrix of small squares, a diamond checkpoint with a filter
funnel (with two small optional dashed boxes above it, joined back into it), a bar-like
normalisation symbol, a short list of highlighted rows, a scatter of points with two
perpendicular axes arrows (PCA), a network graph of dots and edges; from the network
graph the path splits into two branches: upper branch to a set of coloured point
clusters, lower branch to a two-dimensional point embedding; only the upper branch
continues to a heat-map-like marker table and then to a final cluster map with blank
tag shapes. A dashed curved arrow returns from the final map back to the checkpoint.
Warm muted orange-brown accents in the top lane, muted teal-blue accents in the bottom
lane, dark slate arrows of uniform weight with solid triangular heads. Generous white
space. No text, no letters, no numbers, no labels, no symbols, no logos. No 3D, no
gradients, no shadows, no microscope, no DNA double helix, no gears, no people.

Technical output requirement: render a native 2560 × 1440 pixel PNG canvas, exact 16:9 landscape aspect ratio, at least 2400 pixels wide. Keep the entire illustration within this canvas; do not crop to a panoramic aspect ratio. This is a pixel-dimension requirement, not text to draw.
```

看图核验：

- 画面内容：暖色上泳道、冷色下泳道，各图标顺序可辨；上排 9 个主对象、下排 11 个，共 20 个，另有 2 个内部可选小框。
- 无文字：目视未见文字、字母、数字、伪文字或标识。图中没有 ✓/✕、编号红圈或后加标签。
- 主链：上排 8 条相邻步骤箭头方向正确；下排的 C1→C2→Q3→C4→C5→C6→C7 及 C8→C10→C11 可辨。
- C7 分叉：网络向上方聚类、下方二维嵌入分开；只有聚类继续至标志基因热图和终点。未观察到 UMAP → 聚类/注释。
- 反馈：Q1→W2、Q2→W6、C11→Q3 三条虚线反馈指向正确；本轮没有第一轮的终点反向箭头。
- 双样本卡：W1、W2、W3、W4、W5、W6 有叠卡，Q1 和 Q2 菱形没有叠卡；两条样本文库明确汇合为一条的结构仍缺失。
- 可选框：两个小虚线框被塞入 Q3 菱形内部，未按提示词放在其上方。
- 连接符：上右和下左有空圆，二者还由一条绕行长线连起来；测序仪→上圆没有清晰独立箭头。因此仅记“连接存在，交接箭头不完全清楚”。
- 图标细节：组织、酶滴、滤网、微滴和 DNA 短片段可辨；PCR 管偏长，像普通离心管；终点只有围住点簇的虚线轮廓，没有要求的空白标签牌。
- 两处样本合并、独立产物、额外可选步骤等与完整步骤表的差距见后面的逐项表；其中部分内容未写入 V2 英文提示词，不能一概称为模型忽略提示词。
- 风格：仍有柔和明暗及仪器透视，未完全满足严格扁平、无渐变。
- 选用理由：画幅恢复到约 16:9，主分叉和三条指定反馈更清楚；保留真实的不完整处供教学核验。
- 尺寸：1672 × 941，低于 2400 px；第二次明确要求 2560 × 1440 后仍未达到，不宣称已完成出版尺寸验收。

## 5. figures/ch06/ch06-icons-sheet.png

- 工具：image_gen.imagegen (tools.image_gen__imagegen)；模型：不知道；工具返回未提供具体模型名称。
- 次数：第 1 次；选用/保留的输出。
- 原始缓存文件：exec-04a26c26-5a4c-43cf-b781-b00c665cb456.png。
- 实测尺寸：1448 × 1086 px。
- 提示词修改：无，逐字使用规划 §3.6 V3。

实际使用的完整 prompt：

```text
A sheet of twelve flat vector scientific icons arranged in an even grid of four columns
and three rows on a pure white background. Each icon sits centred in its own invisible
square cell with wide white margins and does not touch any other icon. All icons share
the same style: simple geometric shapes, uniform dark slate outline of medium weight,
flat fills, no gradients, no shadows, no 3D.
Row 1 (warm muted orange-brown accent #B5653A with pale beige fills):
 1. a small piece of pink soft tissue on a shallow petri dish;
 2. a conical centrifuge tube with three tiny droplets falling into it;
 3. a round cell strainer mesh sitting on top of a tube;
 4. a square counting grid with five round cells, one cell drawn darker.
Row 2 (same warm accent, except icon 8 in deep amber #8A6D1F):
 5. a small rectangular microfluidic chip with one channel pinching off round droplets,
    each droplet containing one small cell and one small bead;
 6. a single small PCR tube with a closed cap;
 7. three short double-stranded DNA fragments, each with small coloured end caps;
 8. a benchtop sequencing instrument: a box with a small slot holding a flow cell.
Row 3 (muted teal-blue accent #2F6F8F with pale blue-grey fills):
 9. a computer monitor showing several short horizontal bars aligned under one long bar;
10. a square grid matrix of small cells with varied light-to-dark shading;
11. a network of dots connected by thin edges;
12. four clusters of dots, each cluster in a different muted colour, with one blank
    rounded tag shape next to it.
No text, no letters, no numbers, no labels, no arrows between icons, no logos,
no microscope, no DNA double helix, no people. Aspect ratio 4:3.
```

看图核验：

- 布局：4 列 × 3 行，恰好 12 个独立图标；1448 × 1086，严格 4:3。未新增连线或文字。
- 文字：整体及关键局部裁图检查未发现字母、数字、伪文字；管上只有无字刻度线。最终排版阶段的 200% 检查不在此宣称已经完成。
- 背景与间距：白底、图标彼此不接触，适合等分网格切分；背景转透明是后续确定性处理，不是原始生成的透明底。
- 风格与颜色：前两行暖色、第三行冷色大体一致；有高光、轻微渐变及仪器透视，不是严格无渐变的纯平涂。
- 逐个图标结论见 12 项核验表。原 icon 08 的托盘使其明显像打印机，不能标成已合格；因此仅对该图标另做一次局部生成。
- 选用方式：此文件作为原始图标表保留；01–07、09–12 可作为待终稿核验素材，08 使用单独修正版候选。未对整张图标表重新生成或拼贴。
- 本图共 1 次整表生成；icon 08 额外 1 次局部编辑。

## 6. figures/ch06/ch06-icon-08-corrected-source.png

- 工具：image_gen.imagegen (tools.image_gen__imagegen)；模型：不知道；工具返回未提供具体模型名称。
- 次数：第 2 次；选用/保留的输出。
- 原始缓存文件：exec-7deb29ee-8513-4fa0-b92d-6a75025fce11.png。
- 实测尺寸：1254 × 1254 px。
- 提示词修改：按规划允许的单图标修改流程，仅修改 icon 08 的打印机式纸托/出纸口为光学流动池卡匣；此为局部修正提示词，不是原 V3 提示词。
- 引用图：figures/ch06/icons/ch06-icon-08.png。

实际使用的完整 prompt：

```text
Edit only this one sequencing-instrument icon. Preserve its simple scientific icon style, dark slate outline, white background, and approximately square framing. Replace the printer-like front paper tray and paper-output slot with a small closed optical flow-cell cartridge bay: a glass rectangular microfluidic flow cell in a shallow enclosed cartridge, with tiny parallel fluidic channels visible through a small window. The instrument should read as a compact benchtop DNA sequencing instrument, not a printer. Use flat pale beige fills with a restrained deep amber #8A6D1F accent on the cartridge and dark slate outlines. No gradients, no shadows, no 3D rendering. No sheets of paper, no paper trays, no keyboards. No text, no letters, no numbers, no labels, no symbols, no logos. One isolated icon only, with generous white margin. Aspect ratio 1:1.
```

看图核验：

- 输入：并行流程已从本轮图标表切出的 icons/ch06-icon-08.png；在调用编辑前已用 view_image 打开核对。
- 画面：单个测序仪机箱；原先向前伸出的纸托消失，替换为嵌在前面板中的琥珀色流动池卡匣及流道形状。
- 无文字：未见文字、字母、数字、伪文字、商标。卡匣中的折返线是通道图形，不作为字符或标签。
- 核验“测序仪不像打印机”：相较原版有实质改善，纸托与出纸口已去除；但科学仪器识别仍应由作者在最终小尺寸中复核，不能仅凭图像生成保证硬件结构真实。
- 风格：轮廓和配色与图标表相近，但透视与明暗仍然存在，no gradients/no 3D 要求未完全达到。
- 原图 1254 × 1254；另按规划白色阈值转 alpha 并裁出透明候选，未做插值放大或内容绘制。
- 输出透明候选：icons/ch06-icon-08-corrected.png，1264 × 1042；边界框 (63,165,1191,1071)，四周各 68 px 留白。
- 未覆盖并行流程已写入的 icons/ch06-icon-08.png，也未改 TikZ 引用。终稿整合时需明确选用 corrected 文件；现有标准名 08 仍是原始打印机样图标。

## 7. V2 选用图对照步骤表的详细结果

这里区分“画面确实出现了什么”与“规划/提示词本身没有要求什么”。没有为了得到反例而人为添加错误箭头。

### 主对象逐项对应

| ID | 规划对象 | 本图观察与结论 |
|---|---|---|
| W1 | 组织采集 | 培养皿上粉红组织块；有两张叠卡，通过对象存在检查。 |
| W2 | 解离 | 上方酶滴与锥底管；有叠卡，通过简化对象检查。 |
| W3 | 过滤清洗 | 管上细胞滤网；有叠卡，通过对象检查。 |
| Q1 | 计数与活率 | 网格与圆细胞菱形；顺向出口和返回 W2 的虚线均有；没有双样本叠卡。 |
| W4 | 微滴捕获 | 芯片与 3 滴；每滴可见一较大细胞和一较小珠；有叠卡。 |
| W5 | 逆转录/破乳/扩增 | 画成管状物，提示词的小 PCR 管辨识度较弱；这些子过程无法仅凭图标核对。 |
| W6 | 建库 | 三段短双链梯状片段和端帽；有叠卡。 |
| Q2 | 文库质控 | 曲线菱形，通向测序并返回 W6；没有双样本叠卡。 |
| S1 | 混合与测序 | 单机箱可辨；两样本文库的明确双输入汇合没有画出。 |
| C1 | 比对与计数 | 显示器中水平 reads 条；存在。 |
| C2 | 细胞识别 | 网格矩阵存在；仅图标不能证明识别操作与原始矩阵的区别。 |
| Q3 | 细胞质控 | 漏斗菱形存在；两个可选小框画在菱形里面而非上方；没有独立不通过出口。 |
| C4 | 合并与标准化 | 柱状符号存在；没有明确两个过滤矩阵的合并点。 |
| C5 | 高变基因 | 部分高亮行列表存在。 |
| C6 | PCA | 带两条无字坐标轴的散点图存在。 |
| C7 | k 近邻图 | 点边网络存在；向两个下游分叉。 |
| C8 | 聚类 | 上支彩色点簇，接 C10。 |
| C9 | UMAP 展示 | 下支二维嵌入，未接 C8/C11；符合禁止关系检查。 |
| C10 | 标志基因 | 热图表格，接 C11。 |
| C11 | 细胞类型注释 | 彩色簇图存在，但没有 prompt 所要求的空白标签牌。 |

### 结构与规划差异

| 核验项 | 实测结论 |
|---|---|
| 主节点总数 | 20 个主对象均能与上表一一对应。规划写“21 个”，但其步骤表实际列出 9 个湿实验/测序 + 11 个计算主节点，即 20 个；Q3 是单独 ID，C3a/C3b 是可选。不得直接报告“漏 1/21”。 |
| 上排步骤先后 | W1→W2→W3→Q1→W4→W5→W6→Q2→S1：8 条顺向箭头可辨，符合。 |
| 跨泳道交接 | 两个空圆及绕行长线存在；测序仪到上圆没有清楚的独立箭头，部分通过。 |
| 下排主链 | C1→C2→Q3→C4→C5→C6→C7 及 C8→C10→C11 顺向可辨。 |
| 近邻图分叉 | C7→C8、C7→C9 均可辨，通过。 |
| 可选并行框 | 两个小虚线框一起连入漏斗，但位置在 Q3 内；身份不可凭无字图确认，部分通过。 |
| 两样本表示 | 6 个操作节点有叠卡；Q1/Q2 无叠卡，未完整保留提示词“steps 1–8 every step”要求。 |
| 文库与矩阵合并 | S1/C4 没有独立明确的双输入汇合；完整步骤表核验不通过。 |
| 三条 V2 指定反馈 | Q1→W2、Q2→W6、C11→Q3 方向正确。 |
| 第四条终稿反馈 | C11→C8 未画；完整步骤表要求，但 V2 英文提示词本身未要求这条，不能说是模型漏掉已写明的箭头。 |
| 额外可选节点 | W3a、W3b、C6a 未画；这些同样没有写进 V2 英文提示词。 |
| 质控双出口 | Q1/Q2 有顺向与返回两出口；Q3 只有顺向输出，终点返回 Q3 是入箭头，不能计作 Q3 的失败出口。 |
| 独立产物节点 | 单细胞悬液、cDNA、文库、FASTQ、过滤矩阵、注释图谱没有按完整任务书单独画成 6 个产物节点；V2 英文主要要求的是步骤图标。 |
| 无禁止关系 | 没观察到 C9→C8 或 C9→C11，也无参数数值。 |
| 无额外装饰 | 未见显微镜、齿轮、DNA 双螺旋或人物；短双链片段是指定图标，不能误计为禁止的双螺旋。 |

因此建议正文如实写“本次近邻图分叉和三条指定反馈正确，但双样本表示、可选框位置、明确合并点及图标细节仍不完整”，不能写“本次把 UMAP 画在聚类上游”。不填写无法统一口径的“x/21 正确”汇总。

## 8. 图标表逐个核验

以下逐项同时参照整表及可用局部切片。原表的完整 prompt 见第 5 项；每个既有切片的 JSON 记录均附同一完整原文，generation attempt=1，未伪造 12 次独立生成调用。

| 序号 / 对应节点 | 画面结论 | 状态 |
|---|---|---|
| 01 / W1 | 浅培养皿上是小块粉红软组织，并非完整器官。 | 通过对象检查；有轻微高光。 |
| 02 / W2 | 锥底离心管上方恰有 3 滴；管上为短刻度线，无文字刻度、字母或数字。 | 通过。 |
| 03 / W3 | 圆形网状过滤器位于管上。 | 通过。 |
| 04 / Q1 | 方格中恰好 5 个圆细胞，1 个更深；没有非圆细胞或文字。 | 通过。 |
| 05 / W4 | 矩形芯片单通道缩颈，后方 3 滴，每滴一较大细胞（含核）和一颗较小深色珠。细胞核不另计为一个细胞。 | 通过理想化示意检查；并非真实液滴占有率数据。 |
| 06 / W5 | 单个小锥底 PCR 管，帽盖扣在顶部；无标签。 | 通过对象检查；有高光。 |
| 07 / W6 | 恰好 3 段双链梯状短片段、彩色端帽；不是 DNA 双螺旋装饰。 | 通过。 |
| 08 / S1 | 原版前方托盘明显像打印机；深琥珀强调色仅少量出现在托盘。 | 原版不通过；另有 corrected 候选。 |
| 09 / C1 | 显示器有一条长横条及多条错位短横条，没有文本。 | 通过。 |
| 10 / C2 | 方格矩阵明暗变化，没有字符。 | 通过。 |
| 11 / C7 | 多点多边组成网络，无元素符号或化学键文字。 | 通过网络示意检查。 |
| 12 / C11 | 恰好 4 个不同颜色点簇，每簇旁一个空白圆角标签框。 | 通过；标签确实为空白。 |

## 9. 裁切、并行文件和人工修改

- 此轮开始时目标目录没有可见文件；生成期间出现了其他流程写入的 .tex、骨架 PNG、icons/ch06-icon-01.png … 12.png 和 provenance/ch06/icons.txt。它们不是本轮创建，未覆盖；现有 icons.txt 中的“占位图”记录可能已经过时，本记录不追认其内容。
- 计划中的 scripts/ch06_crop_icons.py 属于范围外文件，未修改或调用。本轮曾准备范围内等分裁切脚本，但执行在检测到已有 icon-01 时立即中止，无覆盖；该未使用的自建脚本已撤回。
- 既有 12 张切片与生成图标表画面对应；已列入尺寸快照与 JSON 来源映射，但不声称由本轮裁切。
- 本轮唯一确定性图像处理是新建 icon-08-corrected 的透明裁图：用 PIL，三个 RGB 通道都 >245 的像素置 alpha=0，其余 alpha=255；求 alpha 非空边界框，裁切后按最长边加 6% 留白。没有替换其余图标或给原表拼贴修正版。
- 修正版原图和透明裁图均保留。透明裁图尺寸较原图宽，是加边距所致；没有插值放大。
- 全部 V1/V2/整表 PNG 都是工具原样复制，没有后加文字、改错箭头、改颜色、裁边、扩画布或重采样。
- 规划要求的最终图 200% 检查、TikZ 引用替换、灰度检查、印刷字号和结构 diff 属于后续终稿整合；本轮没有把它们冒记为完成。

## 10. 实测文件清单与像素尺寸

下面逐字粘贴本轮命令输出。目录中的 TikZ、骨架和编译产物为并行流程所有，ls 只列出，未处理其内容。PNG 尺寸检查仅覆盖本轮生成图及其对应图标，不包含 kind:tikz 的骨架 PNG。Pillow Image.verify 全部通过；这仅表示文件可解码，不代表科学或版式已合格。SHA-256 与透明像素统计见 codex-image-verification.json。

```text
$ ls -l figures/ch06
total 18144
-rw-r--r--@  1 zeroone  staff  1994126 Oct 29 16:12 ch06-01-v1-vague-alt1.png
-rw-r--r--@  1 zeroone  staff  1905795 Oct 29 16:09 ch06-01-v1-vague.png
-rw-r--r--@  1 zeroone  staff     2931 Oct 29 16:11 ch06-02-flow-grammar-en.tex
-rw-r--r--@  1 zeroone  staff     2819 Oct 29 16:11 ch06-02-flow-grammar-zh.tex
-rw-r--r--@  1 zeroone  staff      246 Oct 29 16:09 ch06-03-skeleton-en.tex
-rw-r--r--@  1 zeroone  staff    52467 Oct 29 16:12 ch06-03-skeleton-notext.png
-rw-r--r--@  1 zeroone  staff      246 Oct 29 16:09 ch06-03-skeleton-zh.tex
-rw-r--r--@  1 zeroone  staff     3443 Oct 29 16:11 ch06-04-structure-errors-en.tex
-rw-r--r--@  1 zeroone  staff     3323 Oct 29 16:11 ch06-04-structure-errors-zh.tex
-rw-r--r--@  1 zeroone  staff  1356880 Oct 29 16:10 ch06-05-v2-brief-alt1.png
-rw-r--r--@  1 zeroone  staff  1335942 Oct 29 16:13 ch06-05-v2-brief.png
-rw-r--r--@  1 zeroone  staff      265 Oct 29 16:09 ch06-06-final-en.tex
-rw-r--r--@  1 zeroone  staff      304 Oct 29 16:09 ch06-06-final-zh.tex
-rw-r--r--@  1 zeroone  staff      907 Oct 29 16:09 ch06-coords.tex
-rw-r--r--@  1 zeroone  staff  1166421 Oct 29 16:15 ch06-icon-08-corrected-source.png
-rw-r--r--@  1 zeroone  staff  1343766 Oct 29 16:11 ch06-icons-sheet.png
-rw-r--r--@  1 zeroone  staff     2097 Oct 29 16:09 ch06-labels-en.tex
-rw-r--r--@  1 zeroone  staff     2060 Oct 29 16:09 ch06-labels-zh.tex
-rw-r--r--@  1 zeroone  staff       32 Oct 29 16:12 ch06-skeleton-notext-standalone.aux
-rw-r--r--@  1 zeroone  staff    43411 Oct 29 16:12 ch06-skeleton-notext-standalone.log
-rw-r--r--@  1 zeroone  staff     7630 Oct 29 16:12 ch06-skeleton-notext-standalone.pdf
-rw-r--r--@  1 zeroone  staff      358 Oct 29 16:12 ch06-skeleton-notext-standalone.tex
-rw-r--r--@  1 zeroone  staff     2619 Oct 29 16:11 ch06-styles.tex
-rw-r--r--@  1 zeroone  staff     5260 Oct 29 16:11 ch06-workflow-draw.tex
drwxr-xr-x@ 15 zeroone  staff      480 Oct 29 16:16 icons

$ PNG pixel dimensions (Pillow Image.size; Image.verify passed)
figures/ch06/ch06-01-v1-vague-alt1.png: 1672 x 941 px; RGB; 1994126 bytes
figures/ch06/ch06-01-v1-vague.png: 1672 x 941 px; RGB; 1905795 bytes
figures/ch06/ch06-05-v2-brief-alt1.png: 1983 x 793 px; RGB; 1356880 bytes
figures/ch06/ch06-05-v2-brief.png: 1672 x 941 px; RGB; 1335942 bytes
figures/ch06/ch06-icon-08-corrected-source.png: 1254 x 1254 px; RGB; 1166421 bytes
figures/ch06/ch06-icons-sheet.png: 1448 x 1086 px; RGB; 1343766 bytes
figures/ch06/icons/ch06-icon-01.png: 315 x 176 px; RGBA; 64417 bytes
figures/ch06/icons/ch06-icon-02.png: 133 x 347 px; RGBA; 44533 bytes
figures/ch06/icons/ch06-icon-03.png: 245 x 294 px; RGBA; 79047 bytes
figures/ch06/icons/ch06-icon-04.png: 301 x 284 px; RGBA; 88354 bytes
figures/ch06/icons/ch06-icon-05.png: 351 x 199 px; RGBA; 74638 bytes
figures/ch06/icons/ch06-icon-06.png: 154 x 253 px; RGBA; 38425 bytes
figures/ch06/icons/ch06-icon-07.png: 262 x 265 px; RGBA; 74063 bytes
figures/ch06/icons/ch06-icon-08-corrected.png: 1264 x 1042 px; RGBA; 767470 bytes
figures/ch06/icons/ch06-icon-08.png: 349 x 289 px; RGBA; 102478 bytes
figures/ch06/icons/ch06-icon-09.png: 346 x 288 px; RGBA; 68718 bytes
figures/ch06/icons/ch06-icon-10.png: 289 x 279 px; RGBA; 74210 bytes
figures/ch06/icons/ch06-icon-11.png: 309 x 279 px; RGBA; 90455 bytes
figures/ch06/icons/ch06-icon-12.png: 342 x 298 px; RGBA; 119702 bytes
```

