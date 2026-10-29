# 第 9 章 codex-image 底图生成与核验记录

- 日期：2026-10-29（Asia/Shanghai）。
- 任务来源：`(local scratch file)`。
- 规划：`production/plans/ch09.md` 第 4 节 FIG ch09-03、ch09-04；全书规范：`production/book-spec.md` 第 4–5 节。
- 范围：仅新建 `figures/ch09/` 与 `provenance/ch09/` 下本记录所列文件；未生成标签叠加版，未处理 python/tikz 图，未启动子 agent，未 commit/push。目录中的其他图由并行工作产生，以下 ls 实录只列示，不表示本任务修改了它们。
- 实际工具：Codex 内置 `image_gen.imagegen`，由 `functions.exec` 中的 `tools.image_gen__imagegen` 调用；具体模型名称：**不知道（工具未返回）**。没有使用外部 API、CLI、SciDraw AI 或 Figma 出图。
- 每次均为全新生成：`transparent_background=false`；未传 `referenced_image_paths` 或 `num_last_images_to_include`。每张各生成 3 次，共 6 次；无超限生成。
- 英文 prompt 逐字使用规划代码块内容，仅移除 Markdown 代码块的两个空格缩进，保留原始换行；重试未增删或改写提示词。每个文件的完整实际 prompt 在下文单独列出。
- 文件处理：将工具返回的原始 PNG 原样复制到规划路径或 `-altN.png`；未重新编码、重采样、裁切、拉伸、补白、调色或叠加标签。复制前检查目标不存在，复制后验证 SHA-256 与源一致。工具自动保存的原始路径见每图记录。
- 验收方式：逐张查看工具实际返回的图像，检查画面内容与规划核验要点；尺寸/色彩/哈希由 Pillow 和 hashlib 实测。未运行 OCR，不把“未见文字”表述成机器检测的绝对保证。厚度、留白、底层高度为看图估计，不是物理测量。

## 交付和残留偏差

主图：`ch09-03-device-structure-base.png`（第 1 次，1586×992）及 `ch09-04-sem-like-illustration-base.png`（第 3 次，1536×1024），另保留四张备选。

结构图的七层顺序、三支向上箭头和右侧留白正确；与规划仍有差别：轻微渐变/纹理、玻璃略薄于吸光层，以及生成原图宽高比相对 16:10 偏差 -0.075605%。青色中值 #20868D 接近而非精确等于 #1B7F86。类 SEM 主图层序与 3:2 正确，但底层占约 38%–39% 而非约 1/3，底层有轻微颗粒。以上均未掩饰为完全通过。

面板 b 的模型生成声明必须由后续标签/组图步骤补入并随面板保留；当前无字底图不能直接作为已完成来源声明的出版面板。此项是任务明确限定仅生成底图后的交接事项。

## 文件清单

| 文件名 | FIG | 第几次 | 选用 | 像素 | 实际宽高比 |
|---|---|---:|---|---|---:|
| `ch09-03-device-structure-base.png` | ch09-03 | 1 | 主图 | 1586×992 | 1.598790322581 |
| `ch09-03-device-structure-base-alt1.png` | ch09-03 | 2 | 备选 | 1586×992 | 1.598790322581 |
| `ch09-03-device-structure-base-alt2.png` | ch09-03 | 3 | 备选 | 1586×992 | 1.598790322581 |
| `ch09-04-sem-like-illustration-base.png` | ch09-04 | 3 | 主图 | 1536×1024 | 1.500000000000 |
| `ch09-04-sem-like-illustration-base-alt1.png` | ch09-04 | 1 | 备选 | 1536×1024 | 1.500000000000 |
| `ch09-04-sem-like-illustration-base-alt2.png` | ch09-04 | 2 | 备选 | 1536×1024 | 1.500000000000 |

## ch09-03-device-structure-base.png

- FIG：ch09-03；第 1 次；状态：选用主图。
- 实际工具：`image_gen.imagegen (functions tools.image_gen__imagegen)`；具体模型：不知道（工具未返回具体模型名称）。
- 文件：`figures/ch09/ch09-03-device-structure-base.png`。
- 模型原始输出：`codex-output/exec-4340c676-d114-4686-8ed8-d9444f582cda.png`。
- 尺寸：1586×992 px；格式 PNG；模式 RGB。
- SHA-256：`a3669bc018092a5675c3ad9d0ffdd884561da27c48f7197bfd579662aaea9ce0`；源文件逐字节一致：`True`。
- prompt 修改：无；以下为实际完整提交内容。

```text
A clean, flat, two-dimensional scientific schematic of a planar thin-film solar
cell shown as a stack of horizontal layers in side view with a slight sense of
thickness. From bottom to top: a thick pale blue-grey translucent glass slab;
a thin light grey conductive layer; a very thin off-white layer; a thicker
dark reddish-brown absorber layer; an extremely thin teal layer (hex #1B7F86)
directly on top of the absorber; a pale yellow layer; and a thin gold metal
layer on top. Three simple upward-pointing light arrows below the glass,
pale yellow with grey outline. The stack occupies the left 65% of the canvas;
leave the right 35% empty white space for labels added later.
White background, vector illustration style, no gradients, no shadows,
no 3D rendering, no glow, no texture. Layers are not to scale but each layer is
clearly separated by a thin dark grey outline.
Absolutely no text, no letters, no numbers, no labels, no symbols, no scale bar.
Aspect ratio 16:10.
```

逐条看图核验：

1. 层数与顺序：通过。正面从下至上可辨认玻璃、FTO、SnO₂、钙钛矿、钝化层、spiro-OMeTAD、Au，共七层；青色层位于红褐吸光层与浅黄层之间，未多画或漏画层。
2. 各层外观与相对厚度：浅灰蓝玻璃、浅灰 FTO、灰白薄层、红褐吸光层、薄青色层、浅黄层、金色顶层均可辨。玻璃正面厚约 148 px，吸光层约 158 px，故玻璃没有严格成为“最厚”的一层；玻璃透明感有限。层厚为示意，不能据此读出真实厚度。
3. 色彩语义：青色钝化层明确可辨；像素测量中值 #20868D，目标 #1B7F86，RGB 差为 (+5,+7,+7)，属于接近色，未作矢量覆盖或调色。
4. 入射光：通过。玻璃下方恰好三支浅黄、灰色描边箭头，全部向上指向玻璃一侧，无反向或侧入射箭头。
5. 构图与标签留白：通过。正视略带厚度的层叠块，最右边约 x=1028/1586，右侧约 35% 留白，足以供后续另加层名与引线。
6. 风格：白底、深灰轮廓、简洁示意基本满足；层内仍有轻微明暗渐变和颗粒质感，未严格满足 no gradients / no texture。没有外部投影、发光或写实三维渲染。
7. 文字与比例尺：整图目视未见文字、字母、数字、伪文字、标签、比例尺或水印；三支箭头是规划明确要求的元素。
8. 宽高比：实测 1586×992，1.598790322581，接近但不严格等于 16:10；相对偏差 -0.075605%。三次原提示词生成均出现同一尺寸，未裁切或拉伸。
9. 选用结论：选为主图。三次候选中右侧留白最贴近目标，青色较薄且清楚，层数、层序和入射方向均正确；保留上述风格、厚度与像素比例偏差，不记作完全符合。

像素实测：取矩形 (100, 300, 900, 308)（左上角为原点，单位 px），RGB 中值 (32, 134, 141) = `#20868D`；目标 `#1B7F86`。矩形取样只读取像素，未修改图像。

## ch09-03-device-structure-base-alt1.png

- FIG：ch09-03；第 2 次；状态：未选用，保留备选。
- 实际工具：`image_gen.imagegen (functions tools.image_gen__imagegen)`；具体模型：不知道（工具未返回具体模型名称）。
- 文件：`figures/ch09/ch09-03-device-structure-base-alt1.png`。
- 模型原始输出：`codex-output/exec-c968d630-2dca-4fe2-aa42-9a5e1c57931d.png`。
- 尺寸：1586×992 px；格式 PNG；模式 RGB。
- SHA-256：`233c9ca8a9d1e8df9e5f426b7d91ecc1b02f6743cb141591f791ac4930f9077d`；源文件逐字节一致：`True`。
- prompt 修改：无；以下为实际完整提交内容。

```text
A clean, flat, two-dimensional scientific schematic of a planar thin-film solar
cell shown as a stack of horizontal layers in side view with a slight sense of
thickness. From bottom to top: a thick pale blue-grey translucent glass slab;
a thin light grey conductive layer; a very thin off-white layer; a thicker
dark reddish-brown absorber layer; an extremely thin teal layer (hex #1B7F86)
directly on top of the absorber; a pale yellow layer; and a thin gold metal
layer on top. Three simple upward-pointing light arrows below the glass,
pale yellow with grey outline. The stack occupies the left 65% of the canvas;
leave the right 35% empty white space for labels added later.
White background, vector illustration style, no gradients, no shadows,
no 3D rendering, no glow, no texture. Layers are not to scale but each layer is
clearly separated by a thin dark grey outline.
Absolutely no text, no letters, no numbers, no labels, no symbols, no scale bar.
Aspect ratio 16:10.
```

逐条看图核验：

1. 层数与顺序：通过。可辨七层，玻璃→浅灰 FTO→灰白 SnO₂→红褐吸光层→青色钝化层→浅黄 spiro 层→金色 Au；钝化层位置正确。
2. 各层外观与相对厚度：配色和层间深灰分界清楚。玻璃厚约 154 px，吸光层约 171 px，玻璃不是最厚；青色层约 29 px，视觉上比第 1 次更厚，对“极薄”表达较弱。
3. 色彩语义：青色测量中值 #1E838E，目标 #1B7F86，RGB 差 (+3,+4,+8)，近似符合，未覆盖或改色。
4. 入射光：通过。三支浅黄灰边箭头位于玻璃之下并朝上。
5. 构图与标签留白：通过。层叠块到约 x=1028/1586，右侧约 35% 空白；略带厚度的侧边可见。
6. 风格：白底、灰色轮廓、扁平示意基本符合，但层内微小渐变和颗粒质感仍可见，未严格达到 no gradients / no texture；未见外部投影或发光。
7. 文字与比例尺：整图目视未见文字、字母、数字、伪文字、比例尺或水印。
8. 宽高比：1586×992，实际 1.598790322581，相对 16:10 偏差 -0.075605%，未作像素修改。
9. 选用结论：保留为 alt1。颜色接近目标，但钝化层较第 1 次更厚，且没有解决风格与宽高比问题。

像素实测：取矩形 (100, 320, 900, 328)（左上角为原点，单位 px），RGB 中值 (30, 131, 142) = `#1E838E`；目标 `#1B7F86`。矩形取样只读取像素，未修改图像。

## ch09-03-device-structure-base-alt2.png

- FIG：ch09-03；第 3 次；状态：未选用，保留备选。
- 实际工具：`image_gen.imagegen (functions tools.image_gen__imagegen)`；具体模型：不知道（工具未返回具体模型名称）。
- 文件：`figures/ch09/ch09-03-device-structure-base-alt2.png`。
- 模型原始输出：`codex-output/exec-d9c360fb-86d7-412d-b31a-3b57521f293b.png`。
- 尺寸：1586×992 px；格式 PNG；模式 RGB。
- SHA-256：`564a9482a02c018d5f6fbfc651b643c3512986bc96bf74c25e1b1789033c08e2`；源文件逐字节一致：`True`。
- prompt 修改：无；以下为实际完整提交内容。

```text
A clean, flat, two-dimensional scientific schematic of a planar thin-film solar
cell shown as a stack of horizontal layers in side view with a slight sense of
thickness. From bottom to top: a thick pale blue-grey translucent glass slab;
a thin light grey conductive layer; a very thin off-white layer; a thicker
dark reddish-brown absorber layer; an extremely thin teal layer (hex #1B7F86)
directly on top of the absorber; a pale yellow layer; and a thin gold metal
layer on top. Three simple upward-pointing light arrows below the glass,
pale yellow with grey outline. The stack occupies the left 65% of the canvas;
leave the right 35% empty white space for labels added later.
White background, vector illustration style, no gradients, no shadows,
no 3D rendering, no glow, no texture. Layers are not to scale but each layer is
clearly separated by a thin dark grey outline.
Absolutely no text, no letters, no numbers, no labels, no symbols, no scale bar.
Aspect ratio 16:10.
```

逐条看图核验：

1. 层数与顺序：通过。七层自下至上排列正确，青色层仍在红褐层和浅黄层之间，层间界线清楚。
2. 各层外观与相对厚度：青色层较薄，灰白层与浅灰层可区分；玻璃约 171 px，吸光层约 181 px，仍未实现玻璃最厚。吸光层颜色较前两次更偏红、较浅。
3. 色彩语义：仍可理解为青色改性层，但中值 #298F97 与目标 #1B7F86 的 RGB 差为 (+14,+16,+17)，比其他候选偏差大；未覆盖或改色。
4. 入射光：通过。玻璃下方三支浅黄灰边箭头朝上。
5. 构图与标签留白：留白可用；层叠块到约 x=975/1586，右侧约 38.5% 空白，比提示词的 35% 多，构图较主图窄。
6. 风格：白底、灰色边线和略带厚度的层叠形式正确；仍有渐变、细微颗粒，未严格满足 no gradients / no texture；没有外部投影或发光。
7. 文字与比例尺：整图目视未见文字、字母、数字、伪文字、比例尺或水印。
8. 宽高比：1586×992，实际 1.598790322581，相对 16:10 偏差 -0.075605%，未作像素修改。
9. 选用结论：保留为 alt2。青色偏差更大、右侧留白比计划多；未超过每图三次的生成上限。

像素实测：取矩形 (100, 266, 900, 274)（左上角为原点，单位 px），RGB 中值 (41, 143, 151) = `#298F97`；目标 `#1B7F86`。矩形取样只读取像素，未修改图像。

## ch09-04-sem-like-illustration-base.png

- FIG：ch09-04；第 3 次；状态：选用主图。
- 实际工具：`image_gen.imagegen (functions tools.image_gen__imagegen)`；具体模型：不知道（工具未返回具体模型名称）。
- 文件：`figures/ch09/ch09-04-sem-like-illustration-base.png`。
- 模型原始输出：`codex-output/exec-fc2edd74-579c-4083-9ca0-90d59e668bed.png`。
- 尺寸：1536×1024 px；格式 PNG；模式 RGB。
- SHA-256：`d0325d361dcdd9ff6d89e8c327cba9277edecc3a5651bbf752ed370278ec4aa8`；源文件逐字节一致：`True`。
- prompt 修改：无；以下为实际完整提交内容。

```text
A grayscale illustration in the visual style of a cross-sectional scanning
electron micrograph of a layered thin film, for use as a clearly labelled
teaching illustration. From bottom to top: a thick smooth featureless layer
filling the bottom third; a very thin slightly brighter layer; a thicker layer
made of densely packed columnar grains with visible grain boundaries; a
smoother amorphous layer; and a thin bright layer at the top. Dark background
above the top layer. Slightly irregular fractured edge. Even illumination,
moderate contrast. No scale bar, no data bar, no measurement marks, no text,
no letters, no numbers, no labels, no watermark. Aspect ratio 3:2.
```

逐条看图核验：

1. 层序：通过。自下而上为厚且相对均质的灰层、较亮的薄层、较厚且紧密排列的柱状/块状晶粒层、较平滑无定形层、顶部亮薄层；层间关系清楚。
2. 底层厚度与质感：厚底层占整幅高度约 38%–39%，三次候选中最接近 bottom third，但仍大于约 33.3%；底层没有宏观结构，存在轻微细颗粒，因此也不是字面意义上完全无纹理的 featureless。
3. 晶粒与断面：晶粒密集且晶界可见，柱状与块状混合，顶部略不规则；相较第 2 次没有明显的单侧大坡折。
4. 灰度、背景和照明：灰度视觉风格、顶部暗背景、较均匀照明、适中对比度符合；具体 RGB 通道一致性由像素检测记录。
5. 文字、尺度与仪器条：整图目视未见文字、字母、数字、伪文字、比例尺、仪器数据条、测量线或水印。不得为此图补造比例尺。
6. 宽高比：1536×1024，严格为 3:2，保持模型原始像素，没有裁切、拉伸或添加标签。
7. 面板内声明：仅交付无字底图。本次未产生 -zh/-en 标注版，最终面板内“模型生成示意，非显微图像 / Model-generated illustration, not a micrograph”≥8 pt 以及第 9、12、13 章标注一致性留待组图阶段验收。
8. 选用结论：选为主图。层序、灰度、无文字/无比例尺和原始宽高比均满足底图用途，底层占比及微纹理偏差如实保留；不得称为真实显微图像。

像素实测：全图 RGB 三通道逐像素完全相等 = `False`。

## ch09-04-sem-like-illustration-base-alt1.png

- FIG：ch09-04；第 1 次；状态：未选用，保留备选。
- 实际工具：`image_gen.imagegen (functions tools.image_gen__imagegen)`；具体模型：不知道（工具未返回具体模型名称）。
- 文件：`figures/ch09/ch09-04-sem-like-illustration-base-alt1.png`。
- 模型原始输出：`codex-output/exec-fc792df7-89b5-4f90-8577-d0c55a8f41d6.png`。
- 尺寸：1536×1024 px；格式 PNG；模式 RGB。
- SHA-256：`451f5fe68b374c18a4c688b7d569a7c17e9c403c6290d4ca01f6a26d982c10b4`；源文件逐字节一致：`True`。
- prompt 修改：无；以下为实际完整提交内容。

```text
A grayscale illustration in the visual style of a cross-sectional scanning
electron micrograph of a layered thin film, for use as a clearly labelled
teaching illustration. From bottom to top: a thick smooth featureless layer
filling the bottom third; a very thin slightly brighter layer; a thicker layer
made of densely packed columnar grains with visible grain boundaries; a
smoother amorphous layer; and a thin bright layer at the top. Dark background
above the top layer. Slightly irregular fractured edge. Even illumination,
moderate contrast. No scale bar, no data bar, no measurement marks, no text,
no letters, no numbers, no labels, no watermark. Aspect ratio 3:2.
```

逐条看图核验：

1. 层序：通过。底部厚灰色均质层，其上一条较亮薄层，中部紧密的柱状/块状晶粒层，晶粒层上方较平滑无定形层，顶部亮薄层，五个视觉层区分明确。
2. 底层厚度与质感：底层无宏观结构但存在细微 SEM 式颗粒；约占整幅高度 39%–40%，高于提示词的 bottom third（约 33.3%）。
3. 晶粒与断面：紧密排列的柱状/块状晶粒及晶界可见，局部裂隙较突出；顶部断面边缘略有起伏，没有严重缺口。
4. 灰度、背景和照明：灰度风格、顶端暗背景、较均匀照明与适中对比度符合。RGB 是否完全等值见像素实测表，不能仅凭视觉推断文件模式。
5. 文字、尺度与仪器条：整图目视未见任何文字、字母、数字、伪文字、比例尺、伪数据条、测量线或水印；图样没有物理尺度。
6. 宽高比：1536×1024，严格为 3:2，未经裁切、拉伸、加框。
7. 面板内声明：本次仅生成无字底图，未叠加“模型生成示意，非显微图像”；因此最终面板内 ≥8 pt 与第 9、12、13 章声明一致性尚不可验收，必须由后续排版环节完成。
8. 选用结论：保留为 alt1。层序与禁用元素检查合格，但底层占比比第 3 次更大，中部晶粒裂隙也更突出。

像素实测：全图 RGB 三通道逐像素完全相等 = `False`。

## ch09-04-sem-like-illustration-base-alt2.png

- FIG：ch09-04；第 2 次；状态：未选用，保留备选。
- 实际工具：`image_gen.imagegen (functions tools.image_gen__imagegen)`；具体模型：不知道（工具未返回具体模型名称）。
- 文件：`figures/ch09/ch09-04-sem-like-illustration-base-alt2.png`。
- 模型原始输出：`codex-output/exec-17bc2db2-9688-4f85-adef-13eb35f76eb0.png`。
- 尺寸：1536×1024 px；格式 PNG；模式 RGB。
- SHA-256：`62ee30164775e3561c38f0d84b3ed34b9f07de69f30b2b4349dcb6650d36f268`；源文件逐字节一致：`True`。
- prompt 修改：无；以下为实际完整提交内容。

```text
A grayscale illustration in the visual style of a cross-sectional scanning
electron micrograph of a layered thin film, for use as a clearly labelled
teaching illustration. From bottom to top: a thick smooth featureless layer
filling the bottom third; a very thin slightly brighter layer; a thicker layer
made of densely packed columnar grains with visible grain boundaries; a
smoother amorphous layer; and a thin bright layer at the top. Dark background
above the top layer. Slightly irregular fractured edge. Even illumination,
moderate contrast. No scale bar, no data bar, no measurement marks, no text,
no letters, no numbers, no labels, no watermark. Aspect ratio 3:2.
```

逐条看图核验：

1. 层序：通过。厚灰色底层、亮薄层、密集柱状晶粒层、较平滑无定形层、顶部亮层可依次辨认，未见层序颠倒。
2. 底层厚度与质感：底层相对均质，约占整图高度 42%–43%，比要求的 bottom third 偏差更大；细微 SEM 式颗粒仍可见。
3. 晶粒与断面：柱状/块状晶粒和晶界明确；顶部右端有明显向下的坡折，较提示词的 slightly irregular fractured edge 更显著。
4. 灰度、背景和照明：灰度、顶部暗背景、总体均匀照明和适中对比度基本符合。
5. 文字、尺度与仪器条：整图目视未见文字、字母、数字、伪文字、比例尺、伪数据条、测量标记或水印。
6. 宽高比：1536×1024，严格为 3:2，未经裁切或拉伸。
7. 面板内声明：无字底图符合本次范围；8 pt 声明框及跨章标注一致性须留待后续叠加后检查，不能将底图当成已完成标注的面板。
8. 选用结论：保留为 alt2。底层比例偏差最大，顶部右端坡折较明显。

像素实测：全图 RGB 三通道逐像素完全相等 = `False`。

## 实测命令与原样输出

记录时间：2026-10-29T16:20:47.549827+08:00。命令通过 `subprocess.run(..., timeout=10)` 执行；Python 检查进程设 `signal.alarm(25)`。

### 1. 目录列表

命令：

```sh
ls -l figures/ch09/
```

实际输出（包括其他并行任务的文件；本次只交付上表六张 PNG）：

```text
total 23592
-rw-r--r--@  1 zeroone  staff     1436 Oct 29 16:15 ch09-01-panel-argument-map-en.tex
-rw-r--r--@  1 zeroone  staff     1533 Oct 29 16:15 ch09-01-panel-argument-map-zh.tex
-rw-r--r--@  1 zeroone  staff     1758 Oct 29 16:15 ch09-02-layout-wireframes-en.tex
-rw-r--r--@  1 zeroone  staff     1757 Oct 29 16:15 ch09-02-layout-wireframes-zh.tex
-rw-r--r--@  1 zeroone  staff  1042366 Oct 29 16:18 ch09-03-device-structure-base-alt1.png
-rw-r--r--@  1 zeroone  staff  1070056 Oct 29 16:18 ch09-03-device-structure-base-alt2.png
-rw-r--r--@  1 zeroone  staff  1071001 Oct 29 16:18 ch09-03-device-structure-base.png
-rw-r--r--@  1 zeroone  staff  2749463 Oct 29 16:18 ch09-04-sem-like-illustration-base-alt1.png
-rw-r--r--@  1 zeroone  staff  2790040 Oct 29 16:18 ch09-04-sem-like-illustration-base-alt2.png
-rw-r--r--@  1 zeroone  staff  2999324 Oct 29 16:18 ch09-04-sem-like-illustration-base.png
-rw-r--r--@  1 zeroone  staff    22223 Oct 29 16:16 ch09-05-data-panels-en.pdf
-rw-r--r--@  1 zeroone  staff   110038 Oct 29 16:16 ch09-05-data-panels-en.png
-rw-r--r--@  1 zeroone  staff    20443 Oct 29 16:16 ch09-05-data-panels-zh.pdf
-rw-r--r--@  1 zeroone  staff   108064 Oct 29 16:16 ch09-05-data-panels-zh.png
-rw-r--r--@  1 zeroone  staff     1627 Oct 29 16:15 ch09-08-legend-drafting-en.tex
-rw-r--r--@  1 zeroone  staff     1684 Oct 29 16:15 ch09-08-legend-drafting-zh.tex
drwxr-xr-x@ 10 zeroone  staff      320 Oct 29 16:15 work
```

### 2. 每张交付 PNG 的实际尺寸、宽高比及文件一致性

读取方式：`PIL.Image.open(path)` 并执行 `im.load()`；读取 `im.size`、`im.mode`、`im.format`，比较源文件与目标文件字节，计算 `sha256`。

```text
ch09-03-device-structure-base.png: PNG 1586x992 px; mode=RGB; attempt=1; selected=True; aspect=1.598790322581; aspect_error=-0.075605%; source_byte_identical=True
ch09-03-device-structure-base-alt1.png: PNG 1586x992 px; mode=RGB; attempt=2; selected=False; aspect=1.598790322581; aspect_error=-0.075605%; source_byte_identical=True
ch09-03-device-structure-base-alt2.png: PNG 1586x992 px; mode=RGB; attempt=3; selected=False; aspect=1.598790322581; aspect_error=-0.075605%; source_byte_identical=True
ch09-04-sem-like-illustration-base.png: PNG 1536x1024 px; mode=RGB; attempt=3; selected=True; aspect=1.500000000000; aspect_error=0.000000%; source_byte_identical=True
ch09-04-sem-like-illustration-base-alt1.png: PNG 1536x1024 px; mode=RGB; attempt=1; selected=False; aspect=1.500000000000; aspect_error=0.000000%; source_byte_identical=True
ch09-04-sem-like-illustration-base-alt2.png: PNG 1536x1024 px; mode=RGB; attempt=2; selected=False; aspect=1.500000000000; aspect_error=0.000000%; source_byte_identical=True
```

机器可读的完整实测值、原始路径、哈希与逐张 prompt 另存于 `provenance/ch09/codex-images-validation.json`。

### 3. 近灰度输出的通道差异与最终复核

三张类 SEM 图视觉接近灰度，但 RGB 三通道并非逐像素完全相等；因此不能宣称文件为严格灰度。下列实际读数记录剩余微小色偏，未通过转换掩盖生成结果。

```text
ch09-04-sem-like-illustration-base.png: max(R,G,B)-min(R,G,B) max=10; mean=1.205684; meanRGB=100.452058,100.331902,100.534737
ch09-04-sem-like-illustration-base-alt1.png: max(R,G,B)-min(R,G,B) max=10; mean=1.084854; meanRGB=93.811226,93.662654,93.926212
ch09-04-sem-like-illustration-base-alt2.png: max(R,G,B)-min(R,G,B) max=8; mean=1.007449; meanRGB=105.689789,105.501428,105.631434
```

最终复核：六张 PNG 均可完整解码；尺寸与记录一致；六个 SHA-256 均与复制时一致；六个完整 prompt 均与规划去除 Markdown 缩进后的原文相等；主图 2 张、备选 4 张；两张图均恰好生成 3 次。
