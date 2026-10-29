# 第 11 章 Codex 图像生成与核验记录

日期：2026-10-29（Asia/Shanghai）。任务输入：`(local scratch file)`。依据：`production/plans/ch11.md` 与 `production/book-spec.md` §4–5。

## 交付状态

**已生成四个 FIG 的底图和全部四张备选，共 8 次内置生成调用。完整科学/终稿验收未通过。**

- FIG ch11-02 / V1：1 次，保留首次；允许文字/伪文字的反例。
- FIG ch11-03 / V2：3 次，选第 2 次；第 1、3 次分别为 alt1、alt2。所选图只是比较用候选参考，**不是已通过全部验收的结构基准**。
- FIG ch11-04 / V3：3 次，每次独立参考同一 V2；均未观察到明确结构连带变化，选首次，第 2、3 次为 alt1、alt2。**不得编造少索、少传感器、GNSS 消失或网关移位。**
- FIG ch11-06 / V4：1 次，重新参考 V2，附逐项保留清单；局部线型修改完成，主要对象目视保留，但 V2 的布局、红色唯一性、渐变及小图标问题仍在，**不能称为验收通过终稿**。
- 所有原始生成图实测 **1774×887 px、2:1**。V2 提示词要求 2400×1200，工具未按像素要求输出；没有拉伸、补边或人工重绘冒充符合。
- 本次未生成/修改 kind 为 tikz、python、reuse 的图，也未写章节正文、全书规范或范围外项目文件；未 commit/push；未启动子 agent。目录中同期出现的这些其他文件不是本任务产物。

## 执行规则与诚实性

1. 任务文件的“每张最多 3 次”优先于章节 V3 的 4 次上限；V3 只做 3 次，不能写成“4 次均无变化”。V2 达到 3 次后也未按规划的另一条建议无限修订提示词重来。
2. V1、V2、V3 每次 prompt 均逐字取自相应规划代码块，保留英文和换行；没有追加“故意删索”等制造错误的指令。V4 规划没有现成英文代码块，仅要求同义英译，所以完整英译如下逐条保存。
3. 实际工具：**内置 `image_gen.imagegen`**（调用入口 `functions` 的 `tools.image_gen__imagegen`）；**具体模型不知道**，工具未返回模型标识。不记成 SciDraw、DALL·E 或某个 GPT 图像版本。
4. V1/V2 调用参数为 `prompt` 与 `transparent_background:false`；新生成时未传参考图或最近图片数量。V3/V4 另传 `referenced_image_paths`，唯一参考为本任务保存的 `figures/ch11/ch11-03-v2-brief.png`。参考文件在编辑前已通过 `view_image` 查看。
5. 工具自动将原图缓存在 `codex-output/`；逐张原封不动复制到本任务图目录。缓存不是项目交付路径。源文件对应关系与哈希在本记录和 `generation-records.json` 中保存。
6. 核验由本次 Codex 目视完成：查看每次生成的整图，进一步查看 V2 三次的 200% 桥体局部、V4 灰度副本。这里的对象计数不是作者/领域同行签字，也不是算法自动计数。可见走向数与“每根连续且正确连接”是不同验收项。
7. 检查副本只在 `provenance/ch11/` 中生成，用于放大/灰度检查，不是手工修正底图，也不计为新的图像生成尝试：
   - `v2-inspection-200pct.png`：V2 选中图裁取 (25,140,1160,490)，放大 2 倍，2270×700。
   - `ch11-03-v2-brief-alt1-inspection-200pct.png`：V2 第 1 次裁取 (15,150,1260,520)，放大 2 倍，2490×740。
   - `ch11-03-v2-brief-alt2-inspection-200pct.png`：V2 第 3 次裁取 (20,130,1160,490)，放大 2 倍，2280×720。
   - `v4-inspection-grayscale.png`：V4 使用 Pillow ImageOps.grayscale 转为灰度，1774×887。
8. 不在本任务中执行 FIG ch11-05 的差异图脚本；后续制作方应按这里列出的最终参考哈希重算，不应假定生成过程中出现的中间差异图已经对应本次选图。

## 逐图文件、尺寸与选择

| 文件 | 版本/生成次数 | 用途 | 实测像素 | 字节 |
|---|---|---|---|---|
| `ch11-02-v1-vague.png` | V1 第 1 次 | 选中交付（不等于科学验收通过） | 1774×887 | 2390328 |
| `ch11-03-v2-brief-alt1.png` | V2 第 1 次 | 备选保留 | 1774×887 | 1245145 |
| `ch11-03-v2-brief.png` | V2 第 2 次 | 选中交付（不等于科学验收通过） | 1774×887 | 1245807 |
| `ch11-03-v2-brief-alt2.png` | V2 第 3 次 | 备选保留 | 1774×887 | 1236063 |
| `ch11-04-v3-collateral.png` | V3 第 1 次 | 选中交付（不等于科学验收通过） | 1774×887 | 1588813 |
| `ch11-04-v3-collateral-alt1.png` | V3 第 2 次 | 备选保留 | 1774×887 | 1583277 |
| `ch11-04-v3-collateral-alt2.png` | V3 第 3 次 | 备选保留 | 1774×887 | 1596165 |
| `ch11-06-v4-recovered.png` | V4 第 1 次 | 选中交付（不等于科学验收通过） | 1774×887 | 1593124 |

## 主要对象目视计数

| 文件/尝试 | 两塔四个索扇 | 传感器：梁蓝/索蓝/绿/风/GNSS/温/紫 | 网关/云/处理框/终端组 |
|---|---|---|---|
| V2 第 1 次（alt1） | 3+3+3+3，加左外侧孤立线段；不通过 | 3/2/2/1/1/1/2=12，但一索传感器附着异常 | 1/1/3/1 |
| V2 第 2 次（选中） | 4+4+4+4=16 个可辨走向；部分被图标遮断 | 3/2/2/1/1/1/2=12 | 1/1/3/1 |
| V2 第 3 次（alt2） | 4+4+4+4=16 个可辨走向；主跨交叉较拥挤 | 3/2/2/1/1/1/2=12 | 1/1/3/1 |
| V3 第 1 次（选中） | 与所选 V2 一致 | 与所选 V2 一致 | 1/1/3/1 |
| V3 第 2 次（alt1） | 与所选 V2 一致 | 与所选 V2 一致 | 1/1/3/1 |
| V3 第 3 次（alt2） | 与所选 V2 一致 | 与所选 V2 一致 | 1/1/3/1 |
| V4 第 1 次 | 与所选 V2 一致 | 与所选 V2 一致 | 1/1/3/1 |

## 选中参考图的实测定位（供后续排版复测）

坐标为图像归一化坐标，x 向右、y 向下；以下为目视近似对象中心，不是已排版标签坐标。V3/V4 主要对象位置目视相同。不得直接沿用规划中把云放在上方的标签坐标。

| 对象 | 近似中心 (x,y) |
|---|---|
| 左塔塔顶 / 右塔塔顶 | (0.197,0.229) / (0.473,0.229) |
| 主梁 | (0.335,0.505) |
| 主梁蓝方块 3 个 | (0.264,0.484), (0.338,0.484), (0.410,0.484) |
| 外索蓝方块 2 个 | (0.113,0.376), (0.546,0.373) |
| 绿应变计 2 个 | (0.214,0.529), (0.348,0.529) |
| 风速仪 / GNSS | (0.197,0.197) / (0.469,0.196) |
| 温度计 / 两端紫方块 | (0.094,0.460) / (0.036,0.495), (0.631,0.495) |
| 网关 / 云 / 终端组 | (0.778,0.405) / (0.802,0.706) / (0.945,0.536) |
| 云内三个处理框 | (0.738,0.776), (0.798,0.776), (0.859,0.776) |

V1 的可见问题定位建议：写实场景/多塔桥约 (0.32,0.45)；生成监测图表/“92%”约 (0.87,0.23)；生成预警列表约 (0.88,0.56)；城市和光效约 (0.60,0.70)。未添加编号圈，也未强行套用未发生的 S1–S6 错误。

## 每张图的完整 prompt 与逐项看图结论

### ch11-02-v1-vague.png

- 版本与次数：V1，第 1 次。
- 工具：image_gen.imagegen (functions tools.image_gen__imagegen)。具体模型：不知道；工具未返回具体模型名称。
- 选择：选中交付；验收状态见结论。
- 基于：无参考图；从英文 prompt 新生成。
- 原始工具缓存：`codex-output/exec-846c75bd-756d-4f60-b066-04271d156583.png`。
- 输出 SHA-256：`7340b6e3d5e5cc40bdb0ebd080f0c36e0943023c1882bfde97ea433aacb66b7f`。
- Prompt 改动：无；与规划所指定英文代码块逐字一致。

实际提交的完整 prompt：

```text
Create a beautiful, professional illustration of a smart structural health
monitoring system for a bridge with sensors, wireless network, cloud and alerts.
Landscape, aspect ratio 2:1.
```

看图核验：

1. 教学目的：保留模糊提示词的第一次原始结果；符合本图允许文字/伪文字的例外，不因有字重试。
2. 画面内容：写实、透视的长桥，多座可见桥塔，日落、水面、城市、光效及管理人员；不是规划主案例要求的双塔侧视工程图。可见斜拉索，不能称为已观察到悬索桥或主缆/吊杆错误。
3. 传感器与通信：出现多个白色节点盒和无线图标，类型由标签解释；无法按主案例对象表验收 12 个传感器及精确位置。未据此捏造风速仪放错、拉索入水或传感器直连手机的结论。
4. 云与数据：有网关、云、监测面板、预警列表和操作终端。云与网关之间含双向箭头，但未确认存在规划所举的“云直接指向传感器”错误，因此不标注该错误。
5. 文字/数值：可见 Accelerometer、Cloud Platform、Real-Time Monitoring、Intelligent Alerts、92% 和日期等；均为生成内容，没有真实监测数据依据。不能把这些当成实测结果，也不能把未出现的 Senser/Clould 错拼写进正文。
6. 阅读障碍：场景、光效、多个仪表图和文字占据大量画面，明显偏离简明架构图目标。未预设或硬凑“科学错误 ≥3 条”。
7. 核验结论：作为初稿反例保留；正文问题清单只能依据以上实际画面重新编写。

### ch11-03-v2-brief-alt1.png

- 版本与次数：V2，第 1 次。
- 工具：image_gen.imagegen (functions tools.image_gen__imagegen)。具体模型：不知道；工具未返回具体模型名称。
- 选择：未选中，保留真实备选。
- 基于：无参考图；从英文 prompt 新生成。
- 原始工具缓存：`codex-output/exec-2a2f0ba0-79c4-44f4-9888-dd0ef453e34e.png`。
- 输出 SHA-256：`8c15ab544d740f6ad1a8b35bb2b1c2295298c20e3696906dde09a530c0954657`。
- Prompt 改动：无；与规划所指定英文代码块逐字一致。

实际提交的完整 prompt：

```text
Flat 2D engineering schematic, landscape 2:1 (2400 x 1200 px), pure white
background, clean vector style, flat fills, thin dark gray outlines, no
gradients, no shadows, no 3D, no realistic materials, no glow.

ABSOLUTELY NO TEXT: no letters, words, numbers, symbols, labels, legend or title.

LEFT 70% - SIDE VIEW OF A TWIN-PYLON CABLE-STAYED BRIDGE (not a suspension
bridge: no main cable, no vertical hangers):
- A pale blue water band along the bottom (y 0.75-0.88).
- A long light gray deck girder across x 0.03-0.68 at y 0.60-0.63.
- Two medium gray vertical pylons at x 0.22 and x 0.50, from the water up to
  y 0.20, each on a gray pier; two short gray end piers at both deck ends.
- Exactly 16 straight thin dark gray stay cables: from the upper part of each
  pylon, 4 cables fan down to the deck on the left side and 4 on the right side
  of that pylon. Every cable connects pylon to deck. No cable touches the water
  or the ground.
SENSORS (small flat icons, same type = same shape and color):
- 3 small blue squares on top of the deck in the main span (between the pylons)
  at one quarter, one half and three quarters of the span.
- 2 small blue squares at the middle of the longest outer cable of each pylon.
- 2 small green rectangles on the underside of the deck: one at mid main span,
  one next to the left pylon.
- 1 small cup anemometer icon on top of the left pylon.
- 1 small dish antenna (GNSS) icon on top of the right pylon.
- 1 small round thermometer icon on the deck in the left side span.
- 2 small purple squares at the two deck ends (expansion joints).
Each sensor has a tiny black dot beside it (its wireless node).

RIGHT 30% - DATA PATH (bottom to top, then right):
- A small gray cabinet with a short antenna on the right bank at x 0.76,
  y 0.62 (on-site gateway).
- A large light gray cloud outline at x 0.74-0.90, y 0.10-0.35 containing a
  short stack of three gray server bars and, below them, three small empty
  rounded boxes in a row connected by small dark gray arrows (processing steps).
- At the far right x 0.93-0.99, y 0.30-0.50: a small monitor with a phone next
  to it (operator terminal).

LINES:
- Wireless: from several sensor nodes to the gateway, short orange dashed lines
  with small wave marks, clearly different from the straight solid gray cables.
- Upload: one solid orange arrow from the gateway up to the cloud.
- Alert: one solid red arrow from the last processing box to the operator
  terminal. Red is used nowhere else.
- No arrow from the cloud to any sensor; no line from any sensor directly to
  the terminal.

Keep the bottom 10% (y 0.90-1.00) empty for a legend. Do not draw vehicles,
people, buildings, city skyline, trees, charts, curves, cracks, satellites.
```

看图核验：

1. 教学目的：未达到结构基准要求；落选保留。
2. 桥型与数量：双塔斜拉桥侧视、主梁、水面、两塔下基础和两端边墩可辨；无悬索主缆/竖吊杆。
3. 拉索：200% 局部检查见每塔每侧 3 根可追踪至塔身的线，共 12 根；左外侧蓝色传感器所在处另有一段向主梁延伸的孤立斜线，上端没有连续接至桥塔。若把此孤立段也算线段可见 13 条，但不应当作 13 根合格拉索，更不是所需的 16 根。
4. 传感器：可辨主梁蓝方块 3、索部蓝方块 2、梁底绿矩形 2、左塔风速仪 1、右塔碟形天线 1、左侧温度计 1、端部紫方块 2，共 12；索部传感器之一位于上述不连续线段，因此位置/附着关系不完全合格。
5. 子系统：网关 1、云 1、服务器条 3、处理框 3、显示器加手机组成的终端 1 组。
6. 关系：橙色虚线及波纹可见；网关→云橙箭头、云内两段处理箭头、处理末框→终端红箭头方向可辨。云位于右下、网关在其上方，上传箭头朝下，违背规划的右上云布局，但不是语义上的“云→网关”反向箭头。
7. 颜色/风格：温度计内部也有红色，违反红色仅用于预警；存在柔和渐变及阴影感，不满足严格平涂；无可见文字、字母、数字或伪文字。
8. 留白/尺寸：底部约 10% 空白；原生 1774×887，2:1，未达到请求的 2400×1200。
9. 核验结论：拉索数量、连接完整性、云布局、红色唯一性和纯平涂均不通过。

### ch11-03-v2-brief.png

- 版本与次数：V2，第 2 次。
- 工具：image_gen.imagegen (functions tools.image_gen__imagegen)。具体模型：不知道；工具未返回具体模型名称。
- 选择：选中交付；验收状态见结论。
- 基于：无参考图；从英文 prompt 新生成。
- 原始工具缓存：`codex-output/exec-4c620b2f-86cf-4653-9397-45e0d87c3886.png`。
- 输出 SHA-256：`bf6c17a83f4394bb1a83d245984126caf6dfdfb54f35a74bc13198a73f0ecf49`。
- Prompt 改动：无；与规划所指定英文代码块逐字一致。

实际提交的完整 prompt：

```text
Flat 2D engineering schematic, landscape 2:1 (2400 x 1200 px), pure white
background, clean vector style, flat fills, thin dark gray outlines, no
gradients, no shadows, no 3D, no realistic materials, no glow.

ABSOLUTELY NO TEXT: no letters, words, numbers, symbols, labels, legend or title.

LEFT 70% - SIDE VIEW OF A TWIN-PYLON CABLE-STAYED BRIDGE (not a suspension
bridge: no main cable, no vertical hangers):
- A pale blue water band along the bottom (y 0.75-0.88).
- A long light gray deck girder across x 0.03-0.68 at y 0.60-0.63.
- Two medium gray vertical pylons at x 0.22 and x 0.50, from the water up to
  y 0.20, each on a gray pier; two short gray end piers at both deck ends.
- Exactly 16 straight thin dark gray stay cables: from the upper part of each
  pylon, 4 cables fan down to the deck on the left side and 4 on the right side
  of that pylon. Every cable connects pylon to deck. No cable touches the water
  or the ground.
SENSORS (small flat icons, same type = same shape and color):
- 3 small blue squares on top of the deck in the main span (between the pylons)
  at one quarter, one half and three quarters of the span.
- 2 small blue squares at the middle of the longest outer cable of each pylon.
- 2 small green rectangles on the underside of the deck: one at mid main span,
  one next to the left pylon.
- 1 small cup anemometer icon on top of the left pylon.
- 1 small dish antenna (GNSS) icon on top of the right pylon.
- 1 small round thermometer icon on the deck in the left side span.
- 2 small purple squares at the two deck ends (expansion joints).
Each sensor has a tiny black dot beside it (its wireless node).

RIGHT 30% - DATA PATH (bottom to top, then right):
- A small gray cabinet with a short antenna on the right bank at x 0.76,
  y 0.62 (on-site gateway).
- A large light gray cloud outline at x 0.74-0.90, y 0.10-0.35 containing a
  short stack of three gray server bars and, below them, three small empty
  rounded boxes in a row connected by small dark gray arrows (processing steps).
- At the far right x 0.93-0.99, y 0.30-0.50: a small monitor with a phone next
  to it (operator terminal).

LINES:
- Wireless: from several sensor nodes to the gateway, short orange dashed lines
  with small wave marks, clearly different from the straight solid gray cables.
- Upload: one solid orange arrow from the gateway up to the cloud.
- Alert: one solid red arrow from the last processing box to the operator
  terminal. Red is used nowhere else.
- No arrow from the cloud to any sensor; no line from any sensor directly to
  the terminal.

Keep the bottom 10% (y 0.90-1.00) empty for a legend. Do not draw vehicles,
people, buildings, city skyline, trees, charts, curves, cracks, satellites.
```

看图核验：

1. 教学目的：三次中选为后续比较用的候选参考图；没有通过规划的完整结构基准验收，不能使用现有图注中“全部核对通过”的表述。
2. 桥型：双塔斜拉桥侧视，无悬索主缆/竖吊杆；主梁 1、水带 1、两塔下基础加两端边墩共 4。
3. 拉索：200% 放大沿走向核对为每塔每侧 4 条，共 16 条；走向连接塔与主梁，未见入水/入地。部分线被传感器和波纹的白色留空遮断，因此“每根连续、端点完全无遮挡”仍不能判通过。
4. 传感器：主梁 3 蓝方块（约主跨 1/4、1/2、3/4）、外侧最长索中部 2 蓝方块、梁底 2 绿矩形、左塔风速仪 1、右塔 GNSS 碟形天线 1、左边跨圆温度计 1、两端紫方块 2，总数 12；各类位置基本符合，传感器旁黑色节点点可辨。
5. 子系统：网关 1、云 1、服务器条 3、处理框 3、终端 1 组（显示器+手机）。
6. 关系：传感器附近橙色虚线向网关汇聚；网关→云橙色实线箭头、云内处理顺序箭头、末框→终端红箭头可辨；未见云直接到传感器或传感器直接到终端的箭头。
7. 布局：网关约 (0.778,0.405)，云约 (0.802,0.706)，主梁约 y=0.505；云在网关下方，上传箭头向下，明显违背规划的云 y=0.10–0.35、网关 y≈0.62 和主梁 y≈0.60–0.63。此处是空间布局偏差，不能误记为传输语义反向。
8. 颜色/风格：温度计内部红色违反“红色全图只用于预警”；水面、显示器等有渐变，不完全符合平涂约束。同类蓝方块外观相近，但没有验证精确色值一致。
9. 文字与留白：全图目视无文字、字母、数字或伪文字，底部约 10% 留白；禁止的车辆、人物、城市、数据曲线、裂缝、卫星均未见。
10. 印刷可辨性：蓝方块主体约 16–20 px；按通栏 160 mm 换算约 1.44–1.80 mm，小于 F7 的 2 mm，不能判通过；未进行实体打印。
11. 核验结论：对象类别和 16/12 计数比第一次更接近要求，故选为比较参考；布局、红色唯一性、平涂、线连续性和小图标尺寸仍不合格。

### ch11-03-v2-brief-alt2.png

- 版本与次数：V2，第 3 次。
- 工具：image_gen.imagegen (functions tools.image_gen__imagegen)。具体模型：不知道；工具未返回具体模型名称。
- 选择：未选中，保留真实备选。
- 基于：无参考图；从英文 prompt 新生成。
- 原始工具缓存：`codex-output/exec-7f38470d-ac78-4d7d-8e55-9ebfbe2f19da.png`。
- 输出 SHA-256：`6a2b506fd92150d15d9f7e21a3877a7565d49b52ced1c04f64cd11acd2ef2050`。
- Prompt 改动：无；与规划所指定英文代码块逐字一致。

实际提交的完整 prompt：

```text
Flat 2D engineering schematic, landscape 2:1 (2400 x 1200 px), pure white
background, clean vector style, flat fills, thin dark gray outlines, no
gradients, no shadows, no 3D, no realistic materials, no glow.

ABSOLUTELY NO TEXT: no letters, words, numbers, symbols, labels, legend or title.

LEFT 70% - SIDE VIEW OF A TWIN-PYLON CABLE-STAYED BRIDGE (not a suspension
bridge: no main cable, no vertical hangers):
- A pale blue water band along the bottom (y 0.75-0.88).
- A long light gray deck girder across x 0.03-0.68 at y 0.60-0.63.
- Two medium gray vertical pylons at x 0.22 and x 0.50, from the water up to
  y 0.20, each on a gray pier; two short gray end piers at both deck ends.
- Exactly 16 straight thin dark gray stay cables: from the upper part of each
  pylon, 4 cables fan down to the deck on the left side and 4 on the right side
  of that pylon. Every cable connects pylon to deck. No cable touches the water
  or the ground.
SENSORS (small flat icons, same type = same shape and color):
- 3 small blue squares on top of the deck in the main span (between the pylons)
  at one quarter, one half and three quarters of the span.
- 2 small blue squares at the middle of the longest outer cable of each pylon.
- 2 small green rectangles on the underside of the deck: one at mid main span,
  one next to the left pylon.
- 1 small cup anemometer icon on top of the left pylon.
- 1 small dish antenna (GNSS) icon on top of the right pylon.
- 1 small round thermometer icon on the deck in the left side span.
- 2 small purple squares at the two deck ends (expansion joints).
Each sensor has a tiny black dot beside it (its wireless node).

RIGHT 30% - DATA PATH (bottom to top, then right):
- A small gray cabinet with a short antenna on the right bank at x 0.76,
  y 0.62 (on-site gateway).
- A large light gray cloud outline at x 0.74-0.90, y 0.10-0.35 containing a
  short stack of three gray server bars and, below them, three small empty
  rounded boxes in a row connected by small dark gray arrows (processing steps).
- At the far right x 0.93-0.99, y 0.30-0.50: a small monitor with a phone next
  to it (operator terminal).

LINES:
- Wireless: from several sensor nodes to the gateway, short orange dashed lines
  with small wave marks, clearly different from the straight solid gray cables.
- Upload: one solid orange arrow from the gateway up to the cloud.
- Alert: one solid red arrow from the last processing box to the operator
  terminal. Red is used nowhere else.
- No arrow from the cloud to any sensor; no line from any sensor directly to
  the terminal.

Keep the bottom 10% (y 0.90-1.00) empty for a legend. Do not draw vehicles,
people, buildings, city skyline, trees, charts, curves, cracks, satellites.
```

看图核验：

1. 教学目的：第三次使用相同提示词重试；未通过完整基准验收，作为 alt2 保留。
2. 桥型/构件：双塔斜拉桥、主梁、水带及四处支撑可辨；每塔每侧 4 条斜拉索走向，共 16 条。主跨中央有两座塔的斜索交叉，局部被图标遮挡，阅读更拥挤。
3. 传感器：主梁蓝方块 3、索上蓝方块 2、绿矩形 2、风速仪 1、碟形 GNSS 天线 1、圆温度计 1、紫方块 2，共 12；大类位置可辨。风速仪也使用蓝色，类型颜色区分弱于第二次。
4. 子系统：网关 1、云 1、服务器条 3、处理框 3、终端 1 组；网关呈悬空机柜，右岸承托不清楚。
5. 关系：橙虚线及波纹、网关→云、处理顺序、末框→终端均可辨；云仍在下方、上传箭头向下。没有将这种空间问题误判为语义反向箭头。
6. 颜色/风格：温度计红色仍存在；有渐变；云压到水带区域，布局较第二次更拥挤。
7. 文字与限制：无可见文字、字母、数字或伪文字；无车辆、人物、城市、图表、裂缝、卫星；底部留白存在。
8. 尺寸：1774×887，2:1，未达到请求的 2400×1200。
9. 核验结论：达到本任务三次上限；保留失败结果，不追加第四次，也不重写英文提示词再扩大尝试次数。

### ch11-04-v3-collateral.png

- 版本与次数：V3，第 1 次。
- 工具：image_gen.imagegen (functions tools.image_gen__imagegen)。具体模型：不知道；工具未返回具体模型名称。
- 选择：选中交付；验收状态见结论。
- 基于：`figures/ch11/ch11-03-v2-brief.png`；SHA-256 `bf6c17a83f4394bb1a83d245984126caf6dfdfb54f35a74bc13198a73f0ecf49`。
- 原始工具缓存：`codex-output/exec-75680f40-2989-4e5d-8c02-0c4079d0c81d.png`。
- 输出 SHA-256：`b828774d08b8ce51f2307c2bb36c976970421c186c131cf55e1ecf9ce4e2aa12`。
- Prompt 改动：无；与规划所指定英文代码块逐字一致。

实际提交的完整 prompt：

```text
Using the reference image, change only the wireless lines from the sensors to
the gateway: make them thicker orange short-dashed lines with small wave marks,
so they cannot be confused with the stay cables. Keep everything else
unchanged. No text.
```

看图核验：

1. 输入：独立以 V2 第 2 次结果为参考，使用规划 V3 英文原文；不是在前一次 V3 上继续编辑。
2. 目标修改：矩形短划线明显加粗，波纹也更醒目。 无线通信与细灰色实线拉索在颜色和线型上可区分。波纹主要位于节点旁，未实现每条链路中段都带波纹的更严格解读。
3. 对象计数：两塔；拉索可辨走向 4+4+4+4=16；传感器 3+2+2+1+1+1+2=12；网关 1、云 1、服务器条 3、处理框 3、终端 1 组，均与所选 V2 一致。
4. 连接/位置：原有塔梁关系、两塔顶图标、两端紫色位移计和各子系统位置目视保留；继承参考图中图标遮挡导致的拉索局部留空，没有新增入水/入地拉索。
5. L2–L4：橙色网关→云、灰色处理顺序、红色末框→终端保留；没有观察到新增云→传感器或传感器→终端。
6. 连带变化：未观察到足以支持规划反例的结构变化（少索、少传感器、网关移位等）；不能声称图像逐像素不变，也不能人为删除对象来制造失败。
7. 继承缺陷：云仍位于网关下方、温度计仍为红色，渐变与小图标问题仍在；这些是 V2 已有问题，不能计为本次编辑造成的连带变化。
8. 文字与画幅：无可见文字、字母、数字或伪文字；1774×887、2:1，原生文件未经人工重绘。
9. 核验结论：三次均未观察到明显结构连带变化，选择首次结果展示“目标修改完成、主要对象计数一致”；文件名依规划保留 collateral，但不能用作“真实结构失败”证据。

### ch11-04-v3-collateral-alt1.png

- 版本与次数：V3，第 2 次。
- 工具：image_gen.imagegen (functions tools.image_gen__imagegen)。具体模型：不知道；工具未返回具体模型名称。
- 选择：未选中，保留真实备选。
- 基于：`figures/ch11/ch11-03-v2-brief.png`；SHA-256 `bf6c17a83f4394bb1a83d245984126caf6dfdfb54f35a74bc13198a73f0ecf49`。
- 原始工具缓存：`codex-output/exec-acb831c1-61fa-4d27-8839-c99d016b1688.png`。
- 输出 SHA-256：`46f386871699b1d4705b991d3280f933123579af739bdfcc94195f1414c100c1`。
- Prompt 改动：无；与规划所指定英文代码块逐字一致。

实际提交的完整 prompt：

```text
Using the reference image, change only the wireless lines from the sensors to
the gateway: make them thicker orange short-dashed lines with small wave marks,
so they cannot be confused with the stay cables. Keep everything else
unchanged. No text.
```

看图核验：

1. 输入：独立以 V2 第 2 次结果为参考，使用规划 V3 英文原文；不是在前一次 V3 上继续编辑。
2. 目标修改：短划线加粗，波纹较第一次更大；线间距随生成略有差异。 无线通信与细灰色实线拉索在颜色和线型上可区分。波纹主要位于节点旁，未实现每条链路中段都带波纹的更严格解读。
3. 对象计数：两塔；拉索可辨走向 4+4+4+4=16；传感器 3+2+2+1+1+1+2=12；网关 1、云 1、服务器条 3、处理框 3、终端 1 组，均与所选 V2 一致。
4. 连接/位置：原有塔梁关系、两塔顶图标、两端紫色位移计和各子系统位置目视保留；继承参考图中图标遮挡导致的拉索局部留空，没有新增入水/入地拉索。
5. L2–L4：橙色网关→云、灰色处理顺序、红色末框→终端保留；没有观察到新增云→传感器或传感器→终端。
6. 连带变化：未观察到足以支持规划反例的结构变化（少索、少传感器、网关移位等）；不能声称图像逐像素不变，也不能人为删除对象来制造失败。
7. 继承缺陷：云仍位于网关下方、温度计仍为红色，渐变与小图标问题仍在；这些是 V2 已有问题，不能计为本次编辑造成的连带变化。
8. 文字与画幅：无可见文字、字母、数字或伪文字；1774×887、2:1，原生文件未经人工重绘。
9. 核验结论：未观察到明显结构连带变化，作为未选中的真实尝试保存；不是失败例或人工构造例。

### ch11-04-v3-collateral-alt2.png

- 版本与次数：V3，第 3 次。
- 工具：image_gen.imagegen (functions tools.image_gen__imagegen)。具体模型：不知道；工具未返回具体模型名称。
- 选择：未选中，保留真实备选。
- 基于：`figures/ch11/ch11-03-v2-brief.png`；SHA-256 `bf6c17a83f4394bb1a83d245984126caf6dfdfb54f35a74bc13198a73f0ecf49`。
- 原始工具缓存：`codex-output/exec-bb220918-77d8-4609-b9f6-62657cebb91e.png`。
- 输出 SHA-256：`7523c7737483f08b02094f73dfabc61ce18d3b3aab21a3a16c86c088c1f41091`。
- Prompt 改动：无；与规划所指定英文代码块逐字一致。

实际提交的完整 prompt：

```text
Using the reference image, change only the wireless lines from the sensors to
the gateway: make them thicker orange short-dashed lines with small wave marks,
so they cannot be confused with the stay cables. Keep everything else
unchanged. No text.
```

看图核验：

1. 输入：独立以 V2 第 2 次结果为参考，使用规划 V3 英文原文；不是在前一次 V3 上继续编辑。
2. 目标修改：橙色短划线更粗、端部圆润，波纹仍在节点旁。 无线通信与细灰色实线拉索在颜色和线型上可区分。波纹主要位于节点旁，未实现每条链路中段都带波纹的更严格解读。
3. 对象计数：两塔；拉索可辨走向 4+4+4+4=16；传感器 3+2+2+1+1+1+2=12；网关 1、云 1、服务器条 3、处理框 3、终端 1 组，均与所选 V2 一致。
4. 连接/位置：原有塔梁关系、两塔顶图标、两端紫色位移计和各子系统位置目视保留；继承参考图中图标遮挡导致的拉索局部留空，没有新增入水/入地拉索。
5. L2–L4：橙色网关→云、灰色处理顺序、红色末框→终端保留；没有观察到新增云→传感器或传感器→终端。
6. 连带变化：未观察到足以支持规划反例的结构变化（少索、少传感器、网关移位等）；不能声称图像逐像素不变，也不能人为删除对象来制造失败。
7. 继承缺陷：云仍位于网关下方、温度计仍为红色，渐变与小图标问题仍在；这些是 V2 已有问题，不能计为本次编辑造成的连带变化。
8. 文字与画幅：无可见文字、字母、数字或伪文字；1774×887、2:1，原生文件未经人工重绘。
9. 核验结论：未观察到明显结构连带变化，作为未选中的真实尝试保存；不是失败例或人工构造例。

### ch11-06-v4-recovered.png

- 版本与次数：V4，第 1 次。
- 工具：image_gen.imagegen (functions tools.image_gen__imagegen)。具体模型：不知道；工具未返回具体模型名称。
- 选择：选中交付；验收状态见结论。
- 基于：`figures/ch11/ch11-03-v2-brief.png`；SHA-256 `bf6c17a83f4394bb1a83d245984126caf6dfdfb54f35a74bc13198a73f0ecf49`。
- 原始工具缓存：`codex-output/exec-4c546022-ec16-4f2c-b94b-55edbcdcd197.png`。
- 输出 SHA-256：`753b5f1cb2dbd1da15566c004a87efbf6441c99b36d3c0818c20f91f101ee837`。
- Prompt 改动：规划仅提供中文；按要求同义英译。下面是实际提交的全部英文，不是规划中不存在的“英文原文”。

实际提交的完整 prompt：

```text
Use this reference image as the basis for the edit. Change only one thing:
make the wireless transmission lines from the sensors to the gateway thicker
orange short-dashed lines with small wave marks.

The following must remain unchanged, item by item:
- The side view of the twin-pylon cable-stayed bridge; the positions, heights
  and shapes of both pylons.
- All 16 stay cables: 4 on the left and 4 on the right of each pylon, all
  connecting a pylon to the deck; their positions and angles.
- The positions, shapes and colors of all 12 sensors: 3 blue squares on the
  main-span deck; 1 blue square at the middle of each of the two longest
  outer cables; 2 green rectangles under the deck; the anemometer on top of
  the left pylon; the GNSS antenna on top of the right pylon; the thermometer
  on the left side span; and 2 purple squares at the deck ends.
- The positions of the gateway, cloud, 3 processing boxes inside the cloud,
  and operator terminal; the orange upload arrow and the red alert arrow.
- Do not add any new objects, new lines or text.

If you cannot make the edit without changing anything else, leave the
original image unchanged.
```

看图核验：

1. 教学目的：展示回到 V2 并附保留清单的实际修改结果；没有经过 V3，也没有声称 V3 出现过结构破坏。
2. 提示词来源：规划没有提供 V4 英文原文，只要求“英文版同义改写，保留逐项清单”；本次据规划中文逐项英译，未额外要求修正布局或温度计，以遵守“只改一件事”。
3. 目标修改：无线线改为更粗橙色短虚线，节点旁保留波纹；线型比 V2 更醒目，属于完成局部修改。没有观察到新的结构连带变化。
4. F1 桥型：两塔斜拉桥侧视，无主缆/竖吊杆，目视通过。
5. F2 拉索：按走向 4+4+4+4=16，与 V2 相同；图标附近仍有遮挡留空，不能把每条连续连接的严格验收标为完全通过。
6. F3 传感器：按类别 3+2+2+1+1+1+2=12，主要位置、图形和配色目视保持；未精测所有同类色值；图标过小问题没有修改。
7. F4 关系：L1 橙色短虚线+波纹、L2 网关→云、L3 三框间箭头、L4 末框→终端均在；未见禁画直连箭头。但云在下方、温度计也红色的偏差仍在，因此关系/用色总体验收不通过。
8. F5 灰度：已生成并实际查看独立灰度核验副本；通信线为粗虚线，拉索为细实线，数字预览中可区分。未进行印刷灰度打样。
9. F6 文字：底图无可见文字、字母、数字或伪文字；标签未制作，逐字比对不属于此次底图任务。
10. F7 最终尺寸：沿用 V2 的小蓝方块，约 1.44–1.80 mm（160 mm 全图宽换算），小于 2 mm；未制作带字终稿，未检验 6 pt 字号，未做实体打印。
11. F8 与 V2 对照：主要对象数量与位置目视未见新的意外变化；V2 原有缺陷仍未排除，因此不能把此图标为全图恢复合格。
12. F9 图注与 F10 同行签字：本任务仅生成底图，未制作/修改中英图注、未有结构工程同行签字；不得声称已经通过。
13. 其他画面约束：底部留白保留，无车辆、人物、城市、图表、裂缝或卫星；存在渐变，原生尺寸仍为 1774×887。
14. 核验结论：局部编辑保留主要对象，但终稿验收未通过。未触发“两次出现连带变化”条件，故未启动无链路底图/TikZ 替代路线；未执行可选 V5。

## 后续正文/排版必须据实调整（本任务没有修改正文）

- FIG ch11-03 的规划图注当前宣称全部通过，与实测不符。需说明“候选参考图、仍有明确缺陷”，或另立任务取得真正通过验收的基准后重做后续链条。
- FIG ch11-04 应写：“三次独立参考图修改均完成无线线型调整，未观察到明显结构连带变化，仍需整图复核。”不能写成第 N 次少了一根索/消失 GNSS。若用第 7 章作主要反例，须按其原记录核对，这不属于本任务。
- FIG ch11-06 只能说明保留清单后的局部修改结果；不得写“已修复全部错误”“终稿核验通过”或“已经领域同行确认”。
- 版本树中本次 V3 不应标“少索/少传感器”；V4 分支事实是从同一候选 V2 重新修改。不能把规划中的预期剧情写成发生过的事实。
- 目前没有有效依据把底图标为 F1–F10 全通过；无中英终稿、无同行签字。输出原生大小也需要在后续制作说明中保留。

## 实测终端输出

以下为执行本任务时保存的目录快照；同目录的其他 kind 文件由其他流程产生，本任务未处理。

命令（通过 Python subprocess 设置 15 秒超时）：

```text
ls -l figures/ch11/
```

实测输出：

```text
total 37848
-rw-r--r--@ 1 zeroone  staff     2239 Oct 29 16:09 ch11-01-three-levels-en.tex
-rw-r--r--@ 1 zeroone  staff     2173 Oct 29 16:09 ch11-01-three-levels-zh.tex
-rw-r--r--@ 1 zeroone  staff  2390328 Oct 29 16:06 ch11-02-v1-vague.png
-rw-r--r--@ 1 zeroone  staff  1245145 Oct 29 16:07 ch11-03-v2-brief-alt1.png
-rw-r--r--@ 1 zeroone  staff  1236063 Oct 29 16:08 ch11-03-v2-brief-alt2.png
-rw-r--r--@ 1 zeroone  staff  1245807 Oct 29 16:08 ch11-03-v2-brief.png
-rw-r--r--@ 1 zeroone  staff  1583277 Oct 29 16:10 ch11-04-v3-collateral-alt1.png
-rw-r--r--@ 1 zeroone  staff  1596165 Oct 29 16:11 ch11-04-v3-collateral-alt2.png
-rw-r--r--@ 1 zeroone  staff  1588813 Oct 29 16:09 ch11-04-v3-collateral.png
-rw-r--r--@ 1 zeroone  staff   540533 Oct 29 16:10 ch11-05-diff-and-count-en.pdf
-rw-r--r--@ 1 zeroone  staff   814262 Oct 29 16:10 ch11-05-diff-and-count-en.png
-rw-r--r--@ 1 zeroone  staff   655976 Oct 29 16:09 ch11-05-diff-and-count-zh.pdf
-rw-r--r--@ 1 zeroone  staff   832334 Oct 29 16:09 ch11-05-diff-and-count-zh.png
-rw-r--r--@ 1 zeroone  staff  1593124 Oct 29 16:11 ch11-06-v4-recovered.png
-rw-r--r--@ 1 zeroone  staff     1782 Oct 29 16:08 ch11-07-ch07-collateral-en.tex
-rw-r--r--@ 1 zeroone  staff     1783 Oct 29 16:08 ch11-07-ch07-collateral-zh.tex
-rw-r--r--@ 1 zeroone  staff  1291215 Oct 29 16:06 ch11-07a-ch07-v2.png
-rw-r--r--@ 1 zeroone  staff  1300319 Oct 29 16:06 ch11-07b-ch07-v3-alt1.png
-rw-r--r--@ 1 zeroone  staff  1294239 Oct 29 16:06 ch11-07c-ch07-v3.png
-rw-r--r--@ 1 zeroone  staff     2615 Oct 29 16:09 ch11-08-version-tree-en.tex
-rw-r--r--@ 1 zeroone  staff     2624 Oct 29 16:09 ch11-08-version-tree-zh.tex
```

Pillow 读取原始 PNG 的实测尺寸（未重采样）：

```text
ch11-02-v1-vague.png: 1774 x 887 px; aspect = 2:1; bytes = 2390328
ch11-03-v2-brief-alt1.png: 1774 x 887 px; aspect = 2:1; bytes = 1245145
ch11-03-v2-brief.png: 1774 x 887 px; aspect = 2:1; bytes = 1245807
ch11-03-v2-brief-alt2.png: 1774 x 887 px; aspect = 2:1; bytes = 1236063
ch11-04-v3-collateral.png: 1774 x 887 px; aspect = 2:1; bytes = 1588813
ch11-04-v3-collateral-alt1.png: 1774 x 887 px; aspect = 2:1; bytes = 1583277
ch11-04-v3-collateral-alt2.png: 1774 x 887 px; aspect = 2:1; bytes = 1596165
ch11-06-v4-recovered.png: 1774 x 887 px; aspect = 2:1; bytes = 1593124
```

原图复制一致性与 prompt 一致性核验另见 `verification.txt`。

