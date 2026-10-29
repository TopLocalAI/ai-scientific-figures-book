# 第07章 Codex 图像生成与核验记录

记录日期：2026-10-29。任务来源：`ch07-codex.md`。规划：`production/plans/ch07.md` 的图清单 FIG 07、FIG 08；规范：`production/book-spec.md` 第4、5节。

## 范围与实际方法

本轮仅生成 FIG 07、FIG 08 的 PNG 底图，每张恰好生成3次，共6张不同图像。未启动子 agent，未 commit/push，未生成复用图、TikZ标签、充放电叠加层或“一句话尝试”。使用 imagegen 技能及内置 `image_gen.imagegen`（调用名 `tools.image_gen__imagegen`，由 `functions.exec` 调度），具体模型**不知道**，工具结果只披露图像与缓存路径，没有模型标识。未使用第三方生成服务或CLI/API回退。

每次调用的 `transparent_background=false`；没有提供参考图，也没有设置 `referenced_image_paths` 或 `num_last_images_to_include`。各轮分别生成，前一轮只用于看图与决定是否追加纠正约束。原英文prompt中的16:9与最低像素宽度均保留。首次逐字使用规划；第2、3次只追加说明，完整实际文本逐文件列在下文。

生成器自动保存于工具缓存目录。交付PNG由该缓存文件原样复制，没有缩放、裁切、补边、重画、锐化或重新编码；尺寸与SHA-256核验见后文。只在 `figures/ch07/` 与 `provenance/ch07/` 写入本任务文件；shell命令以Python `signal.alarm(20/25/30)` 限时，子进程ls另设20秒超时；图像工具调用使用120秒yield窗口，均在约48–53秒内返回，没有无限前台等待。

## 选图结果与未达标项

| 图 | 最终路径 | 选中轮次 | 其余轮次 |
|---|---|---|---|
| FIG 07 | figures/ch07/ch07-07-battery-errors.png | 第3次 | 第1次alt1；第2次alt2 |
| FIG 08 | figures/ch07/ch07-08-battery-base.png | 第2次 | 第1次alt1；第3次alt2 |

六张均为 **1672×941**，实际比值1.7768331562，与16:9的相对偏差约0.053135%。FIG 07未达到1920像素最低宽度，FIG 08未达到2400像素最低宽度；追加2560×1440要求两次仍未生效。两图各已达3次上限，未通过插值放大伪装原生分辨率。因此这些是**已选定并交付的候选底图，不能标为完全符合规划的终稿**。

所选FIG 07呈现四种指定科学错误，内部6个橙色离子与外导线3个橙色离子数目正确，所有箭头向右。所选FIG 08层序与集流体对应正确、无过程元素，但隔膜孔隙的浅蓝填充不完全一致；两个主图仍有坐标偏差、轻微填充斑驳与接近白而非严格纯白的背景。全部看图未发现文字标签、伪文字行、数字、+/−或水印。这里的无字结论来自看图，不是伪称OCR检测或同行签字。

生成期间其他任务在同目录写入了复用图片、TeX及主文件名；当时两个主PNG的SHA-256与本轮第1次输出（已保存alt1）完全相同。经哈希确认仅为本轮首张图的副本后，将这两个指定主路径更新为上述选定候选；第1次原图仍保存在alt1中。本轮未改动其他任务的复用图片、TeX或记录。**已有标签层可能按首轮坐标制作，需排版任务针对最终主PNG重新定位与检查；本轮没有验证这些TeX。**

## 后续叠加层验收边界

| 规划核验项 | 本轮结论 |
|---|---|
| S1层序、S2集流体 | FIG 08正确；FIG 07按教学要求故意错误 |
| S3电解液位置 | 所选FIG 08没有独立液体层；孔隙浅蓝不均匀，严格连续性未完全通过 |
| S4充电Li⁺、S5充电电子、S6放电方向 | FIG 08纯结构底图没有这些元素，须在叠加层中核验；本轮未做 |
| S7离子路径 | FIG 07故意在外电路画Li⁺；FIG 08没有离子，叠加后才可核对路径 |
| S8中英命名 | 底图无字，须在叠加层与图注核验 |
| (a)(b)共用底图与哈希 | 本轮只交付一个FIG 08结构底图；未生成/核验两面板文件，不能声称两面板哈希已经比对 |
| Li⁺不越出电池、电子不进入内部 | 后续箭头叠加层核验，未完成 |
| 充电器/负载文字与状态一致 | 后续标签层核验，未完成 |
| 电化学同行复核与签字 | 尚未进行；不得写“全部通过”或代签 |

以下所有坐标是看图后的近似定位，原点在左上，x/y分别按图宽/图高归一化；不等于精密测绘。粒子轮廓本身的孔洞/弧线不应冒称为文字识别结果。

## ch07-07-battery-errors-alt1.png

- 图：FIG 07（故意错误反例）；生成第1次；未选中，保留备选。
- 路径：`figures/ch07/ch07-07-battery-errors-alt1.png`
- 工具：image_gen.imagegen (tools.image_gen__imagegen via functions.exec)
- 具体模型：不知道（工具返回中未披露具体模型）
- 工具缓存原图：`codex-output/exec-4a3e29ec-67d3-44aa-a35a-249f98826cdc.png`
- 尺寸：1672×941；文件字节数：1464675。
- SHA-256：`88aa7dd037e44e44b69438be75b73a565e2ce4a684a51cc379d7724ca32bc08e`
- 提示词改动与原因：规划中的英文代码块逐字使用，未改写、未补充。

### 实际使用的完整prompt（逐字）

```text
Flat 2D cross-section schematic of a single cell unit of a lithium-ion pouch
battery, landscape 16:9, at least 1920 px wide, pure white background, clean
vector illustration, flat fills, thin dark gray (#3A3A3A) outlines, no
gradients, no shadows, no highlights, no 3D, no texture.

ABSOLUTELY NO TEXT: no letters, no words, no numbers, no symbols such as "+"
or "-", no labels, no legend, no title, no watermark.

This is a deliberately WRONG teaching example. Draw the layers exactly in the
order given, even though it is not the real order.

LAYERS, drawn as vertical bands side by side, filling x 0.14-0.86 and
y 0.25-0.85 of the image (x from left, y from top), from left to right:
1. Outer pouch film: thin light gray band (#C9C9C9) with a darker inner line,
   x 0.14-0.16.
2. Aluminium foil: thin solid light silver-gray band (#B5B9BE), x 0.19-0.21,
   with a narrow silver tab rising from its top edge to y 0.10.
3. Graphite layer: x 0.21-0.42, many small dark charcoal (#4A4A4A) flat
   flake-shaped particles stacked roughly horizontally.
4. Oxide layer: x 0.42-0.63, many rounded clustered spherical particles in
   muted slate blue (#6F86A6), touching the graphite flakes directly with no
   gap and nothing in between.
5. Separator: x 0.63-0.75, a white band with many tiny round pores and a light
   gray outline.
6. Copper foil: thin solid copper-colored band (#B87333), x 0.75-0.77, with a
   narrow copper tab rising from its top edge to y 0.10.
7. Outer pouch film: thin light gray band, x 0.84-0.86.
Fill the gaps between particles in layers 3 and 4 with a very pale blue
(#E3F0F8).

IONS AND ARROWS:
- Six small solid orange (#D9822B) spheres inside the graphite and oxide
  layers, each with a short solid orange arrow pointing to the RIGHT, moving
  from the graphite layer toward the oxide layer.
- One thin dark gray wire above the cell connecting the top of the silver tab
  to the top of the copper tab at y 0.06. Place three small orange spheres ON
  the wire, each with a small orange arrow pointing along the wire.
No other arrows, no battery symbol, no plus or minus signs.

Bottom 10% of the image left empty.
```

### 看图后逐项核验

1. 层序：外壳膜—银灰铝集流体—炭灰片状石墨—灰蓝圆颗粒正极—白色多孔隔膜—铜色集流体—外壳膜，符合指定的错误层序。
2. 错误①（S2）：负极侧是银灰铝箔，正极侧是铜色箔，集流体对调确实存在；两侧极耳颜色与各自箔一致。
3. 错误②（S1）：石墨与灰蓝颗粒层直接相邻，界面没有隔膜；可见局部颗粒边缘接触。白色多孔隔膜错放在正极与右侧集流体之间。
4. 错误③（S4）：电极内恰有六个橙色圆点，各有一根向右的短箭头，方向为石墨→正极。底图没有“充电”文字，须由后续标签层设定充电语境；未提前声称带标题面板已核验。
5. 错误④（S7）：顶部导线连接两极耳；导线上恰有三个橙色圆点，各配向右的橙色箭头，明确体现把 Li⁺ 画到外电路的指定错误。
6. 额外对象：未见额外离子箭头、电池符号、充电器、负载或其他过程支路。视觉检查未发现第五类明确科学错误；这不代替电化学同行复核。
7. 无字检查：看图未发现文字、字母标签、数字、伪文字行、+/−号、图例文字或水印。多孔带中个别圆圈未闭合，属于孔轮廓绘制瑕疵，不是文字标签。
8. 留白：底部至少10%没有对象。整体为二维横向截面，能看清七个层位；有轻微填充斑驳，背景不是逐像素纯白，未严格满足纯色、无纹理要求。
9. 坐标（目测近似）：层体 y≈0.166–0.805，明显高于要求的0.25–0.85；右铜箔 x≈0.785–0.806，比规定0.75–0.77偏右。导线 y≈0.064 接近0.06。
10. 与正例对比：石墨和正极层的总视觉宽度可比较，但两图层体顶边不齐，不能直接沿用同一标签坐标。
11. 落选原因：四种指定错误均成立，但层体顶部漂移比第3次明显。
12. 像素与宽高比：1672×941；未达到规划最低宽度，非数学上精确16:9。无后期改尺寸；在3次上限后如实保留这一未达标项。

## ch07-07-battery-errors-alt2.png

- 图：FIG 07（故意错误反例）；生成第2次；未选中，保留备选。
- 路径：`figures/ch07/ch07-07-battery-errors-alt2.png`
- 工具：image_gen.imagegen (tools.image_gen__imagegen via functions.exec)
- 具体模型：不知道（工具返回中未披露具体模型）
- 工具缓存原图：`codex-output/exec-808b35de-9c87-41d9-9ec0-1ca2eacb130b.png`
- 尺寸：1672×941；文件字节数：1431517。
- SHA-256：`4fd399ef5e9a2c06bb958536d5612591f310980fc49dfc650abeaf5f140361f2`
- 提示词改动与原因：规划英文代码块完整保留，仅在末尾追加OUTPUT RESOLUTION段。原因：第1次实际输出1672×941，低于要求；请求2560×1440以同时满足两图最低宽度及16:9。结果尺寸要求未生效。

### 实际使用的完整prompt（逐字）

```text
Flat 2D cross-section schematic of a single cell unit of a lithium-ion pouch
battery, landscape 16:9, at least 1920 px wide, pure white background, clean
vector illustration, flat fills, thin dark gray (#3A3A3A) outlines, no
gradients, no shadows, no highlights, no 3D, no texture.

ABSOLUTELY NO TEXT: no letters, no words, no numbers, no symbols such as "+"
or "-", no labels, no legend, no title, no watermark.

This is a deliberately WRONG teaching example. Draw the layers exactly in the
order given, even though it is not the real order.

LAYERS, drawn as vertical bands side by side, filling x 0.14-0.86 and
y 0.25-0.85 of the image (x from left, y from top), from left to right:
1. Outer pouch film: thin light gray band (#C9C9C9) with a darker inner line,
   x 0.14-0.16.
2. Aluminium foil: thin solid light silver-gray band (#B5B9BE), x 0.19-0.21,
   with a narrow silver tab rising from its top edge to y 0.10.
3. Graphite layer: x 0.21-0.42, many small dark charcoal (#4A4A4A) flat
   flake-shaped particles stacked roughly horizontally.
4. Oxide layer: x 0.42-0.63, many rounded clustered spherical particles in
   muted slate blue (#6F86A6), touching the graphite flakes directly with no
   gap and nothing in between.
5. Separator: x 0.63-0.75, a white band with many tiny round pores and a light
   gray outline.
6. Copper foil: thin solid copper-colored band (#B87333), x 0.75-0.77, with a
   narrow copper tab rising from its top edge to y 0.10.
7. Outer pouch film: thin light gray band, x 0.84-0.86.
Fill the gaps between particles in layers 3 and 4 with a very pale blue
(#E3F0F8).

IONS AND ARROWS:
- Six small solid orange (#D9822B) spheres inside the graphite and oxide
  layers, each with a short solid orange arrow pointing to the RIGHT, moving
  from the graphite layer toward the oxide layer.
- One thin dark gray wire above the cell connecting the top of the silver tab
  to the top of the copper tab at y 0.06. Place three small orange spheres ON
  the wire, each with a small orange arrow pointing along the wire.
No other arrows, no battery symbol, no plus or minus signs.

Bottom 10% of the image left empty.

OUTPUT RESOLUTION: Generate the actual PNG at 2560 x 1440 pixels, exactly 16:9. The delivered raster must be 2560 pixels wide and 1440 pixels high; preserve every content requirement above.
```

### 看图后逐项核验

1. 层序：外壳膜—银灰铝集流体—炭灰片状石墨—灰蓝圆颗粒正极—白色多孔隔膜—铜色集流体—外壳膜，符合指定的错误层序。
2. 错误①（S2）：负极侧是银灰铝箔，正极侧是铜色箔，集流体对调确实存在；两侧极耳颜色与各自箔一致。
3. 错误②（S1）：石墨与灰蓝颗粒层直接相邻，界面没有隔膜；可见局部颗粒边缘接触。白色多孔隔膜错放在正极与右侧集流体之间。
4. 错误③（S4）：电极内恰有六个橙色圆点，各有一根向右的短箭头，方向为石墨→正极。底图没有“充电”文字，须由后续标签层设定充电语境；未提前声称带标题面板已核验。
5. 错误④（S7）：顶部导线连接两极耳；导线上恰有三个橙色圆点，各配向右的橙色箭头，明确体现把 Li⁺ 画到外电路的指定错误。
6. 额外对象：未见额外离子箭头、电池符号、充电器、负载或其他过程支路。视觉检查未发现第五类明确科学错误；这不代替电化学同行复核。
7. 无字检查：看图未发现文字、字母标签、数字、伪文字行、+/−号、图例文字或水印。多孔带中个别圆圈未闭合，属于孔轮廓绘制瑕疵，不是文字标签。
8. 留白：底部至少10%没有对象。整体为二维横向截面，能看清七个层位；有轻微填充斑驳，背景不是逐像素纯白，未严格满足纯色、无纹理要求。
9. 坐标（目测近似）：层体 y≈0.194–0.798；右铜箔 x≈0.784–0.808；导线 y≈0.074。与规定坐标仍有偏移。
10. 与正例对比：和所选正例的层体顶边较接近，但本图隔膜宽度约0.14画幅，宽于原定0.12；右侧集流体位置未按反例提示词固定。
11. 落选原因：四种指定错误均成立，但第3次层体更接近原定y区间；第2次分辨率补充没有生效。
12. 像素与宽高比：1672×941；未达到规划最低宽度，非数学上精确16:9。无后期改尺寸；在3次上限后如实保留这一未达标项。

## ch07-07-battery-errors.png

- 图：FIG 07（故意错误反例）；生成第3次；选中，主文件。
- 路径：`figures/ch07/ch07-07-battery-errors.png`
- 工具：image_gen.imagegen (tools.image_gen__imagegen via functions.exec)
- 具体模型：不知道（工具返回中未披露具体模型）
- 工具缓存原图：`codex-output/exec-07c239a5-b194-47dc-983c-2335e647405d.png`
- 尺寸：1672×941；文件字节数：1446231。
- SHA-256：`c91e1f87fcc36bd26aae0f0c4547678c192186c0d4d5927044c5febfc73a1ec9`
- 提示词改动与原因：规划英文代码块完整保留，仅在末尾追加FINAL OUTPUT CHECK段（不包含第2次追加段）。原因：第2次仍为1672×941且坐标漂移、轻微斑驳；最后一次强调尺寸、原有层带坐标和纯色风格。

### 实际使用的完整prompt（逐字）

```text
Flat 2D cross-section schematic of a single cell unit of a lithium-ion pouch
battery, landscape 16:9, at least 1920 px wide, pure white background, clean
vector illustration, flat fills, thin dark gray (#3A3A3A) outlines, no
gradients, no shadows, no highlights, no 3D, no texture.

ABSOLUTELY NO TEXT: no letters, no words, no numbers, no symbols such as "+"
or "-", no labels, no legend, no title, no watermark.

This is a deliberately WRONG teaching example. Draw the layers exactly in the
order given, even though it is not the real order.

LAYERS, drawn as vertical bands side by side, filling x 0.14-0.86 and
y 0.25-0.85 of the image (x from left, y from top), from left to right:
1. Outer pouch film: thin light gray band (#C9C9C9) with a darker inner line,
   x 0.14-0.16.
2. Aluminium foil: thin solid light silver-gray band (#B5B9BE), x 0.19-0.21,
   with a narrow silver tab rising from its top edge to y 0.10.
3. Graphite layer: x 0.21-0.42, many small dark charcoal (#4A4A4A) flat
   flake-shaped particles stacked roughly horizontally.
4. Oxide layer: x 0.42-0.63, many rounded clustered spherical particles in
   muted slate blue (#6F86A6), touching the graphite flakes directly with no
   gap and nothing in between.
5. Separator: x 0.63-0.75, a white band with many tiny round pores and a light
   gray outline.
6. Copper foil: thin solid copper-colored band (#B87333), x 0.75-0.77, with a
   narrow copper tab rising from its top edge to y 0.10.
7. Outer pouch film: thin light gray band, x 0.84-0.86.
Fill the gaps between particles in layers 3 and 4 with a very pale blue
(#E3F0F8).

IONS AND ARROWS:
- Six small solid orange (#D9822B) spheres inside the graphite and oxide
  layers, each with a short solid orange arrow pointing to the RIGHT, moving
  from the graphite layer toward the oxide layer.
- One thin dark gray wire above the cell connecting the top of the silver tab
  to the top of the copper tab at y 0.06. Place three small orange spheres ON
  the wire, each with a small orange arrow pointing along the wire.
No other arrows, no battery symbol, no plus or minus signs.

Bottom 10% of the image left empty.

FINAL OUTPUT CHECK: Deliver one native-resolution 2560 x 1440 pixel PNG, not a smaller preview. Use an exactly 16:9 canvas. The rectangular layer stack must start at y = 0.25 and end at y = 0.85; follow each x-coordinate given above literally. Use perfectly uniform flat colour fills and a pure white background without paper grain, colour mottling, sketch strokes or shading. Keep all the layer materials, particle forms, permitted objects and forbidden objects exactly as specified above.
```

### 看图后逐项核验

1. 层序：外壳膜—银灰铝集流体—炭灰片状石墨—灰蓝圆颗粒正极—白色多孔隔膜—铜色集流体—外壳膜，符合指定的错误层序。
2. 错误①（S2）：负极侧是银灰铝箔，正极侧是铜色箔，集流体对调确实存在；两侧极耳颜色与各自箔一致。
3. 错误②（S1）：石墨与灰蓝颗粒层直接相邻，界面没有隔膜；可见局部颗粒边缘接触。白色多孔隔膜错放在正极与右侧集流体之间。
4. 错误③（S4）：电极内恰有六个橙色圆点，各有一根向右的短箭头，方向为石墨→正极。底图没有“充电”文字，须由后续标签层设定充电语境；未提前声称带标题面板已核验。
5. 错误④（S7）：顶部导线连接两极耳；导线上恰有三个橙色圆点，各配向右的橙色箭头，明确体现把 Li⁺ 画到外电路的指定错误。
6. 额外对象：未见额外离子箭头、电池符号、充电器、负载或其他过程支路。视觉检查未发现第五类明确科学错误；这不代替电化学同行复核。
7. 无字检查：看图未发现文字、字母标签、数字、伪文字行、+/−号、图例文字或水印。多孔带中个别圆圈未闭合，属于孔轮廓绘制瑕疵，不是文字标签。
8. 留白：底部至少10%没有对象。整体为二维横向截面，能看清七个层位；有轻微填充斑驳，背景不是逐像素纯白，未严格满足纯色、无纹理要求。
9. 坐标（目测近似）：层体 x≈0.131–0.871、y≈0.243–0.828，三次中最接近规定的y=0.25–0.85；仍未精确对齐。
10. 坐标残差：石墨/正极交界 x≈0.430（规定0.42）；正极/隔膜交界 x≈0.648（规定0.63）；右铜箔 x≈0.788–0.808（规定0.75–0.77）；导线 y≈0.092（规定0.06），极耳顶端约0.138（规定0.10）。
11. 与所选正例对比：石墨、正极、隔膜宽度量级一致；层体顶边分别约0.243与0.203，右集流体位置相近。不是像素级配准的一对，叠加标签必须按各自实际底图调整。
12. 选用原因：六个内部离子、三个外电路离子与全部右向箭头清楚，四种指定错误齐全；三次中主体纵向位置最接近任务书。尺寸和风格残差仍保留为未达标项。
13. 像素与宽高比：1672×941；未达到规划最低宽度，非数学上精确16:9。无后期改尺寸；在3次上限后如实保留这一未达标项。

## ch07-08-battery-base-alt1.png

- 图：FIG 08（结构正例底图）；生成第1次；未选中，保留备选。
- 路径：`figures/ch07/ch07-08-battery-base-alt1.png`
- 工具：image_gen.imagegen (tools.image_gen__imagegen via functions.exec)
- 具体模型：不知道（工具返回中未披露具体模型）
- 工具缓存原图：`codex-output/exec-b05ae204-6821-49c7-b6c2-2a1ef41eda83.png`
- 尺寸：1672×941；文件字节数：1543750。
- SHA-256：`99224d244362e6b2645dc7a7c84c3b12b3ec678bb99a7c7d52777c4d1fda0476`
- 提示词改动与原因：规划中的英文代码块逐字使用，未改写、未补充。

### 实际使用的完整prompt（逐字）

```text
Flat 2D cross-section schematic of a single cell unit of a lithium-ion pouch
battery, landscape 16:9, at least 2400 px wide, pure white background, clean
vector illustration, flat fills, thin dark gray (#3A3A3A) outlines, no
gradients, no shadows, no highlights, no 3D, no texture, crisp edges.

ABSOLUTELY NO TEXT: no letters, no words, no numbers, no symbols such as "+"
or "-", no labels, no legend, no title, no watermark.

STRUCTURE ONLY: do not draw any ions, electrons, spheres representing ions,
arrows, wires, circuits, battery symbols, chargers or light bulbs. These will
be added later by the author.

LAYERS, drawn as vertical bands side by side, filling x 0.14-0.86 and
y 0.25-0.85 of the image (x from left, y from top), from left to right:
1. Outer pouch film: thin light gray band (#C9C9C9) with a darker inner line,
   x 0.14-0.16.
2. Copper foil current collector: thin solid copper-colored band (#B87333),
   x 0.19-0.21, with a narrow copper tab rising from its top edge, ending at
   y 0.14.
3. Negative electrode coating: x 0.21-0.43, many small dark charcoal (#4A4A4A)
   flat flake-shaped graphite particles stacked roughly horizontally, with
   small gaps between them.
4. Separator: x 0.43-0.57, a white band with many tiny round pores and a light
   gray outline, clearly separating the two electrode coatings; the two
   coatings must not touch each other anywhere.
5. Positive electrode coating: x 0.57-0.79, many rounded clustered spherical
   particles in muted slate blue (#6F86A6), with small gaps between them.
6. Aluminium foil current collector: thin solid light silver-gray band
   (#B5B9BE), x 0.79-0.81, with a narrow silver tab rising from its top edge,
   ending at y 0.14.
7. Outer pouch film: thin light gray band, x 0.84-0.86.

ELECTROLYTE: fill all the gaps between particles in layers 3 and 5 and the
pores of the separator (layer 4) with a very pale blue (#E3F0F8), so that the
pale blue is continuous from the negative coating, through the separator, into
the positive coating. Do not draw the electrolyte as a separate liquid layer.

Both coatings have similar visual density. Keep the region above y 0.14 and
the bottom 12% of the image completely empty. Keep a 4% empty margin on the
left and right.
```

### 看图后逐项核验

1. 层序（S1）：外壳—铜色集流体—炭灰片状石墨负极—白色多孔隔膜—灰蓝圆颗粒正极—银灰铝集流体—外壳，顺序正确。
2. 集流体（S2）：左铜右铝，两种金属各有一个向上延伸的同色极耳，与负极、正极一一对应。
3. 电极隔离：隔膜位于中间并贯穿整个电极高度，左右两电极在图中没有接触。
4. 过程元素禁用：未见独立离子标记、电子、箭头、导线、电路、充电器、灯泡或电池符号。灰蓝圆颗粒是规划规定的正极材料，不是额外离子。
5. 无字检查：未发现文字、字母标签、数字、伪文字行、+/−号、图例或水印；少数孔边缘不闭合，记录为形状瑕疵。
6. 留白：底部12%及左右至少4%没有对象，足以供后续标签层使用。二维横向画法成立，但有轻微斑驳及描边粗细变化，背景不是逐像素纯白。
7. 电解液（S3）：两电极空隙与隔膜多数圆孔均呈浅蓝，能够表达浸润；但外壳和集流体之间额外出现两条浅蓝竖带，容易被理解为独立电解液层，与不另画液体层的要求冲突。
8. 密度：石墨与正极团簇均较密集，形状差异清晰。
9. 坐标（目测近似）：层体 y≈0.201–0.813；极耳顶端 y≈0.109，进入了本应完全留空的y<0.14区域；隔膜 x≈0.432–0.568，横向位置接近规划。
10. 落选原因：额外浅蓝侧带和顶部留白偏差；第2次保留正确层序并去掉侧带，科学表达相对更合适。
11. 像素与宽高比：1672×941；未达到规划最低宽度，非数学上精确16:9。无后期改尺寸；在3次上限后如实保留这一未达标项。

## ch07-08-battery-base.png

- 图：FIG 08（结构正例底图）；生成第2次；选中，主文件。
- 路径：`figures/ch07/ch07-08-battery-base.png`
- 工具：image_gen.imagegen (tools.image_gen__imagegen via functions.exec)
- 具体模型：不知道（工具返回中未披露具体模型）
- 工具缓存原图：`codex-output/exec-95570e2c-f0a7-49c0-bc9f-9047b9509370.png`
- 尺寸：1672×941；文件字节数：1515019。
- SHA-256：`590eed4dfbdb7bbe1f0dcff2a378677d87ffa512c64a62895af27b058d9695c0`
- 提示词改动与原因：规划英文代码块完整保留，仅在末尾追加OUTPUT RESOLUTION段。原因：第1次实际输出1672×941，低于要求；请求2560×1440以同时满足两图最低宽度及16:9。结果尺寸要求未生效。

### 实际使用的完整prompt（逐字）

```text
Flat 2D cross-section schematic of a single cell unit of a lithium-ion pouch
battery, landscape 16:9, at least 2400 px wide, pure white background, clean
vector illustration, flat fills, thin dark gray (#3A3A3A) outlines, no
gradients, no shadows, no highlights, no 3D, no texture, crisp edges.

ABSOLUTELY NO TEXT: no letters, no words, no numbers, no symbols such as "+"
or "-", no labels, no legend, no title, no watermark.

STRUCTURE ONLY: do not draw any ions, electrons, spheres representing ions,
arrows, wires, circuits, battery symbols, chargers or light bulbs. These will
be added later by the author.

LAYERS, drawn as vertical bands side by side, filling x 0.14-0.86 and
y 0.25-0.85 of the image (x from left, y from top), from left to right:
1. Outer pouch film: thin light gray band (#C9C9C9) with a darker inner line,
   x 0.14-0.16.
2. Copper foil current collector: thin solid copper-colored band (#B87333),
   x 0.19-0.21, with a narrow copper tab rising from its top edge, ending at
   y 0.14.
3. Negative electrode coating: x 0.21-0.43, many small dark charcoal (#4A4A4A)
   flat flake-shaped graphite particles stacked roughly horizontally, with
   small gaps between them.
4. Separator: x 0.43-0.57, a white band with many tiny round pores and a light
   gray outline, clearly separating the two electrode coatings; the two
   coatings must not touch each other anywhere.
5. Positive electrode coating: x 0.57-0.79, many rounded clustered spherical
   particles in muted slate blue (#6F86A6), with small gaps between them.
6. Aluminium foil current collector: thin solid light silver-gray band
   (#B5B9BE), x 0.79-0.81, with a narrow silver tab rising from its top edge,
   ending at y 0.14.
7. Outer pouch film: thin light gray band, x 0.84-0.86.

ELECTROLYTE: fill all the gaps between particles in layers 3 and 5 and the
pores of the separator (layer 4) with a very pale blue (#E3F0F8), so that the
pale blue is continuous from the negative coating, through the separator, into
the positive coating. Do not draw the electrolyte as a separate liquid layer.

Both coatings have similar visual density. Keep the region above y 0.14 and
the bottom 12% of the image completely empty. Keep a 4% empty margin on the
left and right.

OUTPUT RESOLUTION: Generate the actual PNG at 2560 x 1440 pixels, exactly 16:9. The delivered raster must be 2560 pixels wide and 1440 pixels high; preserve every content requirement above.
```

### 看图后逐项核验

1. 层序（S1）：外壳—铜色集流体—炭灰片状石墨负极—白色多孔隔膜—灰蓝圆颗粒正极—银灰铝集流体—外壳，顺序正确。
2. 集流体（S2）：左铜右铝，两种金属各有一个向上延伸的同色极耳，与负极、正极一一对应。
3. 电极隔离：隔膜位于中间并贯穿整个电极高度，左右两电极在图中没有接触。
4. 过程元素禁用：未见独立离子标记、电子、箭头、导线、电路、充电器、灯泡或电池符号。灰蓝圆颗粒是规划规定的正极材料，不是额外离子。
5. 无字检查：未发现文字、字母标签、数字、伪文字行、+/−号、图例或水印；少数孔边缘不闭合，记录为形状瑕疵。
6. 留白：底部12%及左右至少4%没有对象，足以供后续标签层使用。二维横向画法成立，但有轻微斑驳及描边粗细变化，背景不是逐像素纯白。
7. 电解液（S3，部分满足）：两个电极颗粒间隙可见浅蓝，隔膜许多圆孔也有浅蓝填充；未另画液体层。个别孔内部接近白色、浅蓝分布不均，不能把严格的“浅蓝在隔膜中连续”判为完全通过；连续性主要靠同色孔隙暗示，未呈现可逐一追踪的贯通孔道。
8. 密度：两侧均为密集颗粒涂层，正极团簇局部更拥挤；大体可比，不是精确相同填充率。
9. 坐标（目测近似）：层体 x≈0.134–0.866、y≈0.203–0.792；极耳顶端约y=0.121，未保持y<0.14区域完全空白；隔膜 x≈0.437–0.565。铜箔约x=0.181–0.207、铝箔约x=0.794–0.820，需要实测调整标签与外电路连接点。
10. 选用原因：层序、集流体、中央隔膜及无过程元素均正确；与第1次相比没有额外浅蓝侧带，与第3次相比隔膜孔隙的蓝色表达更接近要求。仍有分辨率、上方留白、孔隙着色和风格残差，未标为全验收通过。
11. 像素与宽高比：1672×941；未达到规划最低宽度，非数学上精确16:9。无后期改尺寸；在3次上限后如实保留这一未达标项。

## ch07-08-battery-base-alt2.png

- 图：FIG 08（结构正例底图）；生成第3次；未选中，保留备选。
- 路径：`figures/ch07/ch07-08-battery-base-alt2.png`
- 工具：image_gen.imagegen (tools.image_gen__imagegen via functions.exec)
- 具体模型：不知道（工具返回中未披露具体模型）
- 工具缓存原图：`codex-output/exec-d5f5dfd8-eace-4777-bf9c-4cf7a232edc4.png`
- 尺寸：1672×941；文件字节数：1359375。
- SHA-256：`c5c2088cb707ab6a2988db79d380f6baa8cadf6c5662c1934dce079cf1daaf82`
- 提示词改动与原因：规划英文代码块完整保留，仅在末尾追加FINAL OUTPUT CHECK段（不包含第2次追加段）。原因：第2次仍为1672×941且坐标漂移、轻微斑驳；最后一次强调尺寸、原有层带坐标和纯色风格。

### 实际使用的完整prompt（逐字）

```text
Flat 2D cross-section schematic of a single cell unit of a lithium-ion pouch
battery, landscape 16:9, at least 2400 px wide, pure white background, clean
vector illustration, flat fills, thin dark gray (#3A3A3A) outlines, no
gradients, no shadows, no highlights, no 3D, no texture, crisp edges.

ABSOLUTELY NO TEXT: no letters, no words, no numbers, no symbols such as "+"
or "-", no labels, no legend, no title, no watermark.

STRUCTURE ONLY: do not draw any ions, electrons, spheres representing ions,
arrows, wires, circuits, battery symbols, chargers or light bulbs. These will
be added later by the author.

LAYERS, drawn as vertical bands side by side, filling x 0.14-0.86 and
y 0.25-0.85 of the image (x from left, y from top), from left to right:
1. Outer pouch film: thin light gray band (#C9C9C9) with a darker inner line,
   x 0.14-0.16.
2. Copper foil current collector: thin solid copper-colored band (#B87333),
   x 0.19-0.21, with a narrow copper tab rising from its top edge, ending at
   y 0.14.
3. Negative electrode coating: x 0.21-0.43, many small dark charcoal (#4A4A4A)
   flat flake-shaped graphite particles stacked roughly horizontally, with
   small gaps between them.
4. Separator: x 0.43-0.57, a white band with many tiny round pores and a light
   gray outline, clearly separating the two electrode coatings; the two
   coatings must not touch each other anywhere.
5. Positive electrode coating: x 0.57-0.79, many rounded clustered spherical
   particles in muted slate blue (#6F86A6), with small gaps between them.
6. Aluminium foil current collector: thin solid light silver-gray band
   (#B5B9BE), x 0.79-0.81, with a narrow silver tab rising from its top edge,
   ending at y 0.14.
7. Outer pouch film: thin light gray band, x 0.84-0.86.

ELECTROLYTE: fill all the gaps between particles in layers 3 and 5 and the
pores of the separator (layer 4) with a very pale blue (#E3F0F8), so that the
pale blue is continuous from the negative coating, through the separator, into
the positive coating. Do not draw the electrolyte as a separate liquid layer.

Both coatings have similar visual density. Keep the region above y 0.14 and
the bottom 12% of the image completely empty. Keep a 4% empty margin on the
left and right.

FINAL OUTPUT CHECK: Deliver one native-resolution 2560 x 1440 pixel PNG, not a smaller preview. Use an exactly 16:9 canvas. The rectangular layer stack must start at y = 0.25 and end at y = 0.85; follow each x-coordinate given above literally. Use perfectly uniform flat colour fills and a pure white background without paper grain, colour mottling, sketch strokes or shading. Keep all the layer materials, particle forms, permitted objects and forbidden objects exactly as specified above.
```

### 看图后逐项核验

1. 层序（S1）：外壳—铜色集流体—炭灰片状石墨负极—白色多孔隔膜—灰蓝圆颗粒正极—银灰铝集流体—外壳，顺序正确。
2. 集流体（S2）：左铜右铝，两种金属各有一个向上延伸的同色极耳，与负极、正极一一对应。
3. 电极隔离：隔膜位于中间并贯穿整个电极高度，左右两电极在图中没有接触。
4. 过程元素禁用：未见独立离子标记、电子、箭头、导线、电路、充电器、灯泡或电池符号。灰蓝圆颗粒是规划规定的正极材料，不是额外离子。
5. 无字检查：未发现文字、字母标签、数字、伪文字行、+/−号、图例或水印；少数孔边缘不闭合，记录为形状瑕疵。
6. 留白：底部12%及左右至少4%没有对象，足以供后续标签层使用。二维横向画法成立，但有轻微斑驳及描边粗细变化，背景不是逐像素纯白。
7. 电解液（S3，未完全满足）：两电极间隙浅蓝，但中间隔膜更像浅蓝底上留出白色圆孔；孔内没有稳定填入规定的浅蓝，与要求的孔隙浸润表达不一致。
8. 密度：正极颗粒比石墨层更稀疏，大块浅蓝空隙较多，左右视觉密度不够接近。
9. 坐标（目测近似）：层体 y≈0.228–0.800；极耳顶端约0.147，满足y<0.14留白；隔膜 x≈0.434–0.568。虽然顶部位置比前两次改善，但主体下缘仍早于规定0.85。
10. 落选原因：孔隙颜色和电极视觉密度比第2次弱；第3次尺寸、纯色和坐标强调仍未完全奏效。
11. 像素与宽高比：1672×941；未达到规划最低宽度，非数学上精确16:9。无后期改尺寸；在3次上限后如实保留这一未达标项。

## 完成标准：实际命令与输出

### 目录实测

执行等价命令（由 `subprocess.run(..., timeout=20)` 包裹）：

```sh
ls -l figures/ch07/
```

```text
total 43920
-rw-r--r--@ 1 zeroone  staff     3397 Oct 29 16:02 ch07-01-mechanism-grammar-en.tex
-rw-r--r--@ 1 zeroone  staff     3328 Oct 29 16:02 ch07-01-mechanism-grammar-zh.tex
-rw-r--r--@ 1 zeroone  staff     1251 Oct 29 16:03 ch07-02-v0-sketch-overlay.tex
-rw-r--r--@ 1 zeroone  staff  2412444 Oct 29 16:01 ch07-02-v0-sketch.png
-rw-r--r--@ 1 zeroone  staff      962 Oct 29 16:03 ch07-03a-v1-errors.tex
-rw-r--r--@ 1 zeroone  staff  2658302 Oct 29 16:01 ch07-03a-v1-vague.png
-rw-r--r--@ 1 zeroone  staff  1291215 Oct 29 16:01 ch07-03b-v2-brief.png
-rw-r--r--@ 1 zeroone  staff  1245781 Oct 29 16:01 ch07-04a-mixed-arrows.png
-rw-r--r--@ 1 zeroone  staff  1351793 Oct 29 16:01 ch07-04b-unified-arrows.png
-rw-r--r--@ 1 zeroone  staff   406855 Oct 29 16:04 ch07-05a-many-colours-gray.png
-rw-r--r--@ 1 zeroone  staff  1308957 Oct 29 16:01 ch07-05a-many-colours.png
-rw-r--r--@ 1 zeroone  staff   394309 Oct 29 16:04 ch07-05b-v3-revised-gray.png
-rw-r--r--@ 1 zeroone  staff  1294239 Oct 29 16:01 ch07-05b-v3-revised.png
-rw-r--r--@ 1 zeroone  staff  1294170 Oct 29 16:01 ch07-06-v4-base.png
-rw-r--r--@ 1 zeroone  staff     2741 Oct 29 16:02 ch07-06-v4-final-en.tex
-rw-r--r--@ 1 zeroone  staff     2705 Oct 29 16:02 ch07-06-v4-final-zh.tex
-rw-r--r--@ 1 zeroone  staff  1464675 Oct 29 16:00 ch07-07-battery-errors-alt1.png
-rw-r--r--@ 1 zeroone  staff  1431517 Oct 29 16:02 ch07-07-battery-errors-alt2.png
-rw-r--r--@ 1 zeroone  staff     1687 Oct 29 16:04 ch07-07-battery-errors-en.tex
-rw-r--r--@ 1 zeroone  staff     1757 Oct 29 16:04 ch07-07-battery-errors-zh.tex
-rw-r--r--@ 1 zeroone  staff  1446231 Oct 29 16:03 ch07-07-battery-errors.png
-rw-r--r--@ 1 zeroone  staff  1543750 Oct 29 16:01 ch07-08-battery-base-alt1.png
-rw-r--r--@ 1 zeroone  staff  1359375 Oct 29 16:04 ch07-08-battery-base-alt2.png
-rw-r--r--@ 1 zeroone  staff  1515019 Oct 29 16:02 ch07-08-battery-base.png
-rw-r--r--@ 1 zeroone  staff     1905 Oct 29 16:05 ch07-08-battery-charge-discharge-en.tex
-rw-r--r--@ 1 zeroone  staff     3872 Oct 29 16:05 ch07-08-battery-charge-discharge-zh.tex
```

这份ls输出包含并行任务创建的其他图与TeX，不能将它们算作本轮产物。

### 每张本轮PNG的像素尺寸及背景样本实测

Pillow读取每张原始PNG；背景均值取无对象左上角像素框(20,20,150,100)，只读分析，未改动图像。纯白的均值应为(255,255,255)，实测如下，支持“背景不是逐像素纯白”的结论：

```text
ch07-07-battery-errors-alt1.png pixels=1672x941 background_corner_mean_rgb=(253.92, 253.91, 253.91)
ch07-07-battery-errors-alt2.png pixels=1672x941 background_corner_mean_rgb=(253.95, 253.92, 253.92)
ch07-07-battery-errors.png pixels=1672x941 background_corner_mean_rgb=(254.08, 253.93, 253.99)
ch07-08-battery-base-alt1.png pixels=1672x941 background_corner_mean_rgb=(254.0, 253.92, 253.92)
ch07-08-battery-base-alt2.png pixels=1672x941 background_corner_mean_rgb=(253.95, 253.95, 253.95)
ch07-08-battery-base.png pixels=1672x941 background_corner_mean_rgb=(254.08, 253.94, 253.95)
```

### PNG完整性、文件哈希和比例实测

执行 `Image.open(...).verify()` 后重新打开读取尺寸，并对原文件字节计算SHA-256。6张PNG均通过解码完整性检查。以下是实际输出：

```jsonl
{"file": "ch07-07-battery-errors-alt1.png", "size": [1672, 941], "bytes": 1464675, "ratio": 1.7768331562167907, "relative_ratio_error_pct": 0.053134962805516384, "sha256": "88aa7dd037e44e44b69438be75b73a565e2ce4a684a51cc379d7724ca32bc08e"}
{"file": "ch07-07-battery-errors-alt2.png", "size": [1672, 941], "bytes": 1431517, "ratio": 1.7768331562167907, "relative_ratio_error_pct": 0.053134962805516384, "sha256": "4fd399ef5e9a2c06bb958536d5612591f310980fc49dfc650abeaf5f140361f2"}
{"file": "ch07-07-battery-errors.png", "size": [1672, 941], "bytes": 1446231, "ratio": 1.7768331562167907, "relative_ratio_error_pct": 0.053134962805516384, "sha256": "c91e1f87fcc36bd26aae0f0c4547678c192186c0d4d5927044c5febfc73a1ec9"}
{"file": "ch07-08-battery-base-alt1.png", "size": [1672, 941], "bytes": 1543750, "ratio": 1.7768331562167907, "relative_ratio_error_pct": 0.053134962805516384, "sha256": "99224d244362e6b2645dc7a7c84c3b12b3ec678bb99a7c7d52777c4d1fda0476"}
{"file": "ch07-08-battery-base-alt2.png", "size": [1672, 941], "bytes": 1359375, "ratio": 1.7768331562167907, "relative_ratio_error_pct": 0.053134962805516384, "sha256": "c5c2088cb707ab6a2988db79d380f6baa8cadf6c5662c1934dce079cf1daaf82"}
{"file": "ch07-08-battery-base.png", "size": [1672, 941], "bytes": 1515019, "ratio": 1.7768331562167907, "relative_ratio_error_pct": 0.053134962805516384, "sha256": "590eed4dfbdb7bbe1f0dcff2a378677d87ffa512c64a62895af27b058d9695c0"}
```

此处PNG解码通过仅说明文件有效，不代表科学、分辨率、版式或同行审查全部通过。

### 交付前一致性复查（实测）

逐项核对所存PNG与工具缓存原图哈希一致、每次prompt与报告正文一致、第一轮逐字匹配规划、后两轮保留原prompt完整前缀、尺寸一致、选中数与尝试数符合要求。

```text
ch07-07-battery-errors-alt1.png: PNG OK; source SHA-256 match; recorded prompt verified; attempt=1; selected=False; size=1672x941
ch07-07-battery-errors-alt2.png: PNG OK; source SHA-256 match; recorded prompt verified; attempt=2; selected=False; size=1672x941
ch07-07-battery-errors.png: PNG OK; source SHA-256 match; recorded prompt verified; attempt=3; selected=True; size=1672x941
ch07-08-battery-base-alt1.png: PNG OK; source SHA-256 match; recorded prompt verified; attempt=1; selected=False; size=1672x941
ch07-08-battery-base.png: PNG OK; source SHA-256 match; recorded prompt verified; attempt=2; selected=True; size=1672x941
ch07-08-battery-base-alt2.png: PNG OK; source SHA-256 match; recorded prompt verified; attempt=3; selected=False; size=1672x941
PASS: 2 selected images, 4 alternatives, 3 attempts per figure; report and manifest saved.
KNOWN LIMITATIONS: native dimensions below plan, near-16:9 rounding, coordinate/fill deviations; overlay and peer review not verified.
```
