# 第 01 章 codex-image 生成与核验记录

记录时间：2026-10-29T16:11:50+08:00（Asia/Shanghai）。

## 范围与结论

输入为 `production/plans/ch01.md` 的 FIG ch01-05、FIG ch01-06，以及 `production/book-spec.md` 第 4、5 节。本次只生成两幅图的位图：每幅恰好 3 次，共 6 个 PNG；ch01-05 选第 3 次，ch01-06 选第 2 次，其余四张以 alt 留存。**两张主路径文件都是三次中的最佳候选，并未通过全部规划验收。**

- ch01-05：三次均没有可明确认定的工厂排污点源；主候选有水处理设施样建筑，但不能当成工厂污染来源。主要文字可读，有方向箭头，不能沿用“伪文字／缺少流向”的原定图注。
- ch01-06：主候选无文字，主要对象与下游流向可辨，但保留纹理、渐变和立体明暗；支沟有分支，出水口与第三个管口合用，传感器是否完全浸没不明确。实际像素比例近似但非严格 4:5。
- 已达到每张最多 3 次上限。没有追加第四次，也没有改写提示词、添加工厂、后期修造科学对象或假造核验通过。

所有手工新建／写入的交付文件均在 `figures/ch01/` 与 `provenance/ch01/`。没有启动子代理、commit 或 push，没有制作其他 kind 的图或标签叠加。工具自身自动保存的原图缓存位于 `codex-output/`；本任务只将选图和备选复制到授权目录，未改动缓存。目录实测输出含其他同时进行的制作任务产生的文件，不表示这些文件由本任务制作。

## 实际工具与调用方式

- 工具：Codex 内置 `image_gen.imagegen`，本会话通过 `tools.image_gen__imagegen` 调用；不是 SciDraw AI、第三方 API 或本地绘图脚本生成。
- 具体生成模型：**不知道**；工具结果没有提供可确认的具体模型名。
- 每次调用只传 `prompt` 与 `transparent_background: false`。均为新生成，不传参考图，不传前图数量，不执行图像编辑。
- 两段英文 prompt 直接提取自规划代码块，去除 Markdown 代码块外层的两空格缩进，保留内部换行与项目符号缩进；逐字内容未改。没有增强提示、追加禁词、增加工厂要求或更改宽高比。
- 工具没有独立可设置的尺寸／宽高比参数，比例要求使用原文内的 `Aspect ratio 4:3.` 与 `portrait 4:5`；输出尺寸以实际 PNG 为准。
- 目视核验基于工具直接展示的六张完整输出。PNG 尺寸、完整性与 SHA-256 由 Pillow／Python 只读检查。文件复制后没有像素编辑，未做裁切、重采样、补边或伪造文字。

## 文件与次数总表

| 文件（均在 figures/ch01/） | 第几次 | 处置 | 像素尺寸 |
|---|---:|---|---|
| `ch01-05-site-schematic-vague-alt1.png` | 1 | 备选／落选 | 1448 × 1086 |
| `ch01-05-site-schematic-vague-alt2.png` | 2 | 备选／落选 | 1448 × 1086 |
| `ch01-05-site-schematic-vague.png` | 3 | 主候选，非全项通过 | 1448 × 1086 |
| `ch01-06-site-schematic-brief-alt1.png` | 1 | 备选／落选 | 1122 × 1402 |
| `ch01-06-site-schematic-brief.png` | 2 | 主候选，非全项通过 | 1122 × 1402 |
| `ch01-06-site-schematic-brief-alt2.png` | 3 | 备选／落选 | 1122 × 1402 |

## 逐图 prompt 与看图核验

以下每个文件均完整重复实际使用的 prompt，不以共同提示词引用代替。

### ch01-05-site-schematic-vague-alt1.png

- FIG：ch01-05；生成次数：第 1 次／共 3 次。
- 工具：Codex 内置 `image_gen.imagegen`（调用名 `tools.image_gen__imagegen`）；具体模型：不知道。
- 处置：落选；未出现明确的点源污染设施。
- 工具原始文件：`exec-834a1303-33a5-48f3-a2c9-7b700eab66dd.png`（位于上文缓存目录）。
- 实测：1448 × 1086 px，PNG，RGB，3430225 bytes。
- SHA-256：`2f9e11fafc01374517c44521dae51617d180936234afdccbdb449f83ca8a2d87`。
- prompt 修改：无；重试也未改写。

实际使用的完整 prompt：

```text
Illustration of nitrate pollution in an agricultural river watershed. Aspect ratio 4:3.
```

逐项看图结论：

- 教学目的／点源错误：未达到。左上红色农舍和筒仓为农业设施；下方管道被图中文字明确称为 tile drainage，不能把它认作工厂排污管。没有清楚的烟囱、工厂或工业排污口。
- 预期变色水：有，右下河水出现明显绿色藻华；但它是生成模型补充的情境，不是本章监测资料支持的现场事实。
- 预期死鱼／喷药飞机：未见飞机；右下圆形插图中有鱼，不能从姿态确认是死鱼，不应写“死鱼”。
- 预期伪文字：主要标签是可读英文，并含化学式。拖拉机后部小字难以可靠辨认，不能据此断言明确的伪文字问题。该 FIG 是允许含文字的反例，没有以文字为由淘汰。
- 预期装饰性立体效果：有，农田、土壤和水面带写实光照、立体剖面、材质纹理和鱼类插图。
- 监测站与流向：未见本案例的监测站；存在大量地表径流、地下水与河流方向箭头。原定“缺少水流方向”不符合此图。
- 选择结论：保留原始结果作为 alt1。可展示生成模型添加藻华和解释文字，不能用来证明出现了工厂点源。


### ch01-05-site-schematic-vague-alt2.png

- FIG：ch01-05；生成次数：第 2 次／共 3 次。
- 工具：Codex 内置 `image_gen.imagegen`（调用名 `tools.image_gen__imagegen`）；具体模型：不知道。
- 处置：落选；仍无明确的工厂点源。
- 工具原始文件：`exec-f388ab5e-fffc-4dda-87ba-e1b115e28a1c.png`（位于上文缓存目录）。
- 实测：1448 × 1086 px，PNG，RGB，3076186 bytes。
- SHA-256：`2eeef94a0d88fd9e199d9b491ed03c75d7fe80ee04ffe0312fc66f89bd0d6a02`。
- prompt 修改：无；重试也未改写。

实际使用的完整 prompt：

```text
Illustration of nitrate pollution in an agricultural river watershed. Aspect ratio 4:3.
```

逐项看图结论：

- 教学目的／点源错误：未达到。左上为农舍、筒仓和施肥车辆，右上为聚落／水塔；未见明确的工厂、工业烟囱或排污口。不能把聚落自动解释成污染点源。
- 预期变色水：有，前景河流有大片绿色藻华及深绿色水下区域；这些是模型补充的内容。
- 预期死鱼／喷药飞机：无飞机；有水下鱼类和“低氧伤害水生生物”的说明，但无法从鱼的姿态证明死亡。
- 预期伪文字：主要文字清楚可读，未确认明确伪文字；无需为了制造反例而添加乱码。
- 预期装饰性立体效果：有，写实天空、作物、土壤剖面、水面光照与鱼类场景。
- 监测站与流向：未见本案例的监测站；已有多个箭头，不能说没有水流方向。
- 选择结论：作为 alt2 留存。它与第一次一样主要展示模型额外补充藻华、生态影响等情境，未实现规划指定的点源错误。


### ch01-05-site-schematic-vague.png

- FIG：ch01-05；生成次数：第 3 次／共 3 次。
- 工具：Codex 内置 `image_gen.imagegen`（调用名 `tools.image_gen__imagegen`）；具体模型：不知道。
- 处置：三次中的主候选；未通过“明确点源污染对象”的核心验收。
- 工具原始文件：`exec-69b446d5-0197-4b9f-9a65-f32b9e040367.png`（位于上文缓存目录）。
- 实测：1448 × 1086 px，PNG，RGB，3243521 bytes。
- SHA-256：`d49f2bdce4d408699d0440a16f4f162c109dc93c04effc42c9df513b6e293464`。
- prompt 修改：无；重试也未改写。

实际使用的完整 prompt：

```text
Illustration of nitrate pollution in an agricultural river watershed. Aspect ratio 4:3.
```

逐项看图结论：

- 教学目的／点源错误：只部分接近“添加未支持对象”，未达到指定的“工厂排污点源”。右上有水处理设施样建筑及圆形池体、邻近聚落；图中文字讨论饮用水处理成本。看不到它向河流排污的管口或工厂烟囱，不应把它认定为污染来源。
- 预期变色水：有，近景绿色藻华、水下绿色场景明显。右下另有藻类、分解和溶解氧降低的图解，超出本章“只展示时间共同变化”的案例范围。
- 预期死鱼／喷药飞机：未见喷药飞机；水下鱼类没有明确死亡姿态。不得在图注里声称画出了死鱼。
- 预期伪文字：标题、编号说明、化学式及右下图解文字基本可读；未见可明确认定的大块伪文字。原定“不可读的伪文字”不能照用。
- 预期装饰性立体效果：有，写实农田与河流、水下视角、剖面和渐变圆形插图。
- 监测站与流向：没有可识别的 USGS 监测站；有多个径流／地下水方向箭头，不能保留“缺少水流方向”的断言。
- 选择理由：三次均未生成明确工厂点源。第三次额外加入水处理设施样建筑和更多案例未证实的生态／处理后果，最接近“模型补出未提供情境”的教学用途，因此按要求保存到规划主路径；这不是全部验收通过的认定。
- 原定编号①–④和图注不能照搬：①只能描述“本案例材料未支持的水处理设施样建筑”，不能写成工厂排污；②不应标“伪文字”；③可标立体、装饰性效果；④只能说缺少监测站，不得说无流向。编号叠加不属于本任务，未执行。


### ch01-06-site-schematic-brief-alt1.png

- FIG：ch01-06；生成次数：第 1 次／共 3 次。
- 工具：Codex 内置 `image_gen.imagegen`（调用名 `tools.image_gen__imagegen`）；具体模型：不知道。
- 处置：落选；排水剖面与主图支沟断开，且风格不完全合规。
- 工具原始文件：`exec-fbc11f7d-0533-4927-9821-e0df9e011526.png`（位于上文缓存目录）。
- 实测：1122 × 1402 px，PNG，RGB，1579393 bytes。
- SHA-256：`876b08cabeaec87600c70656b3b0d2309ebf31b65426c560aa9647d8f99ec988`。
- prompt 修改：无；重试也未改写。

实际使用的完整 prompt：

```text
Flat 2D scientific schematic for a journal figure panel, portrait 4:5, pure white
background. Clean vector illustration style: flat fills, thin dark-gray outlines,
no gradients, no shadows, no highlights, no 3D, no glow, no texture.

ABSOLUTELY NO TEXT: no letters, no words, no numbers, no symbols, no labels,
no legend, no title, no compass letters. Labels will be added later by the author.

SCENE: a simplified oblique (about 30-degree) view of a small agricultural
landscape with a cut-away soil block in the lower-left quarter.
- Upper half: gently rolling cropland made of 5-6 rectangular fields in two muted
  tones (pale sage green and pale wheat yellow), with faint parallel crop rows.
  No farm buildings, no animals, no machinery, no people, no aircraft.
- A single meandering river (soft medium blue) enters at the upper-left, flows
  diagonally across the panel, and exits at the lower-right edge. One small
  tributary ditch joins the river from the fields on the left.
- Lower-left: a cut-away cross-section of the soil under one field, light warm
  brown, showing a row of 3 small round subsurface drain pipes (gray circles)
  about one third down from the field surface, and one pipe outlet discharging a
  thin stream of water into the tributary ditch.
- Lower-right, on the river bank just before the river exits: a small, simple
  monitoring station - a pale-gray box on short legs with a thin cable running
  into the water to a small cylindrical sensor submerged in the river.
- Two or three small hollow chevrons drawn on the river surface pointing
  downstream (lower-right) to indicate flow direction.
- Leave clear white space beside the fields, the cut-away, the station and the
  river so labels can be placed later.

STRICTLY EXCLUDE: factories, chimneys, smoke, sewage or discharge pipes from
buildings, towns, roads, bridges, dead fish, algae, foam, colored or murky water,
warning signs, droplets, chemical symbols, arrows other than the flow chevrons,
maps, scale bars, north arrows, clouds, sun, trees in rows, decorative border.
Maximum three hues (sage green, wheat yellow, river blue) plus warm brown soil
and grays.
```

逐项看图结论：

- 农田计数：主图 5 块田，加左下剖面顶部 1 块，共 6 块；淡绿／麦黄两色，有平行作物行。
- 河流／支沟：1 条主河，左侧 1 条沟汇入主河；另有剖面旁独立的受水沟，二者之间留有明显白色断口。不能核实“排水管→支沟→主河”的连续路径。
- 剖面排水管与出口：土壤剖面中有 3 个灰色圆形管口，右侧管口兼作 1 个可见出水口；出水进入局部沟渠，但该沟与主图河网未接通。若规划要求 3 个断面另加独立出口，则本版也未充分区分它们。
- 监测站：下游右岸 1 个灰色箱体、短腿、1 根细缆和 1 个圆柱传感器均可见。传感器画在水面位置并有波纹，不能明确确认它完整浸没水下。
- 流向：2 枚白色空心 V 形标记，指向右下游；站点在下游端，方向正确。
- 文字与排除对象：逐图目视未发现字母、数字、文字或伪文字；V 形为规划允许的流向标记。未见工厂、烟囱、烟、建筑排污管、城镇、道路、桥梁、动物、农机、人物、飞机、死鱼、藻华、泡沫、警告牌、化学符号、地图、比例尺、指北针、云、太阳或成排树木。
- 画风／构图：白底、斜视、低饱和配色及留白基本符合；但土壤有颗粒纹理和分层明暗，水面、田块与管口有渐变或立体感，不满足严格“flat fills / no gradients / no texture / no 3D”。
- 宽高比：提示词原样要求 portrait 4:5；实际为 1122×1402，即 561:701，只有近似 4:5，未裁切或拉伸。
- 淘汰原因：连续排水路径无法成立，是比风格瑕疵更重要的教学问题；保留为 alt1。


### ch01-06-site-schematic-brief.png

- FIG：ch01-06；生成次数：第 2 次／共 3 次。
- 工具：Codex 内置 `image_gen.imagegen`（调用名 `tools.image_gen__imagegen`）；具体模型：不知道。
- 处置：三次中的主候选；对象与流向基本符合，严格风格和部分细节仍未达标。
- 工具原始文件：`exec-03a663ff-c84c-415e-8096-f364cda1e224.png`（位于上文缓存目录）。
- 实测：1122 × 1402 px，PNG，RGB，1471479 bytes。
- SHA-256：`8d43c4de4f5bba44e721566bd00f16dca8f7aa9f86d457437247dcb9b0cacdda`。
- prompt 修改：无；重试也未改写。

实际使用的完整 prompt：

```text
Flat 2D scientific schematic for a journal figure panel, portrait 4:5, pure white
background. Clean vector illustration style: flat fills, thin dark-gray outlines,
no gradients, no shadows, no highlights, no 3D, no glow, no texture.

ABSOLUTELY NO TEXT: no letters, no words, no numbers, no symbols, no labels,
no legend, no title, no compass letters. Labels will be added later by the author.

SCENE: a simplified oblique (about 30-degree) view of a small agricultural
landscape with a cut-away soil block in the lower-left quarter.
- Upper half: gently rolling cropland made of 5-6 rectangular fields in two muted
  tones (pale sage green and pale wheat yellow), with faint parallel crop rows.
  No farm buildings, no animals, no machinery, no people, no aircraft.
- A single meandering river (soft medium blue) enters at the upper-left, flows
  diagonally across the panel, and exits at the lower-right edge. One small
  tributary ditch joins the river from the fields on the left.
- Lower-left: a cut-away cross-section of the soil under one field, light warm
  brown, showing a row of 3 small round subsurface drain pipes (gray circles)
  about one third down from the field surface, and one pipe outlet discharging a
  thin stream of water into the tributary ditch.
- Lower-right, on the river bank just before the river exits: a small, simple
  monitoring station - a pale-gray box on short legs with a thin cable running
  into the water to a small cylindrical sensor submerged in the river.
- Two or three small hollow chevrons drawn on the river surface pointing
  downstream (lower-right) to indicate flow direction.
- Leave clear white space beside the fields, the cut-away, the station and the
  river so labels can be placed later.

STRICTLY EXCLUDE: factories, chimneys, smoke, sewage or discharge pipes from
buildings, towns, roads, bridges, dead fish, algae, foam, colored or murky water,
warning signs, droplets, chemical symbols, arrows other than the flow chevrons,
maps, scale bars, north arrows, clouds, sun, trees in rows, decorative border.
Maximum three hues (sage green, wheat yellow, river blue) plus warm brown soil
and grays.
```

逐项看图结论：

- 农田计数：6 块可分辨的田面（上方绿、右上黄、左侧黄、右侧绿、左下局部黄色田块、剖面顶部绿）；含边缘被画框截断的地块。淡绿／麦黄配色和平行作物行符合要求。
- 河流／支沟：1 条蜿蜒主河自左上进入，向右下离开；左侧沟与剖面出水沟在一个 Y 形节点合流，再经同一汇入口进入主河。可视为 1 个有分支的支沟系统；并非最简的单线无分叉支沟，需要在最终组图中留意其表达。
- 剖面排水管与出口：左下土壤中有 3 个灰色圆形管口，右侧一个同时作为出水口，细水流进入与主河相接的沟渠。3 个圆口和 1 次出水均可核对；但“3 根剖面管 + 另 1 个独立出口”的严格视觉区分没有实现。
- 监测站：右下游岸边 1 个浅灰箱体、短腿、1 根细缆、1 个圆柱传感器齐全。传感器末端位于河流区域，但图像表现像水面处的圆柱加波纹，不能明确证明整个传感器已浸没。
- 流向：3 枚白色开放 V 形标记，全部向右下，朝监测站所在下游端；没有反向箭头。
- 文字与排除对象：逐图目视未见文字、字母、数字或伪文字；三枚 V 形为允许的流向标记。未见工厂、烟囱、烟、建筑排污管、城镇、道路、桥梁、动物、机械、人物、飞机、死鱼、藻华、泡沫、浑浊水、警告牌、化学符号、额外箭头、地图、比例尺、指北针、天空装饰或树列。
- 画风／构图：白底、斜视、低饱和颜色与标签留白基本符合。仍有土壤颗粒、土层明暗、河流／田面渐变和箱体立体明暗，不满足严格“无纹理、无渐变、无 3D”。草边与剖面顶部作物行也比极简扁平风格更繁。
- 宽高比：实际 1122×1402（561:701，约 0.800285），相对 4:5 的宽高比偏差约 +0.0357%；请求值仍是原文的 4:5。未进行裁切、缩放、补边或重绘。
- 选择理由：相比第一次，本次排水沟与主河连续；相比第三次，本次只有一个支沟汇入口，较符合“河流 1 条 + 支沟 1 条”的关系。作为三次中的最佳底图保存到规划路径，不声称已通过全部出版验收。
- 剩余验收项：严格扁平风格；支沟分支的简化；独立出口与 3 根管的区分；传感器明确浸没；精确 4:5 像素比例。未在本任务中叠加标签或制作 ch01-07。


### ch01-06-site-schematic-brief-alt2.png

- FIG：ch01-06；生成次数：第 3 次／共 3 次。
- 工具：Codex 内置 `image_gen.imagegen`（调用名 `tools.image_gen__imagegen`）；具体模型：不知道。
- 处置：落选；有两个独立支沟汇入口，偏离“支沟 1 条”。
- 工具原始文件：`exec-8f805340-b4f5-4af7-b99c-45a84382bb5e.png`（位于上文缓存目录）。
- 实测：1122 × 1402 px，PNG，RGB，1492417 bytes。
- SHA-256：`34622619331702a68f4b1e1ddfdf46a116817ace4dd467e2c80add375fdc74ae`。
- prompt 修改：无；重试也未改写。

实际使用的完整 prompt：

```text
Flat 2D scientific schematic for a journal figure panel, portrait 4:5, pure white
background. Clean vector illustration style: flat fills, thin dark-gray outlines,
no gradients, no shadows, no highlights, no 3D, no glow, no texture.

ABSOLUTELY NO TEXT: no letters, no words, no numbers, no symbols, no labels,
no legend, no title, no compass letters. Labels will be added later by the author.

SCENE: a simplified oblique (about 30-degree) view of a small agricultural
landscape with a cut-away soil block in the lower-left quarter.
- Upper half: gently rolling cropland made of 5-6 rectangular fields in two muted
  tones (pale sage green and pale wheat yellow), with faint parallel crop rows.
  No farm buildings, no animals, no machinery, no people, no aircraft.
- A single meandering river (soft medium blue) enters at the upper-left, flows
  diagonally across the panel, and exits at the lower-right edge. One small
  tributary ditch joins the river from the fields on the left.
- Lower-left: a cut-away cross-section of the soil under one field, light warm
  brown, showing a row of 3 small round subsurface drain pipes (gray circles)
  about one third down from the field surface, and one pipe outlet discharging a
  thin stream of water into the tributary ditch.
- Lower-right, on the river bank just before the river exits: a small, simple
  monitoring station - a pale-gray box on short legs with a thin cable running
  into the water to a small cylindrical sensor submerged in the river.
- Two or three small hollow chevrons drawn on the river surface pointing
  downstream (lower-right) to indicate flow direction.
- Leave clear white space beside the fields, the cut-away, the station and the
  river so labels can be placed later.

STRICTLY EXCLUDE: factories, chimneys, smoke, sewage or discharge pipes from
buildings, towns, roads, bridges, dead fish, algae, foam, colored or murky water,
warning signs, droplets, chemical symbols, arrows other than the flow chevrons,
maps, scale bars, north arrows, clouds, sun, trees in rows, decorative border.
Maximum three hues (sage green, wheat yellow, river blue) plus warm brown soil
and grays.
```

逐项看图结论：

- 农田计数：主图 5 块田（上绿、上黄、右上绿、左中绿、右中黄），加剖面顶面黄色田 1 块，共 6 块；有平行作物行。
- 河流／支沟：1 条主河；左中有 1 条沟直接汇入主河，左下剖面出水又经另 1 条沟在更下游独立汇入。共 2 条支沟、2 个独立汇入口，不符合规划的支沟 1 条。
- 剖面排水管与出口：剖面正面有 3 个灰色圆管断面，右侧面另有 1 个独立出水口，水流通向下方支沟；这一项比前两次更接近“3 根 + 出口 1 个”的明确区分。
- 监测站：右下 1 个灰箱短腿站点、细缆及圆柱传感器齐全；传感器仍是水面波纹式表示，完整浸没不明确。
- 流向：3 枚白色空心 V 形，均指向右下；监测站位于下游端，方向正确。
- 文字与排除对象：逐图目视未发现文字、字母、数字、伪文字或工厂等明确排除对象。白色 V 形属于指定流向标记。
- 画风／构图：有白底、斜视、低饱和配色和留白；仍有颗粒土壤纹理、管口明暗、渐变与箱体立体效果，未达到严格扁平要求。
- 宽高比：实际 1122×1402（561:701），近似 4:5，未修整尺寸。
- 淘汰原因：独立出口表现较好，但两条支沟造成可数对象与路径结构偏差；选第二次作为较接近规划的主候选，本张保留为 alt2。


## ch01-05 图注交接建议（未修改章节或规划）

目前的主候选不足以支撑规划预设的“工厂点源污染”反例。后续作者需要调整教学论证与编号，或另行决定怎样补足该缺口；不能将水处理池、农业排水管或聚落自动改称为工厂排污设施。

若使用当前主候选，可据实使用如下图注草案，不再声称有工厂、伪文字或缺少流向：

> 用一句模糊要求生成的研究区插图（Codex 内置图像生成）。模型加入了本案例材料未支持的水处理设施样建筑、藻华、饮用水处理和生态影响说明，并使用装饰性立体效果；本案例的监测站没有明确标出。图中已有可读文字和方向箭头。本图未生成预期的明确工厂排污点源，因此不能用来证明模型在本次生成中添加了该类污染来源。

> A study-area illustration generated from a one-line request using Codex built-in image generation. It adds water-treatment-like infrastructure, algal blooms, and drinking-water and ecological explanations not supported by this case's supplied materials, together with decorative three-dimensional effects; the case's monitoring station is not clearly identified. Readable text and directional arrows are already present. No unambiguous industrial pollution point source was generated, so this image cannot support that specific planned claim.

ch01-06 的标签坐标仍须按实际选图定位；本任务未执行 LaTeX 标签叠加，未验证 ch01-07 组图版式或终尺寸文字。

## 完成标准的实测输出

### 目录清单

实际执行（`subprocess.run` 设置 10 秒超时）：

```sh
ls -l figures/ch01/
```

```text
total 31664
-rw-r--r--@ 1 zeroone  staff     1225 Oct 29 16:03 ch01-01-workflow-en.tex
-rw-r--r--@ 1 zeroone  staff     1196 Oct 29 16:03 ch01-01-workflow-zh.tex
-rw-r--r--@ 1 zeroone  staff     2441 Oct 29 16:04 ch01-02-material-map-en.tex
-rw-r--r--@ 1 zeroone  staff     2486 Oct 29 16:04 ch01-02-material-map-zh.tex
-rw-r--r--@ 1 zeroone  staff    26515 Oct 29 16:05 ch01-03-nitrate-draft-vague-en.pdf
-rw-r--r--@ 1 zeroone  staff   264072 Oct 29 16:05 ch01-03-nitrate-draft-vague-en.png
-rw-r--r--@ 1 zeroone  staff    20111 Oct 29 16:05 ch01-03-nitrate-draft-vague-zh.pdf
-rw-r--r--@ 1 zeroone  staff   275268 Oct 29 16:05 ch01-03-nitrate-draft-vague-zh.png
-rw-r--r--@ 1 zeroone  staff    25409 Oct 29 16:05 ch01-04-nitrate-panel-brief-en-panel.pdf
-rw-r--r--@ 1 zeroone  staff   150344 Oct 29 16:05 ch01-04-nitrate-panel-brief-en-panel.png
-rw-r--r--@ 1 zeroone  staff    25624 Oct 29 16:05 ch01-04-nitrate-panel-brief-en.pdf
-rw-r--r--@ 1 zeroone  staff   188219 Oct 29 16:05 ch01-04-nitrate-panel-brief-en.png
-rw-r--r--@ 1 zeroone  staff    29315 Oct 29 16:05 ch01-04-nitrate-panel-brief-zh-panel.pdf
-rw-r--r--@ 1 zeroone  staff   151447 Oct 29 16:05 ch01-04-nitrate-panel-brief-zh-panel.png
-rw-r--r--@ 1 zeroone  staff    29468 Oct 29 16:05 ch01-04-nitrate-panel-brief-zh.pdf
-rw-r--r--@ 1 zeroone  staff   189412 Oct 29 16:05 ch01-04-nitrate-panel-brief-zh.png
-rw-r--r--@ 1 zeroone  staff  3430225 Oct 29 16:04 ch01-05-site-schematic-vague-alt1.png
-rw-r--r--@ 1 zeroone  staff  3076186 Oct 29 16:04 ch01-05-site-schematic-vague-alt2.png
-rw-r--r--@ 1 zeroone  staff  3243521 Oct 29 16:05 ch01-05-site-schematic-vague.png
-rw-r--r--@ 1 zeroone  staff  1579393 Oct 29 16:06 ch01-06-site-schematic-brief-alt1.png
-rw-r--r--@ 1 zeroone  staff  1492417 Oct 29 16:08 ch01-06-site-schematic-brief-alt2.png
-rw-r--r--@ 1 zeroone  staff  1471479 Oct 29 16:07 ch01-06-site-schematic-brief.png
-rw-r--r--@ 1 zeroone  staff    34240 Oct 29 16:05 ch01-07-figure2-final-en.pdf
-rw-r--r--@ 1 zeroone  staff     1522 Oct 29 16:04 ch01-07-figure2-final-en.tex
-rw-r--r--@ 1 zeroone  staff    56122 Oct 29 16:05 ch01-07-figure2-final-zh.pdf
-rw-r--r--@ 1 zeroone  staff     1531 Oct 29 16:04 ch01-07-figure2-final-zh.tex
-rw-r--r--@ 1 zeroone  staff   192492 Oct 29 16:04 ch01-08-guide-ui-en.png
-rw-r--r--@ 1 zeroone  staff   192433 Oct 29 16:04 ch01-08-guide-ui-zh.png
```

### 六张生成图的像素尺寸与 PNG 完整性

以下为 Pillow `Image.size`、`Image.format`、`Image.mode`、`Image.verify()` 与文件大小的实际结果：

```text
ch01-05-site-schematic-vague.png: 1448 x 1086 px; PNG; RGB; 3243521 bytes; PNG verify PASS
ch01-05-site-schematic-vague-alt1.png: 1448 x 1086 px; PNG; RGB; 3430225 bytes; PNG verify PASS
ch01-05-site-schematic-vague-alt2.png: 1448 x 1086 px; PNG; RGB; 3076186 bytes; PNG verify PASS
ch01-06-site-schematic-brief.png: 1122 x 1402 px; PNG; RGB; 1471479 bytes; PNG verify PASS
ch01-06-site-schematic-brief-alt1.png: 1122 x 1402 px; PNG; RGB; 1579393 bytes; PNG verify PASS
ch01-06-site-schematic-brief-alt2.png: 1122 x 1402 px; PNG; RGB; 1492417 bytes; PNG verify PASS
```

三张 ch01-05 均为严格 4:3。三张 ch01-06 均为 1122:1402 = 561:701，宽高比 0.8002853067，相对 0.8 的偏差 +0.0356633%；如要求整像素精确 4:5，这三张均未通过该项。没有将“提示词中写了 4:5”冒充实际像素符合。

机器可读核验结果（含 SHA-256）保存在同目录 `codex-images-file-verification.json`；规划 prompt 原文副本为 `ch01-05-prompt.txt` 和 `ch01-06-prompt.txt`。
