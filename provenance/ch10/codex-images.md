# 第10章 Codex 图像生成与逐图核验记录

日期：2026-10-29（Asia/Shanghai）。任务依据：`production/plans/ch10.md` 的 FIG ch10-03/04/05/06，及 `production/book-spec.md` 第4、5节。

本次交付4张选定底图、7张落选版本，共11张PNG；没有制作TikZ文字层、python图、PDF或其他kind的图。没有启动子agent，没有commit/push。运行期间同目录出现的ch10-01、02、07由其他工作产生，仅在要求的`ls -l`中原样列出，本次未修改。

**状态：已生成并完成本次看图/文件核验，但不是严格全部符合规划。** 选定图未见文字、字母、数字或伪文字；两种叙事图箭头关系正确，反例保留指定的火线/烟/地球/时钟错误。残余偏差包括：示意图的轻微明暗变化和非纯白背景、中心图比例、终稿约1.6倍而非1.2倍的输出图、反例约15%而非18%的顶部空带。下文逐项列明，未以“通过”掩盖这些差异。

## 工具、原始文件及尺寸处理

- 实际工具：内置 `image_gen.imagegen`，调用接口 `functions` → `tools.image_gen__imagegen`。具体底层模型：**不知道**，工具未返回模型标识；未使用SciDraw、FigureLabs或OpenAI API/CLI生成。
- 每张首轮prompt均与规划英文代码块逐字一致；后续仅针对看图发现的问题修改/追加，逐次全文见下。每图调用次数为2/3/3/3，均未超过3次。
- 所有调用设置 `transparent_background=false`；仅ch10-06第3次使用参考图，其他均为独立生成。各次自动缓存路径和原图SHA-256均列出。
- 工具原始输出均为1983×793，不是声明的2000×800。交付副本用 macOS `sips --resampleHeightWidth 800 2000 <path>` 规范尺寸为2000×800、精确5:2；原图留在工具默认缓存。横向/纵向缩放约1.008573/1.008827，比例校正约0.0252%。没有裁剪、重画科学对象或加入标签。
- 文件处理/检查的shell命令使用Python `signal.alarm`（15–180秒），子进程使用`subprocess.run(timeout=10/20)`；图像调用使用120秒yield，实际单次均在约19–29秒返回。工具无可设置的图像请求取消超时参数，未声称yield是服务端硬超时。
- 看图方法：逐次查看工具返回图；对选定B、反例第2次和终稿另以`view_image(detail=original)`复核，反例第3次查看工具返回全图。未执行独立OCR或全图200%放大，因此C3/C6记录为可视检查，不能等同于人工200%终审。

## 文件与选择

| 文件（均在figures/ch10/） | 第几次 | 选择 | 实测像素 |
|---|---:|---|---|
| ch10-03-composition-a-narrative.png | 1 | 选定 | 2000 × 800 |
| ch10-03-composition-a-narrative-alt1.png | 2 | 落选 | 2000 × 800 |
| ch10-04-composition-b-central-alt1.png | 1 | 落选 | 2000 × 800 |
| ch10-04-composition-b-central-alt2.png | 2 | 落选 | 2000 × 800 |
| ch10-04-composition-b-central.png | 3 | 选定 | 2000 × 800 |
| ch10-05-overclaim-alt1.png | 1 | 落选 | 2000 × 800 |
| ch10-05-overclaim-alt2.png | 2 | 落选 | 2000 × 800 |
| ch10-05-overclaim.png | 3 | 选定 | 2000 × 800 |
| ch10-06-final-base-alt1.png | 1 | 落选 | 2000 × 800 |
| ch10-06-final-base-alt2.png | 2 | 落选 | 2000 × 800 |
| ch10-06-final-base.png | 3 | 选定 | 2000 × 800 |

`alt1/alt2`是落选序号，不等于生成次数；以下每项明确记录对应次数。含数字/疑似刻线的反例alt文件仅存档，不应误用作选定底图。

## 逐次prompt与看图结论

### ch10-03-composition-a-narrative.png — 第1次，选定

- 文件：`figures/ch10/ch10-03-composition-a-narrative.png`
- 工具：image_gen.imagegen (functions tools.image_gen__imagegen)；模型：不知道（工具未返回具体模型标识）。
- 原始尺寸：1983 × 793；交付尺寸：2000 × 800。
- 原始缓存：`codex-output/exec-302a97ae-ea4c-4010-a771-a313e209d688.png`
- 原始SHA-256：`d703c8f6309e3947bf2e077721885a7b5a9a46b65c18043b80ac665a372a4c09`
- 交付SHA-256：`489d293570f0292b39fe966c3535628d3cf5e2cd1ee31fadf093fca855781d7e`
- 参考图：无。

**提示词变化与选择原因：** 首轮逐字使用规划英文 prompt，没有增删；prompt 内的 Three 与画面/核验要求 Two 存在矛盾。生成结果恰为两支箭头。选用首轮，因为网络的连续堆叠形状、深灰轮廓及与终稿第 3 次的一致性优于第 2 次。

**实际发送的完整prompt（不省略）：**

```text
Graphical abstract base art, wide banner, aspect ratio 5:2 (2000 x 800 px),
pure white background, flat 2D vector illustration, flat fills, thin dark gray
outlines, no gradients, no shadows, no 3D, no photographic texture.

ABSOLUTELY NO TEXT: no letters, no words, no numbers, no symbols, no labels,
no title, no legend. Text will be added later.

Keep the top 15% and the bottom 12% of the image completely empty.

Four equal-width stages from left to right, vertically centered:
1. Input (x 0.04-0.25): two square map tiles side by side, both top-down flat
   schematic maps of the same landscape patch. Left tile: muted green vegetation
   patches with a thin pale-blue river line. Right tile: the same patch, same
   river, but a large irregular warm brown-orange area in the middle (burned
   land). Above them, smaller, a third square tile partly covered by a flat
   light-gray cloud shape.
2. Model (x 0.30-0.46): a single blue-gray hourglass shape made of stacked
   rounded rectangles that narrow to a waist and widen again (an
   encoder-decoder), no neurons, no circuit patterns.
3. Output (x 0.52-0.72): one square map tile of the same patch in very pale
   gray, with the burned area drawn as a crisp warm brown-orange polygon.
4. Comparison (x 0.77-0.96): a small square inset of the same patch outline
   showing three boundary lines around the burned area: a dark gray solid line
   (reference), a blue solid line closely following it, and a light gray dashed
   line that clearly deviates from it.
Three identical dark gray arrows with filled heads connect stage 1 to 2 and
2 to 3. No arrow between stage 3 and 4.

Palette only: muted green, warm brown-orange, blue-gray, blue, grays.
Do not draw: flames, smoke plumes, fire fronts, globes, satellites, clocks,
alarms, people, buildings, charts, axes, numbers, photographs.
```

**对照画面内容/核验要点的看图结论：**

1. 画面①：并排火前/火后两图块、上方云遮挡图块均存在；两幅输入图的河流转折与进出边位置一致。云图块略小于输入，但云本身偏大。
2. 画面②：一个蓝灰色、连续矩形逐级收窄再变宽的竖向沙漏；没有神经元或电路装饰。
3. 画面③：浅灰地块与暖棕橙过火多边形齐全；与输入保持相似地块/河流结构，但并非几何注册的数据图。
4. 画面④：深灰实线、蓝实线、浅灰虚线齐全；蓝线贴近参考线，虚线明显偏离。
5. 核验：四段齐全；①→②、②→③恰两支同型实心箭头；③与④之间无箭头。实际各对象宽度并非精确等宽，输入区域略超 x=0.25。
6. 核验：未见火焰、地球、数字、字母或伪文字；无真实影像质感。
7. 核验：顶部15%、底部12%无对象侵入，背景通道范围均为253–255；符合视觉留白，但不满足逐像素纯白。填色有轻微明暗变化，未严格实现无渐变。
8. 教学目的：四段阅读路径与输入端的观测限制可辨；选为候选A底图，保留上述严格规格偏差。

### ch10-03-composition-a-narrative-alt1.png — 第2次，落选

- 文件：`figures/ch10/ch10-03-composition-a-narrative-alt1.png`
- 工具：image_gen.imagegen (functions tools.image_gen__imagegen)；模型：不知道（工具未返回具体模型标识）。
- 原始尺寸：1983 × 793；交付尺寸：2000 × 800。
- 原始缓存：`codex-output/exec-3abc4e4a-bfd0-402a-99dc-d231fcbdf955.png`
- 原始SHA-256：`dfff90c7b3b1794487db6ca6b6d90d8750ac9c7435da911b10aca388eec3cb1a`
- 交付SHA-256：`3d7d192df814974e4572da2318dd33b084000dacceee5e8b803cca8cae6dc650`
- 参考图：无。

**提示词变化与选择原因：** 第2次将原文 Three identical dark gray arrows 改为 Two identical dark gray arrows，消除与中文画面/核验标准的冲突；在原文后追加单列网络、共用地块、较小云块及纯色渲染澄清。未选用：网络轮廓消失、范围更大，和终稿参考版不如首轮一致。

**实际发送的完整prompt（不省略）：**

```text
Graphical abstract base art, wide banner, aspect ratio 5:2 (2000 x 800 px),
pure white background, flat 2D vector illustration, flat fills, thin dark gray
outlines, no gradients, no shadows, no 3D, no photographic texture.

ABSOLUTELY NO TEXT: no letters, no words, no numbers, no symbols, no labels,
no title, no legend. Text will be added later.

Keep the top 15% and the bottom 12% of the image completely empty.

Four equal-width stages from left to right, vertically centered:
1. Input (x 0.04-0.25): two square map tiles side by side, both top-down flat
   schematic maps of the same landscape patch. Left tile: muted green vegetation
   patches with a thin pale-blue river line. Right tile: the same patch, same
   river, but a large irregular warm brown-orange area in the middle (burned
   land). Above them, smaller, a third square tile partly covered by a flat
   light-gray cloud shape.
2. Model (x 0.30-0.46): a single blue-gray hourglass shape made of stacked
   rounded rectangles that narrow to a waist and widen again (an
   encoder-decoder), no neurons, no circuit patterns.
3. Output (x 0.52-0.72): one square map tile of the same patch in very pale
   gray, with the burned area drawn as a crisp warm brown-orange polygon.
4. Comparison (x 0.77-0.96): a small square inset of the same patch outline
   showing three boundary lines around the burned area: a dark gray solid line
   (reference), a blue solid line closely following it, and a light gray dashed
   line that clearly deviates from it.
Two identical dark gray arrows with filled heads connect stage 1 to 2 and
2 to 3. No arrow between stage 3 and 4.

Palette only: muted green, warm brown-orange, blue-gray, blue, grays.
Do not draw: flames, smoke plumes, fire fronts, globes, satellites, clocks,
alarms, people, buildings, charts, axes, numbers, photographs.

Second-attempt clarification: the network is ONE centered vertical stack, every row one continuous rounded rectangle, narrowing to a waist and widening again. All map tiles reuse exactly the same landscape, river geometry and burned-area outline at different scales. The small cloud tile should be smaller than either input tile and sit above the pair entirely below y=0.15. Keep both reserved white bands completely empty. Render as a clean SVG export: completely uniform solid fills, #FFFFFF background, muted green #A8C3A0, brown-orange #C8743C, blue-gray #8FA3B8, reference #3A3A3A, model #2F6DB5, light-gray dashed threshold #A0A0A0. No gradients, highlights, shadows, paper texture, typographic marks or extra objects.
```

**对照画面内容/核验要点的看图结论：**

1. 画面①：火前/火后并排、上方小云块齐全；输入河流基本重合，云块比首轮更小。
2. 画面②：单个连续矩形竖向沙漏正确，但缺少规划要求的深灰外轮廓；网络右边缘超过指定阶段范围。
3. 画面③：浅灰输出图与橙棕色过火区存在；河流穿过过火区，输出与对比的形状不是严格同一轮廓。
4. 画面④：三类边界齐全，蓝实线接近深灰实线，浅灰虚线偏离。
5. 核验：两支同型向右箭头正确；输出与比较之间无箭头；四段齐全但并非精确等宽。
6. 核验：未见文字、字母、数字、伪文字、火焰或地球；顶部和底部可留作文字，但仍有轻微纹理/明暗变化。
7. 教学目的可辨；因描边、几何与风格一致性不及首轮，保留为alt1。

### ch10-04-composition-b-central-alt1.png — 第1次，落选

- 文件：`figures/ch10/ch10-04-composition-b-central-alt1.png`
- 工具：image_gen.imagegen (functions tools.image_gen__imagegen)；模型：不知道（工具未返回具体模型标识）。
- 原始尺寸：1983 × 793；交付尺寸：2000 × 800。
- 原始缓存：`codex-output/exec-becd1470-7980-4036-88a2-006602b52d62.png`
- 原始SHA-256：`3981842b4ff7fb05c2211b241648a3e22058a085c4e2c7e4523e4b5f57187605`
- 交付SHA-256：`53dec33b6479481ae34b9efcbbf345105c1203d7e12a85cbe241dbadd71aa1ab`
- 参考图：无。

**提示词变化与选择原因：** 首轮逐字使用规划 prompt。未选用：中央图保留大量绿色植被；网络被画成左右两组条块，偏离单个竖向沙漏。

**实际发送的完整prompt（不省略）：**

```text
Graphical abstract base art, wide banner, aspect ratio 5:2 (2000 x 800 px),
pure white background, flat 2D vector illustration, flat fills, thin dark gray
outlines, no gradients, no shadows, no 3D, no photographic texture.

ABSOLUTELY NO TEXT: no letters, words, numbers, symbols, labels or title.

Central composition. In the exact center, one large square top-down schematic
map tile (about 70% of the image height) of a landscape patch in very pale gray
with a crisp warm brown-orange irregular burned-area polygon and a thin
pale-blue river line.
Around it, four small elements, each about one quarter the size of the center
tile:
- upper left: a small tile of the same patch in muted green vegetation (before);
- lower left: a small tile of the same patch with a warm brown-orange area
  (after), and next to it an even smaller tile partly covered by a flat light
  gray cloud;
- upper right: a small blue-gray hourglass shape of stacked rounded rectangles
  (encoder-decoder network);
- lower right: a small square inset with three boundary lines around a burned
  area: dark gray solid, blue solid closely following it, light gray dashed
  clearly deviating.
Thin plain gray connector lines without arrowheads run from each small element
toward the central tile.

Palette only: muted green, warm brown-orange, blue-gray, blue, grays.
Do not draw: flames, smoke, globes, satellites, clocks, alarms, people,
charts, axes, numbers, photographs.
```

**对照画面内容/核验要点的看图结论：**

1. 画面：中央大图、左上火前、左下火后、右上网络、右下比较、附加云图块均存在。
2. 中央图不满足非常浅灰的要求；中央高度约占画布80%，超过建议70%；四周元素偏大。
3. 网络为左右分列条块，未形成规划中的单个连续矩形堆叠沙漏。
4. 连接线没有箭头头；左下连接线经过云图块附近，主输入与云限制的关系不够清楚。
5. 比较插图具有深灰实线、蓝实线和浅灰虚线；偏离关系可辨。
6. 与A属于相同对象类别与色相角色，但地块不是同一套几何，绿色占比和视觉重心不同；不是严格色值一致。
7. 未见文字、字母、数字或伪文字；轻微渐变/纹理仍在。结构偏差妨碍与A直接比较，保存为alt1。

### ch10-04-composition-b-central-alt2.png — 第2次，落选

- 文件：`figures/ch10/ch10-04-composition-b-central-alt2.png`
- 工具：image_gen.imagegen (functions tools.image_gen__imagegen)；模型：不知道（工具未返回具体模型标识）。
- 原始尺寸：1983 × 793；交付尺寸：2000 × 800。
- 原始缓存：`codex-output/exec-8b380d56-c883-49dc-9b84-1b0878a9c1b3.png`
- 原始SHA-256：`c4cd9e98b0ed1a14f577a359ef1b35bc11090012790e362823db1191a1e43b84`
- 交付SHA-256：`ac7b54622229e32233a6f20c5cc432d38440b9a7746d1bf6aa788beed7bb929c`
- 参考图：无。

**提示词变化与选择原因：** 第2次原文完整保留，追加单列沙漏、中央浅灰、四条主连接线、小云块不单独连接及统一颜色澄清。未选用：左下主连接线实际接到云图块，火后主图块仍游离。

**实际发送的完整prompt（不省略）：**

```text
Graphical abstract base art, wide banner, aspect ratio 5:2 (2000 x 800 px),
pure white background, flat 2D vector illustration, flat fills, thin dark gray
outlines, no gradients, no shadows, no 3D, no photographic texture.

ABSOLUTELY NO TEXT: no letters, words, numbers, symbols, labels or title.

Central composition. In the exact center, one large square top-down schematic
map tile (about 70% of the image height) of a landscape patch in very pale gray
with a crisp warm brown-orange irregular burned-area polygon and a thin
pale-blue river line.
Around it, four small elements, each about one quarter the size of the center
tile:
- upper left: a small tile of the same patch in muted green vegetation (before);
- lower left: a small tile of the same patch with a warm brown-orange area
  (after), and next to it an even smaller tile partly covered by a flat light
  gray cloud;
- upper right: a small blue-gray hourglass shape of stacked rounded rectangles
  (encoder-decoder network);
- lower right: a small square inset with three boundary lines around a burned
  area: dark gray solid, blue solid closely following it, light gray dashed
  clearly deviating.
Thin plain gray connector lines without arrowheads run from each small element
toward the central tile.

Palette only: muted green, warm brown-orange, blue-gray, blue, grays.
Do not draw: flames, smoke, globes, satellites, clocks, alarms, people,
charts, axes, numbers, photographs.

Correction for the second attempt: use exactly ONE vertically stacked hourglass network, each level a single horizontally centered solid rounded rectangle, with widths decreasing down to one narrow waist then increasing; no paired columns, no split bars, no horizontal bow-tie. The central map must be pale gray rather than green. Its side length is 70% of canvas height. Each of the four surrounding elements is about one quarter of its area; keep the comparison small. Four plain connectors, one from each main surrounding element to the central map; the tiny cloud tile is adjacent to the lower-left input and has no separate connector. Use the same landscape template and burned outline in every map. Render like a clean SVG: truly uniform solid fills, pure #FFFFFF canvas, no shading, no paper texture, no lighting effects. Muted green #A8C3A0, burned area #C8743C, network #8FA3B8, reference #3A3A3A, model #2F6DB5, threshold #A0A0A0. No typographic marks anywhere.
```

**对照画面内容/核验要点的看图结论：**

1. 画面五类对象与一朵云齐全；中央地图已改为浅灰，过火多边形与河流可见。
2. 单列沙漏形正确，但网络没有预期深灰轮廓；中央图约80%画布高，仍大于70%。
3. 四条线没有箭头头；左下线接到云图块，未从火后主图块通向中央，此项失败。
4. 比较图有三类边界；蓝线与深灰边界接近，虚线偏离，缩小时细节较密。
5. 火前、火后与中央的河流/过火形状相似；与A色相角色接近，但并非同一几何或逐像素配色。
6. 未见文字、字母、数字、伪文字或禁用火焰/地球；仍有轻微渐变。
7. 中央图式教学意图可辨，但连接关系不合格，保存为alt2。

### ch10-04-composition-b-central.png — 第3次，选定

- 文件：`figures/ch10/ch10-04-composition-b-central.png`
- 工具：image_gen.imagegen (functions tools.image_gen__imagegen)；模型：不知道（工具未返回具体模型标识）。
- 原始尺寸：1983 × 793；交付尺寸：2000 × 800。
- 原始缓存：`codex-output/exec-a1d57ac6-b360-4973-9776-ffa8cd56955f.png`
- 原始SHA-256：`1c64985a12ac0f99b4ea75a3a2fe90fe489da34d5f9a209bf91078a10536b44b`
- 交付SHA-256：`6374ec3101638537235e6ac298156655392b0c3b98db672c68ffa0b59f832aef`
- 参考图：无。

**提示词变化与选择原因：** 第3次重新保留规划全文，追加四条线的明确连接端点、云图块完全分离、单列沙漏和像素布局要求。选用：四条主连接线正确，云块独立，沙漏带深灰轮廓。

**实际发送的完整prompt（不省略）：**

```text
Graphical abstract base art, wide banner, aspect ratio 5:2 (2000 x 800 px),
pure white background, flat 2D vector illustration, flat fills, thin dark gray
outlines, no gradients, no shadows, no 3D, no photographic texture.

ABSOLUTELY NO TEXT: no letters, words, numbers, symbols, labels or title.

Central composition. In the exact center, one large square top-down schematic
map tile (about 70% of the image height) of a landscape patch in very pale gray
with a crisp warm brown-orange irregular burned-area polygon and a thin
pale-blue river line.
Around it, four small elements, each about one quarter the size of the center
tile:
- upper left: a small tile of the same patch in muted green vegetation (before);
- lower left: a small tile of the same patch with a warm brown-orange area
  (after), and next to it an even smaller tile partly covered by a flat light
  gray cloud;
- upper right: a small blue-gray hourglass shape of stacked rounded rectangles
  (encoder-decoder network);
- lower right: a small square inset with three boundary lines around a burned
  area: dark gray solid, blue solid closely following it, light gray dashed
  clearly deviating.
Thin plain gray connector lines without arrowheads run from each small element
toward the central tile.

Palette only: muted green, warm brown-orange, blue-gray, blue, grays.
Do not draw: flames, smoke, globes, satellites, clocks, alarms, people,
charts, axes, numbers, photographs.

Third-attempt layout correction: four connector lines attach to the CENTER of the right edge of the before tile, the CENTER of the right edge of the after tile, the LEFT side of the network, and the LEFT edge of the comparison, respectively. All terminate at the central map. The tiny cloud tile is detached below-left of the AFTER tile, never crossed by any connector. Draw one vertical hourglass from continuous centered rounded rectangles, not split columns. The central map is a pale-gray square of side 560 px centered at (1000,400) on a 2000 by 800 px canvas. Surrounding main map tiles and network each fit within about 280 by 280 px, cloud tile smaller. Match the same river and burned shape throughout. Uniform #FFFFFF background and uniform flat fills, #A8C3A0 vegetation, #C8743C burned land, #8FA3B8 network, #3A3A3A reference and thin object outlines, #2F6DB5 model, #A0A0A0 dashed threshold. No texture, shading, highlights or typographic marks.
```

**对照画面内容/核验要点的看图结论：**

1. 画面：中央过火区大图、左上火前、左下火后、右上沙漏、右下比较、左下角独立小云图块全部齐全。
2. 连接：从火前、火后、网络、比较分别通向中央，共四条普通灰线；无箭头头；云块无独立连线。
3. 中央为浅灰背景与棕橙过火区、蓝色河流；火后与中央的河流和主要过火斑块布局相似。
4. 比较有深灰参考、蓝色模型、浅灰虚线阈值轮廓；蓝线总体更接近参考，但局部仍有可见偏差；非定量结果。
5. 调色：绿色/棕橙/蓝灰/蓝/灰的语义与A相同；实际色值、斑块细节不同，不能称作精确同一调色或同一地块模板。
6. 未见文字、字母、数字、伪文字；没有火焰、地球、时钟等禁用对象。
7. 残余偏差：中央图高约77%而非70%，宽略大于高；周围网络偏大；表面有轻微明暗变化而非严格纯色。
8. 教学目的：中央重、比较退居角落的布局成立；选为B底图，几何/色值偏差保留说明。

### ch10-05-overclaim-alt1.png — 第1次，落选

- 文件：`figures/ch10/ch10-05-overclaim-alt1.png`
- 工具：image_gen.imagegen (functions tools.image_gen__imagegen)；模型：不知道（工具未返回具体模型标识）。
- 原始尺寸：1983 × 793；交付尺寸：2000 × 800。
- 原始缓存：`codex-output/exec-ef66dd7a-611f-4030-810f-08366ab6b2ca.png`
- 原始SHA-256：`be64380ea343ee02e59eebc4f2523242d2bd8fa8ef276452eceb5bb895bf734a`
- 交付SHA-256：`1675217b6405e1a95a6583a965e812d9b1dfe1b65af553cad67a95df4b4d4b6e`
- 参考图：无。

**提示词变化与选择原因：** 首轮逐字使用规划 prompt。因钟面出现1–12类数字及警报感叹号，违反无字/无数字要求，必须重生成；本图不是允许故意伪文字的反例。

**实际发送的完整prompt（不省略）：**

```text
Deliberately over-dramatic graphical abstract base art for a teaching
counter-example, wide banner, aspect ratio 5:2 (2000 x 800 px).
Dark blue gradient background with glowing accents.
Left: a photorealistic satellite-style top-down view of a forest with a bright
red-orange active fire front and thick gray smoke plumes.
Center: a glowing glossy 3D "AI brain" made of circuit lines, with light rays.
Right: a 3D Earth globe covered by a bright grid, with several red flame icons
on it, a red triangular alarm icon, and an alarm clock.
Glossy, cinematic, high contrast, lens flare.
NO TEXT: no letters, no words, no numbers, no symbols, no labels.
Leave a dark empty band across the top 18% for a headline.
```

**对照画面内容/核验要点的看图结论：**

1. 画面/O1：左侧写实森林俯视场景成立；这是生成示意，不是真实卫星观测。
2. 画面/O2/O7：红橙火线、火焰与浓烟齐全，符合指定的夸大反例，而不是误画成普通过火区。
3. 画面/O3：带明亮网格和多处红色火焰的地球齐全。
4. 画面/O4：闹钟存在，但钟面含数字；警报三角含感叹号，严格无字检查失败。
5. 画面：中央发光电路大脑、深蓝渐变、光束与高对比效果符合反例要求。
6. 核验：O5百分比、O6夸大标题、O1–O7编号和虚构示例注记未生成，须由后续TikZ加入；不是本次底图验收项。
7. 顶部有深色文字带，边缘烟雾/光晕接近其下界；不得宣称整图严格满足空带。
8. 保存为alt1，明确禁用于正文选片。

### ch10-05-overclaim-alt2.png — 第2次，落选

- 文件：`figures/ch10/ch10-05-overclaim-alt2.png`
- 工具：image_gen.imagegen (functions tools.image_gen__imagegen)；模型：不知道（工具未返回具体模型标识）。
- 原始尺寸：1983 × 793；交付尺寸：2000 × 800。
- 原始缓存：`codex-output/exec-f9d0c911-0040-44c8-8534-64bdf711fbc3.png`
- 原始SHA-256：`8f8e3cacac3692b56166e9efd3021de78595574fb2b1fa3231200177a3c75e49`
- 交付SHA-256：`556e50b2942814a1284d44d96ff29b5aa0c79f2144ac858522e992ae15559b6d`
- 参考图：无。

**提示词变化与选择原因：** 第2次保留原文，追加空白钟面（无数字、罗马数字、刻度）、空心警报三角和无字限制。未选用：钟面12点位置仍有一条易被误读为数字1的短刻线。

**实际发送的完整prompt（不省略）：**

```text
Deliberately over-dramatic graphical abstract base art for a teaching
counter-example, wide banner, aspect ratio 5:2 (2000 x 800 px).
Dark blue gradient background with glowing accents.
Left: a photorealistic satellite-style top-down view of a forest with a bright
red-orange active fire front and thick gray smoke plumes.
Center: a glowing glossy 3D "AI brain" made of circuit lines, with light rays.
Right: a 3D Earth globe covered by a bright grid, with several red flame icons
on it, a red triangular alarm icon, and an alarm clock.
Glossy, cinematic, high contrast, lens flare.
NO TEXT: no letters, no words, no numbers, no symbols, no labels.
Leave a dark empty band across the top 18% for a headline.

Correction for the second attempt: the alarm clock face must be completely unmarked: no digits, Roman numerals, tick marks, letters, or glyphs, only two plain hands on a blank dial. The red warning triangle must have an empty interior, with no exclamation mark or any other glyph. Preserve all the requested counter-example objects and the empty top band. Do not add any written or typographic marks anywhere.
```

**对照画面内容/核验要点的看图结论：**

1. 写实森林、活跃火线、浓烟、中央电路大脑、地球网格、火焰图标、警报三角与闹钟全部齐全。
2. 钟面大部分数字消失，警报感叹号已消失；但12点位置的短刻线有字形歧义，因此按严格无字标准继续重生成。
3. 地球与光晕进入顶部约18%区域，完整空带要求未满足；闹钟偏到地球左下，较规划的右下位置有偏移。
4. 深蓝渐变、电影感与高光符合过度主张反例；没有新增真实数据/精度数字。
5. 夸大标题、百分比、编号及虚构示例水印依任务范围留给TikZ；不将其缺失判为本底图失败。
6. 保存为alt2，不选用。

### ch10-05-overclaim.png — 第3次，选定

- 文件：`figures/ch10/ch10-05-overclaim.png`
- 工具：image_gen.imagegen (functions tools.image_gen__imagegen)；模型：不知道（工具未返回具体模型标识）。
- 原始尺寸：1983 × 793；交付尺寸：2000 × 800。
- 原始缓存：`codex-output/exec-366e8ca0-4be8-4292-8c2c-fc3c86305851.png`
- 原始SHA-256：`d554177133ddee2c14fc5c6a0a9c37d593ee37597e33cabca1fe261ddf7640b0`
- 交付SHA-256：`a56e5af8b274afff803171dae63ac46d851808bdeb8c79a5f4f2ebddfc98f894`
- 参考图：无。

**提示词变化与选择原因：** 第3次保留规划全文，追加钟面只保留两支指针、12点位置无刻线、空警报三角、闹钟靠右下及顶部留白澄清。选用：钟面和警报内不再有文字或近似数字的刻线。

**实际发送的完整prompt（不省略）：**

```text
Deliberately over-dramatic graphical abstract base art for a teaching
counter-example, wide banner, aspect ratio 5:2 (2000 x 800 px).
Dark blue gradient background with glowing accents.
Left: a photorealistic satellite-style top-down view of a forest with a bright
red-orange active fire front and thick gray smoke plumes.
Center: a glowing glossy 3D "AI brain" made of circuit lines, with light rays.
Right: a 3D Earth globe covered by a bright grid, with several red flame icons
on it, a red triangular alarm icon, and an alarm clock.
Glossy, cinematic, high contrast, lens flare.
NO TEXT: no letters, no words, no numbers, no symbols, no labels.
Leave a dark empty band across the top 18% for a headline.

Third-attempt correction: the alarm clock has a pristine blank circular dial with ONLY two plain clock hands and a central pivot. Absolutely no indices, ticks, numerals, digits, Roman numerals or marks anywhere around the dial: especially leave the twelve-o'clock location completely blank. Its casing is also unmarked. The triangular warning sign is an empty glowing triangular outline with no exclamation mark. Put the clock near the lower-right corner. Keep every object and bright glow entirely below y=0.20, leaving the top 18% a quiet dark blue band without foreground objects. The forest scene is an overhead satellite-style view. Preserve the active fire front, thick smoke, circuit brain, gridded globe, red flames and cinematic exaggeration; no text or glyphs anywhere.
```

**对照画面内容/核验要点的看图结论：**

1. 画面/O1：左侧为照片质感森林俯视视图，有生成式观测外观；必须在后续图注写明虚构，非真实影像。
2. 画面/O2/O7：红橙活跃火线、大量火焰与浓灰烟均存在；错误类型与规划反例一致。
3. 画面/O3：右侧三维地球带全球网格及多枚红色火焰，明确表达指定的覆盖夸大。
4. 画面/O4：右下闹钟保留两支指针和中心轴，无数字/刻线；旁边为内部空白的红色警报三角。
5. 画面：中央电路大脑、发光光束、深蓝渐变、高反差和镜头高光均存在。
6. 核验：看图未见文字、字母、数字或伪文字；标题/百分比/编号/虚构水印须后续TikZ叠加，本次没有生成这些文字。
7. 残余偏差：顶部完全空的深色带约15%而非18%；烟雾和光晕从其下缘开始。森林为有体积烟柱的俯视效果，并非严格正射影像。
8. 规划内部O7不一致：§3.7写云与烟完全消失，FIG画面/prompt却指定浓烟，本图按FIG具体画面/prompt保留浓烟；后续作者应统一讲解措辞。
9. 选为反例底图。独立底图没有虚构水印，排版发布前仍需完成规划中明确的水印文字层。

### ch10-06-final-base-alt1.png — 第1次，落选

- 文件：`figures/ch10/ch10-06-final-base-alt1.png`
- 工具：image_gen.imagegen (functions tools.image_gen__imagegen)；模型：不知道（工具未返回具体模型标识）。
- 原始尺寸：1983 × 793；交付尺寸：2000 × 800。
- 原始缓存：`codex-output/exec-5b438c6f-d276-4aa3-81ad-e19cee09d476.png`
- 原始SHA-256：`1151e72481c6c31c16e010216101194f5748fb6458b40f068cc577822128da53`
- 交付SHA-256：`08b27235a5ced74b2f0f81cab2d8b181cadbff367b8fecc5dc795c9997bc1e98`
- 参考图：无。

**提示词变化与选择原因：** 首轮逐字使用规划终稿 prompt。未选用：网络条块分成左右两列，阈值轮廓偏离不够突出，输出图比输入大得多。

**实际发送的完整prompt（不省略）：**

```text
Final graphical abstract base art, wide banner, aspect ratio 5:2,
2000 x 800 px, pure white background, flat 2D vector illustration, flat fills,
uniform thin dark gray (#3A3A3A) outlines, no gradients, no shadows, no 3D, no
photographic texture, crisp edges.

THIS IMAGE MUST CONTAIN NO TEXT AT ALL: no letters, words, numbers, symbols,
labels, legend, title or watermark.

EMPTY BANDS: keep y 0.00-0.15 (top), y 0.76-0.84 (caption strip under the four
stages) and y 0.88-1.00 (bottom) completely white.

Four stages, all objects vertically within y 0.18-0.72:
1. x 0.04-0.25: two square schematic map tiles of the same landscape patch side
   by side (left: muted green #A8C3A0 vegetation patches; right: same patch with
   a warm brown-orange #C8743C burned area), same pale-blue river line in both.
   A smaller tile partly covered by a flat light gray (#D5D5D5) cloud sits at
   the upper left corner of the stage.
2. x 0.30-0.45: one blue-gray (#8FA3B8) hourglass of stacked rounded
   rectangles (encoder-decoder), nothing else.
3. x 0.50-0.73: one larger square map tile of the same patch in very pale gray
   with a crisp #C8743C burned-area polygon (about 1.2 times the input tiles).
4. x 0.77-0.96: a square inset of the same patch outline with three thick
   boundary lines around the burned area: #3A3A3A solid (reference), #2F6DB5
   solid closely following it, #A0A0A0 dashed clearly deviating from it.
Two identical #3A3A3A arrows with filled heads: stage 1 -> 2, stage 2 -> 3.
No arrow between stages 3 and 4.

Do not draw: flames, smoke, globes, satellites, clocks, alarms, people, charts,
axes, numbers, photographs, decorative backgrounds.
```

**对照画面内容/核验要点的看图结论：**

1. 画面：火前/火后图对、云遮挡小图、网络、灰底过火区输出、比较插图全部存在；河流位置基本一致。
2. 网络由左右分开的矩形形成X形，未形成单列连续矩形沙漏，失败。
3. 两支同型右向流程箭头正确；输出和比较之间无箭头。
4. 比较有三类轮廓，但阈值虚线离参考不够远，未充分落实教学所需差异。
5. 输出图边长约为输入的1.7倍以上，而非约1.2倍；部分对象下缘接近y=0.75，超过指定0.72。
6. 顶/底/文字带视觉可用；未见数字、文字、字母、伪文字、火焰或地球；仍有轻微渐变。
7. §3.9：C2、C3语义项、C4文件项、C6可视无字项符合；C1需文字层才能完整判断，C5/C7/C8/C9未在本任务执行。
8. 因网络结构与比较显著性问题保存为alt1。

### ch10-06-final-base-alt2.png — 第2次，落选

- 文件：`figures/ch10/ch10-06-final-base-alt2.png`
- 工具：image_gen.imagegen (functions tools.image_gen__imagegen)；模型：不知道（工具未返回具体模型标识）。
- 原始尺寸：1983 × 793；交付尺寸：2000 × 800。
- 原始缓存：`codex-output/exec-d846001b-38b1-4dbf-89e0-c20e3e84e875.png`
- 原始SHA-256：`6aa0c7ca83c70d827d88d6eb82413a8b02833abcc68ec5fc4d8af5ce8fe3f435`
- 交付SHA-256：`90ad7ad0926f35bf2e6b33cb0f28779a77265b816ac3a7917622255c8a6933c2`
- 参考图：无。

**提示词变化与选择原因：** 第2次保留规划全文，追加单列沙漏、1.2倍输出、明确留白范围及阈值偏离澄清。未选用：虽改正网络，输出仍过大，且与最终选用的A版地块/轮廓不同。

**实际发送的完整prompt（不省略）：**

```text
Final graphical abstract base art, wide banner, aspect ratio 5:2,
2000 x 800 px, pure white background, flat 2D vector illustration, flat fills,
uniform thin dark gray (#3A3A3A) outlines, no gradients, no shadows, no 3D, no
photographic texture, crisp edges.

THIS IMAGE MUST CONTAIN NO TEXT AT ALL: no letters, words, numbers, symbols,
labels, legend, title or watermark.

EMPTY BANDS: keep y 0.00-0.15 (top), y 0.76-0.84 (caption strip under the four
stages) and y 0.88-1.00 (bottom) completely white.

Four stages, all objects vertically within y 0.18-0.72:
1. x 0.04-0.25: two square schematic map tiles of the same landscape patch side
   by side (left: muted green #A8C3A0 vegetation patches; right: same patch with
   a warm brown-orange #C8743C burned area), same pale-blue river line in both.
   A smaller tile partly covered by a flat light gray (#D5D5D5) cloud sits at
   the upper left corner of the stage.
2. x 0.30-0.45: one blue-gray (#8FA3B8) hourglass of stacked rounded
   rectangles (encoder-decoder), nothing else.
3. x 0.50-0.73: one larger square map tile of the same patch in very pale gray
   with a crisp #C8743C burned-area polygon (about 1.2 times the input tiles).
4. x 0.77-0.96: a square inset of the same patch outline with three thick
   boundary lines around the burned area: #3A3A3A solid (reference), #2F6DB5
   solid closely following it, #A0A0A0 dashed clearly deviating from it.
Two identical #3A3A3A arrows with filled heads: stage 1 -> 2, stage 2 -> 3.
No arrow between stages 3 and 4.

Do not draw: flames, smoke, globes, satellites, clocks, alarms, people, charts,
axes, numbers, photographs, decorative backgrounds.

Correction for the second attempt: the network is exactly ONE vertical stack, every level ONE horizontally centered rounded rectangle. Bar widths decrease down to a single waist and increase again, making a solid hourglass silhouette; never split each level into left and right bars. Match the same river and same burned polygon across all tiles. Put the entire output and comparison squares inside y 0.22-0.69 so every required text band stays empty. Output square side length is approximately 1.2 times each of the two input squares. Give the comparison exactly three closed contours: dark gray reference and blue model nearly coincide, but the lighter gray dashed threshold must deviate conspicuously by at least 15% of inset width at several edges. Use thick lines so this difference remains visible when small. All fills and background must be truly uniform flat RGB colors like an SVG export: no lighting, no texture, no gradients, no cast shadows. Keep exactly two identical right-pointing arrows and no extra marks.
```

**对照画面内容/核验要点的看图结论：**

1. 四段与云图块齐全；单个连续矩形沙漏正确，带深灰轮廓。
2. 输入对河流走向相近；输出/比较主要过火区形态相似，但不能当成数据配准证据。
3. 两支同型流程箭头正确，输出与比较之间无箭头。
4. 三类轮廓已加粗，灰虚线偏离较清晰；蓝/灰实线部分重叠，比较关系成立。
5. 输出边长约1.6倍输入，而非约1.2倍；对象下缘约y=0.75，超出指定0.72。
6. 未见文字、字母、数字、伪文字或禁用图标；视觉留白充足，但填色不是严格纯色。
7. §3.9：底图语义与格式可检查；完整贡献卡、双语文字层、缩略图和产品实测不能在本次据此宣称通过。
8. 保留为alt2，选第3次以匹配A版构图/地块并增强边界线。

### ch10-06-final-base.png — 第3次，选定

- 文件：`figures/ch10/ch10-06-final-base.png`
- 工具：image_gen.imagegen (functions tools.image_gen__imagegen)；模型：不知道（工具未返回具体模型标识）。
- 原始尺寸：1983 × 793；交付尺寸：2000 × 800。
- 原始缓存：`codex-output/exec-6d309432-8fda-4234-afad-1bca642c5e9c.png`
- 原始SHA-256：`592e78d5e034fbee911a85a514c1a081292aa1c64da0ab236ea3e8b67911ab22`
- 交付SHA-256：`f405cbde737e779762a5d96a9c2dcb9459d0d856b354692fc36de354bc553eca`
- 参考图：`codex-output/exec-302a97ae-ea4c-4010-a771-a313e209d688.png`（对应选定ch10-03首轮）。

**提示词变化与选择原因：** 第3次以ch10-03首轮为参考，保留终稿原文，追加对象保持、单列沙漏、目标像素大小、两箭头和粗边界要求。选用：最接近实际选用A底图，三个边界更粗且比较关系清楚。参考图仅用于生成，没有用程序重画科学内容。

**实际发送的完整prompt（不省略）：**

```text
Final graphical abstract base art, wide banner, aspect ratio 5:2,
2000 x 800 px, pure white background, flat 2D vector illustration, flat fills,
uniform thin dark gray (#3A3A3A) outlines, no gradients, no shadows, no 3D, no
photographic texture, crisp edges.

THIS IMAGE MUST CONTAIN NO TEXT AT ALL: no letters, words, numbers, symbols,
labels, legend, title or watermark.

EMPTY BANDS: keep y 0.00-0.15 (top), y 0.76-0.84 (caption strip under the four
stages) and y 0.88-1.00 (bottom) completely white.

Four stages, all objects vertically within y 0.18-0.72:
1. x 0.04-0.25: two square schematic map tiles of the same landscape patch side
   by side (left: muted green #A8C3A0 vegetation patches; right: same patch with
   a warm brown-orange #C8743C burned area), same pale-blue river line in both.
   A smaller tile partly covered by a flat light gray (#D5D5D5) cloud sits at
   the upper left corner of the stage.
2. x 0.30-0.45: one blue-gray (#8FA3B8) hourglass of stacked rounded
   rectangles (encoder-decoder), nothing else.
3. x 0.50-0.73: one larger square map tile of the same patch in very pale gray
   with a crisp #C8743C burned-area polygon (about 1.2 times the input tiles).
4. x 0.77-0.96: a square inset of the same patch outline with three thick
   boundary lines around the burned area: #3A3A3A solid (reference), #2F6DB5
   solid closely following it, #A0A0A0 dashed clearly deviating from it.
Two identical #3A3A3A arrows with filled heads: stage 1 -> 2, stage 2 -> 3.
No arrow between stages 3 and 4.

Do not draw: flames, smoke, globes, satellites, clocks, alarms, people, charts,
axes, numbers, photographs, decorative backgrounds.

Third attempt, using the supplied composition-A image only as a visual reference. Preserve its single centered vertical stack of continuous rounded rectangles, its two flow arrows, the same landscape and river in the input pair, and the comparison with no connecting arrow. Correct the geometry to the final specification: each input square is about 200 by 200 px, and the output square about 240 by 240 px (1.2 times the input side), with the comparison square about 300 by 300 px. Center the four stages around x=280,760,1240,1720 on a 2000 by 800 canvas; center main objects around y=400. Keep all objects, including the cloud tile, within y=144 to 576. Make the three comparison lines visibly thicker than the reference image, dark gray and blue nearly coincident and dashed light gray clearly deviating. The top, caption and bottom bands must be entirely white. Preserve the exact same burned shape across the post-fire, output and comparison maps. Uniform flat fills with thin gray outlines; no shading, texture, cast shadows or typographic marks.
```

**对照画面内容/核验要点的看图结论：**

1. 画面①：火前/火后影像对及上方云遮挡图块保留；相对于参考A，输入的同一河流/植被结构可辨，没有被改成照片或新场景。
2. 画面②：保留A的单个竖向连续矩形沙漏，没有连带改成分列网络或电路。
3. 画面③：浅灰输出、暖棕橙过火多边形存在，主要河流和轮廓延续A；不宣称严格几何注册。
4. 画面④：深灰、蓝实线与浅灰虚线齐全，线条明显比A更粗；蓝色大部分贴近深灰，虚线有明显偏离。
5. 箭头：恰两支同型实心右箭头，①→②→③；③④无箭头。
6. 留白：顶部0–0.15、阶段文字带0.76–0.84、底部0.88–1均无主要图形；像素抽查不是全255，详见留白实测。
7. 尺寸偏差：手工从图框估读，输入边长约225–230px，输出约365–370px，约1.6倍而非1.2倍；相对A输出也没有放大到1.2倍。少数对象最低到约y=0.75，超0.72。
8. 视觉偏差：云块偏大；填色有轻微明暗变化，颜色未严格等于prompt十六进制值；背景接近白而非逐像素纯白。
9. 无字/禁用项：未见文字、字母、数字、伪文字、照片质感影像、火焰、地球、闹钟或图表。
10. 选为终稿底图；不能称为C1–C9全通过，完整验收状态见后表。

## ch10-06选定底图：§3.9 C1–C9对应状态

| 项目 | 本次状态与证据 |
|---|---|
| C1 贡献卡四行 | 部分具备：影像对/网络/输出/比较及云块有对应；已过火、非火点探测或预测、测试火场等完整限定依赖后续文字层，底图本身不能全部表达。 |
| C2 无超出论文元素 | 底图可视检查通过：都是规划列出的示意对象，未见火焰、地球、预警钟或数值结果。 |
| C3 无数字、数据图、照片质感 | 可视检查通过；未执行独立全图200%终审。 |
| C4 比例与像素 | 交付文件实测2000×800、5:2；高于1328×531。工具原始尺寸不同，规范步骤已记录。 |
| C5 缩略图可读 | 本任务不生成文字层/缩略图，未测试；目录中其他任务的ch10-07不作为本次证据。 |
| C6 底图无伪文字 | 工具显示和view_image原尺寸复核未见文字/伪文字；未执行独立OCR或全图200%终审。 |
| C7 中英仅文字层不同 | 交付一个共用底图，SHA-256见上；未生成或比较中英叠加版，完整项待后续排版核验。 |
| C8 期刊当前要求复核 | 本次只执行本地规划指定出图，未重新访问期刊页面；不可据此声称已复核投稿要求。 |
| C9 PDF转提示词实测归档 | 不在本次任务范围，未上传PDF，未创建或验证pdf-prompt.txt。 |

## 留白像素实测

使用Pillow仅读取交付图RGB像素；所有位置采用左上原点，右/下为半开区间。没有用这些读数改图。完整结果为`band-verification.json`。

| 图 / 区域 | 像素框 | 纯白像素比例 | 各通道均≥245 | RGB通道极值 |
|---|---|---:|---:|---|
| ch10-03 顶部15% | (0,0,2000,120) | 10.8808% | 100% | 253–255 |
| ch10-03 底部12% | (0,704,2000,800) | 10.8188% | 100% | 253–255 |
| ch10-06 顶部15% | (0,0,2000,120) | 12.5483% | 100% | 253–255 |
| ch10-06 阶段文字带 | (0,608,2000,672) | 14.4141% | 100% | 249–255 |
| ch10-06 底部12% | (0,704,2000,800) | 12.4406% | 100% | 253–255 |

结论：预留带无主要图形且视觉近白，严格“完全白”不通过；数值不能替代看图识别文字。B中央图、终稿输出的比例来自目视图框坐标估读，故使用“约”，不是自动分割测量结果。

## 要求的实测输出

下面为实际`ls -l`及逐张Pillow像素输出。`ls`包含同目录其他任务文件，只读列出，不属于本次出图；像素检查限定本次11张。

```text
$ ls -l figures/ch10/
total 36640
-rw-r--r--@ 1 zeroone  staff     2023 Oct 29 16:07 ch10-01-ga-formats-en.tex
-rw-r--r--@ 1 zeroone  staff     2155 Oct 29 16:07 ch10-01-ga-formats-zh.tex
-rw-r--r--@ 1 zeroone  staff     2249 Oct 29 16:06 ch10-02-paper-to-card-en.tex
-rw-r--r--@ 1 zeroone  staff     2234 Oct 29 16:06 ch10-02-paper-to-card-zh.tex
-rw-r--r--@ 1 zeroone  staff  1133899 Oct 29 16:13 ch10-03-composition-a-narrative-alt1.png
-rw-r--r--@ 1 zeroone  staff  1166488 Oct 29 16:13 ch10-03-composition-a-narrative.png
-rw-r--r--@ 1 zeroone  staff  1390664 Oct 29 16:13 ch10-04-composition-b-central-alt1.png
-rw-r--r--@ 1 zeroone  staff  1282775 Oct 29 16:13 ch10-04-composition-b-central-alt2.png
-rw-r--r--@ 1 zeroone  staff  1283931 Oct 29 16:13 ch10-04-composition-b-central.png
-rw-r--r--@ 1 zeroone  staff  2813012 Oct 29 16:13 ch10-05-overclaim-alt1.png
-rw-r--r--@ 1 zeroone  staff  2694703 Oct 29 16:15 ch10-05-overclaim-alt2.png
-rw-r--r--@ 1 zeroone  staff  2901991 Oct 29 16:15 ch10-05-overclaim.png
-rw-r--r--@ 1 zeroone  staff  1159071 Oct 29 16:13 ch10-06-final-base-alt1.png
-rw-r--r--@ 1 zeroone  staff  1167086 Oct 29 16:13 ch10-06-final-base-alt2.png
-rw-r--r--@ 1 zeroone  staff  1189299 Oct 29 16:13 ch10-06-final-base.png
-rw-r--r--@ 1 zeroone  staff    75198 Oct 29 16:07 ch10-07-thumbnail-test-en.pdf
-rw-r--r--@ 1 zeroone  staff   126609 Oct 29 16:07 ch10-07-thumbnail-test-en.png
-rw-r--r--@ 1 zeroone  staff    83468 Oct 29 16:07 ch10-07-thumbnail-test-zh.pdf
-rw-r--r--@ 1 zeroone  staff   136630 Oct 29 16:07 ch10-07-thumbnail-test-zh.png

Pixel dimensions (this run only; Pillow Image.size):
ch10-03-composition-a-narrative-alt1.png: 2000 x 800 px; aspect=2.50000000; RGB; PNG valid
ch10-03-composition-a-narrative.png: 2000 x 800 px; aspect=2.50000000; RGB; PNG valid
ch10-04-composition-b-central-alt1.png: 2000 x 800 px; aspect=2.50000000; RGB; PNG valid
ch10-04-composition-b-central-alt2.png: 2000 x 800 px; aspect=2.50000000; RGB; PNG valid
ch10-04-composition-b-central.png: 2000 x 800 px; aspect=2.50000000; RGB; PNG valid
ch10-05-overclaim-alt1.png: 2000 x 800 px; aspect=2.50000000; RGB; PNG valid
ch10-05-overclaim-alt2.png: 2000 x 800 px; aspect=2.50000000; RGB; PNG valid
ch10-05-overclaim.png: 2000 x 800 px; aspect=2.50000000; RGB; PNG valid
ch10-06-final-base-alt1.png: 2000 x 800 px; aspect=2.50000000; RGB; PNG valid
ch10-06-final-base-alt2.png: 2000 x 800 px; aspect=2.50000000; RGB; PNG valid
ch10-06-final-base.png: 2000 x 800 px; aspect=2.50000000; RGB; PNG valid
```

## 可追溯附件

- `codex-image-calls.json`：每次完整工具prompt、参数、参考图、源路径、原始/交付尺寸与哈希。
- `file-verification.txt`：上述ls/像素输出原件。
- `band-verification.json`：空白带读取结果。
- `audit-validation.txt`：首轮prompt逐字比对、记录完整性和所有交付PNG校验。

后续排版应基于选定文件；alt文件（尤其含数字或疑似字形的反例）仅用于过程存档。本次没有把文字层、投稿要求复核或产品实测错误地列为已完成。

