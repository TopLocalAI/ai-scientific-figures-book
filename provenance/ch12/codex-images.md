# 第 12 章 Codex 图片生成与核验记录

记录日期：2026-10-29T16:12:58.082246+08:00。

## 范围与结果

- 根据 `production/plans/ch12.md` 第 4 节与 `production/book-spec.md` 第 4、5 节，仅生成 FIG ch12-07 的无字底图。图清单中的其他 FIG 为 tikz、python 或 reuse，不在本次范围。
- 同一个英文 prompt 原样调用 3 次，已达到每图最多 3 次；选第 3 次，前两次分别保留为 alt1、alt2。未用图片编辑、裁剪、拉伸、补边或文字覆盖修补生成结果。
- 三次均通过核心的无字、远近差异、抽象海报三项目视核验；但原生输出不为严格 16:9，地面线采用近似透视，海报排跨出右半幅，画风带轻微渐变。这些偏差未隐瞒为完全通过。
- 仅交付底图，距离标签由后续章节 TikZ 叠加；建议最终图注沿用“示意图，人物与距离不按比例”。
- 规划末尾 M1/M2 为可选 fallback，没有本次 ch12 FIG 编号和指定的 ch12 输出路径，且要求按第 9 章 provenance 记录。核查时第 9 章资产尚未出现；此次未扩展执行这两项可选任务，以免越过仅 ch12 图片/溯源目录的写入范围。
- 使用内置工具 `image_gen__imagegen`（通过 `functions.exec` 调用）；具体底层模型：不知道，工具结果未提供模型名。每次参数均为下文完整 prompt、`transparent_background: false`，没有引用图片。宽高比只能通过原 prompt 中的 `landscape 16:9` 请求，工具接口未提供单独的尺寸参数。
- imagegen 技能所列路径不存在，在 `.codex` / `.agents` 的 SKILL.md 中搜索也未找到；直接按当前内置工具说明调用。
- 工具自动将原始输出缓存在下文所列 `.codex/generated_images` 路径；按工具返回要求保留原文件，逐字节复制到指定交付目录。除工具自管缓存外，本次文件写入仅在 `figures/ch12/` 与 `provenance/ch12/`；未改其他项目文件，未启动子 agent，未 commit/push。

## 第 1 次：落选，保留为 alt1

- 文件：`figures/ch12/ch12-07-poster-hall-distances-alt1.png`
- 实际工具：`image_gen__imagegen`；具体模型：不知道。
- 生成次数：第 1 次（全新生成，无参考图）。
- 工具原文件：`codex-output/exec-e45b0e7c-4c7f-46c3-b25d-2fdde1d86d30.png`
- 实测：1672 × 941 px，PNG，RGB；宽高比 1.776833156，相对 16:9 误差 -0.053135%。不满足严格整数像素 16:9。
- SHA-256：`54ba90578a04d172588f66768962ff33b50f07228a68ae9eaa5d49de821bf1b7`；与工具原文件逐字节一致。

### 实际使用的完整 prompt

与规划英文原文逐字相同（993 个字符；Markdown 围栏缩进不属于 prompt），没有增加或修改内容。

```text
A clean flat vector-style illustration of a scientific conference poster hall, side three-quarter view, landscape 16:9, white and very light grey background. A row of five tall portrait poster boards stands along the right half of the image. The posters show only abstract layouts: a solid colored band at the top, two columns of soft grey rectangles and a few simple chart-like shapes in muted teal and grey. One attendee walks along the aisle in the left foreground about four meters away from the posters, glancing at them. A second attendee stands close to the middle poster, about one meter away, reading carefully. Simple, friendly human figures without facial detail. On the floor, two faint dashed lines run parallel to the poster row, one near the walking attendee and one near the reading attendee. Even soft lighting, no shadows clutter, generous empty space at the top. Strictly no text of any kind: no letters, no words, no numbers, no logos, no signage, no labels on the posters.
```

### 看图后逐项对照

| 规划要求 | 实际观察与结论 |
|---|---|
| 教学目的：先远看、再近看 | 左前景行走者与中间海报前的阅读者形成明确远近对照；可用于解释两种观看状态。通过。 |
| 会议展区、侧三分之四视角、五块竖版板 | 五块海报板逐块可数，具有侧向透视；左侧另有浅灰建筑背景。通过数量与场景检查。海报排横跨约右侧七成，未严格局限在右半幅。 |
| 远处行走者侧头看 | 左侧背包人物一只脚抬起，头朝海报方向；行走状态可见，但比第 2、3 次略弱。通过。 |
| 近处观众细看中间海报 | 第二位人物站在第三块海报前，手靠近下巴。通过。 |
| 抽象内容：色带、两栏灰块、少量图形 | 五块海报均为色带、灰矩形与无标注几何图形，未发现真实会议内容。标题带另有橙、紫等色；图形主要为青灰。通过。 |
| 两条浅虚线与海报排平行、靠近两位观众 | 有两条浅灰虚线，但两条线的倾斜差别较大，与展板排的透视方向不够一致。部分符合；这是重生成的主要原因。 |
| 简单人物、无面部细节、柔和光照、顶部留白 | 无眼睛、眉毛等细节；顶部留白充分。人物与背景带柔和渐变、地面浅阴影，并非完全纯色平涂。部分符合 flat vector-style 的严格读法。 |
| 核验：无任何文字、伪文字、徽标 | 已查看完整输出及保存 PNG；未见文字、字母、数字、伪文字、标志或水印。灰条是完整矩形，无字形。通过目视检查。 |
| 核验：两个观众距离差明显 | 一人在左前景通道，另一人在海报前；差别明确。通过。不能据画面精确测得 4 m / 1 m。 |
| 核验：抽象海报，不像真实会议海报 | 无标题、作者、单位与会议信息，内容是通用抽象占位。通过。 |

落选原因：两条虚线的方向分歧最明显；保留原图作为第一次尝试记录。

## 第 2 次：落选，保留为 alt2

- 文件：`figures/ch12/ch12-07-poster-hall-distances-alt2.png`
- 实际工具：`image_gen__imagegen`；具体模型：不知道。
- 生成次数：第 2 次（全新生成，无参考图）。
- 工具原文件：`codex-output/exec-a998315a-ab8f-42a3-bc5f-5a543ff79246.png`
- 实测：1672 × 940 px，PNG，RGB；宽高比 1.778723404，相对 16:9 误差 +0.053191%。不满足严格整数像素 16:9。
- SHA-256：`7c650eabcdae4c0a25e074eb6efb907a5f6e2afa32e92c5cb4d526bcf9c6cdee`；与工具原文件逐字节一致。

### 实际使用的完整 prompt

与规划英文原文逐字相同（993 个字符；Markdown 围栏缩进不属于 prompt），没有增加或修改内容。

```text
A clean flat vector-style illustration of a scientific conference poster hall, side three-quarter view, landscape 16:9, white and very light grey background. A row of five tall portrait poster boards stands along the right half of the image. The posters show only abstract layouts: a solid colored band at the top, two columns of soft grey rectangles and a few simple chart-like shapes in muted teal and grey. One attendee walks along the aisle in the left foreground about four meters away from the posters, glancing at them. A second attendee stands close to the middle poster, about one meter away, reading carefully. Simple, friendly human figures without facial detail. On the floor, two faint dashed lines run parallel to the poster row, one near the walking attendee and one near the reading attendee. Even soft lighting, no shadows clutter, generous empty space at the top. Strictly no text of any kind: no letters, no words, no numbers, no logos, no signage, no labels on the posters.
```

### 看图后逐项对照

| 规划要求 | 实际观察与结论 |
|---|---|
| 教学目的：先远看、再近看 | 走动与驻足阅读区分清楚，远近位置符合教学意图。通过。 |
| 会议展区、侧三分之四视角、五块竖版板 | 五块海报板清楚可数，右侧列队排列；海报排仍占约右侧七成，未严格局限在右半幅。场景、数量通过。 |
| 远处行走者侧头看 | 左前景人物跨步、头转向海报。通过，行走姿态较第 1 次明确。 |
| 近处观众细看中间海报 | 第二位人物靠近第三块海报，站立阅读。通过。 |
| 抽象内容：色带、两栏灰块、少量图形 | 色带、两栏矩形、无标注的柱形、散点、曲线、环形等；没有真实会议内容。图形主要青灰。通过；图形种类较多。 |
| 两条浅虚线与海报排平行、靠近两位观众 | 有两条浅灰虚线，其中近线从阅读者脚边经过；远线经过行走者身后而非脚边，近线和远线透视方向仍不完全一致。部分符合。 |
| 简单人物、无面部细节、柔和光照、顶部留白 | 人物无五官细节，留白充分；存在柔和渐变与浅阴影，并非完全纯色平涂。部分符合严格的 flat 要求。 |
| 核验：无任何文字、伪文字、徽标 | 已查看完整输出和保存 PNG；未见文字、字母、数字、伪文字、徽标、水印。通过目视检查。 |
| 核验：两个观众距离差明显 | 左前景行走者与中间海报前阅读者距离关系明确。通过；绝对米数不可从图中检定。 |
| 核验：抽象海报，不像真实会议海报 | 无真实会议标题、姓名、单位、标志；仅几何占位。通过。 |

重生成原因：虽然人物姿态改善，但输出仍不为严格 16:9，虚线与人物位置仍有改进空间；用相同 prompt 进行最后一次生成。落选原因：第 3 次的虚线位置、配色与抽象布局更符合教学用途。

## 第 3 次：选用

- 文件：`figures/ch12/ch12-07-poster-hall-distances.png`
- 实际工具：`image_gen__imagegen`；具体模型：不知道。
- 生成次数：第 3 次（全新生成，无参考图）。
- 工具原文件：`codex-output/exec-fbc47720-0aa7-4e4e-8fd2-6a18c91922eb.png`
- 实测：1672 × 941 px，PNG，RGB；宽高比 1.776833156，相对 16:9 误差 -0.053135%。不满足严格整数像素 16:9。
- SHA-256：`f105797f66e1687d603829c9f37cdbe89b55b7bd7c21c8846c18b9e7bed77be0`；与工具原文件逐字节一致。

### 实际使用的完整 prompt

与规划英文原文逐字相同（993 个字符；Markdown 围栏缩进不属于 prompt），没有增加或修改内容。

```text
A clean flat vector-style illustration of a scientific conference poster hall, side three-quarter view, landscape 16:9, white and very light grey background. A row of five tall portrait poster boards stands along the right half of the image. The posters show only abstract layouts: a solid colored band at the top, two columns of soft grey rectangles and a few simple chart-like shapes in muted teal and grey. One attendee walks along the aisle in the left foreground about four meters away from the posters, glancing at them. A second attendee stands close to the middle poster, about one meter away, reading carefully. Simple, friendly human figures without facial detail. On the floor, two faint dashed lines run parallel to the poster row, one near the walking attendee and one near the reading attendee. Even soft lighting, no shadows clutter, generous empty space at the top. Strictly no text of any kind: no letters, no words, no numbers, no logos, no signage, no labels on the posters.
```

### 看图后逐项对照

| 规划要求 | 实际观察与结论 |
|---|---|
| 教学目的：先远看、再近看 | 左前景行走者朝向海报；中间观众停留细看。两种观看状态与远近层次清楚。通过，选为正式底图。 |
| 会议展区、侧三分之四视角、五块竖版板 | 五块独立竖版海报板逐块可数；画面为侧三分之四视角。场景与数量通过。海报排占约右侧四分之三，未严格局限在右半幅。 |
| 远处行走者侧头看 | 左前景人物跨步、抬起后脚，头朝海报方向。通过。 |
| 近处观众细看中间海报 | 第二位人物站在第三块海报前，手近下巴，停留阅读。通过。 |
| 抽象内容：色带、两栏灰块、少量图形 | 海报均有蓝/青标题色带、两栏灰矩形与少量无标注图形；配色比前两次更统一，图形仍仅作抽象占位。通过。 |
| 两条浅虚线与海报排平行、靠近两位观众 | 两条浅灰虚线清楚可见，分别经过行走者脚边和阅读者前方；比前两次更贴合所需的距离标注位置。方向与展板排大体同向，但没有严格构造共同消失点，不能宣称是精确的透视平行线。部分符合，保留这一近似。 |
| 简单人物、无面部细节、柔和光照、顶部留白 | 人物无五官细节，白色/浅灰环境，顶部大面积留白；保留少量渐变和浅阴影，属于柔和矢量风格，非完全纯色平涂。部分符合严格的 flat 要求。 |
| 核验：无任何文字、伪文字、徽标 | 已查看生成输出及保存文件预览；逐块检查五张海报、人物服饰与包、环境、地面与留白，未见文字、字母、数字、伪文字、徽标或水印。灰条是完整矩形。通过目视检查。 |
| 核验：两个观众距离差明显 | 左前景通道人物与靠近中间海报的人物之间有明显的观看距离差。通过；人物与绝对距离不按比例。 |
| 核验：抽象海报，不像真实会议海报 | 没有任何会议名称、作者、机构、品牌与可引用数据，仅通用色块与图形。通过。 |

选用原因：三次中虚线最接近两个观看位置，蓝/青/灰配色最统一，人物远近与行走/驻足状态明确，且无字检查通过。三次机会已用完，未将技术偏差改写成完全符合。

## 完成标准：实测输出

命令：`ls -l figures/ch12`（经 Python subprocess 执行，timeout=8 s）。

```text
total 7888
-rw-r--r--@ 1 zeroone  staff  1431926 Oct 29 16:10 ch12-07-poster-hall-distances-alt1.png
-rw-r--r--@ 1 zeroone  staff  1320945 Oct 29 16:10 ch12-07-poster-hall-distances-alt2.png
-rw-r--r--@ 1 zeroone  staff  1280200 Oct 29 16:11 ch12-07-poster-hall-distances.png
```

逐张读取 PNG（Pillow `Image.open().size` / `verify()`），并比对 SHA-256 与工具原文件；下列是实际输出：

```text
ch12-07-poster-hall-distances-alt1.png: 1672 x 941 px; PNG RGB; bytes=1431926; aspect=1.776833156; deviation_from_16:9=-0.053135%; integrity=PASS; source_hash_match=PASS
ch12-07-poster-hall-distances-alt2.png: 1672 x 940 px; PNG RGB; bytes=1320945; aspect=1.778723404; deviation_from_16:9=+0.053191%; integrity=PASS; source_hash_match=PASS
ch12-07-poster-hall-distances.png: 1672 x 941 px; PNG RGB; bytes=1280200; aspect=1.776833156; deviation_from_16:9=-0.053135%; integrity=PASS; source_hash_match=PASS
```

提示词核验：3 个完整 prompt 块均与规划提取的英文原文一致；没有额外补充语句。尺寸检查与文件完整性检查不替代前述人工目视核验。
