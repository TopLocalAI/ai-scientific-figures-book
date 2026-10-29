# 图 8-7：生成式放大实验记录

- 执行日期：2026-10-29（Asia/Shanghai）；记录时间：2026-10-29T16:29:35+08:00。
- 任务：使用低分辨率叶表皮 SEM 局部，独立进行三次生成式放大，作为图像诚信教学反例。
- 实际工具：内置 `image_gen.imagegen`（本环境调用名 `tools.image_gen__imagegen`），经 `functions.exec` 调用；未使用 CLI/API 替代。工具接口没有提供可核实的底层模型名称、版本或随机种子，故不推测这些信息。
- 模式：图像编辑/参考图模式。**三次都实际传入了同一张本地输入图**，并非纯文字生成；没有把前一次生成结果作为下一次输入。
- 调用次数：恰好 3 次，三次均成功；没有重试、淘汰或替换。编号严格按调用先后排列。**正文固定使用第 1 次，另外两次存档**，没有挑选“最离谱”的结果。

## 输入及来源核对

- 输入文件：`data/ch08/fig07-input-lowres.png`。
- 输入尺寸/格式：128 × 128 像素，PNG，`L` 模式（8 位灰度）。
- 输入 SHA-256：`297c5e39691ea41f4f31b2e20a8e9a18e0b476b114c994fb0f4d58851da8d58e`。
- 调用前使用 `view_image` 实际查看了输入：灰度叶表皮 SEM 局部，可见不规则细胞轮廓、气孔样开口、右侧较大的毛状体结构，以及左下斜向的毛状结构。
- 来源依据：项目规划将其源图列为 S3（Louisa Howard，Dartmouth Electron Microscope Facility 的 `Leaf_epidermis.jpg`）。本次没有另行联网复核许可。
- 本地读回验证：源图 `data/ch08/sourced/Leaf_epidermis.jpg` 的裁剪框 `(640, 680, 1152, 1192)`（左、上含端点，右、下不含端点）为 512 × 512 像素；对每个 4 × 4 区块做面积平均并转换为 uint8，所得 128 × 128 数组与输入 PNG **逐像素完全一致**。这与 `scripts/ch08_figures.py` 的输入准备逻辑吻合。
- 高分辨率源图只用于此次本地来源核验，**没有作为参考图传给生成工具**。

## 三次完全相同的调用参数

```json
{
  "referenced_image_paths": [
    "data/ch08/fig07-input-lowres.png"
  ],
  "transparent_background": false
}
```

`prompt` 参数如下，保留规划 `FIG ch08-07` 中英文全文的措辞、标点与换行（仅去掉 Markdown 代码块的排版缩进）。保存记录时已程序核对与规划一致，没有追加尺寸说明、风格词或其他要求。

```text
Upscale this grayscale scanning electron microscope image to 512 x 512 pixels.
Make it sharper and more detailed, remove blur and noise, and enhance the fine
surface structures so it looks like a high-resolution micrograph.
Keep it grayscale. Do not add any text, letters, numbers, labels, or scale bars.
Square 1:1 aspect ratio.
```

## 输出文件与尺寸

| 次序 | 保存文件 | 像素尺寸 | 实际色彩模式 | 文件字节数 | 最大通道差 | 平均通道差 |
|---|---|---|---|---:|---:|---:|
| 1 | `figures/ch08/ch08-07-ai-upscaled-1.png` | 1254 × 1254 | RGB，8 位/通道 | 3,616,138 | 12 | 1.175431 |
| 2 | `figures/ch08/ch08-07-ai-upscaled-2.png` | 1254 × 1254 | RGB，8 位/通道 | 3,392,627 | 10 | 0.901030 |
| 3 | `figures/ch08/ch08-07-ai-upscaled-3.png` | 1254 × 1254 | RGB，8 位/通道 | 3,508,098 | 12 | 0.936203 |

“通道差”为每像素 `max(R,G,B) - min(R,G,B)`，数值范围 0–255。三图视觉上接近灰度，但 RGB 三通道并不完全相同，因此不能把这些原始输出描述为严格单通道灰度图。

提示词要求 512 × 512（相对输入边长放大 4 倍），工具实际均返回 1254 × 1254（边长约 9.796875 倍）。当前工具接口没有独立的像素尺寸参数。本次按任务要求保留全部原始生成输出，**逐字节复制，没有重采样、转灰度、锐化、裁剪或配准**。未因尺寸不符而重试。

后续组合图如需与 512 × 512 GT 作比较，应按规划仅为比较使用 Lanczos 调整尺寸，并记录从 RGB 到灰度的具体转换及顺序；若发现平移/旋转，还须按规划核查并记录刚性配准。这些比较处理与组图不在本次交付中。

实测 `ls -l`：

```text
-rw-r--r--@ 1 zeroone  staff  3616138 Oct 29 16:27 figures/ch08/ch08-07-ai-upscaled-1.png
-rw-r--r--@ 1 zeroone  staff  3392627 Oct 29 16:27 figures/ch08/ch08-07-ai-upscaled-2.png
-rw-r--r--@ 1 zeroone  staff  3508098 Oct 29 16:27 figures/ch08/ch08-07-ai-upscaled-3.png
```

输出 SHA-256：

- `ch08-07-ai-upscaled-1.png`：`a49e9d57324c6eda2081c9b202984d86936863e28af288e2be91be761fb2caae`
- `ch08-07-ai-upscaled-2.png`：`6549295f2db7844173b0700b04018e1cd06141f1d9fa09ff9186716be0662c95`
- `ch08-07-ai-upscaled-3.png`：`f7ec1478c1f3c1cdf596ae57099d7f5a0ac9011ca04ba9f3f95a0200b2cafdf0`

内置工具自动保存的原始产物（保留原位，未改动）与项目文件对应如下；已核对每份复制品与工具产物字节完全相同：

- 第 1 次：`codex-output/exec-21c5616c-0d7f-4e1f-9061-f448111f4426.png` → `figures/ch08/ch08-07-ai-upscaled-1.png`
- 第 2 次：`codex-output/exec-7023fe13-2a59-4ee5-9c8f-90d64cf490d7.png` → `figures/ch08/ch08-07-ai-upscaled-2.png`
- 第 3 次：`codex-output/exec-3a1d1a8b-2b79-4fa9-a855-f52f562f7ef1.png` → `figures/ch08/ch08-07-ai-upscaled-3.png`

## 逐次可见差异

以下基于实际查看输入及三次完整输出，位置用相对图幅描述；只记录可见形态，不据此认定具体生物学结构或测量结果。

| 次序 | 实际看到的特征与差异 |
|---|---|
| 1（正文用图） | 大体保留了左中气孔样开口、右侧大型毛状体及左下斜向毛状体的位置。左中开口外围出现规则的多层环形边缘与齿状纹理；大部分表面是紧密条片/鳞片状细纹。右侧大型结构的基部呈层叠条片，左下毛状体顶端显得较平滑而模糊。 |
| 2（存档） | 多数表面细纹变成更圆钝、更密集的颗粒/卵石状凸起；左中开口外围的环形层次和颗粒分布与第 1 次不同。左下毛状体顶端出现更清楚的多边形分块；右侧大型结构基部的纹理更像圆钝的叶片。中心及右侧还可见数个明亮孤立点状/短条状形态。 |
| 3（存档） | 表面更偏细长指状/鳞片状纹理；右侧大型结构基部出现明显的放射状细长褶片。左中开口的内外环更厚且层次清楚；左下毛状体顶端呈少数较大的圆钝分块。细纹走向、开口边缘及明亮小形态的轮廓又与前两次不同。 |

三次均未见文字、标签或比例尺。三图都保留输入的大体构图，但细部纹理和局部轮廓在重复生成之间不同。低分辨率输入无法为这些新出现的高频细节提供直接测量证据。这里没有完成与 GT 的细节逐区对照、伪结构圈注、刚性配准、MAE 或 SSIM 计算，不能把上述观察冒充为这些分析的结果；正文圈注应由组图作者对照 GT 后确定。

## 交接与范围

- 本次在项目内仅新建三个指定 PNG 与本记录，未修改其他项目文件，未提交或推送，未启动子代理。
- 第 1 次输出的正式交接路径是 `figures/ch08/ch08-07-ai-upscaled-1.png`。
- 检查时，现有 `scripts/ch08_figures.py` 的 `find_ai_upscale()` 查找的是 `ch08-07-ai-upscaled-run1.png`、`work/ch08-07-codex-upscaled-run1.png` 或 `ch08-07-ai-upscaled.png`，尚不包含本任务规定的 `ch08-07-ai-upscaled-1.png`。后续组图负责人需对接该路径；本任务未改脚本，也未额外建立别名文件。
- 所有 shell 读取、复制与验证命令均在发现任务的超时要求后加上了显式超时（Python `signal.alarm` 或子进程 `timeout`）；最初读取任务文件和查找项目约定的两个短命令在获知该要求前执行，均已立即结束。
