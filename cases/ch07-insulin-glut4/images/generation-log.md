# 第7章 GLUT4 机制图：图像生成与实测核验记录

日期：2026-10-29。执行与目视核验：Codex。具体图像模型：**不知道（内置工具未返回）**。

## 交付状态

已生成8个指定主文件及7个备选稿，共15张PNG。B-2复用 `v3-revised.png`，未另生成。每版均未超过3次生成。**文件已交付，但不能判定全部符合终稿要求**：所有16:9图实际为1672×941，未达宽≥2400；V2–V4仍有R5催化连接/空心头、T端贴合、部分空间与留白偏差。V4应作为待修底图，不应标成已通过13条关系和同行复核的终稿。

主要偏差：V0第3次有双T但流动线仍是短虚线，且少了原定的下方激活输入；V1自然出现装饰、结构和线型错误，却未出现明显伪文字；A1/A2主要箭头教学目的达成，但有轻微渐变和线端间隙；B1以V3参考后保留主要布局，但R5头型也发生变化，并非完全只改颜色。

## 输入、方法与范围

- 任务书：`(local scratch file)`。
- 脚本：`../case-plan.md`；已读取第3、4节、2.2节R1–R13和第6节核验要求。
- 脚本生成前后SHA-256均为 `1974cdafef04180d72da2c8e1b1f111a1adda5208560f318fbaff050c7c4e834`，未修改。
- 实际工具：`image_gen.imagegen`（内置）；未使用SciDraw服务或外部图像API。模型名不知道，不以工具名称推断模型。
- 所有请求均 `transparent_background=false`。无参考的请求省略参考参数；有参考的请求使用 `referenced_image_paths`，参考图已先查看。未使用 `num_last_images_to_include`。
- V3首次使用脚本允许的完整重生成方式；失败后用选定V2作参考，仍使用完整英文V3提示词。V4执行方案A，保留 `[ARROWS]` 全段；第2、3次以V3为参考。B1第2次以V3为参考，以减少结构变化。
- 每张图均逐字保留脚本英文代码块（含原换行）。接口没有size参数，因此统一在末尾追加仅画布/分辨率设置：16:9优先请求3840×2160，A组4:3优先请求3200×2400，并要求最大可用原生尺寸。实际工具未按该尺寸返回，也未说明尺寸上限，不能声称已证明其最大能力。
- V0第3次、V4第3次额外追加了针对失败点的修复段；修改原因与**实际完整提示词**逐图记录在下方。没有删改或缩写原脚本英文。
- 不对主交付图进行重采样、人工补画、去字或拼接。所有PNG均原样复制生成文件。200%局部和灰度图仅在内存中产生供检查，没有替换交付文件，也未保存为新增图像。
- 手动创建文件限于本目录；内置工具自动缓存于 `$CODEX_HOME/generated_images/`，逐图保留其实际来源路径。未改case-plan、未commit/push、未启动子agent。
- 后续文件操作设30秒闹钟，外部核验命令另设超时；图像请求以120秒工具等待窗口调用。工具等待窗口不是服务端生成超时承诺；本次调用均已完成，没有留待后台的任务。

## 文件、次数与尺寸

| 文件 | 生成次数序号 | 参考图 | 原生像素 | 选择 |
|---|---:|---|---|---|
| `v0-sketch-alt1.png` | 1 / 3 | 无 | 1672×941 | 落选保留 |
| `v0-sketch-alt2.png` | 2 / 3 | 无 | 1672×941 | 落选保留 |
| `v0-sketch.png` | 3 / 3 | 无 | 1672×941 | 选用 |
| `v1-vague.png` | 1 / 1 | 无 | 1672×941 | 选用 |
| `v2-brief-alt1.png` | 1 / 2 | 无 | 1672×941 | 落选保留 |
| `v2-brief.png` | 2 / 2 | 无 | 1672×941 | 选用 |
| `v3-revised-alt1.png` | 1 / 2 | 无 | 1672×941 | 落选保留 |
| `v3-revised.png` | 2 / 2 | `v2-brief.png` | 1672×941 | 选用 |
| `v4-base-alt1.png` | 1 / 3 | 无 | 1672×941 | 落选保留 |
| `v4-base-alt2.png` | 2 / 3 | `v3-revised.png` | 1672×941 | 落选保留 |
| `v4-base.png` | 3 / 3 | `v3-revised.png` | 1672×941 | 选用 |
| `cmp-a1-mixed-arrows.png` | 1 / 1 | 无 | 1448×1086 | 选用 |
| `cmp-a2-unified-arrows.png` | 1 / 1 | 无 | 1448×1086 | 选用 |
| `cmp-b1-too-many-colors-alt1.png` | 1 / 2 | 无 | 1672×941 | 落选保留 |
| `cmp-b1-too-many-colors.png` | 2 / 2 | `v3-revised.png` | 1672×941 | 选用 |

16:9实际比值1672/941≈1.7768，为近似16:9；A组1448/1086=4/3。1672px图在174mm宽时等效244.07ppi；A组在80mm宽时等效459.74ppi。没有把增加DPI标签或插值放大当作新增原生细节。

实际 `ls -l`、逐图尺寸、PNG解码、源图复制哈希和提示词原文保留检查的完整输出见 [`verification.txt`](verification.txt)。完整机器记录见 [`generation-records.json`](generation-records.json)、[`prompts.json`](prompts.json)、[`verification-metrics.json`](verification-metrics.json)。

## 逐图生成与目视核验

无字图的分子身份是按脚本规定的位置、形状和颜色推定，不是OCR识别；标签尚未叠加，不能宣称其语义已由标签独立验证。下列结论是对本脚本的图像核验，不是领域同行签字。

### v0-sketch-alt1.png

- 工具：`image_gen.imagegen`（内置）。具体模型：不知道。
- 第1次生成；本版共3次；落选保留。
- 参考图：无（新生成）。
- 像素：1672×941；文件字节：2605113；SHA-256：`e4f5b9a1c1bacbc2727a2a652ce1b22f78082f04056164206b9179c837ac4281`。
- 自动缓存原文件：`codex-output/exec-31763f22-a4c0-4baa-bf9d-ec2732215e1c.png`。
- 提示词改动：原脚本英文逐字完整保留；仅追加上述画布/最大原生分辨率设置。

目视结论：无文字；铅笔纸纹、三分区、底部留白和左到右五团块均有。仅一条T形端，右下抑制节点与主链断开，Rab小珠缺失。葡萄糖线为虚线，止于膜上方而未穿膜。配体未直接接触受体。失败稿保留。

| 脚本检查项 | 实测结论 |
|---|---|
| 分区 | 水平双线膜在上方约1/5，胞外/膜/胞质可辨；铅笔、纸纹、涂擦痕符合模拟草图。 |
| 主链 | 左侧跨膜受体，膜下左到右5团块、弧形连线及第四团块下方向上输入可见。 |
| 双抑制 | 不通过：只有一条T形线，右下节点和主链断开；Rab表面小珠未明确表达。 |
| 转位和流动 | 有向上虚线，但葡萄糖线也是虚线并止于膜上方，没有完整跨膜点线。 |
| 文字 | 无任何文字、数字或伪字母；不把纸纹当文字。 |
| 留白 | 底部十分之一空白，未见手、笔或纸上物件。 |
| 处置 | AI模拟草图，非真实手稿；保留作失败稿，已重试。 |

**实际提交的完整提示词（逐字，包含追加内容）：**

```text
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

Output settings only: landscape 16:9; render at the maximum native resolution available, preferably 3840 x 2160 pixels. Do not render these output settings as image text.
```

### v0-sketch-alt2.png

- 工具：`image_gen.imagegen`（内置）。具体模型：不知道。
- 第2次生成；本版共3次；落选保留。
- 参考图：无（新生成）。
- 像素：1672×941；文件字节：2776574；SHA-256：`43da5d3f168b6d10f87fa9e2ef8c2ec656b1454d488b4853eb98f97fdb65abcc`。
- 自动缓存原文件：`codex-output/exec-f87ae8c4-bfe2-4af8-bc97-edfe20314a41.png`。
- 提示词改动：原脚本英文逐字完整保留；仅追加上述画布/最大原生分辨率设置。

目视结论：无文字；铅笔风格与三分区、五团块、下方额外团块及底部留白均符合。只有一条T形线，且终点未接到明确Rab珠；右下团块与主信号链断开；转位虚线具实心头，葡萄糖虚线止于膜上方未穿膜，配体未接触。

| 脚本检查项 | 实测结论 |
|---|---|
| 分区 | 水平双线膜在上方约1/5，胞外/膜/胞质可辨；铅笔、纸纹、涂擦痕符合模拟草图。 |
| 主链 | 左侧跨膜受体，膜下左到右5团块、弧形连线及第四团块下方向上输入可见。 |
| 双抑制 | 不通过：只有一条T形线，右下节点和主链断开；Rab表面小珠未明确表达。 |
| 转位和流动 | 有向上虚线，但葡萄糖线也是虚线并止于膜上方，没有完整跨膜点线。 |
| 文字 | 无任何文字、数字或伪字母；不把纸纹当文字。 |
| 留白 | 底部十分之一空白，未见手、笔或纸上物件。 |
| 处置 | AI模拟草图，非真实手稿；保留作失败稿，已重试。 |

**实际提交的完整提示词（逐字，包含追加内容）：**

```text
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

Output settings only: landscape 16:9; render at the maximum native resolution available, preferably 3840 x 2160 pixels. Do not render these output settings as image text.
```

### v0-sketch.png

- 工具：`image_gen.imagegen`（内置）。具体模型：不知道。
- 第3次生成；本版共3次；选用。
- 参考图：无（新生成）。
- 像素：1672×941；文件字节：2412444；SHA-256：`67c463fda097480a00e59fc5adaf2ca1e7fb7c69823386c649385b9e25526258`。
- 自动缓存原文件：`codex-output/exec-1133a8e8-4968-429e-98ae-34ef06e359ab.png`。
- 提示词改动：原脚本英文逐字完整保留；前两次都只画一条T形线且下游断开；保留脚本完整英文原文，追加具体修复两条串联T线、Rab接触与点线穿膜要求。

目视结论：选用。模拟铅笔草图，非手稿扫描。无文字数字；质膜约上方1/5、左侧受体、膜下五团块、三囊泡与底部留白均有；两条T端串联已出现，Rab小珠在囊泡表面。转位为向上虚线，葡萄糖线终于穿膜向下但仍是短虚线而非点线。胰岛素珠仍与受体微分离；原提示词要求的第四团块下方另一个向上激活输入被下游T线节点替代，因此草图仍不完全符合原脚本。

| 脚本检查项 | 实测结论 |
|---|---|
| 分区 | 上方约1/5处有双线膜，三分区明确。 |
| 主链 | 左侧受体与膜下5个团块沿左到右排列，第二至第三附近有弧形箭头。 |
| 双抑制 | 通过主要目的：两条T端串联，从第四主团块至右下团块、再至囊泡表面小珠。 |
| 转位和流动 | 向上虚线转位和穿膜向下流动存在，但流动仍为短虚线而非点线；两种移动线区分不足。 |
| 其他偏差 | 配体与受体仍有小间隙；第四团块下方原定的向上激活输入被下游抑制节点替代，未保住所有草图元素。 |
| 文字 | 无文字、数字、标注或标题；单色铅笔。 |
| 留白和来源 | 底部十分之一空白，AI模拟草图，非手稿扫描。 |
| 处置 | 第3次在2条T线方面明显优于前两次，故选用；已达重试上限。 |

**实际提交的完整提示词（逐字，包含追加内容）：**

```text
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

Output settings only: landscape 16:9; render at the maximum native resolution available, preferably 3840 x 2160 pixels. Do not render these output settings as image text.

Targeted correction after two unsuccessful attempts: the lower-right pathway must be connected to the fourth main-chain blob. Draw exactly TWO consecutive inhibitory connections, each with a clear perpendicular T-bar: fourth main-chain blob to lower-right blob, then lower-right blob to a tiny bead touching the vesicle surface. Do not leave the lower-right blob isolated. The glucose-flow line must be DOTTED, not dashed, and continue through the membrane rectangle into the cytoplasm, with its arrowhead below the membrane. Keep the vesicle translocation line DASHED and upward. The extracellular dot cluster must touch the receptor. Preserve the pencil-only, completely text-free planning-sketch appearance.
```

### v1-vague.png

- 工具：`image_gen.imagegen`（内置）。具体模型：不知道。
- 第1次生成；本版共1次；选用。
- 参考图：无（新生成）。
- 像素：1672×941；文件字节：2658302；SHA-256：`ab39c44c4037c5cf0eac8465853702525d30a9515cfe2194f320f110b8c08c56`。
- 自动缓存原文件：`codex-output/exec-2020c1b6-b8f9-4cec-8c6d-c2a6fcb6ee5b.png`。
- 提示词改动：原脚本英文逐字完整保留；仅追加上述画布/最大原生分辨率设置。

目视结论：自然生成3D光泽、渐变、发光P标记、细胞核、内质网、高尔基体、微管、肌动蛋白等额外对象；明显可读英文，大多拼写正常，未发现明确伪文字，未人为制造拼写错误。缺mTORC2；Akt到AS160被画成激活；Rab游离未结合囊泡；PI3K/PDK1/Akt离膜较远；各种激活与移动同用实心箭头，图例缺失。

| 脚本检查项 | 实测结论 |
|---|---|
| 13条关系 | 逐条表已填写：mTORC2缺失，Akt→AS160激活错误，招募/转位等线型未区分。 |
| 文字 | 标签大多是正常可读英文；未发现明确伪文字或明显拼写错，未为制造失败强行增加错字。 |
| 装饰与3D | 有光泽、渐变、发光P、景深、复杂膜与蛋白立体材质，符合自然出现的过度装饰问题。 |
| 额外对象 | 细胞核、内质网、高尔基体、微管、肌动蛋白、SNARE描述、多个膜GLUT4与额外囊泡；未见明确MAPK分支。 |
| 空间与计数 | 胰岛素在胞外、受体跨膜，未出现脚本举例的全部空间错误；PI3K/PDK1/Akt远离膜，Rab未附囊泡，膜GLUT4明显多于1个。 |
| 箭头 | 多类关系混用白实心箭头，AS160→Rab虽有T端，但Akt→AS160仍用激活；未见清楚的Akt直接到GLUT4捷径。 |
| 印刷 | 复杂背景和较小英文使缩至174mm时多处标签难读；本次未实体打印，不能将标签字号当作矢量排版字号精确验收。 |
| 处置 | 采用唯一一次自然生成；可展示自然结构错误与装饰问题，不适合声称展示了明显伪文字。 |

**2.2节 R1–R13逐条核验**（“部分正确”不能按完整通过处理）：

| 关系 | 图中是否正确体现 | 实际看见的证据与偏差 |
|---|---|---|
| R1 | 错误（按本案例规范） | 胞外胰岛素至受体使用箭头而非直接接触。 |
| R2 | 正确 | 受体胞内多处P标记表达磷酸化；V1允许文字。 |
| R3 | 正确 | 受体至IRS-1箭头及IRS-1磷酸化标记可见。 |
| R4 | 无法充分判断 | IRS-1与PI3K重叠相邻，缺少独立清楚的激活箭头。 |
| R5 | 部分正确 | 可读PIP2与PIP3及向右转化箭头存在，但PI3K指向PIP2，未连接转化弧中点。 |
| R6 | 错误 | PIP3用箭头连接PDK1/Akt，两者位于膜下较远处，不是贴膜接触。 |
| R7 | 正确 | PDK1有弯曲实心箭头指向Akt。 |
| R8 | 缺失 | 未见mTORC2及其向Akt的激活箭头。 |
| R9 | 错误 | Akt到AS160画成实心激活箭头，缺少抑制T端。 |
| R10 | 部分正确 | AS160到Rab有T端，但Rab游离于胞质、未结合GSV表面。 |
| R11 | 部分正确／线型错 | 囊泡移动向膜可追溯，但与信号相同为白色实线实心箭头，Rab促进转位的连接不清楚。 |
| R12 | 部分正确 | 膜凹陷融合和膜上多个GLUT4可见；并非要求的单个膜GLUT4和唯一粗虚线终点。 |
| R13 | 部分正确 | 摄取大箭头朝胞内且有内外葡萄糖，但没有规定的穿GLUT4点线。 |

**实际提交的完整提示词（逐字，包含追加内容）：**

```text
Make a beautiful, professional scientific illustration of insulin signaling and
GLUT4 translocation for a top journal.

Output settings only: landscape 16:9; render at the maximum native resolution available, preferably 3840 x 2160 pixels. Do not render these output settings as image text.
```

### v2-brief-alt1.png

- 工具：`image_gen.imagegen`（内置）。具体模型：不知道。
- 第1次生成；本版共2次；落选保留。
- 参考图：无（新生成）。
- 像素：1672×941；文件字节：1308336；SHA-256：`6edbf96d765920fff45b60033d43980d848c396c5aa2ec566152d0d0ea1819a6`。
- 自动缓存原文件：`codex-output/exec-bf89649b-0169-49db-91fb-e7f7283cef9f.png`。
- 提示词改动：原脚本英文逐字完整保留；仅追加上述画布/最大原生分辨率设置。

目视结论：无文字。受体、IRS-1、PI3K、PDK1、Akt、mTORC2、AS160与3个GSV、膜GLUT4齐全，但Rab样灰蓝珠2个。关键错误：指向AS160的T形线来自mTORC2而非Akt；R5弧线实心头且PI3K接触线成为指向PI3K的箭头；微渐变；转位箭头端点接近膜GLUT4但有间隙。

| 脚本检查项 | 实测结论 |
|---|---|
| 对象 | 主要对象齐；Rab样灰蓝珠有2个，胞外4葡萄糖且胞内另有1葡萄糖；GSV 3个各1 GLUT4。 |
| 关系与线型 | R3/R4/R7/R8存在；两条T线中第一条错误地由mTORC2指向AS160；催化线有反向实心头。不能作为结构正确稿。 |
| 禁止项 | 无Akt直达GSV捷径、无mTORC2上游线、无细胞器/骨架/数据。 |
| 布局 | 胞外/膜/胞质清楚、主路径大致左到右，GSV偏大并右移；底部12%为空。 |
| 文字 | 未见任何文字或伪文字。 |
| 风格 | 蓝色不统一、轻微渐变、两颗Rab制造对象歧义；符合部分预期问题但科学错误需重试。 |
| 处置 | 保留失败稿；被第2次生成替代。 |

**2.2节 R1–R13逐条核验**（“部分正确”不能按完整通过处理）：

| 关系 | 图中是否正确体现 | 实际看见的证据与偏差 |
|---|---|---|
| R1 | 正确 | 3颗胰岛素珠位于胞外并接触受体胞外臂；无结合箭头。 |
| R2 | 正确 | 受体胞内两臂各有一个琥珀圆点，无P字母。 |
| R3 | 正确 | 受体向右下IRS-1画实线实心头，IRS-1有一个磷酸化点。 |
| R4 | 正确 | IRS-1向右上PI3K画实线实心头，顺序可辨。 |
| R5 | 错误 | 转化弧使用实心头；连接PI3K的短线成为从膜侧指向PI3K的箭头，未表达PI3K接触弧中点的催化关系。 |
| R6 | 部分正确／招募位置不够明确 | PDK1与Akt的上缘接触膜内叶，未画PIP3招募箭头；PDK1靠近PIP3，Akt与特殊PIP3头基相隔一段距离，不能清楚看到两者都在PIP3处。 |
| R7 | 正确 | PDK1向右指向Akt，实线实心头；Akt有两个磷酸化点。 |
| R8 | 正确 | Akt下方的三叶mTORC2向上指向Akt；没有指向mTORC2的上游箭头。 |
| R9 | 错误 | 指向AS160的T形线来自Akt下方mTORC2，而不是Akt；Akt到AS160缺失。 |
| R10 | 部分正确／对象重复 | AS160的T端朝右上灰蓝珠，但囊泡旁另有第二颗灰蓝珠；Rab身份与计数出现歧义。 |
| R11 | 基本正确 | 橙色粗虚线由GSV簇近旁向上弯至膜侧，方向与移动语义可辨；起点并未紧贴囊泡轮廓。 |
| R12 | 部分正确／融合终点未贴合 | 膜上及3个囊泡膜上均有同形GLUT4；转位头朝膜GLUT4，但与其下缘仍有间隙，融合以接近关系表示，未严格连至GLUT4。 |
| R13 | 正确 | 深橙点线沿膜GLUT4轴从胞外到胞内，箭头朝下；膜蛋白遮挡中段，不另加错误方向。 |

**实际提交的完整提示词（逐字，包含追加内容）：**

```text
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

Output settings only: landscape 16:9; render at the maximum native resolution available, preferably 3840 x 2160 pixels. Do not render these output settings as image text.
```

### v2-brief.png

- 工具：`image_gen.imagegen`（内置）。具体模型：不知道。
- 第2次生成；本版共2次；选用。
- 参考图：无（新生成）。
- 像素：1672×941；文件字节：1291215；SHA-256：`e015f1063cc3a71de4449550943637b12de3d9e240cb263eadc365e4a11192f0`。
- 自动缓存原文件：`codex-output/exec-6077c99d-d9b5-4f23-a7ea-d5c8f935c02f.png`。
- 提示词改动：原脚本英文逐字完整保留；仅追加上述画布/最大原生分辨率设置。

目视结论：选用。无文字；对象计数基本符合，3个胰岛素珠、4个胞外葡萄糖、3个GSV各1个GLUT4、Rab 1个。R9/R10均为正确串联T形线，mTORC2仅有向Akt箭头。R5为空心三角头而非严格开口V，PI3K短接线靠弧线起点而非中点；PDK1/Akt贴膜但Akt与PIP3聚集点较远；T端与目标有窄间隙，转位头与GLUT4有窄间隙；填色仍带轻微明暗。

| 脚本检查项 | 实测结论 |
|---|---|
| 对象计数 | 受体、IRS-1、PI3K、PDK1、Akt、mTORC2、AS160、Rab、GSV簇、膜GLUT4各1；GSV簇含3个囊泡，各有1个膜GLUT4；胰岛素3珠、胞外葡萄糖4个。 |
| 箭头与禁止项 | 4条激活、2条抑制、1条酶促弧、1条转位、1条物质流动，共5类；未见Akt/受体直达GSV捷径、mTORC2上游线、细胞器、骨架或数据。R5及部分线端仍有偏差，详见逐条关系表。 |
| 布局 | 三分区及左→右→右上阅读路径清楚；膜约y=0.20–0.28。Rab/GSV整体比脚本靠右/靠上，mTORC2约y=0.47而非0.57，部分偏移超过0.05；不能声称逐坐标通过。 |
| 文字 | 全图目视未见文字、伪文字、数字、水印；琥珀圆点不是字母P。 |
| 风格与层级 | 蓝/灰蓝/橙主色系、灰膜、琥珀磷酸化点；同类蓝色接近但非严格一致指定色值。蛋白与GSV、小分子层级可辨，仍有轻微渐变。脚本配色中的琥珀点按允许项保留。 |
| 留白 | 底部12%为空；多数标签可放置，但对象四周并未各留一个蛋白宽，需按实际图调整标签。 |
| 印刷与标签 | 原生1672×941，174mm宽等效244.07ppi，低于300ppi且不满足宽≥2400。未生成标签层，故6–8pt字号、17个标签、图例和中英文底图哈希一致性属于后续排版检查，不能勾选已完成。 |

**2.2节 R1–R13逐条核验**（“部分正确”不能按完整通过处理）：

| 关系 | 图中是否正确体现 | 实际看见的证据与偏差 |
|---|---|---|
| R1 | 正确 | 3颗胰岛素珠位于胞外并接触受体胞外臂；无结合箭头。 |
| R2 | 正确 | 受体胞内两臂各有一个琥珀圆点，无P字母。 |
| R3 | 正确 | 受体向右下IRS-1画实线实心头，IRS-1有一个磷酸化点。 |
| R4 | 正确 | IRS-1向右上PI3K画实线实心头，顺序可辨。 |
| R5 | 部分正确／线型及连接不符 | PIP2至PIP3的细弧方向向右；头为闭合空心三角而非开放V，PI3K短线接在弧线左端附近而非中点，且短线与蛋白间有小间隙。 |
| R6 | 部分正确／招募位置不够明确 | PDK1与Akt的上缘接触膜内叶，未画PIP3招募箭头；PDK1靠近PIP3，Akt与特殊PIP3头基相隔一段距离，不能清楚看到两者都在PIP3处。 |
| R7 | 正确 | PDK1向右指向Akt，实线实心头；Akt有两个磷酸化点。 |
| R8 | 正确 | Akt下方的三叶mTORC2向上指向Akt；没有指向mTORC2的上游箭头。 |
| R9 | 部分正确／端点不贴靶标 | Akt至AS160的方向与T形线正确，AS160有磷酸化点；T端与AS160轮廓有窄白隙，未严格满足贴靶标。 |
| R10 | 部分正确／端点不贴靶标 | AS160至Rab为T形抑制，Rab位于上方囊泡边缘；T端与Rab轮廓有窄白隙。 |
| R11 | 基本正确 | 橙色粗虚线由GSV簇近旁向上弯至膜侧，方向与移动语义可辨；起点并未紧贴囊泡轮廓。 |
| R12 | 部分正确／融合终点未贴合 | 膜上及3个囊泡膜上均有同形GLUT4；转位头朝膜GLUT4，但与其下缘仍有间隙，融合以接近关系表示，未严格连至GLUT4。 |
| R13 | 正确 | 深橙点线沿膜GLUT4轴从胞外到胞内，箭头朝下；膜蛋白遮挡中段，不另加错误方向。 |

**实际提交的完整提示词（逐字，包含追加内容）：**

```text
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

Output settings only: landscape 16:9; render at the maximum native resolution available, preferably 3840 x 2160 pixels. Do not render these output settings as image text.
```

### v3-revised-alt1.png

- 工具：`image_gen.imagegen`（内置）。具体模型：不知道。
- 第1次生成；本版共2次；落选保留。
- 参考图：无（新生成）。
- 像素：1672×941；文件字节：1300319；SHA-256：`6c850ef6b0fb88541a1db65fc6c18fe585dc298d62e337bd9fc02617f45c5a84`。
- 自动缓存原文件：`codex-output/exec-a42ed59f-9418-4544-ae0c-12a8d4ad6bac.png`。
- 提示词改动：原脚本英文逐字完整保留；仅追加上述画布/最大原生分辨率设置。

目视结论：无文字；两条T线拓扑正确，转位/流动线型可分辨，色彩克制。与V2相比磷酸化圆点全部丢失，胰岛素仅2珠且不接触受体，PDK1/Akt均离膜，增加PI3K→PDK1的未授权激活箭头；Rab过大且与囊泡接触不明确，每囊泡GLUT4由1个增加到多个。不能作为结构合格修订稿。

| 脚本检查项 | 实测结论 |
|---|---|
| 对象 | 各位置主要团块和3个GSV存在，但胰岛素仅2珠、mTORC2变单团块、Rab过大；每囊泡上GLUT4增加为多个，全部磷酸化点丢失。 |
| 关系与线型 | T形抑制主干存在，额外增加PI3K→PDK1激活线；PDK1/Akt离膜，受体未接触配体。详见R表。 |
| 风格 | 颜色克制但仍有轻微明暗；GSV过于复杂，蛋白形状过于相似，不能靠配色掩盖缺项。 |
| 文字 | 无文字、数字或伪字母；没有P标记。 |
| 留白与布局 | 三分区、底部12%留白存在；对象与V2坐标明显漂移，蛋白膜下距离增加。 |
| 对照V2意外变化 | 丢失磷酸化、减少胰岛素珠、增加连线/GLUT4、改变mTORC2形状和Rab大小，均影响科学表达。 |
| 处置 | 保留失败稿，第2次改用V2参考图编辑。 |

**2.2节 R1–R13逐条核验**（“部分正确”不能按完整通过处理）：

| 关系 | 图中是否正确体现 | 实际看见的证据与偏差 |
|---|---|---|
| R1 | 错误 | 仅2颗胰岛素珠且与受体胞外臂有明显白隙，未直接接触。 |
| R2 | 缺失 | 受体胞内磷酸化圆点全部消失。 |
| R3 | 部分正确 | 受体到IRS-1箭头存在，IRS-1磷酸化圆点缺失。 |
| R4 | 正确 | IRS-1向右上PI3K画实线实心头，顺序可辨。 |
| R5 | 部分正确／对象不易区分 | PI3K短线接触弧中点，方向向右；两端均画为相同橙色圆头，PIP2/PIP3结构差别不清，箭头为闭合空心三角。 |
| R6 | 错误 | PDK1与Akt明显离膜，且额外出现PI3K→PDK1实心激活箭头。 |
| R7 | 部分正确 | PDK1→Akt箭头存在，Akt两个磷酸化圆点消失。 |
| R8 | 基本正确 | 下方单个蓝色团块向上指向Akt且无上游线，但mTORC2不再是要求的三圆簇。 |
| R9 | 部分正确 | Akt→AS160为T形线，但AS160磷酸化点缺失且端点留有间隙。 |
| R10 | 部分正确／位置不清 | 第二条T线存在，但Rab画得接近蛋白大小，未明确附在囊泡表面。 |
| R11 | 基本正确 | 橙色粗虚线由GSV簇近旁向上弯至膜侧，方向与移动语义可辨；起点并未紧贴囊泡轮廓。 |
| R12 | 部分正确／融合终点未贴合 | 膜上及3个囊泡膜上均有同形GLUT4；转位头朝膜GLUT4，但与其下缘仍有间隙，融合以接近关系表示，未严格连至GLUT4。 |
| R13 | 正确 | 深橙点线沿膜GLUT4轴从胞外到胞内，箭头朝下；膜蛋白遮挡中段，不另加错误方向。 |

**实际提交的完整提示词（逐字，包含追加内容）：**

```text
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

Output settings only: landscape 16:9; render at the maximum native resolution available, preferably 3840 x 2160 pixels. Do not render these output settings as image text.
```

### v3-revised.png

- 工具：`image_gen.imagegen`（内置）。具体模型：不知道。
- 第2次生成；本版共2次；选用。
- 参考图：`v2-brief.png`（本目录；作为编辑/参考输入）。
- 像素：1672×941；文件字节：1294239；SHA-256：`3708ab7446cbf30599e3c761f399388b527a89fffaa2e07a06746041633db346`。
- 自动缓存原文件：`codex-output/exec-3e2a03be-be2f-4679-a74b-6113a9e4aba6.png`。
- 提示词改动：原脚本英文逐字完整保留；仅追加上述画布/最大原生分辨率设置。

目视结论：选用。使用已查看的V2第2次图作参考，以完整V3英文提示词修订。主要结构与磷酸化标记保留，无文字，无额外箭头，5类线型可辨。配色仍接近V2，蓝色未严格达到#A9C4E0，轻微渐变未消除；R5接点仍非弧中点、空心头为闭合三角；R6虽贴膜但Akt远离PIP3；T端和转位端仍有窄间隙。未实现明显的层级/留白改善。

| 脚本检查项 | 实测结论 |
|---|---|
| 对象计数 | 受体、IRS-1、PI3K、PDK1、Akt、mTORC2、AS160、Rab、GSV簇、膜GLUT4各1；GSV簇含3个囊泡，各有1个膜GLUT4；胰岛素3珠、胞外葡萄糖4个。 |
| 箭头与禁止项 | 4条激活、2条抑制、1条酶促弧、1条转位、1条物质流动，共5类；未见Akt/受体直达GSV捷径、mTORC2上游线、细胞器、骨架或数据。R5及部分线端仍有偏差，详见逐条关系表。 |
| 布局 | 三分区及左→右→右上阅读路径清楚；膜约y=0.20–0.28。Rab/GSV整体比脚本靠右/靠上，mTORC2约y=0.47而非0.57，部分偏移超过0.05；不能声称逐坐标通过。 |
| 文字 | 全图目视未见文字、伪文字、数字、水印；琥珀圆点不是字母P。 |
| 风格与层级 | 蓝/灰蓝/橙主色系、灰膜、琥珀磷酸化点；同类蓝色接近但非严格一致指定色值。蛋白与GSV、小分子层级可辨，仍有轻微渐变。脚本配色中的琥珀点按允许项保留。 |
| 留白 | 底部12%为空；多数标签可放置，但对象四周并未各留一个蛋白宽，需按实际图调整标签。 |
| 印刷与标签 | 原生1672×941，174mm宽等效244.07ppi，低于300ppi且不满足宽≥2400。未生成标签层，故6–8pt字号、17个标签、图例和中英文底图哈希一致性属于后续排版检查，不能勾选已完成。 |
| 对照V2的变化 | 参考图修订保住全部主要结构和磷酸化点；没有首次重生成的额外PI3K→PDK1线。整体与V2很接近，不能夸大配色、大小和留白的改善。 |
| 灰度实测 | 实际转换为灰度后查看：实心激活头、T端、细弧、粗虚线及点线仍能区分，橙色虚线/囊泡边界转灰后偏浅；未做实体打印。 |

**2.2节 R1–R13逐条核验**（“部分正确”不能按完整通过处理）：

| 关系 | 图中是否正确体现 | 实际看见的证据与偏差 |
|---|---|---|
| R1 | 正确 | 3颗胰岛素珠位于胞外并接触受体胞外臂；无结合箭头。 |
| R2 | 正确 | 受体胞内两臂各有一个琥珀圆点，无P字母。 |
| R3 | 正确 | 受体向右下IRS-1画实线实心头，IRS-1有一个磷酸化点。 |
| R4 | 正确 | IRS-1向右上PI3K画实线实心头，顺序可辨。 |
| R5 | 部分正确／线型及连接不符 | PIP2至PIP3的细弧方向向右；头为闭合空心三角而非开放V，PI3K短线接在弧线左端附近而非中点，且短线与蛋白间有小间隙。 |
| R6 | 部分正确／招募位置不够明确 | PDK1与Akt的上缘接触膜内叶，未画PIP3招募箭头；PDK1靠近PIP3，Akt与特殊PIP3头基相隔一段距离，不能清楚看到两者都在PIP3处。 |
| R7 | 正确 | PDK1向右指向Akt，实线实心头；Akt有两个磷酸化点。 |
| R8 | 正确 | Akt下方的三叶mTORC2向上指向Akt；没有指向mTORC2的上游箭头。 |
| R9 | 部分正确／端点不贴靶标 | Akt至AS160的方向与T形线正确，AS160有磷酸化点；T端与AS160轮廓有窄白隙，未严格满足贴靶标。 |
| R10 | 部分正确／端点不贴靶标 | AS160至Rab为T形抑制，Rab位于上方囊泡边缘；T端与Rab轮廓有窄白隙。 |
| R11 | 基本正确 | 橙色粗虚线由GSV簇近旁向上弯至膜侧，方向与移动语义可辨；起点并未紧贴囊泡轮廓。 |
| R12 | 部分正确／融合终点未贴合 | 膜上及3个囊泡膜上均有同形GLUT4；转位头朝膜GLUT4，但与其下缘仍有间隙，融合以接近关系表示，未严格连至GLUT4。 |
| R13 | 正确 | 深橙点线沿膜GLUT4轴从胞外到胞内，箭头朝下；膜蛋白遮挡中段，不另加错误方向。 |

**实际提交的完整提示词（逐字，包含追加内容）：**

```text
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

Output settings only: landscape 16:9; render at the maximum native resolution available, preferably 3840 x 2160 pixels. Do not render these output settings as image text.
```

### v4-base-alt1.png

- 工具：`image_gen.imagegen`（内置）。具体模型：不知道。
- 第1次生成；本版共3次；落选保留。
- 参考图：无（新生成）。
- 像素：1672×941；文件字节：1339241；SHA-256：`dcc4617f68f8044345b67c08938613780a9b27ec13b9bbaa9a89f18bc2dfc8b6`。
- 自动缓存原文件：`codex-output/exec-186d8d21-378a-4a84-bb98-07f48e89bdea.png`。
- 提示词改动：原脚本英文逐字完整保留；仅追加上述画布/最大原生分辨率设置。

目视结论：无文字；3颗胰岛素珠与受体不接触；激活与两条抑制主干存在，磷酸化圆点齐；PIP2→PIP3弧为实心头且PI3K连接短线缺失，PDK1/Akt未贴膜。3个GLUT4被画在囊泡腔内而非囊泡膜，膜上GLUT4与囊泡内图形相似但不能替代正确嵌膜位置；转位/流动两线可辨。终稿不合格。

| 脚本检查项 | 实测结论 |
|---|---|
| 对象 | 主要蛋白1个各在相应区域、胰岛素3珠、葡萄糖4个、GSV 3个与膜GLUT4 1个；但囊泡GLUT4错误地置于腔内。 |
| 关系 | R1不接触、R5缺PI3K催化连接且实心头、R6蛋白不贴膜、R12储存态嵌膜错误。 |
| 线型 | 四激活和双抑制存在；转位粗虚线与葡萄糖点线存在，但催化线语义未按规范。 |
| 文字与禁止项 | 未见文字或伪字母；未见细胞器、数据、Akt直达GSV及mTORC2上游线。 |
| 布局留白 | 膜/胞外/胞质可辨，底部留白有；部分标签位受实际位置偏移影响，不能用原坐标直接叠加。 |
| 风格 | 配色比V2浅但仍有渐变，信号与运输形状较粗；未满足纯平面精确要求。 |
| 处置 | 失败稿保留，后两次以V3为参考修订。 |

**2.2节 R1–R13逐条核验**（“部分正确”不能按完整通过处理）：

| 关系 | 图中是否正确体现 | 实际看见的证据与偏差 |
|---|---|---|
| R1 | 错误 | 3颗胞外胰岛素珠与受体之间有白隙，没有直接接触。 |
| R2 | 正确 | 受体胞内两臂各有一个琥珀圆点，无P字母。 |
| R3 | 正确 | 受体向右下IRS-1画实线实心头，IRS-1有一个磷酸化点。 |
| R4 | 正确 | IRS-1向右上PI3K画实线实心头，顺序可辨。 |
| R5 | 错误／催化连接缺失 | PIP2→PIP3有弧线但头为实心；PI3K到转化弧的短接线缺失。 |
| R6 | 错误 | PDK1与Akt位于膜下空白，均未贴膜内叶。 |
| R7 | 正确 | PDK1向右指向Akt，实线实心头；Akt有两个磷酸化点。 |
| R8 | 正确 | Akt下方的三叶mTORC2向上指向Akt；没有指向mTORC2的上游箭头。 |
| R9 | 部分正确／端点不贴靶标 | Akt至AS160的方向与T形线正确，AS160有磷酸化点；T端与AS160轮廓有窄白隙，未严格满足贴靶标。 |
| R10 | 部分正确／端点不贴靶标 | AS160至Rab为T形抑制，Rab位于上方囊泡边缘；T端与Rab轮廓有窄白隙。 |
| R11 | 基本正确 | 橙色粗虚线由GSV簇近旁向上弯至膜侧，方向与移动语义可辨；起点并未紧贴囊泡轮廓。 |
| R12 | 错误／储存态位置错 | 膜上的GLUT4存在，但3个GSV中的GLUT4画在囊泡腔内，未嵌囊泡膜；不能正确表达膜蛋白转位融合。 |
| R13 | 正确 | 深橙点线沿膜GLUT4轴从胞外到胞内，箭头朝下；膜蛋白遮挡中段，不另加错误方向。 |

**实际提交的完整提示词（逐字，包含追加内容）：**

```text
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

Output settings only: landscape 16:9; render at the maximum native resolution available, preferably 3840 x 2160 pixels. Do not render these output settings as image text.
```

### v4-base-alt2.png

- 工具：`image_gen.imagegen`（内置）。具体模型：不知道。
- 第2次生成；本版共3次；落选保留。
- 参考图：`v3-revised.png`（本目录；作为编辑/参考输入）。
- 像素：1672×941；文件字节：1274903；SHA-256：`75b1fae46f20eebae16d3d358f97fb077c15f2eb29e8d3e60fea64321263ac87`。
- 自动缓存原文件：`codex-output/exec-4fe39d02-3118-4c55-aeb9-2d5b42c465d4.png`。
- 提示词改动：原脚本英文逐字完整保留；仅追加上述画布/最大原生分辨率设置。

目视结论：无文字；参考V3后恢复3个GSV膜上的GLUT4与所有磷酸化标记。主要结构接近V3，仍有R5接点非弧中点、闭合空心三角头、T端间隙、转位终点间隙、微渐变、标签区域占用。颜色仍接近V3，未达到终稿全部验收。

| 脚本检查项 | 实测结论 |
|---|---|
| 对象计数 | 受体、IRS-1、PI3K、PDK1、Akt、mTORC2、AS160、Rab、GSV簇、膜GLUT4各1；GSV簇含3个囊泡，各有1个膜GLUT4；胰岛素3珠、胞外葡萄糖4个。 |
| 箭头与禁止项 | 4条激活、2条抑制、1条酶促弧、1条转位、1条物质流动，共5类；未见Akt/受体直达GSV捷径、mTORC2上游线、细胞器、骨架或数据。R5及部分线端仍有偏差，详见逐条关系表。 |
| 布局 | 三分区及左→右→右上阅读路径清楚；膜约y=0.20–0.28。Rab/GSV整体比脚本靠右/靠上，mTORC2约y=0.47而非0.57，部分偏移超过0.05；不能声称逐坐标通过。 |
| 文字 | 全图目视未见文字、伪文字、数字、水印；琥珀圆点不是字母P。 |
| 风格与层级 | 蓝/灰蓝/橙主色系、灰膜、琥珀磷酸化点；同类蓝色接近但非严格一致指定色值。蛋白与GSV、小分子层级可辨，仍有轻微渐变。脚本配色中的琥珀点按允许项保留。 |
| 留白 | 底部12%为空；多数标签可放置，但对象四周并未各留一个蛋白宽，需按实际图调整标签。 |
| 印刷与标签 | 原生1672×941，174mm宽等效244.07ppi，低于300ppi且不满足宽≥2400。未生成标签层，故6–8pt字号、17个标签、图例和中英文底图哈希一致性属于后续排版检查，不能勾选已完成。 |
| 对照V3的变化 | 参考图编辑后主要内容与V3几乎相同，未解决所要求的标签矩形全部留空，未达到终稿验收。 |

**2.2节 R1–R13逐条核验**（“部分正确”不能按完整通过处理）：

| 关系 | 图中是否正确体现 | 实际看见的证据与偏差 |
|---|---|---|
| R1 | 正确 | 3颗胰岛素珠位于胞外并接触受体胞外臂；无结合箭头。 |
| R2 | 正确 | 受体胞内两臂各有一个琥珀圆点，无P字母。 |
| R3 | 正确 | 受体向右下IRS-1画实线实心头，IRS-1有一个磷酸化点。 |
| R4 | 正确 | IRS-1向右上PI3K画实线实心头，顺序可辨。 |
| R5 | 部分正确／线型及连接不符 | PIP2至PIP3的细弧方向向右；头为闭合空心三角而非开放V，PI3K短线接在弧线左端附近而非中点，且短线与蛋白间有小间隙。 |
| R6 | 部分正确／招募位置不够明确 | PDK1与Akt的上缘接触膜内叶，未画PIP3招募箭头；PDK1靠近PIP3，Akt与特殊PIP3头基相隔一段距离，不能清楚看到两者都在PIP3处。 |
| R7 | 正确 | PDK1向右指向Akt，实线实心头；Akt有两个磷酸化点。 |
| R8 | 正确 | Akt下方的三叶mTORC2向上指向Akt；没有指向mTORC2的上游箭头。 |
| R9 | 部分正确／端点不贴靶标 | Akt至AS160的方向与T形线正确，AS160有磷酸化点；T端与AS160轮廓有窄白隙，未严格满足贴靶标。 |
| R10 | 部分正确／端点不贴靶标 | AS160至Rab为T形抑制，Rab位于上方囊泡边缘；T端与Rab轮廓有窄白隙。 |
| R11 | 基本正确 | 橙色粗虚线由GSV簇近旁向上弯至膜侧，方向与移动语义可辨；起点并未紧贴囊泡轮廓。 |
| R12 | 部分正确／融合终点未贴合 | 膜上及3个囊泡膜上均有同形GLUT4；转位头朝膜GLUT4，但与其下缘仍有间隙，融合以接近关系表示，未严格连至GLUT4。 |
| R13 | 正确 | 深橙点线沿膜GLUT4轴从胞外到胞内，箭头朝下；膜蛋白遮挡中段，不另加错误方向。 |

**实际提交的完整提示词（逐字，包含追加内容）：**

```text
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

Output settings only: landscape 16:9; render at the maximum native resolution available, preferably 3840 x 2160 pixels. Do not render these output settings as image text.
```

### v4-base.png

- 工具：`image_gen.imagegen`（内置）。具体模型：不知道。
- 第3次生成；本版共3次；选用。
- 参考图：`v3-revised.png`（本目录；作为编辑/参考输入）。
- 像素：1672×941；文件字节：1294170；SHA-256：`088030f98a9a151537fe18b880dfe425b52e177fc409b9679779c7c1d45b382e`。
- 自动缓存原文件：`codex-output/exec-3d694651-5b7c-4e25-91d9-43e326c4e4e4.png`。
- 提示词改动：原脚本英文逐字完整保留；前两次存在嵌膜位置或R5/线端/留白错误；保留V4完整方案A提示词，追加针对酶促线中点、开放V头、贴膜、T端贴合、囊泡GLUT4、统一平色和标签留白的可核查修复要求。

目视结论：选用。无文字、伪字母、水印；对象计数与磷酸化标记保留，主干4激活、2抑制、橙虚线及葡萄糖点线均可追溯。颜色比V3略浅，但仍不等于指定色值且有微渐变。R5催化短线仍靠起点、未触PI3K，头仍闭合三角；PDK1/Akt贴膜但Akt与PIP3聚集点相距较远；T端与转位终点存在小间隙；200%复核见Rab底部基本接触GSV边缘。部分标签矩形被对象/线占用。原生1672×941，宽度不达2400。3次上限已用尽，保留为待修底图，不能标注终稿合格。

| 脚本检查项 | 实测结论 |
|---|---|
| 对象计数 | 受体、IRS-1、PI3K、PDK1、Akt、mTORC2、AS160、Rab、GSV簇、膜GLUT4各1；GSV簇含3个囊泡，各有1个膜GLUT4；胰岛素3珠、胞外葡萄糖4个。 |
| 箭头与禁止项 | 4条激活、2条抑制、1条酶促弧、1条转位、1条物质流动，共5类；未见Akt/受体直达GSV捷径、mTORC2上游线、细胞器、骨架或数据。R5及部分线端仍有偏差，详见逐条关系表。 |
| 布局 | 三分区及左→右→右上阅读路径清楚；膜约y=0.20–0.28。Rab/GSV整体比脚本靠右/靠上，mTORC2约y=0.47而非0.57，部分偏移超过0.05；不能声称逐坐标通过。 |
| 文字 | 全图目视未见文字、伪文字、数字、水印；琥珀圆点不是字母P。 |
| 风格与层级 | 蓝/灰蓝/橙主色系、灰膜、琥珀磷酸化点；同类蓝色接近但非严格一致指定色值。蛋白与GSV、小分子层级可辨，仍有轻微渐变。脚本配色中的琥珀点按允许项保留。 |
| 留白 | 底部12%为空；多数标签可放置，但对象四周并未各留一个蛋白宽，需按实际图调整标签。 |
| 印刷与标签 | 原生1672×941，174mm宽等效244.07ppi，低于300ppi且不满足宽≥2400。未生成标签层，故6–8pt字号、17个标签、图例和中英文底图哈希一致性属于后续排版检查，不能勾选已完成。 |
| 200%实测 | 已把左、中、右关键区域在内存中放大到200%逐一查看；无文字伪字母或水印，GLUT4竖条为蛋白结构描线。明确看见R5短线接在弧左端、T端白隙及转位端白隙；Rab底部基本接触囊泡边缘。 |
| 标签区像素检查 | 16个指定矩形中7个检出明显图形像素，最高20.31%；检测条件与各区结果见本日志后表。不是全空白底图。 |
| 灰度实测 | 转换灰度后5类线型仍可辨，转位虚线与囊泡边界偏浅。未作实体打印；未进行领域同行复核签字。 |
| 对照V3的变化 | 蓝色变浅、部分线更细；主要坐标和连接问题仍在。已达3次生成上限，选作待修底图，不是合格终稿。 |

**2.2节 R1–R13逐条核验**（“部分正确”不能按完整通过处理）：

| 关系 | 图中是否正确体现 | 实际看见的证据与偏差 |
|---|---|---|
| R1 | 正确 | 3颗胰岛素珠位于胞外并接触受体胞外臂；无结合箭头。 |
| R2 | 正确 | 受体胞内两臂各有一个琥珀圆点，无P字母。 |
| R3 | 正确 | 受体向右下IRS-1画实线实心头，IRS-1有一个磷酸化点。 |
| R4 | 正确 | IRS-1向右上PI3K画实线实心头，顺序可辨。 |
| R5 | 部分正确／线型及连接不符 | PIP2至PIP3的细弧方向向右；头为闭合空心三角而非开放V，PI3K短线接在弧线左端附近而非中点，且短线与蛋白间有小间隙。 |
| R6 | 部分正确／招募位置不够明确 | PDK1与Akt的上缘接触膜内叶，未画PIP3招募箭头；PDK1靠近PIP3，Akt与特殊PIP3头基相隔一段距离，不能清楚看到两者都在PIP3处。 |
| R7 | 正确 | PDK1向右指向Akt，实线实心头；Akt有两个磷酸化点。 |
| R8 | 正确 | Akt下方的三叶mTORC2向上指向Akt；没有指向mTORC2的上游箭头。 |
| R9 | 部分正确／端点不贴靶标 | Akt至AS160的方向与T形线正确，AS160有磷酸化点；T端与AS160轮廓有窄白隙，未严格满足贴靶标。 |
| R10 | 部分正确／端点不贴靶标 | AS160至Rab为T形抑制，Rab位于上方囊泡边缘；T端与Rab轮廓有窄白隙。 |
| R11 | 基本正确 | 橙色粗虚线由GSV簇近旁向上弯至膜侧，方向与移动语义可辨；起点并未紧贴囊泡轮廓。 |
| R12 | 部分正确／融合终点未贴合 | 膜上及3个囊泡膜上均有同形GLUT4；转位头朝膜GLUT4，但与其下缘仍有间隙，融合以接近关系表示，未严格连至GLUT4。 |
| R13 | 正确 | 深橙点线沿膜GLUT4轴从胞外到胞内，箭头朝下；膜蛋白遮挡中段，不另加错误方向。 |

**实际提交的完整提示词（逐字，包含追加内容）：**

```text
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

Output settings only: landscape 16:9; render at the maximum native resolution available, preferably 3840 x 2160 pixels. Do not render these output settings as image text.

Specific repairs to the reference image, while preserving its objects and the stated signaling topology: visibly recolor all six signaling proteins with a uniform flat #A9C4E0 fill, removing every gradient. Draw the PI3K catalytic stub from PI3K to the MIDDLE of the thin PIP2-to-PIP3 arc, not its start; its arrowhead must be an open V, not a closed triangle. Keep both PDK1 and Akt touching the membrane inner leaflet and make their spatial association with PIP3 clear without introducing another arrow. Both inhibition T-bars must touch their target objects. The Rab bead must touch the upper-left vesicle, and each vesicle GLUT4 must remain embedded in its perimeter, never floating inside its lumen. Connect the dashed translocation arrow endpoint to the plasma-membrane GLUT4. Retain all phosphorylation dots. Keep every reserved label rectangle empty; move object outlines slightly if necessary rather than leaving drawings inside the label areas. No letters, glyphs, numbers or captions may appear. Generate the largest native canvas supported; do not preserve a low-resolution canvas merely because the reference is small.
```

### cmp-a1-mixed-arrows.png

- 工具：`image_gen.imagegen`（内置）。具体模型：不知道。
- 第1次生成；本版共1次；选用。
- 参考图：无（新生成）。
- 像素：1448×1086；文件字节：1245781；SHA-256：`8568953ae8f5d49d08039134ab90b84a67481d3f6f8c2cd782c2d1f382e2fa4c`。
- 自动缓存原文件：`codex-output/exec-0628cafd-8eac-496a-91c1-a7bc4c18e5b8.png`。
- 提示词改动：原脚本英文逐字完整保留；仅追加上述画布/最大原生分辨率设置。

目视结论：无文字；蓝椭圆、灰蓝形、Rab珠、3囊泡、膜GLUT4齐全。恰4条线：粗红弯曲实心箭头、较细绿虚线空心头、黑色实线实心转位箭头、蓝椭圆至膜的紫色双向箭头；均与设计的语义混用一致。微渐变/筒体立体感是额外风格偏差，未发现额外连线。

| 脚本检查项 | 实测结论 |
|---|---|
| 对象 | 灰膜、右侧膜GLUT4、蓝椭圆、灰蓝团块、Rab珠及3囊泡齐全。 |
| 设计错误1 | 蓝椭圆→灰蓝形为粗红色弯曲实心箭头，将抑制误作激活。 |
| 设计错误2 | 灰蓝形→Rab为细绿色虚线空心头，与前一段线型/颜色不一致。 |
| 设计错误3 | GSV→膜GLUT4为黑色实线实心头，与普通激活同型。 |
| 设计错误4 | 蓝椭圆和膜之间多出紫色双向箭头；共4条线，未多出其他连线。 |
| 文字 | 无文字、字母、数字、伪文字。 |
| 其他偏差 | 轻微渐变和膜GLUT4筒体透视感超出平色要求；膜条带位置略高。 |
| 处置 | 选用第1次；主要预设反例均可逐条指出。 |

**实际提交的完整提示词（逐字，包含追加内容）：**

```text
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

Output settings only: landscape 4:3; render at the maximum native resolution available, preferably 3200 x 2400 pixels. Do not render these output settings as image text.
```

### cmp-a2-unified-arrows.png

- 工具：`image_gen.imagegen`（内置）。具体模型：不知道。
- 第1次生成；本版共1次；选用。
- 参考图：无（新生成）。
- 像素：1448×1086；文件字节：1351793；SHA-256：`bcf7f8d819d1bbb57a9fde1b7a2c1c6a45befea881032c241936ab4dcca697e8`。
- 自动缓存原文件：`codex-output/exec-96c7e4c4-a406-4d61-a510-4c3c6ef42a04.png`。
- 提示词改动：原脚本英文逐字完整保留；仅追加上述画布/最大原生分辨率设置。

目视结论：无文字；对象齐全；恰3条线2种线型：两条深灰等粗T形线串联，唯一橙色粗虚线大空心头向上到膜GLUT4；无其他线。Rab贴囊泡表面。两T端与靶标有约20px间隙；橙转位末端与GLUT4亦有小间隙；图形和线较粗且存在轻微渐变，未严格达到纯平色。

| 脚本检查项 | 实测结论 |
|---|---|
| 对象 | 蓝椭圆、灰蓝团块、附在3囊泡簇表面的Rab、膜与膜GLUT4齐全。 |
| 两条抑制 | 两条同粗深灰T形线串联，方向正确；端点有窄间隙，未严格贴靶标。 |
| 转位 | 唯一一条橙色粗虚线大空心头从囊泡簇朝上指向膜GLUT4；末端也有窄间隙。 |
| 线数 | 恰3条连接、2种线型；没有额外双向或激活箭头。 |
| 文字 | 无文字、伪文字、字母、数字。 |
| 风格偏差 | 描边与连接线较粗，存在轻微渐变；语义较A1一致，但不能声称平色/端点全部符合。 |
| 印刷 | 1448×1086为准确4:3；若按80mm宽排版，等效约459.74ppi；不是16:9，按对比组专属要求执行。 |

**实际提交的完整提示词（逐字，包含追加内容）：**

```text
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

Output settings only: landscape 4:3; render at the maximum native resolution available, preferably 3200 x 2400 pixels. Do not render these output settings as image text.
```

### cmp-b1-too-many-colors-alt1.png

- 工具：`image_gen.imagegen`（内置）。具体模型：不知道。
- 第1次生成；本版共2次；落选保留。
- 参考图：无（新生成）。
- 像素：1672×941；文件字节：1378668；SHA-256：`daa7f83d51014ac2c9cf2f39c599d94f72d5b01db8f8ae99529f30922afd5ad7`。
- 自动缓存原文件：`codex-output/exec-1b31ad69-b9af-4a3e-99fa-aca6cbf4a97b.png`。
- 提示词改动：原脚本英文逐字完整保留；仅追加上述画布/最大原生分辨率设置。

目视结论：无文字；饱和多色蛋白、彩虹膜、亮粉囊泡、青绿葡萄糖符合配色反例。六蛋白被连成一条全激活链，两条抑制、mTORC2支路、PIP转化均消失，葡萄糖流向反转朝胞外，GSV到膜转位线缺失，囊泡内画了多余小珠，未保持V3结构。不能用于控制结构一致的配色对照。

| 脚本检查项 | 实测结论 |
|---|---|
| 配色目的 | 蛋白采用红、黄绿、紫、青、洋红、黄、深蓝；膜彩虹；囊泡粉色；葡萄糖青绿；符合颜色过多反例。 |
| 结构 | 6蛋白变为单条线性激活链，双抑制、PIP转化、mTORC2支路缺失；GSV转位线缺失、葡萄糖箭头反向向外。 |
| 对象 | 胰岛素珠/葡萄糖数增加，囊泡内多出小珠；没有保持V3对象形状和数量。 |
| 文字 | 无文字、伪文字、字母或数字。 |
| 风格 | 仍有轻微渐变，但主要问题是结构同时变化，不能作为同结构仅变色对照。 |
| 处置 | 保留失败稿，第2次以V3为参考。 |

**实际提交的完整提示词（逐字，包含追加内容）：**

```text
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

Output settings only: landscape 16:9; render at the maximum native resolution available, preferably 3840 x 2160 pixels. Do not render these output settings as image text.
```

### cmp-b1-too-many-colors.png

- 工具：`image_gen.imagegen`（内置）。具体模型：不知道。
- 第2次生成；本版共2次；选用。
- 参考图：`v3-revised.png`（本目录；作为编辑/参考输入）。
- 像素：1672×941；文件字节：1308957；SHA-256：`d30ababd86e65bf7980411b4f5aa9832e04c0b3255af2edcd98e804a08a9aa6e`。
- 自动缓存原文件：`codex-output/exec-33149efd-fe99-439f-823a-33c05e3c033a.png`。
- 提示词改动：原脚本英文逐字完整保留；仅追加上述画布/最大原生分辨率设置。

目视结论：选用。无文字；使用V3参考后保留主要对象、支路、两条T线、粗虚线与点线，彩虹膜、亮粉囊泡、青绿葡萄糖及多种饱和蛋白色符合反例；各箭头多色，部分颜色重复；R5空心头意外变实心。与V3不是完全严格的仅变色对照，正文需注明此差异。

| 脚本检查项 | 实测结论 |
|---|---|
| 配色目的 | 彩虹膜、亮粉囊泡、青绿葡萄糖、多种高饱和蛋白色及多色箭头清楚，膜抢占视觉注意。 |
| 对象与布局 | 参考V3后主要对象、3颗配体、4个葡萄糖、3个GSV、膜GLUT4和支路位置基本保留。 |
| 箭头语义 | 双T、上行转位粗虚线、下行葡萄糖点线仍在；酶促弧由空心头意外变成实心头。不能描述为完全仅变色的严格对照。 |
| 颜色逐项 | 蛋白大多不同色，但mTORC2与Rab均深蓝，部分线色重复，未字面满足每个对象/箭头全部异色。 |
| 文字 | 无文字、伪文字、字母或数字。 |
| 灰度实测 | 已转灰度查看：膜较重、mTORC2/Rab偏暗、PI3K/PDK1附近部分箭头偏浅，层级不统一；双T和转位/点线仍可辨，不能声称灰度后全部不可读。 |
| B2复用 | B2直接使用v3-revised.png，不另生成、不另复制图像；本图实际参考的也是该文件。 |

**实际提交的完整提示词（逐字，包含追加内容）：**

```text
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

Output settings only: landscape 16:9; render at the maximum native resolution available, preferably 3840 x 2160 pixels. Do not render these output settings as image text.
```

## V4标签留白实测

对脚本16个指定矩形逐一取原始像素，统计 `max(R,G,B)-min(R,G,B)>25 或 mean(R,G,B)<220` 的比例，用于发现彩色对象和深色线条占用；这不是“所有像素等于纯白”的严格测试，也不能替代目视判断。共有7个区域检出图形像素，故不能勾选标签区全空白。

| 区域序号 | x范围 | y范围 | 检出图形像素占比 |
|---|---|---|---:|
| 1 | 0.02–0.1 | 0.02–0.07 | 0.00% |
| 2 | 0.17–0.26 | 0.05–0.09 | 0.00% |
| 3 | 0.17–0.33 | 0.12–0.17 | 1.10% |
| 4 | 0.16–0.26 | 0.52–0.57 | 0.00% |
| 5 | 0.24–0.36 | 0.41–0.46 | 4.51% |
| 6 | 0.33–0.45 | 0.3–0.34 | 11.07% |
| 7 | 0.4–0.48 | 0.41–0.45 | 0.00% |
| 8 | 0.57–0.62 | 0.39–0.44 | 5.17% |
| 9 | 0.58–0.66 | 0.6–0.64 | 0.00% |
| 10 | 0.68–0.8 | 0.47–0.51 | 20.31% |
| 11 | 0.62–0.7 | 0.66–0.7 | 0.00% |
| 12 | 0.83–0.97 | 0.82–0.86 | 0.00% |
| 13 | 0.9–0.99 | 0.3–0.35 | 2.85% |
| 14 | 0.92–0.99 | 0.08–0.12 | 16.91% |
| 15 | 0.02–0.12 | 0.8–0.85 | 0.00% |
| 16 | 0.6–0.78 | 0.15–0.19 | 0.00% |

## 已完成与仍未满足的验收

- 已完成：8种指定图、7个落选稿、逐张完整实际提示词和来源、每版次数、尺寸与目录实测、全部15张目视检查，以及V2/V3/V4所有主稿和备选稿的R1–R13表（连同V1共104条）。
- 已完成：V4关键区域200%检查；V3、V4、B1实际灰度预览；脚本哈希前后核对；B2复用V3。
- 未满足：16:9图宽≥2400及174mm下300ppi；V4全部科学关系/线端/标签留白/平色要求；A组完全平色与端点贴合；B组严格只变色。
- 不在本次图像生成交付内：LaTeX/TikZ标签和图例、中文英文成稿PDF、标签字号排版检查、实体打印和领域同行复核签字。未把这些项目虚报为通过。

所有不满足项保留实测证据；本次没有为迎合教学剧本而伪造V1错字、把失败稿当合格终稿，或把插值图称作原生高分辨率。

