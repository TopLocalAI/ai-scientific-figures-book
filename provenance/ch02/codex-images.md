# 第 02 章 Codex 图像生成记录

日期：2026-10-29（Asia/Shanghai）。

## 范围与方法

本次仅生成 FIG ch02-04、ch02-05、ch02-06 的 PNG 底图，以及本目录内的核验记录。未制作或修改 TikZ 标签、正文、规划、reuse 图或数据图；未 commit/push；未启动子 agent。目录清单中的其他文件由并行制作流程出现，不属于本次交付。

实际工具：Codex 内置图像生成：image_gen__imagegen，经 functions.exec 调用；具体底层模型不知道（工具未返回模型标识）。所有调用均为新图生成，transparent_background=false，不传参考图，也不使用 num_last_images_to_include。没有调用付费外部 API/CLI 生成流程。工具默认输出缓存由工具自身写入 ~/.codex/generated_images；本次只把返回的 PNG 原样复制到授权的 figures/ch02，未裁剪、重采样、修字、后处理或用代码替代生成。

提示词从 production/plans/ch02.md 代码块提取，去除 Markdown 的两空格结构缩进，保留正文与换行。V1 和 V2 完全原样。V3 用 V2 全文，追加规划的 CORRECTIONS 标题和两条实际相关条目；其余条目没有证据支持，不追加。三次 V3 用同一完整提示词。

生成次数：ch02-04 为 1 次；ch02-05 为 1 次；ch02-06 为 3 次。共 5 张，未超过每图 3 次。所有 PNG 均为 1672 × 941，按工具原始像素保存；请求宽高比 16:9，输出比值 1.776833，与 16/9 相对差 -0.053135%，属于整数像素近似，未声称输出为数学上精确的 16:9。

核验方法：逐张看实际图，橙点用 RGB 阈值连通域计数并人工按位置分到石墨层间与 SEI；见 pixel-checks.json。裂纹是连通网络，所列条数按主要外向分支目视计数，不冒充精确独立曲线计数。没有进行材料/电化学专业签字审校。

## 文件与选用结果

| 文件 | FIG / 第几次 | 结果 | 像素 |
|---|---|---|---|
| `ch02-04-nmc-vague.png` | ch02-04 / 1 | 选用 | 1672 × 941 |
| `ch02-05-nmc-brief-v2.png` | ch02-05 / 1 | 选用 | 1672 × 941 |
| `ch02-06-nmc-v3-base-alt1.png` | ch02-06 / 1 | 落选保留 | 1672 × 941 |
| `ch02-06-nmc-v3-base-alt2.png` | ch02-06 / 2 | 落选保留 | 1672 × 941 |
| `ch02-06-nmc-v3-base.png` | ch02-06 / 3 | 选用 | 1672 × 941 |



## 不应被正文误写的结论

- 反例确实有前后阶段、部分可读机制与后果，不能套用规划中的全部预期缺陷；应按下列真实问题撰写图注。

- V2 为真实初稿，未人为植入缺陷；R1–R8 打分单独存于 v2-review.json。

- V3 第 3 次为最合适候选，并非全部严格验收通过：仍有晶粒数、粒径、左右晶粒图样、尺寸一致性与轻微背景纹理偏差。

- 终稿的标签字号、R6 实线框、R9 唯一虚线框、图例和专业审校均需在叠加/审校任务中检查；这里不声称已完成。



## ch02-04 / 第 1 次 / ch02-04-nmc-vague.png

**文件：** `figures/ch02/ch02-04-nmc-vague.png`

**工具：** Codex 内置图像生成：image_gen__imagegen，经 functions.exec 调用；具体底层模型不知道（工具未返回模型标识）

**生成方式：** 全新生成；不引用上一版图像；无生成后编辑。

**选择：** 选用；本图只生成 1 次，无备选。

**提示词变动及原因：** 无；逐字使用规划的一句英文，未为了制造反例增改任何内容。

**原始输出：** `codex-output/exec-fbe4ede6-c6cb-4be3-829c-083011107067.png`

**SHA-256：** `d56fd30a7db5abedcf063cffff23556bef19ff5cf49683a735a6f4aecbca7bb3`

### 实际使用的完整英文 prompt（逐字）
```text
Make a beautiful, professional scientific illustration of lithium-ion battery cathode degradation for a top journal. Landscape 16:9.
```

### 对照规划逐项看图结论

- **教学目的：** 适合作为“主题正确、任务书关系缺失/越界”的真实反例，而不是一无是处的图。画面包含新鲜、循环中、衰减后的正极，并能找到 active material loss、impedance 等文字，不能写成“没有前后比较”或“完全没有后果”。

- **画面内容：不控制：** 实际是有质感的 3D 正极颗粒剖面、球棍/多面体晶体模型、多个机制放大圆、蓝紫橙渐变背景；不是圆柱电池。未出现电池外壳或闪电，不能把这些预期当成实测。

- **文字/伪文字例外：** 大量英文、数字、化学式存在，此反例按规划允许。大多英文可读；中间颗粒上方局部电解液标签破碎/叠写，可指认这一局部，不笼统把所有术语或正常化学式说成伪文字/伪化学式。

- **实际问题 1：结构核验：** 裂纹/孔洞叠加于复杂 3D 表面，无法像关系表那样检查 6–10 条裂纹是否仅沿可辨识初级晶界；分离碎块不止一处。

- **实际问题 2：正负极与 SEI：** 没有石墨负极新鲜/循环后对照，无法核对石墨 SEI 增厚及层间锂减少。图中的 CEI 标识不能当作图中画错了石墨 SEI 的直接证据。

- **实际问题 3：范围越界：** 明确加入 Transition metal dissolution 一组机制，违反本案例不画过渡金属溶出/沉积的范围限定。

- **实际问题 4：证据状态：** 没有把 S6 作者推测单列为虚线框，也未区分其与文献确立关系。

- **实际问题 5：画风：** 3D 光泽、光晕、复杂材料纹理和深色渐变抢占了用于核对对象/关系的空间；与任务书的白底平涂要求不符。

- **图注/编号建议：** 可按实际画面标注：局部破碎标签、3D 纹理掩盖晶界、无法检查沿晶裂纹、缺少负极 SEI 对照、范围外溶出及证据状态未区分。不在本任务添加红圈或标签。

- **核验结论：** 反例入选；没有人为指定错误箭头或强行制造缺陷，记录仅反映原样模糊提示词的实际输出。



## ch02-05 / 第 1 次 / ch02-05-nmc-brief-v2.png

**文件：** `figures/ch02/ch02-05-nmc-brief-v2.png`

**工具：** Codex 内置图像生成：image_gen__imagegen，经 functions.exec 调用；具体底层模型不知道（工具未返回模型标识）

**生成方式：** 全新生成；不引用上一版图像；无生成后编辑。

**选择：** 选用作为 V2 教学初稿；本图只生成 1 次，保留真实问题作为修订起点。

**提示词变动及原因：** 无；逐字使用规划英文全文，包括换行；未添加额外提示。

**原始输出：** `codex-output/exec-a8a36bde-68ce-4fb8-a7f5-db75ba595ba9.png`

**SHA-256：** `999019d19e4f27ce5c0514fa8f79c9b2346fded600cff07451f96ec75e5c14f7`

### 实际使用的完整英文 prompt（逐字）
```text
Flat 2D scientific schematic for a journal figure, landscape 16:9, pure white
background. Clean vector illustration: flat fills, thin dark-gray outlines,
no gradients, no shadows, no highlights, no 3D, no glow, no texture.

ABSOLUTELY NO TEXT: no letters, no words, no numbers, no chemical formulas,
no symbols, no labels, no legend, no title. Labels will be added later.

LAYOUT: a 2 x 2 grid of four cross-section drawings.
Left column = pristine (before cycling). Right column = after long cycling.
Top row = cathode particles. Bottom row = anode particles.
Between the two columns, a vertical strip of white space containing one single
wide hollow arrow pointing from left to right, centred vertically.
Leave the bottom 12% of the image completely empty. Leave generous white space
around each particle for labels.

TOP LEFT - pristine cathode secondary particle: a round cross-section about 30%
of the image height in diameter, made of 30-40 tightly packed polygonal primary
grains in low-saturation blue-gray tones with thin gray grain boundaries.
No cracks, no gaps, no dark rim, no blue inside.

TOP RIGHT - the same particle after cycling, same diameter and same grain pattern:
6-10 thin cracks that run only along the boundaries between grains, radiating
roughly from the centre outward; no crack cuts through the interior of a grain.
The cracks are filled with pale light-blue (electrolyte). A thin, uniform
dark slate-blue rim covers the outer surface of the particle. At the right edge,
exactly one small group of 3-5 grains is slightly separated from the particle
by a narrow pale-blue gap.

BOTTOM LEFT - pristine graphite anode particle: a flattened rounded flake about
70% of its column width, drawn as stacked parallel medium-gray layers. A thin, even pale olive shell surrounds it (the SEI). About 20 small
orange dots sit between the gray layers.

BOTTOM RIGHT - the same graphite particle after cycling, same size: the pale
olive shell is clearly thicker and slightly uneven. Only about 8 orange dots
remain between the gray layers, and about 6 orange dots are embedded inside the
olive shell.

Only the graphite particles have an olive shell; the cathode particles have none.
The only arrow in the image is the single hollow arrow between the columns.

STRICTLY EXCLUDE: battery casings, cylindrical or pouch cells, jelly rolls,
current collectors, separators, electrolyte bath, lightning bolts, glowing
particles, sparks, bubbles, dendrites, metal ions, charts, axes, curves,
numbers, scale bars, background patterns, decorative borders.
Colours: blue-gray (cathode), pale blue (electrolyte), dark slate-blue (rim),
medium gray (graphite), pale olive (SEI), orange (lithium dots) - nothing else.
```

### 对照规划逐项看图结论

- **R1 [partial]：** 4 个主颗粒、1 个空心左→右箭头，无额外箭头；两正极外形接近，但循环后石墨含壳外轮廓明显更大，不能声称严格同尺寸。

- **R2 [pass_visual]：** 循环后可见约 8 个向外裂纹分支，沿多边形晶界延伸，未见明确切穿晶粒内部的裂纹；新鲜正极无浅蓝裂纹。分支构成连通网络，非 8 条彼此独立曲线。

- **R3 [pass_visual]：** 循环后晶界裂隙填浅蓝；新鲜正极内部没有同类浅蓝填充。蓝灰色晶粒本身不计为电解液。

- **R4 [pass_visual]：** 右侧只有一处分离晶粒群，目视约 5 个晶粒，与主体间有浅蓝窄隙；没有多处飞散或爆裂。

- **R5 [pass_visual]：** 深灰蓝重构薄缘仅出现在循环后正极外表面，新鲜正极只有细轮廓而无同类深色厚缘。

- **R6 [not_in_base_scope]：** 底图提供可指向的表面重构层；“阻抗升高”实线框属叠加工作，未生成，不能据底图判整条通过。

- **R7 [pass_visual]：** 橄榄色壳只包围两个石墨颗粒；新鲜薄且基本均匀，循环后明显更厚且略不均匀。

- **R8 [partial]：** 橙点检测并逐点看图：新鲜层间 22；循环后层间 7、SEI 内 8。层间减少且 SEI 含点，趋势通过；未完全对应提示词约 20 / 8 / 6，尤其壳内 8 而非约 6，保留为修订依据。

- **石墨层条纹：** 层状构图成立，但有不规则白色高光、灰度变化，违背 no highlights / no texture。

- **教学目的：** 四个颗粒与单一过程箭头可用于按关系表核对；仅为机制示意，不是实验图像或实验数据。

- **文字检查：** 逐张看图未见文字、字母、数字、化学式、伪文字、标签、图例或标题；唯一箭头为规划要求的空心右箭头。

- **排除对象：** 未见电池外壳、卷绕结构、集流体、隔膜、浴槽、闪电、发光粒子、气泡、枝晶、金属离子、坐标轴、曲线、比例尺或装饰边框。

- **布局与标签空间：** 2 × 2 布局成立；底部至少约 12% 无对象。顶部颗粒偏大、顶部及右侧标签空间较紧，后续叠加必须根据实际画面重新定位。

- **画风与底色：** 是二维示意，未见 3D 或投影；但背景含极轻微纹理，采样值常为 RGB(254,254,254) 而非严格纯白，填色也有轻微明暗变化，不能记为“完全纯色、无纹理”通过。

- **30–40 晶粒、粒径约图高 30%、同一晶粒图样：** 目视晶粒数量多于 40；正极直径约占图高 42–47%，超过约 30%；左右多边形拼接图样未严格一一相同。此项不通过。

- **终稿标签与专业审校：** 本任务仅生成底图；R6 后果标签、R9 唯一推测虚线框、图例、双语标签字号 ≥6 pt 和材料/电化学专业审校均未在本任务执行或验收。不得据底图声称第 2.9 节全部通过。



## ch02-06 / 第 1 次 / ch02-06-nmc-v3-base-alt1.png

**文件：** `figures/ch02/ch02-06-nmc-v3-base-alt1.png`

**工具：** Codex 内置图像生成：image_gen__imagegen，经 functions.exec 调用；具体底层模型不知道（工具未返回模型标识）

**生成方式：** 全新生成；不引用上一版图像；无生成后编辑。

**选择：** 落选，保留为 alt1。

**提示词变动及原因：** V2 全文不变；只保留规划 CORRECTIONS 中针对 V2 实际问题的同尺寸和橙点两项。未添加其他修正词；与 V3 第 2、3 次完整提示词一致。

**原始输出：** `codex-output/exec-6ff22096-136c-4694-910c-859676b81609.png`

**SHA-256：** `8fe93b29911b276d03ee8e8971ffba09b4ed6f026b1d9e093fa0b3830c4b78b0`

### 实际使用的完整英文 prompt（逐字）
```text
Flat 2D scientific schematic for a journal figure, landscape 16:9, pure white
background. Clean vector illustration: flat fills, thin dark-gray outlines,
no gradients, no shadows, no highlights, no 3D, no glow, no texture.

ABSOLUTELY NO TEXT: no letters, no words, no numbers, no chemical formulas,
no symbols, no labels, no legend, no title. Labels will be added later.

LAYOUT: a 2 x 2 grid of four cross-section drawings.
Left column = pristine (before cycling). Right column = after long cycling.
Top row = cathode particles. Bottom row = anode particles.
Between the two columns, a vertical strip of white space containing one single
wide hollow arrow pointing from left to right, centred vertically.
Leave the bottom 12% of the image completely empty. Leave generous white space
around each particle for labels.

TOP LEFT - pristine cathode secondary particle: a round cross-section about 30%
of the image height in diameter, made of 30-40 tightly packed polygonal primary
grains in low-saturation blue-gray tones with thin gray grain boundaries.
No cracks, no gaps, no dark rim, no blue inside.

TOP RIGHT - the same particle after cycling, same diameter and same grain pattern:
6-10 thin cracks that run only along the boundaries between grains, radiating
roughly from the centre outward; no crack cuts through the interior of a grain.
The cracks are filled with pale light-blue (electrolyte). A thin, uniform
dark slate-blue rim covers the outer surface of the particle. At the right edge,
exactly one small group of 3-5 grains is slightly separated from the particle
by a narrow pale-blue gap.

BOTTOM LEFT - pristine graphite anode particle: a flattened rounded flake about
70% of its column width, drawn as stacked parallel medium-gray layers. A thin, even pale olive shell surrounds it (the SEI). About 20 small
orange dots sit between the gray layers.

BOTTOM RIGHT - the same graphite particle after cycling, same size: the pale
olive shell is clearly thicker and slightly uneven. Only about 8 orange dots
remain between the gray layers, and about 6 orange dots are embedded inside the
olive shell.

Only the graphite particles have an olive shell; the cathode particles have none.
The only arrow in the image is the single hollow arrow between the columns.

STRICTLY EXCLUDE: battery casings, cylindrical or pouch cells, jelly rolls,
current collectors, separators, electrolyte bath, lightning bolts, glowing
particles, sparks, bubbles, dendrites, metal ions, charts, axes, curves,
numbers, scale bars, background patterns, decorative borders.
Colours: blue-gray (cathode), pale blue (electrolyte), dark slate-blue (rim),
medium gray (graphite), pale olive (SEI), orange (lithium dots) - nothing else.

CORRECTIONS compared with the previous version (apply all, change nothing else):
- Both cathode particles have the same diameter; both graphite particles have
  the same size.
- Pristine graphite: about 20 orange dots between layers. Cycled graphite: about
  8 orange dots between layers and about 6 inside the olive shell.
```

### 对照规划逐项看图结论

- **R1：四颗粒与箭头：** 4 个主颗粒、1 个空心向右箭头；两列同类颗粒接近但不完全同尺寸。

- **R2/R3：裂纹与电解液：** 新鲜正极未见裂纹或浅蓝；循环后可见约 7 个主要沿晶外向分支，浅蓝填充，未见明显横切晶粒的裂纹。

- **R4：分离碎块：** 仅右侧 1 处晶粒群分离，但目视约 6 个晶粒，多于规定 3–5 个，是落选原因之一。

- **R5：表面重构：** 深灰蓝薄缘仅在循环后正极外表面，新鲜正极没有该薄缘。

- **R7：SEI：** 只有石墨颗粒有橄榄色壳，循环后较厚且不均匀；成立。

- **R8：锂点：** 实测新鲜层间 20；循环后层间 7、壳内 8。趋势正确，壳内点仍比提示词约 6 偏多。

- **相较 V2：** 石墨层显著减少了白色高光，呈现更规整的灰条；晶粒数、粒径、左右图样及近白背景偏差仍在。

- **教学目的：** 四个颗粒与单一过程箭头可用于按关系表核对；仅为机制示意，不是实验图像或实验数据。

- **文字检查：** 逐张看图未见文字、字母、数字、化学式、伪文字、标签、图例或标题；唯一箭头为规划要求的空心右箭头。

- **排除对象：** 未见电池外壳、卷绕结构、集流体、隔膜、浴槽、闪电、发光粒子、气泡、枝晶、金属离子、坐标轴、曲线、比例尺或装饰边框。

- **布局与标签空间：** 2 × 2 布局成立；底部至少约 12% 无对象。顶部颗粒偏大、顶部及右侧标签空间较紧，后续叠加必须根据实际画面重新定位。

- **画风与底色：** 是二维示意，未见 3D 或投影；但背景含极轻微纹理，采样值常为 RGB(254,254,254) 而非严格纯白，填色也有轻微明暗变化，不能记为“完全纯色、无纹理”通过。

- **30–40 晶粒、粒径约图高 30%、同一晶粒图样：** 目视晶粒数量多于 40；正极直径约占图高 42–47%，超过约 30%；左右多边形拼接图样未严格一一相同。此项不通过。

- **终稿标签与专业审校：** 本任务仅生成底图；R6 后果标签、R9 唯一推测虚线框、图例、双语标签字号 ≥6 pt 和材料/电化学专业审校均未在本任务执行或验收。不得据底图声称第 2.9 节全部通过。



## ch02-06 / 第 2 次 / ch02-06-nmc-v3-base-alt2.png

**文件：** `figures/ch02/ch02-06-nmc-v3-base-alt2.png`

**工具：** Codex 内置图像生成：image_gen__imagegen，经 functions.exec 调用；具体底层模型不知道（工具未返回模型标识）

**生成方式：** 全新生成；不引用上一版图像；无生成后编辑。

**选择：** 落选，保留为 alt2；禁止用作已通过核验的终稿。

**提示词变动及原因：** 与 V3 第 1 次逐字相同；同提示词重新生成，无参考图、无局部修改。

**原始输出：** `codex-output/exec-b1a62fb3-3ddf-4201-9d17-5967262c532e.png`

**SHA-256：** `df66acbcbb60be47cde475b6c961590daad4c3bf8dfef1e8081ef81849e657ca`

### 实际使用的完整英文 prompt（逐字）
```text
Flat 2D scientific schematic for a journal figure, landscape 16:9, pure white
background. Clean vector illustration: flat fills, thin dark-gray outlines,
no gradients, no shadows, no highlights, no 3D, no glow, no texture.

ABSOLUTELY NO TEXT: no letters, no words, no numbers, no chemical formulas,
no symbols, no labels, no legend, no title. Labels will be added later.

LAYOUT: a 2 x 2 grid of four cross-section drawings.
Left column = pristine (before cycling). Right column = after long cycling.
Top row = cathode particles. Bottom row = anode particles.
Between the two columns, a vertical strip of white space containing one single
wide hollow arrow pointing from left to right, centred vertically.
Leave the bottom 12% of the image completely empty. Leave generous white space
around each particle for labels.

TOP LEFT - pristine cathode secondary particle: a round cross-section about 30%
of the image height in diameter, made of 30-40 tightly packed polygonal primary
grains in low-saturation blue-gray tones with thin gray grain boundaries.
No cracks, no gaps, no dark rim, no blue inside.

TOP RIGHT - the same particle after cycling, same diameter and same grain pattern:
6-10 thin cracks that run only along the boundaries between grains, radiating
roughly from the centre outward; no crack cuts through the interior of a grain.
The cracks are filled with pale light-blue (electrolyte). A thin, uniform
dark slate-blue rim covers the outer surface of the particle. At the right edge,
exactly one small group of 3-5 grains is slightly separated from the particle
by a narrow pale-blue gap.

BOTTOM LEFT - pristine graphite anode particle: a flattened rounded flake about
70% of its column width, drawn as stacked parallel medium-gray layers. A thin, even pale olive shell surrounds it (the SEI). About 20 small
orange dots sit between the gray layers.

BOTTOM RIGHT - the same graphite particle after cycling, same size: the pale
olive shell is clearly thicker and slightly uneven. Only about 8 orange dots
remain between the gray layers, and about 6 orange dots are embedded inside the
olive shell.

Only the graphite particles have an olive shell; the cathode particles have none.
The only arrow in the image is the single hollow arrow between the columns.

STRICTLY EXCLUDE: battery casings, cylindrical or pouch cells, jelly rolls,
current collectors, separators, electrolyte bath, lightning bolts, glowing
particles, sparks, bubbles, dendrites, metal ions, charts, axes, curves,
numbers, scale bars, background patterns, decorative borders.
Colours: blue-gray (cathode), pale blue (electrolyte), dark slate-blue (rim),
medium gray (graphite), pale olive (SEI), orange (lithium dots) - nothing else.

CORRECTIONS compared with the previous version (apply all, change nothing else):
- Both cathode particles have the same diameter; both graphite particles have
  the same size.
- Pristine graphite: about 20 orange dots between layers. Cycled graphite: about
  8 orange dots between layers and about 6 inside the olive shell.
```

### 对照规划逐项看图结论

- **R1：四颗粒与箭头：** 4 个主颗粒、1 个空心向右箭头；两列尺寸近似，非严格一致。

- **R2/R3：新鲜正极错误：** 左上新鲜正极约 (x=245–300, y=285–318) 像素处有浅蓝晶界裂隙；违反新鲜无裂纹、内部无浅蓝的硬性约束，是主要落选原因。

- **R2/R3：循环后：** 右上有约 6 个外向沿晶分支，填浅蓝；未见明确切穿晶粒内部的分支。

- **R4：分离碎块：** 只有右侧一处分离晶粒群，目视约 4 个晶粒，符合 3–5。

- **R5：表面重构：** 深色薄缘在循环后正极外表面，新鲜无同类外缘。

- **R7：SEI：** 橄榄壳仅在石墨，循环后更厚且不规则；成立。

- **R8：锂点：** 实测新鲜层间 21；循环后层间 8、SEI 内 6，接近约 20 / 8 / 6。数量较好不能抵消新鲜正极被画出裂纹的科学表达错误。

- **相较 V2：** 石墨条纹更平整，白色高光已明显减少；但引入了新鲜正极裂隙错误。

- **教学目的：** 四个颗粒与单一过程箭头可用于按关系表核对；仅为机制示意，不是实验图像或实验数据。

- **文字检查：** 逐张看图未见文字、字母、数字、化学式、伪文字、标签、图例或标题；唯一箭头为规划要求的空心右箭头。

- **排除对象：** 未见电池外壳、卷绕结构、集流体、隔膜、浴槽、闪电、发光粒子、气泡、枝晶、金属离子、坐标轴、曲线、比例尺或装饰边框。

- **布局与标签空间：** 2 × 2 布局成立；底部至少约 12% 无对象。顶部颗粒偏大、顶部及右侧标签空间较紧，后续叠加必须根据实际画面重新定位。

- **画风与底色：** 是二维示意，未见 3D 或投影；但背景含极轻微纹理，采样值常为 RGB(254,254,254) 而非严格纯白，填色也有轻微明暗变化，不能记为“完全纯色、无纹理”通过。

- **30–40 晶粒、粒径约图高 30%、同一晶粒图样：** 目视晶粒数量多于 40；正极直径约占图高 42–47%，超过约 30%；左右多边形拼接图样未严格一一相同。此项不通过。

- **终稿标签与专业审校：** 本任务仅生成底图；R6 后果标签、R9 唯一推测虚线框、图例、双语标签字号 ≥6 pt 和材料/电化学专业审校均未在本任务执行或验收。不得据底图声称第 2.9 节全部通过。



## ch02-06 / 第 3 次 / ch02-06-nmc-v3-base.png

**文件：** `figures/ch02/ch02-06-nmc-v3-base.png`

**工具：** Codex 内置图像生成：image_gen__imagegen，经 functions.exec 调用；具体底层模型不知道（工具未返回模型标识）

**生成方式：** 全新生成；不引用上一版图像；无生成后编辑。

**选择：** 三个候选中选用；可交给叠加环节继续处理，但不是严格全部验收通过。

**提示词变动及原因：** 与 V3 第 1、2 次逐字相同；同提示词重新生成，无参考图、无局部修改。

**原始输出：** `codex-output/exec-143391c8-57da-4821-a011-b51508cd2f19.png`

**SHA-256：** `08b3b01bf1b2024ce090352fc0b284f2bc4940c7b530915f221a4578eebc88d9`

### 实际使用的完整英文 prompt（逐字）
```text
Flat 2D scientific schematic for a journal figure, landscape 16:9, pure white
background. Clean vector illustration: flat fills, thin dark-gray outlines,
no gradients, no shadows, no highlights, no 3D, no glow, no texture.

ABSOLUTELY NO TEXT: no letters, no words, no numbers, no chemical formulas,
no symbols, no labels, no legend, no title. Labels will be added later.

LAYOUT: a 2 x 2 grid of four cross-section drawings.
Left column = pristine (before cycling). Right column = after long cycling.
Top row = cathode particles. Bottom row = anode particles.
Between the two columns, a vertical strip of white space containing one single
wide hollow arrow pointing from left to right, centred vertically.
Leave the bottom 12% of the image completely empty. Leave generous white space
around each particle for labels.

TOP LEFT - pristine cathode secondary particle: a round cross-section about 30%
of the image height in diameter, made of 30-40 tightly packed polygonal primary
grains in low-saturation blue-gray tones with thin gray grain boundaries.
No cracks, no gaps, no dark rim, no blue inside.

TOP RIGHT - the same particle after cycling, same diameter and same grain pattern:
6-10 thin cracks that run only along the boundaries between grains, radiating
roughly from the centre outward; no crack cuts through the interior of a grain.
The cracks are filled with pale light-blue (electrolyte). A thin, uniform
dark slate-blue rim covers the outer surface of the particle. At the right edge,
exactly one small group of 3-5 grains is slightly separated from the particle
by a narrow pale-blue gap.

BOTTOM LEFT - pristine graphite anode particle: a flattened rounded flake about
70% of its column width, drawn as stacked parallel medium-gray layers. A thin, even pale olive shell surrounds it (the SEI). About 20 small
orange dots sit between the gray layers.

BOTTOM RIGHT - the same graphite particle after cycling, same size: the pale
olive shell is clearly thicker and slightly uneven. Only about 8 orange dots
remain between the gray layers, and about 6 orange dots are embedded inside the
olive shell.

Only the graphite particles have an olive shell; the cathode particles have none.
The only arrow in the image is the single hollow arrow between the columns.

STRICTLY EXCLUDE: battery casings, cylindrical or pouch cells, jelly rolls,
current collectors, separators, electrolyte bath, lightning bolts, glowing
particles, sparks, bubbles, dendrites, metal ions, charts, axes, curves,
numbers, scale bars, background patterns, decorative borders.
Colours: blue-gray (cathode), pale blue (electrolyte), dark slate-blue (rim),
medium gray (graphite), pale olive (SEI), orange (lithium dots) - nothing else.

CORRECTIONS compared with the previous version (apply all, change nothing else):
- Both cathode particles have the same diameter; both graphite particles have
  the same size.
- Pristine graphite: about 20 orange dots between layers. Cycled graphite: about
  8 orange dots between layers and about 6 inside the olive shell.
```

### 对照规划逐项看图结论

- **R1：四颗粒与箭头：** 4 个主颗粒、1 个空心左→右箭头，位于两列之间；正极直径接近，石墨主体与含壳尺寸仍未严格保持一致。部分通过。

- **R2：沿晶微裂纹：** 新鲜正极无浅蓝裂纹；循环后约 7 个主要外向分支沿多边形边界，未见明确横切晶粒内部的裂纹。图像层面通过。

- **R3：电解液：** 浅蓝只出现在循环后裂纹和分离间隙；新鲜正极无同类填充。图像层面通过。

- **R4：一个分离群：** 右侧只有一处分离晶粒群，目视 4 个晶粒，与主体间为浅蓝间隙；没有爆裂或多处飞散。图像层面通过。

- **R5：重构薄缘：** 深灰蓝薄缘只覆盖循环后正极外表面；新鲜正极没有该薄缘。图像层面通过。

- **R6/R9：确立/推测：** 底图提供表面薄缘和裂纹两个可加引线的锚点；实线/虚线框与后果标签未在本任务制作，不能据底图宣称其已区分。

- **R7：SEI：** 只有石墨有橄榄色壳；新鲜薄且近均匀，循环后明显更厚、稍不规则。图像层面通过。

- **R8：锂点：** 实测新鲜层间 22；循环后层间 8、SEI 内 7。层间明显减少、壳内含点的关系正确；与提示词约 20 / 8 / 6 有小幅数量差异，点数仅为示意而非观测数据。

- **选用理由：** 没有 alt2 的新鲜裂纹错误，分离群为 4 个晶粒而非 alt1 的约 6 个，循环后层间 8 点与目标一致，壳内 7 点比 alt1 的 8 点接近约 6；科学对象与关系优先于纯数量贴合。

- **实际改善与残留：** 相较 V2，石墨层的大片白色高光减少，循环后层间与 SEI 点数更接近目标；颗粒尺寸、晶粒数量和拼接图样及背景纹理仍不完全符合，不能写成修订已解决所有问题。

- **教学目的：** 四个颗粒与单一过程箭头可用于按关系表核对；仅为机制示意，不是实验图像或实验数据。

- **文字检查：** 逐张看图未见文字、字母、数字、化学式、伪文字、标签、图例或标题；唯一箭头为规划要求的空心右箭头。

- **排除对象：** 未见电池外壳、卷绕结构、集流体、隔膜、浴槽、闪电、发光粒子、气泡、枝晶、金属离子、坐标轴、曲线、比例尺或装饰边框。

- **布局与标签空间：** 2 × 2 布局成立；底部至少约 12% 无对象。顶部颗粒偏大、顶部及右侧标签空间较紧，后续叠加必须根据实际画面重新定位。

- **画风与底色：** 是二维示意，未见 3D 或投影；但背景含极轻微纹理，采样值常为 RGB(254,254,254) 而非严格纯白，填色也有轻微明暗变化，不能记为“完全纯色、无纹理”通过。

- **30–40 晶粒、粒径约图高 30%、同一晶粒图样：** 目视晶粒数量多于 40；正极直径约占图高 42–47%，超过约 30%；左右多边形拼接图样未严格一一相同。此项不通过。

- **终稿标签与专业审校：** 本任务仅生成底图；R6 后果标签、R9 唯一推测虚线框、图例、双语标签字号 ≥6 pt 和材料/电化学专业审校均未在本任务执行或验收。不得据底图声称第 2.9 节全部通过。



## 实测输出（原样粘贴）

下面是完成时实际执行的 ls -l 与 Pillow 像素尺寸/PNG 校验输出。清单含并行流程创建的其他文件；本次仅认领上表五张 PNG。
```text
$ ls -l figures/ch02
total 18584
-rw-r--r--@ 1 zeroone  staff     2107 Oct 29 16:06 ch02-01-brief-vs-prompt-en.tex
-rw-r--r--@ 1 zeroone  staff     2184 Oct 29 16:06 ch02-01-brief-vs-prompt-zh.tex
-rw-r--r--@ 1 zeroone  staff  1065006 Oct 29 11:06 ch02-02-abstract-mechanism.png
-rw-r--r--@ 1 zeroone  staff     3989 Oct 29 16:06 ch02-03-paragraph-to-table-en.tex
-rw-r--r--@ 1 zeroone  staff     3789 Oct 29 16:06 ch02-03-paragraph-to-table-zh.tex
-rw-r--r--@ 1 zeroone  staff  2756172 Oct 29 16:03 ch02-04-nmc-vague.png
-rw-r--r--@ 1 zeroone  staff  1386863 Oct 29 16:04 ch02-05-nmc-brief-v2.png
-rw-r--r--@ 1 zeroone  staff     2144 Oct 29 16:03 ch02-06-nmc-final-en.tex
-rw-r--r--@ 1 zeroone  staff     2058 Oct 29 16:03 ch02-06-nmc-final-zh.tex
-rw-r--r--@ 1 zeroone  staff  1334555 Oct 29 16:05 ch02-06-nmc-v3-base-alt1.png
-rw-r--r--@ 1 zeroone  staff  1328578 Oct 29 16:06 ch02-06-nmc-v3-base-alt2.png
-rw-r--r--@ 1 zeroone  staff  1406312 Oct 29 16:06 ch02-06-nmc-v3-base.png
-rw-r--r--@ 1 zeroone  staff    15484 Oct 29 11:25 ch02-07-paired-comparison-en.pdf
-rw-r--r--@ 1 zeroone  staff    76489 Oct 29 11:25 ch02-07-paired-comparison-en.png
-rw-r--r--@ 1 zeroone  staff    19660 Oct 29 11:25 ch02-07-paired-comparison-zh.pdf
-rw-r--r--@ 1 zeroone  staff    82291 Oct 29 11:25 ch02-07-paired-comparison-zh.png

$ python3 (Pillow Image.open; five files generated by this task)
ch02-04-nmc-vague.png: 1672 x 941 pixels; PNG; RGB
ch02-05-nmc-brief-v2.png: 1672 x 941 pixels; PNG; RGB
ch02-06-nmc-v3-base.png: 1672 x 941 pixels; PNG; RGB
ch02-06-nmc-v3-base-alt1.png: 1672 x 941 pixels; PNG; RGB
ch02-06-nmc-v3-base-alt2.png: 1672 x 941 pixels; PNG; RGB
```



## 交接提醒

用于正文的缺陷描述必须跟随实际选用图；请勿写“V3 已全通过”或把正极 CEI 的字样误当作石墨 SEI 被画错的证据。第 3 次 V3 的标签空间比规划示例更紧，叠加坐标应按实际底图调整；专业审校仍待执行。
