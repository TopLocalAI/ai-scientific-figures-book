# FIG ch09-06 / ch09-07 组图组装 provenance

生成日期：2026-10-29。脚本：`scripts/ch09_assemble.py`（`--version v1|v2 --lang zh|en`），数据面板逻辑：`scripts/ch09_plot_utils.py`（c/d 与 `sim_perovskite` CSV 一致）。a/b 底图：`figures/ch09/ch09-03-device-structure-base.png`、`ch09-04-sem-like-illustration-base.png`（合成时叠加矢量/文字标签，不依赖单独 codex 导出 PNG）。

## 十个问题：v1 体现与 v2 修正

| # | 问题 | v1（ch09-06）中的体现 | v2（ch09-07）中的修正 |
|---|------|------------------------|------------------------|
| 1 | 面板字母混用 | `A`（14 pt 衬线）、`(b)`（9 pt 右上）、`c.`（8 pt）、d 无字母 | 统一 **TeX Gyre Heros Bold** 小写 **a–d**，10 pt，上排/下排各一条基线，框左上角外偏 1 mm（画布顶留 5 mm，避免 a、b 被裁掉） |
| 2 | c/d 字号不一致 | c 在 8×6 in、`font.size=10` 下重绘后 raster 缩入格内，刻度约 **4–5 pt**；d 按 84×56 mm、8 pt 出图 | c、d **直接在 174 mm 画布上**按 84×56 mm 格、`font.size=8` 重绘，拼合缩放系数 **1.0** |
| 3 | 颜色语义不一致 | c 默认蓝/橙；d 红/绿；a 底图经 `purple_shift` 把钝化层偏紫 | 对照 `#6E6E6E` 虚线、改性 `#1B7F86` 实线；a 标签中钝化层文字为青色 |
| 4 | 灰度不可分 | v1 中 c、d 均为实线 | 虚线/实线 + 灰/青，灰度下仍可分 |
| 5 | 图例压线 | c、d 带边框 `legend` | 去掉图例框，曲线端直接标注「对照/改性」 |
| 6 | c/d 轴框未对齐 | 源图轴位置 `(0.125,0.11)` vs `(0.143,0.179)`，缩入同格后实测错位约 **left 1.4 mm、bottom 3.2 mm**（见 `provenance/ch09/ch09-06.json`） | a 与 c、b 与 d 的左右缘对齐。轴框 **底边 11.0 mm、高度 46.0 mm、宽度 69.0 mm**（c 左 13 mm、右 82 mm；d 左 101 mm、右 170 mm），右缘再留 4 mm 给末位刻度。脚本 `assert` 四框的 x0/x1 一致 |
| 7 | b 被拉伸 | `imshow(..., aspect='auto')` 填满与 a 同高的格 | `aspect=原图宽高比`，格内居中留白 |
| 8 | 面板间距不一 | `GridSpec` 非均匀 `wspace`/`hspace` | 列距 **6 mm**（a|b、c|d），行距 **8 mm**（上排解释组与下排数据组） |
| 9 | 缺少面板内声明 | b 无模型生成说明；c/d 无「模拟数据」；d 无 0.8 线 | b 左下半透明白底（无描边）包住全部「模型生成示意，非显微图像」；c/d 右上「模拟数据」；d 浅灰点线 0.8，标签在对照穿过 0.8 之后的点线上方 |
| 10 | 面板标题重复图注 | c「J-V curve」、d「Stability test」；c 单位 `mA/cm2` | 删除面板标题；单位 **V、mA cm⁻²、h** |

## 面板实际字号（pt，按脚本 rcParams / `fig.text`）

| 元素 | v1 | v2 |
|------|----|----|
| 数据轴刻度、轴标题、曲线端标注、PCE、T80、80% | c ≈ **4.5 pt**（缩入后）；d **8 pt** | **8 pt** |
| 面板字母 | 混用 5–14 pt | **10 pt** TeX Gyre Heros Bold |
| a 层名与声明（合成叠加） | （v1 仅用底图 + 紫色偏移，无 v2 层名表） | **8 pt**（FandolHei / Helvetica；SnO₂ 为 `$\mathrm{SnO_2}$`，不用 Fandol 的 U+2082） |
| b 模型生成声明 | 无 | **8 pt** |

中文 PDF 经 PGF/XeLaTeX 导出（`pdf.fonttype=42`）；英文 PDF 为 matplotlib 矢量文字。

## 位图面板有效分辨率（ppi）

在 **300 dpi** 导出 PNG（整图 174 mm → 2055 px 宽）前提下，a/b 与 c/d **同宽、上沿对齐、保持宽高比** 后的占用尺寸与源像素：

| 面板 | 源像素 | v2 印刷占用（约） | 有效 ppi |
|------|--------|-------------------|----------|
| a | 1586×992 | 宽 69.0 mm × 高 43.2 mm（与 c 同宽，保持宽高比） | **1586 / (69.0/25.4) ≈ 584** |
| b | 1536×1024 | 宽 69.0 mm × 高 46.0 mm（与 d 同宽，保持宽高比） | **1536 / (69.0/25.4) ≈ 565** |

v1 中 b 被 `aspect='auto'` 拉伸，垂直方向有效 ppi 低于上表（约按 ~1.4× 垂直拉伸劣化）。c、d 在 v2 PDF 中为矢量；合成 PNG 在 300 dpi 下与整图一致，数据区约 **300 ppi**。

## 输出文件

- v1：`figures/ch09/ch09-06-assembly-v1-{zh,en}.{pdf,png}`，元数据 `provenance/ch09/ch09-06.json`
- v2：`figures/ch09/ch09-07-assembly-final-{zh,en}.{pdf,png}`。不保留 `ch09-07-assembly-final-en-600dpi.tif`（约 44 MB，仓库不收；脚本若发现旧文件会删掉）。

## v2 看图修订（2026-10-29）

只改 `scripts/ch09_plot_utils.py` 的 `good=True` 路径和 `scripts/ch09_assemble.py` 的 `assemble_v2`。未重跑 v1。

画布 **174 × 116 mm**。四块面板左右缘对齐：a/c 为 x = 13–82 mm，b/d 为 x = 101–170 mm。a、b 用与图像相同的宽高比（不再把 `imshow` 的 `aspect` 设成像素宽高比，那会把坐标轴改成窄条）。c、d 直接画在这块矩形上，没有外包一层 0–1 坐标轴。系列名放在线末端左侧的空白里，末位刻度「1000」「1.2」完整落在画布内。全图最小字号 8 pt。
