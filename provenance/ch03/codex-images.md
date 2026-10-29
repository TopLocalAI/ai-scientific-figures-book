# 第 03 章 codex-image 生成与核验记录

核验日期：2026-10-29T16:27:10.808925+08:00。状态：8 张规定路径底图均已保存；**部分验收未通过，不能当作全章已合格终稿**。

## 范围、工具与诚信说明

- 只交付 FIG 03-02a/b/c、03-03a/b/c、03-05b、03-06 的 PNG 底图；未制作 TikZ、文字标签、章节或非 codex-image 图。
- 实际工具：Codex 内置 image_gen.imagegen（functions.exec 内 tools.image_gen__imagegen）。具体模型：不知道：工具未返回具体模型标识。
- 21 次图像生成调用；22 个 PNG 文件 = 8 张正文路径文件 + 7 张 figures 下备选 + 7 张 provenance 下中间版/备选。05b 正文图复制 r3，不额外调用生成。
- 每张草图、候选及每个修订阶段最多 3 次。修改失败时回到上一阶段选定版重试；每条参考图路径见下文。未运行子 agent，未 commit/push。
- 02a/b/c 是模型模拟铅笔草图。所有图都是教学示意，不是实验图或数据。
- 图像均逐张进行了模型视觉检查，没有观察到文字、字母、数字或伪文字；没有执行 OCR（本机未找到 tesseract），也没有真人同事测试或基因编辑同行签名复核。RNA 发夹、DNA 横档、箭头和 indel 标记按图形对象判断，不当作标签。
- 图片没有手工修图、裁切、插值放大或补画；只复制原始输出。工具自动在自身 generated_images 缓存中落盘，交付副本及本任务手动写入文件仅在 figures/ch03 和 provenance/ch03。逐张源路径保存在 generation-manifest.json。
- 规划 prompt 逐字保留，公共开头与布局段用空行连接；候选图依规划将 LAYOUT 占位符替换为 A/B/C 对应原文。重试追加说明逐条列出，**不是所有调用都与规划字符串完全相同**，且三张候选的最终文字不完全相同。不能沿用“只换草图、提示词完全相同”的图注表述。

## 总体验收和需交回作者的差异

| 项目 | 实测/结论 |
|---|---|
| 正文路径 | 8/8 已保存；所有 PNG 可解码 |
| 像素尺寸 | 全部 1672×941，未达到 ≥2400 px；原生宽高比 1.776833，较 16:9 偏差约 0.0531% |
| 提高分辨率尝试 | 02b 第 1 次追加 2560×1440 和 ≥2400 px，仍未生效；工具没有独立尺寸参数；未插值冒充高分辨率 |
| 无字 | 逐张视觉检查未见文字；不等于 OCR 或真人校对 |
| 02c | 分支各到一条通道；框仍不等高，RNA 双描线，风格与 A/B 非严格一致 |
| 03b | 最终候选箭头两进两出，但 NHEJ/PAM 细节位置漂移及额外 PAM 未解决；不通过全部科学/画面验收 |
| 03c 实际问题 | 缺口两侧重复 PAM、153/198 px 不等高框；没有漂浮/重复供体，没有细胞核；DNA 端点已基本对齐 |
| 05b | 单侧 PAM、唯一 HDR 供体及两种结果保留；端点误差 0.224% <2%，框高仍差 5.96% |
| 06 | 端点误差 0.224% <2%；框高差 5.71%；右 30% 的纯空白高度约 32%，目标约35%，连接线侵入预定插图区域下缘 |
| 平涂风格 | 候选和后续图含轻微蓝色纹理及橙色高光，未严格满足 no gradients/no highlights/no texture |
| 修改 4 | 无多余细胞核/背景对象，按 §3.8 条件跳过；没有 r4.png，不伪造“四步全执行” |
| 标签/插图/最终尺寸 | 本轮只做底图，标签不压对象、6.5 pt 字号、174 mm 排版及精确 PAM 插图未验证 |
| 阅读顺序/同行复核 | 未做真人测试；编号只能写“作者预期”，不能虚构同事测试或领域审核 |

## 终稿 C1–C9 视觉核验

| 关系 | 结论 | 观察 |
|---|---|---|
| C1 sgRNA–Cas9 | ✓ | 第一步橙 RNA 与蓝灰 Cas9 接触；发夹可辨 |
| C2 PAM 识别 | ✓ 示意层面 | 第二步蛋白/RNA 复合物邻近黄色段 |
| C3 靶链配对/R 环 | ? | 有橙线和置换轮廓，但横档、双描边使配对对象含混，不能据此验证靶链身份 |
| C4 PAM 非靶链位置 | 部分 | 第三步黄色段在上链、缺口右侧；精确方向/碱基几何需另行 TikZ 插图 |
| C5 双链断裂 | ✓ 简化 | 两条链在同一 x 位置有缺口，右侧黄段相邻；3 bp 距离未在底图表达 |
| C6/C7 NHEJ | ✓ 示意层面 | 上通道无模板，结果有单一红紫 indel 标记；“可能”须由标签/图注说明 |
| C8/C9 HDR | 部分 | 下通道有唯一短供体及青绿写入段，中心接近；两段青绿长度不严格相等，没有画修复中间步骤 |
| 阅读路径 | 模型检查通过，真人未测 | 上排三步→同一右侧分叉→上下两结果；选定 06 第2次，未使用分叉脱节的第3次 |
| 禁止项 | 视觉检查通过 | 无细胞核、剪刀、闪电、发光及文字；轻微高光属于风格未达标，已另列 |
| 同行科学复核 | 未完成 | 未请基因编辑同行复核，不填写虚构签名 |

## 每次修改的副作用

| 阶段 | 尝试次数 | 处理与实际结果 |
|---|---:|---|
| PAM r1 | 2 | 原文第1次无效；第2次追加定位后删除左侧重复 PAM；细线/色纹再渲染 |
| 供体 r2 | 2 | 第1次删掉供体，弃用；回到 r1 后重试，保留并略下移唯一供体 |
| 对齐 r3 | 3 | 第1次删除供体并混合两结果颜色，弃用；第2次仍不等高；第3次框高差减小但未消除，下通道连带下移 |
| 删除背景 r4 | 0 | 条件不成立，跳过 |
| 终稿留白 | 3 | 第1次留白不足且路径脱节；第2次连通、留白高度稍不足；第3次留白增加但分叉脱节，弃用，选第2次 |

## 每个文件的完整调用和逐条视觉结论


### figures/ch03/ch03-02a-sketch-linear.png

- 工具：Codex 内置 image_gen.imagegen（functions.exec 内 tools.image_gen__imagegen）
- 模型：不知道：工具未返回具体模型标识。
- 日期：2026-10-29
- 本阶段第几次：1
- 参考图：无；从文字生成
- 输出：1672×941，RGB PNG；SHA-256：`dc6ede54676ec401fffd564b4ca4e46d409e6382c126a257a587afc5f856b390`
- prompt 改动原因：未追加/改写规划英文 prompt；仅作规划要求的公共段拼接或 LAYOUT 占位替换。
- 人工图像修改：无。

画面内容 / 核验要点逐条检查：

- 保留；第 1 次。线性四步、右端上下挤放的两个结果及下方短供体均可见。
- 入口在左，箭头总体左→右，分支末端分别指向上下结果；阶段间箭头未画成连续连线。
- 双叶轮廓、内部波线、梯状 DNA、切口右侧阴影小段齐全；下端约 10% 留白。
- 模拟铅笔草图；与另外两张均为灰铅笔、暖白纸，但纸纹、线宽和中央蛋白排线并非严格一致。
- 共通核验：未见文字；像素宽度未达2400；约16:9；未真人复核。

实际完整 prompt（保留换行）：

```text
A rough pencil planning sketch on slightly off-white sketchbook paper,
photographed flat from directly above, evenly lit, no hands, no pencil, no other
objects. Landscape 16:9. Single graphite pencil, loose confident lines, a few
construction lines and faint erasure marks. Simple shapes only: rounded blobs,
pairs of parallel lines with short rungs (double-stranded DNA), a wavy line
(RNA), arrows. Strictly no writing of any kind: no letters, no words, no
numbers, no labels, no title, no annotations. Pencil gray only, no color.
Bottom tenth of the page left blank.

Layout: one horizontal row of four steps from left to right, connected by short
arrows. Step 1 at far left: a rounded two-lobed blob with a short wavy line
tucked inside it. Step 2: a horizontal ladder-like double line with the same
blob sitting on it; a small shaded rectangle on the upper line at the right
edge of the blob. Step 3: the double line with a clear gap cut through both
lines, the small shaded rectangle right next to the gap. Step 4 at far right,
squeezed: the arrow splits into two small arrows, one going up-right and one
going down-right, each ending at a short double line; the lower one has a
small separate short double line floating above it.
```


### figures/ch03/ch03-02b-sketch-hub-alt1.png

- 工具：Codex 内置 image_gen.imagegen（functions.exec 内 tools.image_gen__imagegen）
- 模型：不知道：工具未返回具体模型标识。
- 日期：2026-10-29
- 本阶段第几次：1
- 参考图：无；从文字生成
- 输出：1672×941，RGB PNG；SHA-256：`2ff17e753142f863f1753f33e45b65c91bd22c6957852d6d8fbb88aef9894109`
- prompt 改动原因：保留规划全文，末尾追加输出分辨率，以尝试达到章节的 ≥2400 px 要求；工具仍输出 1672×941。
- 人工图像修改：无。

画面内容 / 核验要点逐条检查：

- 落选；第 1 次。中心蛋白与四角对象齐全，无唯一线性入口。
- 箭头为右上、右下向内，左上、左下向外，满足数量上的两进两出，但与最后选中的方向分配不同。
- 左下 indel 被画成偏大的独立闪电状折线，偏离 tiny zigzag mark；中心蛋白为上下双叶、排线较重。
- 为满足章节 ≥2400 px 的要求追加了输出分辨率句，但实际仍为 1672×941；后续不再重复这一无效追加。
- 共通核验：未见文字；像素宽度未达2400；约16:9；未真人复核。

实际完整 prompt（保留换行）：

```text
A rough pencil planning sketch on slightly off-white sketchbook paper,
photographed flat from directly above, evenly lit, no hands, no pencil, no other
objects. Landscape 16:9. Single graphite pencil, loose confident lines, a few
construction lines and faint erasure marks. Simple shapes only: rounded blobs,
pairs of parallel lines with short rungs (double-stranded DNA), a wavy line
(RNA), arrows. Strictly no writing of any kind: no letters, no words, no
numbers, no labels, no title, no annotations. Pencil gray only, no color.
Bottom tenth of the page left blank.

Layout: radial. In the exact center, a large rounded two-lobed blob sitting on a
short ladder-like double line. Around it, at the four corners of the page,
four smaller shapes: top-left a short wavy line, top-right a small shaded
rectangle on a short double line, bottom-left a short double line with a tiny
zigzag mark, bottom-right a short double line with a short thick inserted
segment and a separate short double line above it. Arrows connect the center
to each corner: two arrows point inward, two point outward. No clear starting
point.

Output resolution: 2560 × 1440 pixels (16:9); at least 2400 pixels wide.
```


### figures/ch03/ch03-02b-sketch-hub.png

- 工具：Codex 内置 image_gen.imagegen（functions.exec 内 tools.image_gen__imagegen）
- 模型：不知道：工具未返回具体模型标识。
- 日期：2026-10-29
- 本阶段第几次：2
- 参考图：无；从文字生成
- 输出：1672×941，RGB PNG；SHA-256：`9779f77a6fb4d39671222fee26c103b34de3fe8671471eb8e5c2bbed235e702e`
- prompt 改动原因：未追加/改写规划英文 prompt；仅作规划要求的公共段拼接或 LAYOUT 占位替换。
- 人工图像修改：无。

画面内容 / 核验要点逐条检查：

- 保留；第 2 次，恢复规划原 prompt。中心双叶蛋白压在 DNA 上，四角对象齐全。
- 四支单头箭头：左上→中心、左下→中心、中心→右上、中心→右下；两进两出，没有唯一入口。
- 左下折线已附着于 DNA，右下插入段与短供体可见；底部留白。
- 暖白纸、灰铅笔与 A/C 同类，但中央排线更浓；不宣称笔触或纸张像素级一致。
- 共通核验：未见文字；像素宽度未达2400；约16:9；未真人复核。

实际完整 prompt（保留换行）：

```text
A rough pencil planning sketch on slightly off-white sketchbook paper,
photographed flat from directly above, evenly lit, no hands, no pencil, no other
objects. Landscape 16:9. Single graphite pencil, loose confident lines, a few
construction lines and faint erasure marks. Simple shapes only: rounded blobs,
pairs of parallel lines with short rungs (double-stranded DNA), a wavy line
(RNA), arrows. Strictly no writing of any kind: no letters, no words, no
numbers, no labels, no title, no annotations. Pencil gray only, no color.
Bottom tenth of the page left blank.

Layout: radial. In the exact center, a large rounded two-lobed blob sitting on a
short ladder-like double line. Around it, at the four corners of the page,
four smaller shapes: top-left a short wavy line, top-right a small shaded
rectangle on a short double line, bottom-left a short double line with a tiny
zigzag mark, bottom-right a short double line with a short thick inserted
segment and a separate short double line above it. Arrows connect the center
to each corner: two arrows point inward, two point outward. No clear starting
point.
```


### figures/ch03/ch03-02c-sketch-branch-alt1.png

- 工具：Codex 内置 image_gen.imagegen（functions.exec 内 tools.image_gen__imagegen）
- 模型：不知道：工具未返回具体模型标识。
- 日期：2026-10-29
- 本阶段第几次：1
- 参考图：无；从文字生成
- 输出：1672×941，RGB PNG；SHA-256：`e4cb32e8752f0ce4c497981be0f89b1612f319be1530b0406ff2e479815c991e`
- prompt 改动原因：未追加/改写规划英文 prompt；仅作规划要求的公共段拼接或 LAYOUT 占位替换。
- 人工图像修改：无。

画面内容 / 核验要点逐条检查：

- 落选；第 1 次。上排三步、上下两条宽通道及下通道短供体齐全。
- 失败：分叉后的两个箭头都落在上方矩形上沿，未分别通往两个结果。
- 上通道中部变成明显开口及独立折线；上下框高度不同。DNA 端点大致对齐。
- 共通核验：未见文字；像素宽度未达2400；约16:9；未真人复核。

实际完整 prompt（保留换行）：

```text
A rough pencil planning sketch on slightly off-white sketchbook paper,
photographed flat from directly above, evenly lit, no hands, no pencil, no other
objects. Landscape 16:9. Single graphite pencil, loose confident lines, a few
construction lines and faint erasure marks. Simple shapes only: rounded blobs,
pairs of parallel lines with short rungs (double-stranded DNA), a wavy line
(RNA), arrows. Strictly no writing of any kind: no letters, no words, no
numbers, no labels, no title, no annotations. Pencil gray only, no color.
Bottom tenth of the page left blank.

Layout: two tiers. Upper third of the page: a compact row of three small steps
from left to right connected by arrows (a two-lobed blob with a wavy line
inside; the blob sitting on a ladder-like double line with a small shaded
rectangle; the double line with a gap through both lines, the shaded rectangle
right next to the gap). From the third step, one arrow goes down and splits
into two arrows. Lower part of the page: two wide horizontal lanes of equal
height, stacked one above the other, each framed by a light pencil rectangle.
Upper lane: a long double line with a tiny zigzag mark at the middle. Lower
lane: a short separate double line floating above the middle of a long double
line, and the long double line has a short thick inserted segment at the
middle. The long double lines in both lanes start and end at the same x
positions.
```


### figures/ch03/ch03-02c-sketch-branch-alt2.png

- 工具：Codex 内置 image_gen.imagegen（functions.exec 内 tools.image_gen__imagegen）
- 模型：不知道：工具未返回具体模型标识。
- 日期：2026-10-29
- 本阶段第几次：2
- 参考图：无；从文字生成
- 输出：1672×941，RGB PNG；SHA-256：`de88a932d6c07e424137f4ec9a0d4a74d5283a1c39b9aa3570bf67db50c0d1d4`
- prompt 改动原因：未追加/改写规划英文 prompt；仅作规划要求的公共段拼接或 LAYOUT 占位替换。
- 人工图像修改：无。

画面内容 / 核验要点逐条检查：

- 落选；第 2 次，原 prompt 重试。上排与两通道保留，DNA 端点大致对齐。
- 失败：两个箭头仍都指向上通道；下通道无明确入箭头。
- 上通道折线悬在大缺口中，框高度仍不同；没有文字。
- 共通核验：未见文字；像素宽度未达2400；约16:9；未真人复核。

实际完整 prompt（保留换行）：

```text
A rough pencil planning sketch on slightly off-white sketchbook paper,
photographed flat from directly above, evenly lit, no hands, no pencil, no other
objects. Landscape 16:9. Single graphite pencil, loose confident lines, a few
construction lines and faint erasure marks. Simple shapes only: rounded blobs,
pairs of parallel lines with short rungs (double-stranded DNA), a wavy line
(RNA), arrows. Strictly no writing of any kind: no letters, no words, no
numbers, no labels, no title, no annotations. Pencil gray only, no color.
Bottom tenth of the page left blank.

Layout: two tiers. Upper third of the page: a compact row of three small steps
from left to right connected by arrows (a two-lobed blob with a wavy line
inside; the blob sitting on a ladder-like double line with a small shaded
rectangle; the double line with a gap through both lines, the shaded rectangle
right next to the gap). From the third step, one arrow goes down and splits
into two arrows. Lower part of the page: two wide horizontal lanes of equal
height, stacked one above the other, each framed by a light pencil rectangle.
Upper lane: a long double line with a tiny zigzag mark at the middle. Lower
lane: a short separate double line floating above the middle of a long double
line, and the long double line has a short thick inserted segment at the
middle. The long double lines in both lanes start and end at the same x
positions.
```


### figures/ch03/ch03-02c-sketch-branch.png

- 工具：Codex 内置 image_gen.imagegen（functions.exec 内 tools.image_gen__imagegen）
- 模型：不知道：工具未返回具体模型标识。
- 日期：2026-10-29
- 本阶段第几次：3
- 参考图：无；从文字生成
- 输出：1672×941，RGB PNG；SHA-256：`6bfa80f7c121743f3b1c0b81dc750c019649a29f9ef24b9da87ec0f66a58e035`
- prompt 改动原因：保留规划全文，追加明确路由及连续 indel 要求；前两次都把两个分支箭头画到同一通道。
- 人工图像修改：无。

画面内容 / 核验要点逐条检查：

- 保留；第 3 次。追加分支路由说明后，一支沿右侧进入上通道，另一支继续向下进入下通道。
- 上排三步齐全，长 DNA 两端基本对齐；上通道为小折线、下通道为短供体与插入段，底部留白。
- 未完全通过：两条通道高度仍不同；RNA 波线被画成近似双描线，纸张/笔触与 A/B 只是同类风格。
- 这是模型模拟草图；不是作者真实手绘。达到三次上限后选结构最接近的一张。
- 共通核验：未见文字；像素宽度未达2400；约16:9；未真人复核。

实际完整 prompt（保留换行）：

```text
A rough pencil planning sketch on slightly off-white sketchbook paper,
photographed flat from directly above, evenly lit, no hands, no pencil, no other
objects. Landscape 16:9. Single graphite pencil, loose confident lines, a few
construction lines and faint erasure marks. Simple shapes only: rounded blobs,
pairs of parallel lines with short rungs (double-stranded DNA), a wavy line
(RNA), arrows. Strictly no writing of any kind: no letters, no words, no
numbers, no labels, no title, no annotations. Pencil gray only, no color.
Bottom tenth of the page left blank.

Layout: two tiers. Upper third of the page: a compact row of three small steps
from left to right connected by arrows (a two-lobed blob with a wavy line
inside; the blob sitting on a ladder-like double line with a small shaded
rectangle; the double line with a gap through both lines, the shaded rectangle
right next to the gap). From the third step, one arrow goes down and splits
into two arrows. Lower part of the page: two wide horizontal lanes of equal
height, stacked one above the other, each framed by a light pencil rectangle.
Upper lane: a long double line with a tiny zigzag mark at the middle. Lower
lane: a short separate double line floating above the middle of a long double
line, and the long double line has a short thick inserted segment at the
middle. The long double lines in both lanes start and end at the same x
positions.

Routing clarification: the two outgoing branch arrows MUST end at two DIFFERENT lanes. Route the branch down along the far right OUTSIDE both rectangles. One left-pointing arrow enters the upper rectangle through its right edge; the other continues downward outside the upper rectangle and enters the LOWER rectangle through its right edge. Never point both arrowheads at the upper rectangle. The upper lane DNA is continuous through its tiny zigzag indel mark, not a large open break.
```


### figures/ch03/ch03-03a-cand-linear.png

- 工具：Codex 内置 image_gen.imagegen（functions.exec 内 tools.image_gen__imagegen）
- 模型：不知道：工具未返回具体模型标识。
- 日期：2026-10-29
- 本阶段第几次：1
- 参考图：figures/ch03/ch03-02a-sketch-linear.png
- 输出：1672×941，RGB PNG；SHA-256：`5cb88f76617d168699b75001dce03a9b3343057ab0fa99d40c3962b8b6ccfea3`
- prompt 改动原因：未追加/改写规划英文 prompt；仅作规划要求的公共段拼接或 LAYOUT 占位替换。
- 人工图像修改：无。

画面内容 / 核验要点逐条检查：

- 保留；第 1 次，参考 02a。一行三步后在右端分叉为上下两个拥挤结果，与草图区域分配基本一致。
- Cas9 蓝灰、RNA 橙、PAM 黄、indel 红紫、供体/写入段青绿，身份可辨；供体只在右下结果。
- 对照草图的偏离：切割步骤 PAM 从草图缺口右侧移到缺口左侧；RNA 从波线变为发夹；NHEJ 补上红紫标记，供体及写入段着色。
- RNA 与靶链配对、非靶链置换不够清楚；供体中段与 HDR 写入段长度并非严格相等。
- 画面有轻微蓝色明暗和纹理，不是完全均匀平涂；保留作为候选，不作为已验证科学终稿。
- 共通核验：未见文字；像素宽度未达2400；约16:9；未真人复核。

实际完整 prompt（保留换行）：

```text
Flat 2D scientific overview schematic for a journal figure, landscape 16:9,
pure white background. Clean vector illustration style: flat fills, thin dark
gray outlines, no gradients, no shadows, no highlights, no 3D, no glow, no
texture. ABSOLUTELY NO TEXT: no letters, no words, no numbers, no symbols, no
labels, no legend, no title.

Follow the layout of the attached pencil sketch closely: same regions, same
relative positions, same arrow directions.

OBJECTS (use these exact visual identities in every step where they appear):
- Cas9: a rounded two-lobed protein shape, muted blue-gray (#7C93A8).
- sgRNA: a single orange (#E69F00) strand with a short straight segment (the
  spacer) and a small hairpin loop scaffold, partly inside Cas9.
- Genomic DNA: two parallel dark gray (#4D4D4D) lines with short light gray
  rungs between them.
- PAM: a short bright yellow (#F0E442) segment on the upper DNA line.
- Double-strand break: a clean gap through both DNA lines, right next to the PAM.
- Donor template: a short separate double-stranded DNA; its two ends dark gray
  (homology arms), its middle segment teal (#009E73).
- NHEJ result: a continuous DNA with one small reddish-purple (#CC79A7) mark at
  the former break site.
- HDR result: a continuous DNA with a teal (#009E73) segment at the former
  break site, the same length as the donor's middle segment.

STEPS: (1) Cas9 bound to sgRNA. (2) Cas9-sgRNA sitting on the DNA at the PAM, the
orange spacer lying alongside the lower DNA line, the upper line slightly
pushed away. (3) The DNA with the break next to the PAM, Cas9 lifted away.
(4) Repair by end joining, giving the NHEJ result, with no donor. (5) Repair
using the donor template, giving the HDR result; the donor appears only here.
Steps are connected by solid dark gray arrows with filled heads; after step 3
the arrow splits into two equal arrows.

DO NOT DRAW: cells, nucleus, chromosomes, scissors, lightning, sparkles,
double-helix twisting, realistic protein structure, any charts or data.
Bottom 10% of the image empty.

LAYOUT: one row of five steps left to right; steps 4 and 5 stacked at the
right end.
```


### figures/ch03/ch03-03b-cand-hub-alt1.png

- 工具：Codex 内置 image_gen.imagegen（functions.exec 内 tools.image_gen__imagegen）
- 模型：不知道：工具未返回具体模型标识。
- 日期：2026-10-29
- 本阶段第几次：1
- 参考图：figures/ch03/ch03-02b-sketch-hub.png
- 输出：1672×941，RGB PNG；SHA-256：`fa8b4bbcf4edd6f12cd3ed32caa370be532b0c516850bd2f7a1727481bc435a5`
- prompt 改动原因：未追加/改写规划英文 prompt；仅作规划要求的公共段拼接或 LAYOUT 占位替换。
- 人工图像修改：无。

画面内容 / 核验要点逐条检查：

- 落选；第 1 次，参考 02b。中心加四角骨架和颜色身份基本保留。
- 失败：草图左下→中心的箭头被反转，变成一进三出，左上形成较明确的入口，削弱预定反例。
- 左上 RNA 扩展成 Cas9–RNA，右上 PAM 细节变成断裂 DNA；中央未合并表现断裂。
- 供体仅右下，NHEJ 在左下，未见文字。
- 共通核验：未见文字；像素宽度未达2400；约16:9；未真人复核。

实际完整 prompt（保留换行）：

```text
Flat 2D scientific overview schematic for a journal figure, landscape 16:9,
pure white background. Clean vector illustration style: flat fills, thin dark
gray outlines, no gradients, no shadows, no highlights, no 3D, no glow, no
texture. ABSOLUTELY NO TEXT: no letters, no words, no numbers, no symbols, no
labels, no legend, no title.

Follow the layout of the attached pencil sketch closely: same regions, same
relative positions, same arrow directions.

OBJECTS (use these exact visual identities in every step where they appear):
- Cas9: a rounded two-lobed protein shape, muted blue-gray (#7C93A8).
- sgRNA: a single orange (#E69F00) strand with a short straight segment (the
  spacer) and a small hairpin loop scaffold, partly inside Cas9.
- Genomic DNA: two parallel dark gray (#4D4D4D) lines with short light gray
  rungs between them.
- PAM: a short bright yellow (#F0E442) segment on the upper DNA line.
- Double-strand break: a clean gap through both DNA lines, right next to the PAM.
- Donor template: a short separate double-stranded DNA; its two ends dark gray
  (homology arms), its middle segment teal (#009E73).
- NHEJ result: a continuous DNA with one small reddish-purple (#CC79A7) mark at
  the former break site.
- HDR result: a continuous DNA with a teal (#009E73) segment at the former
  break site, the same length as the donor's middle segment.

STEPS: (1) Cas9 bound to sgRNA. (2) Cas9-sgRNA sitting on the DNA at the PAM, the
orange spacer lying alongside the lower DNA line, the upper line slightly
pushed away. (3) The DNA with the break next to the PAM, Cas9 lifted away.
(4) Repair by end joining, giving the NHEJ result, with no donor. (5) Repair
using the donor template, giving the HDR result; the donor appears only here.
Steps are connected by solid dark gray arrows with filled heads; after step 3
the arrow splits into two equal arrows.

DO NOT DRAW: cells, nucleus, chromosomes, scissors, lightning, sparkles,
double-helix twisting, realistic protein structure, any charts or data.
Bottom 10% of the image empty.

LAYOUT: radial; the DNA-bound Cas9 complex (step 2-3 merged) in the
center, steps 1, 4, 5 and the PAM detail around it.
```


### figures/ch03/ch03-03b-cand-hub-alt2.png

- 工具：Codex 内置 image_gen.imagegen（functions.exec 内 tools.image_gen__imagegen）
- 模型：不知道：工具未返回具体模型标识。
- 日期：2026-10-29
- 本阶段第几次：2
- 参考图：figures/ch03/ch03-02b-sketch-hub.png
- 输出：1672×941，RGB PNG；SHA-256：`e98086b1cc0622089cb132d6aed072ae2d59eee2c8f9e843db7efa4c2f2823a9`
- prompt 改动原因：未追加/改写规划英文 prompt；仅作规划要求的公共段拼接或 LAYOUT 占位替换。
- 人工图像修改：无。

画面内容 / 核验要点逐条检查：

- 落选；第 2 次，原 prompt 重试。颜色和四角对象与第 1 次近似。
- 失败：左下连线带两个箭头头部，成为双向箭头；不符合草图四支单头箭头。
- 中央仍未体现断裂，右上变成独立断裂步骤；供体只在右下。
- 共通核验：未见文字；像素宽度未达2400；约16:9；未真人复核。

实际完整 prompt（保留换行）：

```text
Flat 2D scientific overview schematic for a journal figure, landscape 16:9,
pure white background. Clean vector illustration style: flat fills, thin dark
gray outlines, no gradients, no shadows, no highlights, no 3D, no glow, no
texture. ABSOLUTELY NO TEXT: no letters, no words, no numbers, no symbols, no
labels, no legend, no title.

Follow the layout of the attached pencil sketch closely: same regions, same
relative positions, same arrow directions.

OBJECTS (use these exact visual identities in every step where they appear):
- Cas9: a rounded two-lobed protein shape, muted blue-gray (#7C93A8).
- sgRNA: a single orange (#E69F00) strand with a short straight segment (the
  spacer) and a small hairpin loop scaffold, partly inside Cas9.
- Genomic DNA: two parallel dark gray (#4D4D4D) lines with short light gray
  rungs between them.
- PAM: a short bright yellow (#F0E442) segment on the upper DNA line.
- Double-strand break: a clean gap through both DNA lines, right next to the PAM.
- Donor template: a short separate double-stranded DNA; its two ends dark gray
  (homology arms), its middle segment teal (#009E73).
- NHEJ result: a continuous DNA with one small reddish-purple (#CC79A7) mark at
  the former break site.
- HDR result: a continuous DNA with a teal (#009E73) segment at the former
  break site, the same length as the donor's middle segment.

STEPS: (1) Cas9 bound to sgRNA. (2) Cas9-sgRNA sitting on the DNA at the PAM, the
orange spacer lying alongside the lower DNA line, the upper line slightly
pushed away. (3) The DNA with the break next to the PAM, Cas9 lifted away.
(4) Repair by end joining, giving the NHEJ result, with no donor. (5) Repair
using the donor template, giving the HDR result; the donor appears only here.
Steps are connected by solid dark gray arrows with filled heads; after step 3
the arrow splits into two equal arrows.

DO NOT DRAW: cells, nucleus, chromosomes, scissors, lightning, sparkles,
double-helix twisting, realistic protein structure, any charts or data.
Bottom 10% of the image empty.

LAYOUT: radial; the DNA-bound Cas9 complex (step 2-3 merged) in the
center, steps 1, 4, 5 and the PAM detail around it.
```


### figures/ch03/ch03-03b-cand-hub.png

- 工具：Codex 内置 image_gen.imagegen（functions.exec 内 tools.image_gen__imagegen）
- 模型：不知道：工具未返回具体模型标识。
- 日期：2026-10-29
- 本阶段第几次：3
- 参考图：figures/ch03/ch03-02b-sketch-hub.png
- 输出：1672×941，RGB PNG；SHA-256：`da342fbc65813812249bf117c83f5f553d36f475b2b959e85e865ba6f048354c`
- prompt 改动原因：保留公共正文和 B 布局替换段，追加四支单头箭头的方向；前两次分别出现方向反转和双头箭头。
- 人工图像修改：无。

画面内容 / 核验要点逐条检查：

- 保留为最接近箭头要求的候选，但未通过全部画面内容验收；第 3 次。
- 追加说明后四支单头箭头确为左上/左下向内、右上/右下向外，符合两进两出与入口含混的教学目标。
- 重要偏离：原草图左下 NHEJ 结果与右上 PAM 细节的身份发生漂移；红紫结果出现在右上，左下变为断裂 DNA。左下缺口两侧各有黄色段，右下又新增黄色段。
- 供体仅右下且颜色身份可辨，但中央没有清楚的双链断裂；不能把这张描述成仅有布局层级问题的科学正确反例。
- 达到三次上限，保留实际结果并明确标为待修正，不为配合正文隐瞒对象交换和多余 PAM。
- 共通核验：未见文字；像素宽度未达2400；约16:9；未真人复核。

实际完整 prompt（保留换行）：

```text
Flat 2D scientific overview schematic for a journal figure, landscape 16:9,
pure white background. Clean vector illustration style: flat fills, thin dark
gray outlines, no gradients, no shadows, no highlights, no 3D, no glow, no
texture. ABSOLUTELY NO TEXT: no letters, no words, no numbers, no symbols, no
labels, no legend, no title.

Follow the layout of the attached pencil sketch closely: same regions, same
relative positions, same arrow directions.

OBJECTS (use these exact visual identities in every step where they appear):
- Cas9: a rounded two-lobed protein shape, muted blue-gray (#7C93A8).
- sgRNA: a single orange (#E69F00) strand with a short straight segment (the
  spacer) and a small hairpin loop scaffold, partly inside Cas9.
- Genomic DNA: two parallel dark gray (#4D4D4D) lines with short light gray
  rungs between them.
- PAM: a short bright yellow (#F0E442) segment on the upper DNA line.
- Double-strand break: a clean gap through both DNA lines, right next to the PAM.
- Donor template: a short separate double-stranded DNA; its two ends dark gray
  (homology arms), its middle segment teal (#009E73).
- NHEJ result: a continuous DNA with one small reddish-purple (#CC79A7) mark at
  the former break site.
- HDR result: a continuous DNA with a teal (#009E73) segment at the former
  break site, the same length as the donor's middle segment.

STEPS: (1) Cas9 bound to sgRNA. (2) Cas9-sgRNA sitting on the DNA at the PAM, the
orange spacer lying alongside the lower DNA line, the upper line slightly
pushed away. (3) The DNA with the break next to the PAM, Cas9 lifted away.
(4) Repair by end joining, giving the NHEJ result, with no donor. (5) Repair
using the donor template, giving the HDR result; the donor appears only here.
Steps are connected by solid dark gray arrows with filled heads; after step 3
the arrow splits into two equal arrows.

DO NOT DRAW: cells, nucleus, chromosomes, scissors, lightning, sparkles,
double-helix twisting, realistic protein structure, any charts or data.
Bottom 10% of the image empty.

LAYOUT: radial; the DNA-bound Cas9 complex (step 2-3 merged) in the
center, steps 1, 4, 5 and the PAM detail around it.

Match the deliberately confusing hub sketch exactly: use exactly FOUR connecting arrows, each with exactly ONE arrowhead. Top-left to center (inward); bottom-left to center (inward); center to top-right (outward); center to bottom-right (outward). No bidirectional arrows, no additional arrows. This is a pedagogical example of ambiguous reading order, so preserve these mixed directions.
```


### figures/ch03/ch03-03c-cand-branch.png

- 工具：Codex 内置 image_gen.imagegen（functions.exec 内 tools.image_gen__imagegen）
- 模型：不知道：工具未返回具体模型标识。
- 日期：2026-10-29
- 本阶段第几次：1
- 参考图：figures/ch03/ch03-02c-sketch-branch.png
- 输出：1672×941，RGB PNG；SHA-256：`589b0ebc028c8477fd064fd1958a3384d58ee7d09b36ae6f5c9111030951667b`
- prompt 改动原因：未追加/改写规划英文 prompt；仅作规划要求的公共段拼接或 LAYOUT 占位替换。
- 人工图像修改：无。

画面内容 / 核验要点逐条检查：

- 保留；第 1 次，参考 02c。上排三步、右侧分叉及上下修复通道均跟随草图；各对象颜色身份正确。
- 实际问题：切割步骤缺口两侧各出现一个 PAM；两通道框高分别 153 与 198 px。
- 对照草图偏离：RNA 变为发夹并新增配对横杠，灰色插入段改为青绿，indel 改为红紫；DNA 轮廓出现双描线。
- 供体已只在 HDR 通道且大致对中，没有漂在通道间、没有复制；无细胞核等额外背景对象，不能虚构这些问题。
- DNA 左右端点误差仅 2/4 px，已小于 2%；修订需改善的是框高，不应把端点描述为严重错位。
- 共通核验：未见文字；像素宽度未达2400；约16:9；未真人复核。

实际完整 prompt（保留换行）：

```text
Flat 2D scientific overview schematic for a journal figure, landscape 16:9,
pure white background. Clean vector illustration style: flat fills, thin dark
gray outlines, no gradients, no shadows, no highlights, no 3D, no glow, no
texture. ABSOLUTELY NO TEXT: no letters, no words, no numbers, no symbols, no
labels, no legend, no title.

Follow the layout of the attached pencil sketch closely: same regions, same
relative positions, same arrow directions.

OBJECTS (use these exact visual identities in every step where they appear):
- Cas9: a rounded two-lobed protein shape, muted blue-gray (#7C93A8).
- sgRNA: a single orange (#E69F00) strand with a short straight segment (the
  spacer) and a small hairpin loop scaffold, partly inside Cas9.
- Genomic DNA: two parallel dark gray (#4D4D4D) lines with short light gray
  rungs between them.
- PAM: a short bright yellow (#F0E442) segment on the upper DNA line.
- Double-strand break: a clean gap through both DNA lines, right next to the PAM.
- Donor template: a short separate double-stranded DNA; its two ends dark gray
  (homology arms), its middle segment teal (#009E73).
- NHEJ result: a continuous DNA with one small reddish-purple (#CC79A7) mark at
  the former break site.
- HDR result: a continuous DNA with a teal (#009E73) segment at the former
  break site, the same length as the donor's middle segment.

STEPS: (1) Cas9 bound to sgRNA. (2) Cas9-sgRNA sitting on the DNA at the PAM, the
orange spacer lying alongside the lower DNA line, the upper line slightly
pushed away. (3) The DNA with the break next to the PAM, Cas9 lifted away.
(4) Repair by end joining, giving the NHEJ result, with no donor. (5) Repair
using the donor template, giving the HDR result; the donor appears only here.
Steps are connected by solid dark gray arrows with filled heads; after step 3
the arrow splits into two equal arrows.

DO NOT DRAW: cells, nucleus, chromosomes, scissors, lightning, sparkles,
double-helix twisting, realistic protein structure, any charts or data.
Bottom 10% of the image empty.

LAYOUT: steps 1-3 as a compact
row across the top third; below, two equal-height horizontal lanes stacked
vertically, upper lane step 4, lower lane step 5, with the DNA in both lanes
aligned at the same x positions and length.
```


### provenance/ch03/ch03-05b-r1-alt1.png

- 工具：Codex 内置 image_gen.imagegen（functions.exec 内 tools.image_gen__imagegen）
- 模型：不知道：工具未返回具体模型标识。
- 日期：2026-10-29
- 本阶段第几次：1
- 参考图：figures/ch03/ch03-03c-cand-branch.png
- 输出：1672×941，RGB PNG；SHA-256：`8de6cdb3bf02739b8603813a1c2b6856d333031ef47208dc61f31a4b5eff9d0a`
- prompt 改动原因：未追加/改写规划英文 prompt；仅作规划要求的公共段拼接或 LAYOUT 占位替换。
- 人工图像修改：无。

画面内容 / 核验要点逐条检查：

- 落选；PAM 修改第 1 次。按 §3.8 修改 1 原文调用，结果仍在缺口左右各保留一个黄色 PAM。
- 目标未达成；其他对象布局大致保留，但存在再渲染差异。下一次回到候选 C 重试。
- 共通核验：未见文字；像素宽度未达2400；约16:9；未真人复核。

实际完整 prompt（保留换行）：

```text
Edit the selected image. Change only one thing: move the small yellow PAM
segment so that it sits directly next to the right side of the DNA gap at the
cleavage step, on the upper strand, touching the gap. Keep every other object,
color, line weight and position unchanged. Do not add any text.
```


### provenance/ch03/ch03-05b-r1.png

- 工具：Codex 内置 image_gen.imagegen（functions.exec 内 tools.image_gen__imagegen）
- 模型：不知道：工具未返回具体模型标识。
- 日期：2026-10-29
- 本阶段第几次：2
- 参考图：figures/ch03/ch03-03c-cand-branch.png
- 输出：1672×941，RGB PNG；SHA-256：`7f3ff13203e69334edceb56d434c32d241b5ac376ba268eab8df9057594de9a0`
- prompt 改动原因：保留修改 1 全文，追加删除左侧重复 PAM 的定位说明；原文首次调用无效。
- 人工图像修改：无。

画面内容 / 核验要点逐条检查：

- 保留；PAM 修改第 2 次。追加定位说明后，删除切口左侧黄色段，只保留右侧上链、贴近缺口的黄色段。
- 两结果、供体、箭头及上排对象均保留，未发现新的对象增删。
- 并非像素锁定：与候选 C 相比，RGB 差值 >15 的像素占全图 3.7144%，上排占 4.0165%；细描边和色彩纹理发生再渲染。
- 共通核验：未见文字；像素宽度未达2400；约16:9；未真人复核。

实际完整 prompt（保留换行）：

```text
Edit the selected image. Change only one thing: move the small yellow PAM
segment so that it sits directly next to the right side of the DNA gap at the
cleavage step, on the upper strand, touching the gap. Keep every other object,
color, line weight and position unchanged. Do not add any text.

The cleavage-step DNA at the TOP RIGHT currently has TWO yellow highlights, one on each side of the gap. Erase the yellow highlight LEFT of that gap, replacing it with the ordinary dark-gray DNA line. Retain exactly ONE yellow highlight RIGHT of that gap, touching the gap on the upper strand. This is the only change.
```


### provenance/ch03/ch03-05b-r2-alt1.png

- 工具：Codex 内置 image_gen.imagegen（functions.exec 内 tools.image_gen__imagegen）
- 模型：不知道：工具未返回具体模型标识。
- 日期：2026-10-29
- 本阶段第几次：1
- 参考图：provenance/ch03/ch03-05b-r1.png
- 输出：1672×941，RGB PNG；SHA-256：`c1d47829a2d155e8d7fe6198e97fe974be05e3e9c1d753112b61772aa9666622`
- prompt 改动原因：未追加/改写规划英文 prompt；仅作规划要求的公共段拼接或 LAYOUT 占位替换。
- 人工图像修改：无。

画面内容 / 核验要点逐条检查：

- 落选；供体修改第 1 次。原指令把下通道唯一短供体直接删掉。
- 科学内容受影响：HDR 的模板来源缺失。两条结果及 PAM 仍在。
- 处理：不继续沿此失败版修改，回到 r1，再追加保留唯一可见供体的说明。
- 共通核验：未见文字；像素宽度未达2400；约16:9；未真人复核。

实际完整 prompt（保留换行）：

```text
Edit the selected image. Change only one thing: move the short teal donor DNA
so that it lies inside the lower repair lane only, directly above the DNA gap
in that lane, horizontally centered on the gap. Remove any copy of the donor
outside the lower lane. Keep everything else unchanged. No text.
```


### provenance/ch03/ch03-05b-r2.png

- 工具：Codex 内置 image_gen.imagegen（functions.exec 内 tools.image_gen__imagegen）
- 模型：不知道：工具未返回具体模型标识。
- 日期：2026-10-29
- 本阶段第几次：2
- 参考图：provenance/ch03/ch03-05b-r1.png
- 输出：1672×941，RGB PNG；SHA-256：`4625b1b689b237edc0d5449af1137a819fc8fbe8ffe105edbb1eac42984c8e05`
- prompt 改动原因：保留修改 2 全文，追加保留唯一供体说明；原文首次调用删除了供体。
- 人工图像修改：无。

画面内容 / 核验要点逐条检查：

- 保留；供体修改第 2 次。短供体保留在下通道，在青绿写入段正上方，数量为 1，上通道没有供体。
- 供体相对 r1 向下移动约 15 px；其青绿中心与结果青绿中心接近。
- 供体原本已在正确通道；此次是微调，不宣称解决了不存在的通道外供体或复制问题。
- 未经要求的再渲染仍存在：差值 >15 的像素占全图 4.1006%，上排 3.5317%；未见新增科学对象。
- 共通核验：未见文字；像素宽度未达2400；约16:9；未真人复核。

实际完整 prompt（保留换行）：

```text
Edit the selected image. Change only one thing: move the short teal donor DNA
so that it lies inside the lower repair lane only, directly above the DNA gap
in that lane, horizontally centered on the gap. Remove any copy of the donor
outside the lower lane. Keep everything else unchanged. No text.

Keep exactly one visible separate donor double-stranded DNA inside the LOWER rectangle. Its existing location, directly above the teal inserted segment, is already close to correct: retain that short donor and horizontally align its teal middle with the teal middle of the long lower DNA. Do not erase or merge the donor with the long DNA. There is no donor outside the lower rectangle to remove.
```


### provenance/ch03/ch03-05b-r3-alt1.png

- 工具：Codex 内置 image_gen.imagegen（functions.exec 内 tools.image_gen__imagegen）
- 模型：不知道：工具未返回具体模型标识。
- 日期：2026-10-29
- 本阶段第几次：1
- 参考图：provenance/ch03/ch03-05b-r2.png
- 输出：1672×941，RGB PNG；SHA-256：`5d070c4471264ea5bc9e980075a5a31001b6492020268550c46803b64b0a3c75`
- prompt 改动原因：未追加/改写规划英文 prompt；仅作规划要求的公共段拼接或 LAYOUT 占位替换。
- 人工图像修改：无。

画面内容 / 核验要点逐条检查：

- 落选；通道对齐第 1 次。两框趋于等高、两条长 DNA 端点对齐。
- 严重副作用：短供体消失，两条结果都同时带青绿和红紫标记，NHEJ/HDR 的区别被抹去。
- 不接受；回到 r2 重试，没有沿此错误版本继续。
- 共通核验：未见文字；像素宽度未达2400；约16:9；未真人复核。

实际完整 prompt（保留换行）：

```text
Edit the selected image. Change only one thing: make the two repair lanes the
same height, and draw the DNA in both lanes at the same horizontal position and
the same length, so the two results line up vertically for comparison. Keep
colors, objects and the top row unchanged. No text.
```


### provenance/ch03/ch03-05b-r3-alt2.png

- 工具：Codex 内置 image_gen.imagegen（functions.exec 内 tools.image_gen__imagegen）
- 模型：不知道：工具未返回具体模型标识。
- 日期：2026-10-29
- 本阶段第几次：2
- 参考图：provenance/ch03/ch03-05b-r2.png
- 输出：1672×941，RGB PNG；SHA-256：`892863f51d88ada681e7c5bfd431171a2823bbeafc44f71955e422fb905df697`
- prompt 改动原因：保留修改 3 全文，追加通道对象身份与 180 px 框高限制；首次修改混淆两结果并删除供体。
- 人工图像修改：无。

画面内容 / 核验要点逐条检查：

- 落选；通道对齐第 2 次。追加身份保留说明后，NHEJ 红紫、HDR 青绿及短供体均恢复/保留。
- 框高度仍明显不同，下框被加高而不是与上框等高；下通道整体下移。
- 对象科学身份较第 1 次正确，但几何目标没有充分达成，故第 3 次仍从 r2 开始。
- 共通核验：未见文字；像素宽度未达2400；约16:9；未真人复核。

实际完整 prompt（保留换行）：

```text
Edit the selected image. Change only one thing: make the two repair lanes the
same height, and draw the DNA in both lanes at the same horizontal position and
the same length, so the two results line up vertically for comparison. Keep
colors, objects and the top row unchanged. No text.

Align geometry only, NOT the identities of the two repair outcomes. Upper lane must retain ONLY its tiny magenta indel mark, with absolutely no teal and no donor. Lower lane must retain its teal inserted segment and exactly ONE SEPARATE short donor DNA above it, with absolutely no magenta. Preserve both outcomes and the visible donor exactly. Make both rectangular lanes 180 pixels high; keep their long DNA left endpoints and right endpoints aligned. Do not alter any top-row object.
```


### provenance/ch03/ch03-05b-r3.png

- 工具：Codex 内置 image_gen.imagegen（functions.exec 内 tools.image_gen__imagegen）
- 模型：不知道：工具未返回具体模型标识。
- 日期：2026-10-29
- 本阶段第几次：3
- 参考图：provenance/ch03/ch03-05b-r2.png
- 输出：1672×941，RGB PNG；SHA-256：`da95a663832c5d81d95763fc09a25b5d4177583a32bb583debbaedfb459d2ff0`
- prompt 改动原因：保留修改 3 全文，追加框顶边像素定位和保护已有科学对象说明；第二次框高仍不同。
- 人工图像修改：无。

画面内容 / 核验要点逐条检查：

- 保留；通道对齐第 3 次。只针对框边界追加精确定位说明，结果保留了所有科学对象与两种颜色身份。
- 实测框高 201.5 与 213.5 px，仍相差 12 px（相对上框 5.96%），不能称严格等高；较最初 153/198 px 改善。
- 长 DNA 左端 x=95/94、右端 x=1435/1432；最大差 3 px，约为上 DNA 长度的 0.224%，满足端点误差 <2%。
- 意外变化：下框、下 DNA 和短供体均小幅下移，线条变深、RNA 高光/轮廓改变；差值 >15 的像素全图 13.6888%，上排 7.2865%。
- 条件性修改 4 未执行：候选及历版均没有细胞核或多余背景对象；两通道矩形是布局分组，不是要删除的背景。
- 共通核验：未见文字；像素宽度未达2400；约16:9；未真人复核。

实际完整 prompt（保留换行）：

```text
Edit the selected image. Change only one thing: make the two repair lanes the
same height, and draw the DNA in both lanes at the same horizontal position and
the same length, so the two results line up vertically for comparison. Keep
colors, objects and the top row unchanged. No text.

Minimal geometric operation on this 1672 by 941 image: the lower lane rectangle already spans approximately y=568 to y=768 (200 pixels). Move ONLY the TOP BORDER of the upper lane rectangle from approximately y=386 up to y=340, leaving its bottom border at approximately y=540 (also 200 pixels). The long DNA endpoints are already aligned closely enough: keep both long DNA drawings and their positions unchanged. Keep the separate donor above the lower DNA, all color marks and the entire top row unchanged. Upper outcome stays magenta-only; lower outcome stays teal-only with one separate donor. Do not make the two outcomes identical.
```


### figures/ch03/ch03-05b-v3-revised.png

- 工具：Codex 内置 image_gen.imagegen（functions.exec 内 tools.image_gen__imagegen）
- 模型：不知道：工具未返回具体模型标识。
- 日期：2026-10-29
- 本阶段第几次：3
- 参考图：provenance/ch03/ch03-05b-r2.png
- 输出：1672×941，RGB PNG；SHA-256：`da95a663832c5d81d95763fc09a25b5d4177583a32bb583debbaedfb459d2ff0`
- prompt 改动原因：与 r3 相同，无新调用；沿用 r3 实际完整 prompt。
- 人工图像修改：无。

画面内容 / 核验要点逐条检查：

- 直接复制选中的 ch03-05b-r3.png；不是一次额外生成，与 r3 的 SHA-256 相同。
- PAM 单段位于切口右侧上链，供体只在下通道，两种结果可辨；DNA 端点误差 0.224% <2%。
- 仍有 5.96% 框高差、轻微纹理/高光；RNA 与靶链配对的线条表达不够明确，应由确定性 PAM 插图澄清。
- 与 03c 尺寸相同，可并排比较；预期的供体复制或细胞核问题实际上未出现，正文标注必须改用实际问题。
- 共通核验：未见文字；像素宽度未达2400；约16:9；未真人复核。

实际完整 prompt（保留换行）：

```text
Edit the selected image. Change only one thing: make the two repair lanes the
same height, and draw the DNA in both lanes at the same horizontal position and
the same length, so the two results line up vertically for comparison. Keep
colors, objects and the top row unchanged. No text.

Minimal geometric operation on this 1672 by 941 image: the lower lane rectangle already spans approximately y=568 to y=768 (200 pixels). Move ONLY the TOP BORDER of the upper lane rectangle from approximately y=386 up to y=340, leaving its bottom border at approximately y=540 (also 200 pixels). The long DNA endpoints are already aligned closely enough: keep both long DNA drawings and their positions unchanged. Keep the separate donor above the lower DNA, all color marks and the entire top row unchanged. Upper outcome stays magenta-only; lower outcome stays teal-only with one separate donor. Do not make the two outcomes identical.
```


### figures/ch03/ch03-06-final-base-alt1.png

- 工具：Codex 内置 image_gen.imagegen（functions.exec 内 tools.image_gen__imagegen）
- 模型：不知道：工具未返回具体模型标识。
- 日期：2026-10-29
- 本阶段第几次：1
- 参考图：figures/ch03/ch03-05b-v3-revised.png
- 输出：1672×941，RGB PNG；SHA-256：`e86ceaaaf7ec3c699beacdb1a4a1a2736657fb6daa0e916e3b965d68cce53460`
- prompt 改动原因：未追加/改写规划英文 prompt；仅作规划要求的公共段拼接或 LAYOUT 占位替换。
- 人工图像修改：无。

画面内容 / 核验要点逐条检查：

- 落选；终稿留白第 1 次。上排向左移动，底部两通道内容保留。
- 右上仅约 23% 宽留白，第三步 DNA 仍侵入右 30% 区域；右侧分叉干线未随第三步连接位置一起移动，视觉上脱节。
- 未满足插图空间和顺畅路径要求；上排对象宽度亦有变化，违背严格的 keep sizes。
- 共通核验：未见文字；像素宽度未达2400；约16:9；未真人复核。

实际完整 prompt（保留换行）：

```text
Edit the selected image. Change only one thing: shift the three steps of the top
row to the left so that the right 30% of the top row is empty white space.
Keep sizes, colors and the two lower lanes unchanged. No text.
```


### figures/ch03/ch03-06-final-base.png

- 工具：Codex 内置 image_gen.imagegen（functions.exec 内 tools.image_gen__imagegen）
- 模型：不知道：工具未返回具体模型标识。
- 日期：2026-10-29
- 本阶段第几次：2
- 参考图：figures/ch03/ch03-05b-v3-revised.png
- 输出：1672×941，RGB PNG；SHA-256：`16aec379a84d184d28c4126cf997ddbe9dafa9adbb09fa42b2c708ffae1b1119`
- prompt 改动原因：保留终稿留白指令全文，追加空白矩形及连线位置；第一次留白不足且连接脱节。
- 人工图像修改：无。

画面内容 / 核验要点逐条检查：

- 保留；终稿留白第 2 次。三步压缩至左侧，折线从切割步骤接到右侧共同分叉，供体和两种结果保持。
- 实测右 30%（x≥1170）无遮挡高度为 301 px，即画布高的 31.99%；目标约 35%，略不足。右上 30%×35% 区域下缘有连接线，不可当作完全空白。
- DNA 两端最大误差 3 px，约 0.224%；两框高 201.5/213.0 px，相差 5.71%，并非严格等高。
- 上排对象较 05b 缩小、间距改变，属于未要求的变化；下排对象身份保留。仍有蓝色纹理和橙线高光，不是完全平涂。
- 灰度数值抽样：PAM 中位 RGB=(249,242,12)，亮度约226.88；供体=(1,164,144)，亮度约127.90。亮度差约98.98，且 PAM 有深色边界，可区分；这不是实际印刷验证。
- 仅为无字底图，标签、图例、PAM 矢量插图、6.5 pt 字号/174 mm 排版可读性均不在本轮完成范围，不能声称已验收。
- 共通核验：未见文字；像素宽度未达2400；约16:9；未真人复核。

实际完整 prompt（保留换行）：

```text
Edit the selected image. Change only one thing: shift the three steps of the top
row to the left so that the right 30% of the top row is empty white space.
Keep sizes, colors and the two lower lanes unchanged. No text.

Reserve the entire rectangle x=1170 to 1671, y=0 to 329 as EMPTY WHITE for a later inset; absolutely no DNA or connector in this rectangle. Arrange all three top-row steps to finish before x=1130. Keep the top-row process continuous: route the arrow from the cleavage DNA downward to y=335 and then rightward below the reserved rectangle to meet the existing two-way branch. Retain exactly one yellow PAM on the upper strand immediately right of the cleavage gap. Preserve both lower lanes, their separate donor and distinct magenta/teal outcomes.
```


### figures/ch03/ch03-06-final-base-alt2.png

- 工具：Codex 内置 image_gen.imagegen（functions.exec 内 tools.image_gen__imagegen）
- 模型：不知道：工具未返回具体模型标识。
- 日期：2026-10-29
- 本阶段第几次：3
- 参考图：figures/ch03/ch03-05b-v3-revised.png
- 输出：1672×941，RGB PNG；SHA-256：`fb8d7f5b1645f169255a44d6358b36bde182b1c10d263074b841fe53f0a9ff7a`
- prompt 改动原因：保留终稿留白指令全文，追加比例化留白与连线约束；第二次留白高度略不足。
- 人工图像修改：无。

画面内容 / 核验要点逐条检查：

- 落选；终稿留白第 3 次。右上留白增加到目标附近。
- 但第三步连接线改为只指向上方矩形，与右侧两分支干线脱节，破坏同一断裂、两条并列修复的路径。
- 下方两通道整体下移；尽管颜色身份保留，因拓扑副作用选回第 2 次。
- 共通核验：未见文字；像素宽度未达2400；约16:9；未真人复核。

实际完整 prompt（保留换行）：

```text
Edit the selected image. Change only one thing: shift the three steps of the top
row to the left so that the right 30% of the top row is empty white space.
Keep sizes, colors and the two lower lanes unchanged. No text.

Reserve a completely empty inset rectangle covering the RIGHT 30% of the canvas and the TOP 35% of its height. All three top-row steps must fit inside the LEFT 68% of the canvas. Connect the cleavage step to the two existing repair branches by a right-angle connector that travels DOWN first and then RIGHT, with its entire horizontal part immediately ABOVE the upper lane rectangle's top border. The horizontal connector must be BELOW the inset rectangle, not across it. Keep every lower-lane object, donor and outcome mark unchanged. Keep the cleavage PAM as ONE yellow segment on the upper strand, on the RIGHT side of the gap.
```


## 实测输出

以下为脚本直接读取文件所得，不是规划预期值。几何测量采用明确 ROI 的深色像素阈值；边框中心取覆盖率超过90%的行均值。差值统计包含图像重绘纹理，不等价于对象语义变化。

```text
$ ls -l figures/ch03/
total 48016
-rw-r--r--@ 1 zeroone  staff     3982 Oct 29 16:10 ch03-01-reading-order-en.tex
-rw-r--r--@ 1 zeroone  staff     4085 Oct 29 16:10 ch03-01-reading-order-zh.tex
-rw-r--r--@ 1 zeroone  staff     1233 Oct 29 16:08 ch03-02-three-sketches-en.tex
-rw-r--r--@ 1 zeroone  staff     1269 Oct 29 16:08 ch03-02-three-sketches-zh.tex
-rw-r--r--@ 1 zeroone  staff  2382319 Oct 29 16:11 ch03-02a-sketch-linear.png
-rw-r--r--@ 1 zeroone  staff  2182569 Oct 29 16:11 ch03-02b-sketch-hub-alt1.png
-rw-r--r--@ 1 zeroone  staff  2447360 Oct 29 16:11 ch03-02b-sketch-hub.png
-rw-r--r--@ 1 zeroone  staff  2317470 Oct 29 16:11 ch03-02c-sketch-branch-alt1.png
-rw-r--r--@ 1 zeroone  staff  2199212 Oct 29 16:11 ch03-02c-sketch-branch-alt2.png
-rw-r--r--@ 1 zeroone  staff  2343218 Oct 29 16:11 ch03-02c-sketch-branch.png
-rw-r--r--@ 1 zeroone  staff     1533 Oct 29 16:09 ch03-03-three-candidates-en.tex
-rw-r--r--@ 1 zeroone  staff     1533 Oct 29 16:09 ch03-03-three-candidates-zh.tex
-rw-r--r--@ 1 zeroone  staff  1045115 Oct 29 16:14 ch03-03a-cand-linear.png
-rw-r--r--@ 1 zeroone  staff  1085445 Oct 29 16:14 ch03-03b-cand-hub-alt1.png
-rw-r--r--@ 1 zeroone  staff  1090641 Oct 29 16:14 ch03-03b-cand-hub-alt2.png
-rw-r--r--@ 1 zeroone  staff  1109512 Oct 29 16:14 ch03-03b-cand-hub.png
-rw-r--r--@ 1 zeroone  staff  1111858 Oct 29 16:14 ch03-03c-cand-branch.png
-rw-r--r--@ 1 zeroone  staff     2692 Oct 29 16:09 ch03-04-layout-comparison-en.tex
-rw-r--r--@ 1 zeroone  staff     2673 Oct 29 16:09 ch03-04-layout-comparison-zh.tex
-rw-r--r--@ 1 zeroone  staff      840 Oct 29 16:09 ch03-05a-v1-issues-en.tex
-rw-r--r--@ 1 zeroone  staff      840 Oct 29 16:09 ch03-05a-v1-issues-zh.tex
-rw-r--r--@ 1 zeroone  staff  1245218 Oct 29 16:19 ch03-05b-v3-revised.png
-rw-r--r--@ 1 zeroone  staff  1375060 Oct 29 16:20 ch03-06-final-base-alt1.png
-rw-r--r--@ 1 zeroone  staff  1394046 Oct 29 16:23 ch03-06-final-base-alt2.png
-rw-r--r--@ 1 zeroone  staff  1163589 Oct 29 16:20 ch03-06-final-base.png
-rw-r--r--@ 1 zeroone  staff      856 Oct 29 16:09 ch03-06-final-en.tex
-rw-r--r--@ 1 zeroone  staff      871 Oct 29 16:09 ch03-06-final-zh.tex
-rw-r--r--@ 1 zeroone  staff     1901 Oct 29 16:09 ch03-07-pam-inset-en.tex
-rw-r--r--@ 1 zeroone  staff     1886 Oct 29 16:09 ch03-07-pam-inset-zh.tex

$ PNG pixel dimensions (Pillow read + verify)
figures/ch03/ch03-02a-sketch-linear.png	1672 x 941	RGB	2382319 bytes
figures/ch03/ch03-02b-sketch-hub-alt1.png	1672 x 941	RGB	2182569 bytes
figures/ch03/ch03-02b-sketch-hub.png	1672 x 941	RGB	2447360 bytes
figures/ch03/ch03-02c-sketch-branch-alt1.png	1672 x 941	RGB	2317470 bytes
figures/ch03/ch03-02c-sketch-branch-alt2.png	1672 x 941	RGB	2199212 bytes
figures/ch03/ch03-02c-sketch-branch.png	1672 x 941	RGB	2343218 bytes
figures/ch03/ch03-03a-cand-linear.png	1672 x 941	RGB	1045115 bytes
figures/ch03/ch03-03b-cand-hub-alt1.png	1672 x 941	RGB	1085445 bytes
figures/ch03/ch03-03b-cand-hub-alt2.png	1672 x 941	RGB	1090641 bytes
figures/ch03/ch03-03b-cand-hub.png	1672 x 941	RGB	1109512 bytes
figures/ch03/ch03-03c-cand-branch.png	1672 x 941	RGB	1111858 bytes
figures/ch03/ch03-05b-v3-revised.png	1672 x 941	RGB	1245218 bytes
figures/ch03/ch03-06-final-base-alt1.png	1672 x 941	RGB	1375060 bytes
figures/ch03/ch03-06-final-base-alt2.png	1672 x 941	RGB	1394046 bytes
figures/ch03/ch03-06-final-base.png	1672 x 941	RGB	1163589 bytes
provenance/ch03/ch03-05b-r1-alt1.png	1672 x 941	RGB	1418615 bytes
provenance/ch03/ch03-05b-r1.png	1672 x 941	RGB	1473993 bytes
provenance/ch03/ch03-05b-r2-alt1.png	1672 x 941	RGB	1471157 bytes
provenance/ch03/ch03-05b-r2.png	1672 x 941	RGB	1475263 bytes
provenance/ch03/ch03-05b-r3-alt1.png	1672 x 941	RGB	1431122 bytes
provenance/ch03/ch03-05b-r3-alt2.png	1672 x 941	RGB	1309372 bytes
provenance/ch03/ch03-05b-r3.png	1672 x 941	RGB	1245218 bytes

$ Geometry measurement
{
  "ch03-03c-cand-branch": {
    "dna_bboxes_xyxy": [
      [
        96,
        443,
        1436,
        492
      ],
      [
        94,
        684,
        1432,
        734
      ]
    ],
    "frame_rows": [
      387.0,
      540.0,
      569.0,
      767.0
    ],
    "frame_heights": [
      153.0,
      198.0
    ],
    "frame_height_difference_percent": 29.41176470588236,
    "dna_endpoint_max_error_px": 4,
    "dna_endpoint_error_percent": 0.2985074626865672
  },
  "ch03-05b-v3-revised": {
    "dna_bboxes_xyxy": [
      [
        95,
        443,
        1435,
        493
      ],
      [
        94,
        698,
        1432,
        748
      ]
    ],
    "frame_rows": [
      356.0,
      557.5,
      583.0,
      796.5
    ],
    "frame_heights": [
      201.5,
      213.5
    ],
    "frame_height_difference_percent": 5.955334987593042,
    "dna_endpoint_max_error_px": 3,
    "dna_endpoint_error_percent": 0.22388059701492538
  },
  "ch03-06-final-base": {
    "dna_bboxes_xyxy": [
      [
        95,
        444,
        1435,
        493
      ],
      [
        93,
        698,
        1432,
        747
      ]
    ],
    "frame_rows": [
      356.0,
      557.5,
      583.0,
      796.0
    ],
    "frame_heights": [
      201.5,
      213.0
    ],
    "frame_height_difference_percent": 5.707196029776673,
    "dna_endpoint_max_error_px": 3,
    "dna_endpoint_error_percent": 0.22388059701492538,
    "right_30_percent_clear_height_px": 301,
    "right_30_percent_clear_height_percent": 31.987247608926673,
    "grayscale_samples": {
      "PAM": {
        "roi_xyxy": [
          928,
          220,
          958,
          232
        ],
        "median_rgb": [
          249.0,
          242.0,
          12.0
        ],
        "luma": 226.88219999999998
      },
      "donor": {
        "roi_xyxy": [
          710,
          648,
          735,
          670
        ],
        "median_rgb": [
          1.0,
          164.0,
          144.0
        ],
        "luma": 127.90219999999998
      }
    }
  }
}

$ Revision pixel comparison
{
  "r1": {
    "changed_pixels_percent": 3.714426269518836,
    "top_row_changed_percent": 4.016547049441786,
    "threshold": "max absolute RGB channel difference > 15/255"
  },
  "r2": {
    "changed_pixels_percent": 4.100608128378138,
    "top_row_changed_percent": 3.531698564593302,
    "threshold": "max absolute RGB channel difference > 15/255"
  },
  "r3": {
    "changed_pixels_percent": 13.688799454921721,
    "top_row_changed_percent": 7.286483253588518,
    "threshold": "max absolute RGB channel difference > 15/255"
  }
}
```
