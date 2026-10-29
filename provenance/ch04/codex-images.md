# 第 04 章 codex-image 出图记录

日期：2026-10-29。依据：`production/plans/ch04.md` 中 FIG ch04-04，以及 `production/book-spec.md` 第 4、5 节。图清单中只有 FIG ch04-04 的两张底图属于本任务；其他 FIG 均为 python。标签叠加不在本次范围内。

## 交付与结论

生成并保存 `figures/ch04/ch04-04a-schematic-bad.png`、`figures/ch04/ch04-04b-schematic-base.png`，另保留 4b 的两张落选图。4a 共生成 1 次；4b 共生成 3 次，选第 2 次，未超过每图 3 次上限。全部为 PNG，1672 × 941 px。

4a 能展示指定的错误：红色同时表示工厂排放与热进入海洋，蓝色同时表示海气交换与水体环流；仍有未要求的鲸、鱼与海底装饰。4b 第 2 次具备要求的主要对象、数量和箭头方向，且比第 1 次没有输运方向冲突，比第 3 次热箭头在数值色觉模拟后的最弱背景对比更高；因此选为目前最接近规划的一版。**4b 未严格合格**：分区比例、指定 HEX、纯平涂、线宽和浮游植物位置仍有偏差，不能把它描述为精确遵循视觉规范的终稿。

四图提示词均逐字取自规划（保留换行），没有添加或修改文字。工具调用为 Codex 内置 `image_gen.imagegen`（函数接口 `image_gen__imagegen`）；工具没有返回具体底层模型名称，**不知道具体模型**。均设置 `transparent_background=false`，没有传入参考图。没有使用 SciDraw AI、外部素材或其他生成服务。

工具自动输出到其默认 generated_images 暂存目录，随后原样复制到指定文件名；没有删除工具原文件。除工具自身默认暂存外，本次只在 `figures/ch04/` 和 `provenance/ch04/` 写文件。没有修改章节、规划、脚本或其他类型的图，没有生成 TikZ 标签，没有 commit/push，没有启动子 agent。目录中同时出现的其他图和标签文件并非本次产物，下面 `ls -l` 仅如实保留核验时的目录快照。

### 尺寸和导出限制

- 提示词要求 landscape 16:9，实际为 1672/941 = 1.776833；严格 16:9 的相应高度是 940.5 px，因此有 0.5 px 的整数尺寸取整差。未裁切、拉伸或补边。
- 在规划的 174 mm 宽度下，原生有效分辨率约 244.1 ppi，并非规划视觉规范 §3.4 F 的 600 dpi。未用插值放大冒充更高原生分辨率。
- PNG 没有可编辑矢量线宽，不能直接核验为 0.75 pt。此任务只提供生成的底图，不提供矢量重绘。

## 逐张提示词与看图核验

以下结论来自逐张查看工具返回的完整原图；未见可辨认的文字、字母、数字、标签或伪文字。箭头及人字纹属于规划要求的图形符号。没有 OCR 证明，也没有把“未发现”表述为机器检测保证。

### ch04-04a-schematic-bad.png

- 路径：`figures/ch04/ch04-04a-schematic-bad.png`。
- 图号：4a；该图第 1 次生成；状态：选用。
- 实际工具：`image_gen.imagegen` / `image_gen__imagegen`；具体模型：不知道（工具未提供）。
- 原始输出：`codex-output/exec-71ef99df-a147-4833-9294-9fb393babe40.png`。
- PNG：1672 × 941 px；2645803 bytes。
- SHA-256：`8fcfb95647a8d5553a0d27b012f36b59f88b8aaad0a5c3f4aed6f7d08f073630`。
- Prompt 与规划逐字一致；修改原因：不适用，未修改。Prompt SHA-256：`dd8296ead7bc6db99a8fd72f2151ce4128b514a255a3d3aaf4828c2ae9bfcbc2`。

实际发送的完整 prompt：

```text
A glossy, highly polished 3D illustration of an ocean cross-section for a
climate science paper, landscape 16:9. Photorealistic blue waves on top, a
bright sun with radiating rays in a gradient orange-to-blue sky, a small ship
on the surface, shiny glass-like water with caustics and depth of field.
Thick glowing red 3D arrows go from the sky into the water and also from a
factory into the sky; thick glowing blue 3D arrows curve through the water and
also go from the air into the water. Dramatic lighting, lens flare, strong
shadows, saturated colors. No text, no letters, no numbers, no labels.
```

| 对照项 | 看图结论 |
|---|---|
| 光泽 3D 海洋剖面、写实波浪、渐变天空 | 符合。强立体、水下光束、焦散和饱和蓝色清楚可见。 |
| 太阳与光线、船只 | 符合。左上太阳与强放射光线，海面中部船只。 |
| 红色箭头同时用于 CO₂ 与热 | 符合。右侧工厂烟囱向大气的红箭头表示排放，太阳/天空向海面的红箭头表示热；确实是规划指定的颜色多义错误。下行红箭头主要终止在海面，深入混合层的距离不明确。 |
| 蓝色箭头同时用于水流与碳 | 符合。天空入海的蓝箭头与海内弯曲循环蓝箭头并存。 |
| 与统一规范相冲突的夸张风格 | 符合。发光粗箭头、浓重阴影、镜头光效和写实背景足以形成反例；不用文字错误代替风格错误。 |
| 不含任何文字/伪文字 | 逐张人工查看未发现；船舱细节表现为窗格，没有识别到可辨文字。 |
| 未要求的对象 | 偏差：增加鲸、鱼群、岩石与海底细节，超过规划所列的太阳和船等装饰。4a prompt 未明文禁止这些对象，但不属于要求内容，作为额外偏差保留记录。 |
| 选用理由 | 已呈现所有核心错误，无需用额外生成替换本轮；不能用这幅反例作为科学过程图。 |

### ch04-04b-schematic-base-alt1.png

- 路径：`figures/ch04/ch04-04b-schematic-base-alt1.png`。
- 图号：4b；该图第 1 次生成；状态：落选。
- 实际工具：`image_gen.imagegen` / `image_gen__imagegen`；具体模型：不知道（工具未提供）。
- 原始输出：`codex-output/exec-0cf8b856-ce82-4200-a6b8-074a73544821.png`。
- PNG：1672 × 941 px；1148937 bytes。
- SHA-256：`75d89d2f728747e350dab44a479db58e263cd5cc5bdf42d76e494065db98cef1`。
- Prompt 与规划逐字一致；修改原因：不适用，未修改。Prompt SHA-256：`fb451300970c042f40d0a802b9608a21247793bda4b2a518f62411dc094a01f8`。

实际发送的完整 prompt：

```text
Flat 2D scientific schematic of ocean heat and carbon uptake, landscape 16:9,
pure white background. ABSOLUTELY NO TEXT: no letters, no words, no numbers, no
symbols, no labels, no legend, no title.

STYLE (paper-wide visual spec v1): flat vector illustration; all outlines 0.75 pt
dark gray #3C3C3C with rounded joins; no gradients, no shadows, no highlights,
no 3D, no glow, no texture, no realistic water. Icons use neutral fills only
(#F2F2F2, #BDBDBD). Colour is used ONLY for the following quantities:
orange #E69F00 = CO2 in the atmosphere; blue #0072B2 = dissolved inorganic
carbon in seawater; vermilion #D55E00 = heat; sky blue #56B4E9 = water
transport. Nothing else may use these colours.

REGIONS (top to bottom):
- Top 25%: atmosphere, white.
- A thin dark gray gently wavy line across the full width at 25% height: the
  sea surface.
- 25-45%: surface mixed layer, very pale blue #DCEBF5.
- 45-90%: ocean interior, pale blue #C9DEEE, separated from the mixed layer by a
  faint thin line.
- Bottom 10%: empty white, reserved for a legend.

OBJECTS AND PROCESSES (draw exactly these, nothing else):
1. Top-left: one simple factory chimney icon in neutral gray standing on a short
   ground line at the left edge, with one straight dark gray arrow (filled
   triangular head) rising from it into the atmosphere.
2. In the atmosphere: about 12 small orange dots scattered in the left and
   middle parts.
3. Air-sea gas exchange: two straight dark gray arrows with filled heads, going
   down from the atmosphere through the sea surface into the mixed layer, in
   the left-middle part of the image.
4. In the mixed layer: about 10 small blue #0072B2 dots near the two arrows.
5. Heat uptake: three vermilion wavy arrows with open V-shaped heads, going down
   from the atmosphere into the mixed layer in the middle of the image; the
   rightmost of them continues further down into the ocean interior.
6. Water transport: on the right side, one broad semi-transparent sky-blue band
   that starts in the mixed layer near the right edge, curves downward into the
   ocean interior, and then runs leftward along the interior, with a few
   chevron marks inside the band pointing along the flow.
7. Biological pump: three or four small round phytoplankton cell icons (neutral
   fill, gray outline) in the middle of the mixed layer, and below them two
   dotted dark gray arrows with small filled heads pointing down into the
   interior.

DO NOT DRAW: sun, rays, clouds, ships, fish, ice, land masses other than the
short ground line, sea floor details, coral, bubbles, any charts or data.
Leave white space around each process for labels.
```

| 对照项 | 看图结论 |
|---|---|
| 大气、混合层、内部、底部图例留白 | 分区存在，但海面/层间/留白起点约 32.8%/51.0%/83.2%，不是 25%/45%/90%。底部留白约 16.8%，超过 10%。 |
| 灰色烟囱与直线上行碳箭头 | 存在，烟囱在左上，灰色图标；描边与填充并非严格平涂。 |
| 大气橙点和表层蓝点 | 存在，约 12 个橙点、约 10 个蓝点，分别在大气与混合层，颜色未用于细胞本体。 |
| 两条直线海气交换箭头 | 符合，左中部两条深灰直线、实心头，穿过海面进入表层。 |
| 三条波浪热箭头，右一深入内部 | 符合，三条波浪线、开口 V 头，右一较长。 |
| 右侧输运宽带与顺流人字纹 | **不符合。** 带的形状由右上弯向左下，但右侧上段与中段人字纹指向右/右上，底段指左，方向互相冲突；这是落选的主要原因。 |
| 3–4 个中性细胞和两条向下颗粒线 | 4 个圆形细胞、2 条较细向下短点划线；在中右部而非规划的中部。没有把蓝色碳点直接连到细胞再连向深海。 |
| 图标中性、无装饰对象 | 细胞和烟囱均为灰色；没有太阳、船、鱼、冰、陆块或数据图。 |
| 无文字 | 未见文字、字母、数字、标签或伪文字。 |
| 精确色值、无渐变、无纹理 | 不符合。颜色仅近似，白底有轻微纹理，水层与圆点有细微色调变化。逐色采样见下。 |
| 生物泵不成为唯一人为碳主路径 | 有独立海气交换与输运带，颗粒线也较细，未画成一条串联唯一主路径；科学意义仍须同行核查。 |
| 重试 | 作为 4b 第 1 次落选图保留，随后沿用原提示词重新生成。 |

实测代表色（指定对象 ROI 中满足颜色条件的像素 RGB 中位数；不是保证每个像素同色）：

| 对象 | 规划 HEX | 代表实测 HEX |
|---|---|---|
| 大气橙点 | #E69F00 | #EF9608 |
| 海水蓝点 | #0072B2 | #0A76C3 |
| 热箭头 | #D55E00 | #EF590A |
| 碳箭头 | #3C3C3C | #404040 |
| 输运带可见色 | #56B4E9 | #82C4F1 |
| 白色大气 | #FFFFFF | #FEFEFE |
| 混合层背景 | #DCEBF5 | #D1E7F5 |
| 内部背景 | #C9DEEE | #BEDCF1 |

输运带允许半透明，因此可见色不同于源色不能单独证明源色错误；栅格 PNG 无法反推出唯一的原始颜色与透明度。橙点、蓝点、热箭头都应是不透明语义色，但全图中各自指定 HEX 的精确像素数均为 0，因此严格色值要求确实未实现。

### ch04-04b-schematic-base.png

- 路径：`figures/ch04/ch04-04b-schematic-base.png`。
- 图号：4b；该图第 2 次生成；状态：选用；仍有规划偏差。
- 实际工具：`image_gen.imagegen` / `image_gen__imagegen`；具体模型：不知道（工具未提供）。
- 原始输出：`codex-output/exec-33c4bdb6-9560-4dac-a711-2b165c6df849.png`。
- PNG：1672 × 941 px；1164556 bytes。
- SHA-256：`cfd1ac4ea8bb1e2c3c55d8c84db03ac0bb90b4b6d8021ea5e4ece0e58eae5048`。
- Prompt 与规划逐字一致；修改原因：不适用，未修改。Prompt SHA-256：`fb451300970c042f40d0a802b9608a21247793bda4b2a518f62411dc094a01f8`。

实际发送的完整 prompt：

```text
Flat 2D scientific schematic of ocean heat and carbon uptake, landscape 16:9,
pure white background. ABSOLUTELY NO TEXT: no letters, no words, no numbers, no
symbols, no labels, no legend, no title.

STYLE (paper-wide visual spec v1): flat vector illustration; all outlines 0.75 pt
dark gray #3C3C3C with rounded joins; no gradients, no shadows, no highlights,
no 3D, no glow, no texture, no realistic water. Icons use neutral fills only
(#F2F2F2, #BDBDBD). Colour is used ONLY for the following quantities:
orange #E69F00 = CO2 in the atmosphere; blue #0072B2 = dissolved inorganic
carbon in seawater; vermilion #D55E00 = heat; sky blue #56B4E9 = water
transport. Nothing else may use these colours.

REGIONS (top to bottom):
- Top 25%: atmosphere, white.
- A thin dark gray gently wavy line across the full width at 25% height: the
  sea surface.
- 25-45%: surface mixed layer, very pale blue #DCEBF5.
- 45-90%: ocean interior, pale blue #C9DEEE, separated from the mixed layer by a
  faint thin line.
- Bottom 10%: empty white, reserved for a legend.

OBJECTS AND PROCESSES (draw exactly these, nothing else):
1. Top-left: one simple factory chimney icon in neutral gray standing on a short
   ground line at the left edge, with one straight dark gray arrow (filled
   triangular head) rising from it into the atmosphere.
2. In the atmosphere: about 12 small orange dots scattered in the left and
   middle parts.
3. Air-sea gas exchange: two straight dark gray arrows with filled heads, going
   down from the atmosphere through the sea surface into the mixed layer, in
   the left-middle part of the image.
4. In the mixed layer: about 10 small blue #0072B2 dots near the two arrows.
5. Heat uptake: three vermilion wavy arrows with open V-shaped heads, going down
   from the atmosphere into the mixed layer in the middle of the image; the
   rightmost of them continues further down into the ocean interior.
6. Water transport: on the right side, one broad semi-transparent sky-blue band
   that starts in the mixed layer near the right edge, curves downward into the
   ocean interior, and then runs leftward along the interior, with a few
   chevron marks inside the band pointing along the flow.
7. Biological pump: three or four small round phytoplankton cell icons (neutral
   fill, gray outline) in the middle of the mixed layer, and below them two
   dotted dark gray arrows with small filled heads pointing down into the
   interior.

DO NOT DRAW: sun, rays, clouds, ships, fish, ice, land masses other than the
short ground line, sea floor details, coral, bubbles, any charts or data.
Leave white space around each process for labels.
```

| 对照项 | 看图结论 |
|---|---|
| 大气、混合层、内部、底部图例留白 | 分区和留白均存在，**比例不符**。海面约 32.0%，层间约 48.1%，白色图例区从约 79.8% 起，分别要求 25%、45%、90%。实际图例区约 20.2%。 |
| 灰色烟囱与上行排放箭头 | 有一座左上灰色烟囱和向上的深灰直线实心箭头，地线很短；箭头稍斜，不是精确竖直。增加一小块厂房轮廓，仍为同一工厂图标。 |
| 大气约 12 个橙点 | 约 12 个橙点位于左中大气，符合数量与位置意图；点面存在明暗变化，色值不符。 |
| 两条海气交换碳箭头 | 左中部两条深灰直线箭头穿过海面向下进入表层，均为实心三角头；符合。 |
| 表层约 10 个蓝点 | 约 10 个蓝点围绕两条交换箭头末端，符合对象、数量与分区。 |
| 三条热箭头 | 三条向下波浪线，均有开口 V 头；右一延伸到海洋内部，符合。颜色为近似朱红，未精确命中 #D55E00。 |
| 水体下沉与输运 | 单条浅天蓝宽带从右侧表层弯向深层，再向左延伸。上段人字纹朝左下，弯段朝左下，底段朝左，整体流向一致。顶部带入口接触右侧边界；没有明确终端箭头，仅靠内部人字纹示意。 |
| 浮游植物与下沉颗粒 | 4 个中性灰圆形细胞，位于混合层中右部，偏离规划的正中位置；下方 2 条细短点划线、实心小头向下，颗粒线比碳主线细。点线更接近方点/短划，非理想均匀圆点。 |
| 生物泵与人为 CO₂ 的关系 | 没有从烟囱/橙点直接串联细胞到深海的单一主路径。碳直线箭头共 3 条（含排放）而颗粒线 2 条；若仅比较海气交换，则都是 2 条，不能称“颗粒线比海气交换线数量少”。这由原 prompt 同时指定两者各 2 条造成，未自行改 prompt。 |
| 颜色只用于规定对象 | 橙用于大气点、深蓝用于海水点、朱红用于热箭头、天蓝用于输运带，图标本体中性灰；浅蓝水层是原规划明确允许的背景。语义分配符合，但精确色值不符合。 |
| 扁平、无渐变、描边 0.75 pt | 主体为 2D，没有 3D 光效和明显投影；仍有水层色调变化、圆点明暗、灰色烟囱填充变化及白底细纹理，所以不能判为严格无渐变。没有矢量路径，0.75 pt 未得到验证。 |
| 无太阳、船、鱼及其他未要求对象 | 未见太阳、光线、云、船、鱼、冰、珊瑚、海床、图表或数据。 |
| 无文字与标签留白 | 未见文字、字母、数字、标签或伪文字；右上与底部留白充分，原规划 TikZ 坐标仍需按真实位置调整。 |
| 色觉模拟下以形状区分 | 人工查看确认直线/波浪线/宽带/点线四种形状不同；另做三种 100% 严重度的颜色数值模拟，见下。没有做模拟全图的人工观看或真实读者测试，不能声称该项已完全验收。 |
| 科学复核 | 未获得物理海洋或海洋碳循环同行复核；“完整、无误导”的要求尚不能签署通过。 |
| 选用状态 | 第 2 次是三版中综合更好的底图，但仍属有明确偏差的选用稿，不是严格合格终稿。 |

实测代表色（指定对象 ROI 中满足颜色条件的像素 RGB 中位数；不是保证每个像素同色）：

| 对象 | 规划 HEX | 代表实测 HEX |
|---|---|---|
| 大气橙点 | #E69F00 | #ED9106 |
| 海水蓝点 | #0072B2 | #0571BA |
| 热箭头 | #D55E00 | #DD4E0A |
| 碳箭头 | #3C3C3C | #3F3F40 |
| 输运带可见色 | #56B4E9 | #84C5F1 |
| 白色大气 | #FFFFFF | #FEFEFE |
| 混合层背景 | #DCEBF5 | #D3E7F5 |
| 内部背景 | #C9DEEE | #BEDBEF |

输运带允许半透明，因此可见色不同于源色不能单独证明源色错误；栅格 PNG 无法反推出唯一的原始颜色与透明度。橙点、蓝点、热箭头都应是不透明语义色，但全图中各自指定 HEX 的精确像素数均为 0，因此严格色值要求确实未实现。

### ch04-04b-schematic-base-alt2.png

- 路径：`figures/ch04/ch04-04b-schematic-base-alt2.png`。
- 图号：4b；该图第 3 次生成；状态：落选。
- 实际工具：`image_gen.imagegen` / `image_gen__imagegen`；具体模型：不知道（工具未提供）。
- 原始输出：`codex-output/exec-2f875108-43e6-42c3-a6f8-9e6d9e7f8987.png`。
- PNG：1672 × 941 px；1135610 bytes。
- SHA-256：`f62aa3ddd9e49539e7bcde60301d1cce735d184654742c2fabcfb72b67e8eef0`。
- Prompt 与规划逐字一致；修改原因：不适用，未修改。Prompt SHA-256：`fb451300970c042f40d0a802b9608a21247793bda4b2a518f62411dc094a01f8`。

实际发送的完整 prompt：

```text
Flat 2D scientific schematic of ocean heat and carbon uptake, landscape 16:9,
pure white background. ABSOLUTELY NO TEXT: no letters, no words, no numbers, no
symbols, no labels, no legend, no title.

STYLE (paper-wide visual spec v1): flat vector illustration; all outlines 0.75 pt
dark gray #3C3C3C with rounded joins; no gradients, no shadows, no highlights,
no 3D, no glow, no texture, no realistic water. Icons use neutral fills only
(#F2F2F2, #BDBDBD). Colour is used ONLY for the following quantities:
orange #E69F00 = CO2 in the atmosphere; blue #0072B2 = dissolved inorganic
carbon in seawater; vermilion #D55E00 = heat; sky blue #56B4E9 = water
transport. Nothing else may use these colours.

REGIONS (top to bottom):
- Top 25%: atmosphere, white.
- A thin dark gray gently wavy line across the full width at 25% height: the
  sea surface.
- 25-45%: surface mixed layer, very pale blue #DCEBF5.
- 45-90%: ocean interior, pale blue #C9DEEE, separated from the mixed layer by a
  faint thin line.
- Bottom 10%: empty white, reserved for a legend.

OBJECTS AND PROCESSES (draw exactly these, nothing else):
1. Top-left: one simple factory chimney icon in neutral gray standing on a short
   ground line at the left edge, with one straight dark gray arrow (filled
   triangular head) rising from it into the atmosphere.
2. In the atmosphere: about 12 small orange dots scattered in the left and
   middle parts.
3. Air-sea gas exchange: two straight dark gray arrows with filled heads, going
   down from the atmosphere through the sea surface into the mixed layer, in
   the left-middle part of the image.
4. In the mixed layer: about 10 small blue #0072B2 dots near the two arrows.
5. Heat uptake: three vermilion wavy arrows with open V-shaped heads, going down
   from the atmosphere into the mixed layer in the middle of the image; the
   rightmost of them continues further down into the ocean interior.
6. Water transport: on the right side, one broad semi-transparent sky-blue band
   that starts in the mixed layer near the right edge, curves downward into the
   ocean interior, and then runs leftward along the interior, with a few
   chevron marks inside the band pointing along the flow.
7. Biological pump: three or four small round phytoplankton cell icons (neutral
   fill, gray outline) in the middle of the mixed layer, and below them two
   dotted dark gray arrows with small filled heads pointing down into the
   interior.

DO NOT DRAW: sun, rays, clouds, ships, fish, ice, land masses other than the
short ground line, sea floor details, coral, bubbles, any charts or data.
Leave white space around each process for labels.
```

| 对照项 | 看图结论 |
|---|---|
| 四个纵向分区 | 存在，海面/层间/留白起点约 30.8%/48.5%/81.3%，仍偏离 25%/45%/90%。底部留白约 18.7%。 |
| 灰色烟囱与上行排放 | 符合主要结构，左上单烟囱、短地线和向上直线深灰实心箭头。 |
| 橙点、蓝点和两条海气交换箭头 | 大气中约 13 个橙点、混合层中约 10 个蓝点；两条深灰直线向下过海面，符合“约”数量及对象分配。 |
| 三条波浪热箭头 | 符合三条、开口 V 头、右侧较长深入内部；朱红偏亮，未精确命中色值。 |
| 右侧输运带 | 流向基本一致，由右侧表层向左下弯曲，再向左延伸，未出现第 1 次相反的上段人字纹。 |
| 生物泵 | 4 个中性圆形细胞及两条下行圆点线，形状区分明确；细胞仍偏右，圆点与箭头头部偏粗。细胞增加鞭毛状附属，未要求这些细节。 |
| 保守科学关系 | 海气交换、输运和颗粒路径互相独立，没有把细胞吸收人为 CO₂ 画成唯一主路径；仍未通过同行复核。 |
| 无文字、无太阳/船/鱼等 | 未见任何文字、字母、数字或伪文字，未出现禁止的装饰对象。 |
| 精确颜色、纯平涂与线宽 | 不符合严格要求。色值漂移、纹理和轻微渐变仍在，未获得 0.75 pt 的矢量线宽。 |
| 色觉及形状核验 | 直线、波浪、宽带、圆点四种形状可见；数值模拟中热箭头在深层背景的最小亮度对比约 2.17:1，低于选用稿的约 2.36:1。没有全图模拟观看和读者测试。 |
| 落选理由 | 分区略更接近，但色值和平涂没有解决，颗粒表达较重，综合未优于第 2 次。第 3 次达到生成上限后停止，没有追加第 4 次。 |

实测代表色（指定对象 ROI 中满足颜色条件的像素 RGB 中位数；不是保证每个像素同色）：

| 对象 | 规划 HEX | 代表实测 HEX |
|---|---|---|
| 大气橙点 | #E69F00 | #E99205 |
| 海水蓝点 | #0072B2 | #0567B6 |
| 热箭头 | #D55E00 | #E7520C |
| 碳箭头 | #3C3C3C | #404447 |
| 输运带可见色 | #56B4E9 | #8ACAF1 |
| 白色大气 | #FFFFFF | #FEFEFE |
| 混合层背景 | #DCEBF5 | #D1E8F6 |
| 内部背景 | #C9DEEE | #BDDBF0 |

输运带允许半透明，因此可见色不同于源色不能单独证明源色错误；栅格 PNG 无法反推出唯一的原始颜色与透明度。橙点、蓝点、热箭头都应是不透明语义色，但全图中各自指定 HEX 的精确像素数均为 0，因此严格色值要求确实未实现。

## 像素与色觉数值检查方法

原始结果保存在 `provenance/ch04/pixel-audit.json`，仅收录本次四张图。Pillow 解码 RGB，NumPy 只读分析；没有通过 Python 或其他工具编辑、缩放、裁剪、调色这些图片。

背景取样 ROI（左上原点，单位 px，右/下边界不含）：大气 (1300,80,1500,200)，混合层 (100,330,200,420)，内部 (100,540,300,700)，底部白 (300,850,600,900)。语义色 ROI 与筛选后的像素数已存入 JSON；语义色使用 ROI 中颜色筛选后的 RGB 分量中位数，不把抗锯齿边缘的任一像素冒充整个对象颜色。主稿内部背景 ROI 的 RGB 范围为 (188–192,217–220,238–240)，并非均匀填色。白底样本范围 253–255，也非每点纯白。

分层读数来自 x=150 的扫描列，找相邻行 RGB 欧氏距离超过 15 的跃迁，再与原图海面/层间/底边位置核对。扫描也可能命中橙点等对象，所以仅选用对应分层的跃迁，未把其余跃迁当作边界。海面是波线，百分比只是该列近似值，误差为几个像素；偏离规划的幅度远大于该误差。

色觉数值检查：本地已安装 colorspacious，使用 `cspace_convert(rgb, {"name":"sRGB1+CVD","cvd_type":...,"severity":100}, "sRGB1")`，分别为 deuteranomaly、protanomaly、tritanomaly，裁切到 sRGB [0,1]，然后转线性 sRGB 计算相对亮度与对象/背景对比。输入为以上取样代表色，而非整幅模拟图；因此只是颜色的数值检查，不等于模拟图视觉验收，也不等于读者可读性认证。普通彩色原图已人工看图，四种箭头形式明确不同；色觉变换不改变其几何形状。

选用稿热箭头/海洋内部背景的亮度对比实测：正常 2.82:1；第二色觉差异 2.36:1；第一色觉差异 3.91:1；第三色觉差异 2.85:1。选用稿碳箭头/内部背景分别为 7.30:1、7.15:1、7.53:1、7.32:1。热箭头最弱处仍需最终尺寸下的模拟图与真实读者复查；没有用本表宣称通过特定可访问性标准。

## 完成标准实测输出

以下内容从 `provenance/ch04/verification.txt` 原样嵌入。`ls -l` 包括其他并行工作产物；尺寸、哈希核验仅针对本任务四张 PNG。

```text
核验时间：2026-10-29T16:13:36.892556+08:00
$ ls -l figures/ch04
total 37720
-rw-r--r--@ 1 zeroone  staff  1085793 Oct 29 16:13 ch04-01-inconsistent-set-en.pdf
-rw-r--r--@ 1 zeroone  staff  1269783 Oct 29 16:13 ch04-01-inconsistent-set-en.png
-rw-r--r--@ 1 zeroone  staff  1055302 Oct 29 16:12 ch04-01-inconsistent-set-zh.pdf
-rw-r--r--@ 1 zeroone  staff  1254288 Oct 29 16:12 ch04-01-inconsistent-set-zh.png
-rw-r--r--@ 1 zeroone  staff    21056 Oct 29 16:12 ch04-02-spec-page-en.pdf
-rw-r--r--@ 1 zeroone  staff   147631 Oct 29 16:12 ch04-02-spec-page-en.png
-rw-r--r--@ 1 zeroone  staff    35674 Oct 29 16:12 ch04-02-spec-page-zh.pdf
-rw-r--r--@ 1 zeroone  staff   164030 Oct 29 16:12 ch04-02-spec-page-zh.png
-rw-r--r--@ 1 zeroone  staff   281298 Oct 29 16:13 ch04-03-cvd-check-en.pdf
-rw-r--r--@ 1 zeroone  staff   267771 Oct 29 16:13 ch04-03-cvd-check-en.png
-rw-r--r--@ 1 zeroone  staff   269557 Oct 29 16:12 ch04-03-cvd-check-zh.pdf
-rw-r--r--@ 1 zeroone  staff   259796 Oct 29 16:12 ch04-03-cvd-check-zh.png
-rw-r--r--@ 1 zeroone  staff  2645803 Oct 29 16:08 ch04-04a-schematic-bad.png
-rw-r--r--@ 1 zeroone  staff  1148937 Oct 29 16:09 ch04-04b-schematic-base-alt1.png
-rw-r--r--@ 1 zeroone  staff  1135610 Oct 29 16:10 ch04-04b-schematic-base-alt2.png
-rw-r--r--@ 1 zeroone  staff  1164556 Oct 29 16:10 ch04-04b-schematic-base.png
-rw-r--r--@ 1 zeroone  staff     1020 Oct 29 16:10 ch04-04b-schematic-en.tex
-rw-r--r--@ 1 zeroone  staff      963 Oct 29 16:10 ch04-04b-schematic-zh.tex
-rw-r--r--@ 1 zeroone  staff    72970 Oct 29 16:12 ch04-05-fig2-carbonate-bad-en.png
-rw-r--r--@ 1 zeroone  staff    62745 Oct 29 16:12 ch04-05-fig2-carbonate-bad-zh.png
-rw-r--r--@ 1 zeroone  staff    31743 Oct 29 16:12 ch04-05-fig2-carbonate-en.pdf
-rw-r--r--@ 1 zeroone  staff   139291 Oct 29 16:12 ch04-05-fig2-carbonate-en.png
-rw-r--r--@ 1 zeroone  staff    33258 Oct 29 16:12 ch04-05-fig2-carbonate-zh.pdf
-rw-r--r--@ 1 zeroone  staff   141391 Oct 29 16:12 ch04-05-fig2-carbonate-zh.png
-rw-r--r--@ 1 zeroone  staff    25093 Oct 29 16:12 ch04-06-fig3-ohc-bad-en.png
-rw-r--r--@ 1 zeroone  staff    25093 Oct 29 16:12 ch04-06-fig3-ohc-bad-zh.png
-rw-r--r--@ 1 zeroone  staff    15217 Oct 29 16:12 ch04-06-fig3-ohc-en.pdf
-rw-r--r--@ 1 zeroone  staff    64103 Oct 29 16:12 ch04-06-fig3-ohc-en.png
-rw-r--r--@ 1 zeroone  staff    14093 Oct 29 16:12 ch04-06-fig3-ohc-zh.pdf
-rw-r--r--@ 1 zeroone  staff    62441 Oct 29 16:12 ch04-06-fig3-ohc-zh.png
-rw-r--r--@ 1 zeroone  staff    50211 Oct 29 16:12 ch04-07-fig4-budget-bad-en.png
-rw-r--r--@ 1 zeroone  staff    50211 Oct 29 16:12 ch04-07-fig4-budget-bad-zh.png
-rw-r--r--@ 1 zeroone  staff    21947 Oct 29 16:12 ch04-07-fig4-budget-en.pdf
-rw-r--r--@ 1 zeroone  staff   194819 Oct 29 16:12 ch04-07-fig4-budget-en.png
-rw-r--r--@ 1 zeroone  staff    22317 Oct 29 16:12 ch04-07-fig4-budget-zh.pdf
-rw-r--r--@ 1 zeroone  staff   190528 Oct 29 16:12 ch04-07-fig4-budget-zh.png
-rw-r--r--@ 1 zeroone  staff   587448 Oct 29 16:13 ch04-08-consistent-set-en.pdf
-rw-r--r--@ 1 zeroone  staff   663450 Oct 29 16:13 ch04-08-consistent-set-en.png
-rw-r--r--@ 1 zeroone  staff   555361 Oct 29 16:13 ch04-08-consistent-set-zh.pdf
-rw-r--r--@ 1 zeroone  staff   661084 Oct 29 16:13 ch04-08-consistent-set-zh.png

$ Pillow Image.open(...).size（仅本任务四张 PNG）
ch04-04a-schematic-bad.png: 1672 x 941 px; 2645803 bytes; source SHA-256 MATCH; PNG verify OK
ch04-04b-schematic-base-alt1.png: 1672 x 941 px; 1148937 bytes; source SHA-256 MATCH; PNG verify OK
ch04-04b-schematic-base.png: 1672 x 941 px; 1164556 bytes; source SHA-256 MATCH; PNG verify OK
ch04-04b-schematic-base-alt2.png: 1672 x 941 px; 1135610 bytes; source SHA-256 MATCH; PNG verify OK

4a: 1 generation; 4b: 3 generations; total: 4. No image was edited, resized, cropped, recoloured or relabelled after generation.
```
