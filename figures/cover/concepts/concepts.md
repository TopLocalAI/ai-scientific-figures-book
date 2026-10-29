# 《用 AI 画好科研图》封面主视觉方案

生成与检查日期：2026-10-29。

## 交付与生成方式

本目录交付三张无文字 PNG 和本说明。选用 A 的第二次生成、B 和 C 的第一次生成；共调用四次内置图像生成，没有使用子代理，没有执行 commit 或 push。

- 生成工具：内置 `image_gen.imagegen`（本会话实际工具调用标识：`image_gen__imagegen`），经 `functions.exec` 调用。
- 具体图像模型：不知道；工具返回内容未提供模型名称或版本，不据此推断。
- 生成参数：每次均以完整提示词作为 `prompt`，`transparent_background=false`；均为全新生成，没有传入参考图片。
- 分辨率：三张实际输出均为 **1024 × 1536 像素，2:3 竖版**。提示词要求最高可用原生竖版分辨率，并提出 2048 × 3072 或更高，但当前工具接口没有独立的尺寸、质量或模型选择参数，实际未返回该更高尺寸，不能声称交付为 2K / 300 dpi 印刷终稿。没有插值放大、裁剪或图像后期编辑。
- 图像先由内置工具自动保存到其默认缓存，选定原图再原样复制进本目录；所有主动创建的项目交付文件均位于本目录。
- 数据曲线、散点及细胞是封面概念示意，未使用实测研究数据，不代表具体研究结论。

## 看图检查与实际问题

已打开保存后的三张本地文件，逐张检查整体构图、细胞与分子区域、箭头、曲线和轴线、图层边缘及留白。以下无文字结论来自人工视觉检查，不冒充 OCR 检测结果；留白比例为目测近似值。

| 文件 | 实际尺寸 | 文字 / 伪文字 | 留白与主体位置 | 看图后发现的问题 |
| --- | --- | --- | --- | --- |
| concept-a-sketch-to-figure.png | 1024 × 1536 | 未见可读文字、字母、数字、伪文字、Logo 或水印；线粒体内部为结构线，非文字 | 最高的曲线轴线约从画面高度 44% 开始；上方 40% 干净。草图在左下、成图在右侧，过渡方向正确 | 第二版较首版扁平，但色面仍有轻微纹理和色差，未达到完全纯色矢量效果；暖色点缀略多，曲线实际有两条。右侧细胞较大，右边距约 6%，左下草图边缘也有较淡辅助线 |
| concept-b-layers.png | 1024 × 1536 | 未见文字、伪文字、图版字母、刻度数字、Logo 或水印 | 最高面板约从画面高度 40% 开始，上方 35% 干净；三个面板居中，底层散点、中层机制、上层四格组图关系明确 | 面板上的散点和细胞纹理比提示词更密；背景有轻微明暗变化，并非严格单色。最下面板底角距底边约 5%，后续适配出血比例时需保留该角；发光较克制但仍比 A/C 更有科技感 |
| concept-c-minimal.png | 1024 × 1536 | 未见文字、伪文字、标签、Logo 或水印；圆环为明确几何图元 | 主体最高点约从画面高度 57% 开始，上半部留白充足；图形为下半部的横向序列，未发生意外偏位 | 主体纵向占比小，气质安静但视觉冲击力较弱；生成了五段箭头，较提示词预想更多。底色与圆点有极轻微纹理/色差，未达到数学意义的纯色平面，没有明显投影或三维厚度 |

三张均保留为无文字概念图，书名和其他文字后续由 LaTeX 排版叠加。原图为 2:3，与含出血 176 × 246 mm 的比例不同，正式排版仍需确定适配方式；尤其 B 不宜未经检查直接裁掉底边。

### A 首版淘汰原因

首版未发现文字或伪文字，但小曲线顶部约在画面高度 38% 处，侵入目标上方 40% 留白；分子节点和细胞也出现较明显立体高光。第二次重新生成后留白与扁平程度改善，因此只将第二版交付为 `concept-a-sketch-to-figure.png`。首版未复制进交付目录，未对其默认缓存做修改。

## 实测输出

工作目录：`figures/cover/concepts`。

### PNG 文件存在：ls -l

实际执行的有界命令：

```sh
perl -e 'alarm 20; exec @ARGV' -- ls -l concept-a-sketch-to-figure.png concept-b-layers.png concept-c-minimal.png
```

原始输出：

```text
-rw-r--r--@ 1 zeroone  staff  1270663 Oct 29 15:34 concept-a-sketch-to-figure.png
-rw-r--r--@ 1 zeroone  staff  1602825 Oct 29 15:34 concept-b-layers.png
-rw-r--r--@ 1 zeroone  staff   948589 Oct 29 15:34 concept-c-minimal.png
```

### 每张图的像素尺寸：sips

实际执行的有界命令：

```sh
perl -e 'alarm 20; exec @ARGV' -- sips -g pixelWidth -g pixelHeight concept-a-sketch-to-figure.png concept-b-layers.png concept-c-minimal.png
```

原始输出：

```text
figures/cover/concepts/concept-a-sketch-to-figure.png
  pixelWidth: 1024
  pixelHeight: 1536
figures/cover/concepts/concept-b-layers.png
  pixelWidth: 1024
  pixelHeight: 1536
figures/cover/concepts/concept-c-minimal.png
  pixelWidth: 1024
  pixelHeight: 1536
```

另以 Python 读取 PNG 签名和 IHDR 尺寸，三张均通过；逐字节比较交付文件与选定的工具原图，三张完全相同。下面是每次真实传给工具的完整提示词，没有将最终提示词概括或删节。

## A：从草图到成图（交付为第二版）

文件：`concept-a-sketch-to-figure.png`  
生成工具：`image_gen__imagegen`；具体模型：不知道。  
选定原图：`codex-output/exec-37f6a964-2433-4ee8-9f7a-8620d781a6f4.png`

完整实际提示词：

```text
Use case: stylized-concept.
Asset type: image-only cover artwork for a refined academic book. Single portrait canvas, no book mockup.
Resolution and format: generate at the highest native portrait resolution available, preferably 2048 x 3072 pixels or larger, with a 2:3 width-to-height aspect ratio.
Background: uniform very pale off-white #F1F6F5.
Composition is critical: the TOP 45 PERCENT OF THE ENTIRE CANVAS MUST BE COMPLETELY EMPTY PALE BACKGROUND. All marks must stay in the bottom 55 percent. The highest edge of any object, including the small graph, begins only halfway down the canvas at y=50 percent. Keep every part of the artwork at least 8 percent of canvas width away from the left and right edges and at least 8 percent of canvas height above the bottom.
Primary image: a delicate scientific pencil sketch at lower left gradually becomes a polished flat vector scientific figure toward upper right, but this whole diagonal progression takes place exclusively in the lower half of the cover. Use a compact coherent assembly of a lightly sketched cell outline, a few circle-and-bond molecular shapes and clear arrows at lower left. The same pictorial forms progress through a subtle graphite-to-color transition into a clean teal flat cell diagram at middle right. Place one small simple unlabeled line graph above the finished cell, entirely below y=50 percent. The graph is a minor accent, not a large feature. Make the visual transition continuous and elegant, without frames, cards or dividing lines.
Finished illustration style: truly FLAT vector-like color areas with crisp consistent outlines. The finished cell has a pale teal solid interior, a flat teal circular nucleus and a few simple flat organelle contours. Molecular nodes are matte solid circles. No shiny spheres, no highlights, no volumetric rendering, no watercolor, no 3D shading, no gradients in the colored scientific artwork. The graphite sketch end may have delicate pencil texture, but no dense messy scribbling.
Palette: teal #176C68, deep ink #23363E and soft graphite gray against #F1F6F5. Only two or three small muted coral accents.
Mood: precise, calm, intellectually clear, beautifully restrained, high-quality academic publishing.
Absolutely no text anywhere: no title, letters, digits, chemical element letters, math symbols, labels, captions, handwriting, pseudo-writing, tiny fake text, logos, watermarks, signatures. Graph axes have no ticks or labels. Molecules are only circles and bonds. No mark may resemble a handwritten annotation.
Avoid robots, brains, gears, lightbulbs, cyberpunk, glow, neon, real pencils, hands, book mockups, typography, overcomplicated biological detail, heavy texture, any object in the top 45 percent.
```

## B：图层拆解

文件：`concept-b-layers.png`  
生成工具：`image_gen__imagegen`；具体模型：不知道。  
选定原图：`codex-output/exec-10395362-d077-414a-8113-88ffcf029ae0.png`

完整实际提示词：

```text
Use case: stylized-concept.
Asset type: original full-bleed portrait artwork for an elegant scientific publishing book cover, artwork only, not a book mockup.
Canvas: use the highest available native portrait resolution, ideally 2048 x 3072 pixels or higher at a 2:3 width-to-height aspect ratio. A single portrait image.
Background: a uniform deep ink field #23363E, quiet and refined.
Primary request: an isometric exploded stack of exactly three delicate translucent glass-like rectangular panels in the lower two-thirds of the cover, separated vertically by generous visible air gaps, sharing one parallel isometric orientation. Lowest panel: a beautifully simple scatter plot made of unlabeled thin axes and a restrained cloud of small teal and pale cyan points. Middle panel: a clean scientific mechanism / flow diagram using a few circular biological nodes, a minimal stylized cell and clear connecting arrows. Top panel: an elegant multi-panel scientific paper figure layout, a clearly organized 2-by-2 grid of thin compartments containing very sparse miniature unlabeled scientific diagram and data-curve marks. This is a paper figure composition, not a dashboard or interface.
Composition: the entire top 35 percent must remain clean uninterrupted dark ink background with no objects, light bloom, particles or markings, ready for later title typesetting. Keep all panel corners below y=39%. Place the stack centered horizontally, spanning about x=12%-88% and y=41%-90%; all three layers fully visible, comfortably inset from edges.
Style and lighting: precise editorial 3D/isometric scientific illustration with subtle translucency, thin restrained teal and pale cyan luminous edges, soft understated glow confined to panel edges. Confident geometry, quiet contrast, premium academic publishing. Glass sheets are thin and airy, not thick slabs; no circuitry.
Palette: #23363E deep ink background, #176C68 teal and pale cyan lines, very sparse soft off-white detail.
Text constraint: absolutely no letters, words, numbers, mathematical symbols, chemical element symbols, panel labels, axis ticks, tick labels, captions, pseudo-text, pseudo-writing, logos, signatures or watermarks anywhere. Every graph is unlabeled. Grid compartments contain only actual pictorial dots, curves, circles and arrows, no text-like dashes or simulated paragraphs.
Avoid: cyberpunk, futuristic dashboards, interfaces, HUDs, sci-fi brains, robots, gears, lightbulbs, giant glow halos, neon purple, decorative floating particles, busy circuitry, over-dense charts, typographic ornament, frames around the overall cover, realistic book mockups.
```

## C：极简几何

文件：`concept-c-minimal.png`  
生成工具：`image_gen__imagegen`；具体模型：不知道。  
选定原图：`codex-output/exec-f5a6ece9-ed1a-487f-b56b-21c619706a06.png`

完整实际提示词：

```text
Use case: stylized-concept.
Asset type: original full-bleed portrait artwork for an elegant academic book cover, pure visual artwork only, not a book mockup.
Canvas: use the highest available native portrait resolution, ideally 2048 x 3072 pixels or higher at a 2:3 width-to-height aspect ratio. A single portrait image.
Background: uniform warm off-white, close to #F5F3ED.
Primary request: extremely restrained Swiss editorial geometric design that abstracts the relationship of research ideas becoming a clear scientific figure. In the lower half, just a small purposeful group of solid circular nodes, two thin directional arrows, one larger open circular ring and one fine data curve create a disciplined left-to-right progression. Begin with three or four small circular nodes, connect them through clear arrow geometry toward a single crisp open ring, and conclude with a delicate smooth data curve over two short unlabeled perpendicular axis lines. One tiny coral circular node provides the only warm accent. Every element has a role; avoid additional decoration.
Composition: the entire upper half, from y=0% through y=50%, must be completely empty warm off-white, reserved for title typesetting. Place the abstract motif well within the lower half, roughly x=14%-86%, y=58%-83%, optically balanced with ample empty space around and below. Asymmetric yet carefully aligned Swiss editorial rhythm, lucid geometric spacing, strong shape hierarchy, quiet confidence.
Style: exceptionally crisp flat vector-like geometry, uniform fine strokes and small solid disks, refined academic editorial design. Entirely two dimensional, no shadows, no textures, no gradients, no depth, no glass, no lighting effects.
Palette: teal #176C68 and deep ink #23363E on warm off-white; one small coral #D97865 accent occupying less than one percent of the image.
Text constraint: absolutely no typography, letters, words, digits, mathematical symbols, chemical notation, labels, pseudo-text, writing-like marks, logos, signatures or watermarks. Curves and axes must be unlabeled and have no tick marks. Do not depict written formulas. The ring and nodes are clearly diagram geometry, never arranged to resemble text.
Avoid: too many nodes, crowded networks, decorative confetti, visual noise, generic stock icons, cyberpunk, glowing brains, robots, gears, lightbulbs, book mockups, 3D rendering.
```

## 附录：A 首版完整实际提示词（未选用）

生成工具：`image_gen__imagegen`；具体模型：不知道。  
未选用原图：`codex-output/exec-ad0c5a98-7662-4b60-b2ea-f718fa29c091.png`

```text
Use case: stylized-concept.
Asset type: original full-bleed portrait artwork for an elegant academic book cover, artwork only, not a book mockup.
Canvas: use the highest available native portrait resolution, ideally 2048 x 3072 pixels or higher at a 2:3 width-to-height aspect ratio. A single portrait image.
Background: very light warm white / pale gray, close to #F1F6F5.
Primary request: "from sketch to scientific figure." A coherent scientific drawing evolves naturally along an ascending diagonal from the lower left toward the middle right. At the lower-left end, delicate graphite pencil linework depicts a simplified biological cell, a few molecule-like circles connected by bonds, and two clear directional arrows. Progressing along the same composition, graphite strokes gradually resolve into precise, clean, beautifully proportioned flat vector-style scientific illustration: teal cell outlines, a restrained mechanism of small molecular nodes and arrows, plus one compact elegant data line plot near the right end. No drawing tools or realistic objects. Keep the transition organic and visually continuous, with no dividing line, no frame and no separate cards.
Composition: reserve the entire upper 40 percent of the canvas as completely clean, uninterrupted pale background for later title typesetting. Every mark, arrow, cell, graph and pencil stroke must be below 42 percent of canvas height. The diagonal artwork spans approximately x=10%-90%, y=44%-89%, with its pencil end at lower left and its polished end at upper right within that lower artwork area. Maintain generous breathing room at all edges.
Style: refined scientific editorial illustration, subtle pencil texture transitioning to crisp flat vector-like edges; meticulous restrained detail, calm, clear, credible, high-quality academic publishing.
Palette: dominant teal #176C68, deep ink #23363E, soft graphite gray, pale background #F1F6F5; only two or three tiny warm coral accents.
Text constraint: absolutely no text, letters, numbers, chemical element symbols, mathematical symbols, captions, labels, pseudo-writing, scribbles resembling handwriting, logos, signatures or watermarks anywhere. Graph axes must be unlabeled, without ticks or tick labels; draw just simple axes and one smooth curve. Molecular diagrams must use only circles and connecting strokes, no letter-like shapes. Pencil content must be purely pictorial and structural.
Avoid: typography of any kind, decorative borders, excessive complexity, stock clip-art, cyberpunk, neon effects, science-fiction brains, robots, gears, lightbulbs, gradients in the flat vector area, heavy shadows, photorealistic glass, hands, pencils, book mockups.
```

