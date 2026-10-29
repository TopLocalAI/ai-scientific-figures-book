"""Read-only image inspection; write chapter-local measurement/provenance files."""
import collections
import datetime
import hashlib
import json
import pathlib
import signal
import subprocess

import numpy as np
from PIL import Image

signal.alarm(60)
ROOT = pathlib.Path(__file__).resolve().parents[2]
OUT = ROOT / "provenance/ch03"
FIG = ROOT / "figures/ch03"
records = json.loads((OUT / "generation-manifest.json").read_text())
inspection = json.loads((OUT / "visual-inspection.json").read_text())
date = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=8))).isoformat()
tool = "Codex 内置 image_gen.imagegen（functions.exec 内 tools.image_gen__imagegen）"
model = "不知道：工具未返回具体模型标识。"
ls_output = subprocess.run(["ls", "-l", str(FIG) + "/"], check=True,
                           capture_output=True, text=True, timeout=15).stdout
size_lines = []
metrics = {"checked_at": date, "images": {}, "geometry": {}, "revision_differences": {}}
for record in records:
    path = ROOT / record["file"]
    with Image.open(path) as im:
        im.verify()
    with Image.open(path) as im:
        width, height = im.size
        mode = im.mode
        pixels = np.asarray(im.convert("RGB")).astype(int)
    record.update({"date": date[:10], "tool": tool, "model": model,
                   "dimensions": [width, height],
                   "sha256": hashlib.sha256(path.read_bytes()).hexdigest()})
    info = {"width": width, "height": height, "mode": mode,
            "bytes": path.stat().st_size, "sha256": record["sha256"],
            "width_at_least_2400": width >= 2400,
            "aspect_ratio": width / height,
            "ratio_relative_error_percent": abs(width / height / (16 / 9) - 1) * 100,
            "bottom_tenth_dark_pixels": int((pixels[int(height * .9):].max(2) < 120).sum())}
    metrics["images"][record["file"]] = info
    size_lines.append(f"{record['file']}\t{width} x {height}\t{mode}\t{info['bytes']} bytes")

for name in ["ch03-03c-cand-branch", "ch03-05b-v3-revised", "ch03-06-final-base"]:
    pixels = np.asarray(Image.open(FIG / (name + ".png")).convert("RGB")).astype(int)
    dark = pixels.max(2) < 125
    bands = [(435, 500), (680, 738)] if "03c" in name else [(435, 505), (690, 755)]
    dna_boxes = []
    for low, high in bands:
        mask = dark[low:high, 80:1450]
        xs = np.where(mask.any(0))[0] + 80
        ys = np.where(mask.any(1))[0] + low
        dna_boxes.append([int(xs.min()), int(ys.min()), int(xs.max()), int(ys.max())])
    ranges = ([(375, 400), (525, 550), (555, 590), (755, 785)] if "03c" in name
              else [(345, 370), (545, 570), (575, 600), (785, 810)])
    frame_rows = []
    for low, high in ranges:
        candidates = np.where(dark[low:high, 150:1400].mean(1) > .9)[0] + low
        assert len(candidates), (name, low, high)
        frame_rows.append(float(candidates.mean()))
    heights = [frame_rows[1] - frame_rows[0], frame_rows[3] - frame_rows[2]]
    error = max(abs(dna_boxes[0][i] - dna_boxes[1][i]) for i in [0, 2])
    length = dna_boxes[0][2] - dna_boxes[0][0]
    entry = {"dna_bboxes_xyxy": dna_boxes, "frame_rows": frame_rows,
             "frame_heights": heights, "frame_height_difference_percent": abs(heights[1] / heights[0] - 1) * 100,
             "dna_endpoint_max_error_px": error, "dna_endpoint_error_percent": error / length * 100}
    if "final" in name:
        occupied_rows = np.where(dark[:330, 1170:].any(1))[0]
        clear_height = int(occupied_rows.min()) if len(occupied_rows) else 330
        entry["right_30_percent_clear_height_px"] = clear_height
        entry["right_30_percent_clear_height_percent"] = clear_height / pixels.shape[0] * 100
        entry["grayscale_samples"] = {}
        for label, box in [("PAM", (928, 220, 958, 232)), ("donor", (710, 648, 735, 670))]:
            x1, y1, x2, y2 = box
            patch = pixels[y1:y2, x1:x2]
            mask = (((patch[:, :, 0] > 180) & (patch[:, :, 1] > 140) & (patch[:, :, 2] < 150))
                    if label == "PAM" else
                    ((patch[:, :, 1] > patch[:, :, 0] + 30) & (patch[:, :, 1] > patch[:, :, 2] + 10)))
            rgb = np.median(patch[mask], axis=0)
            entry["grayscale_samples"][label] = {"roi_xyxy": list(box), "median_rgb": rgb.tolist(),
                                                  "luma": float(rgb @ np.array([.2126, .7152, .0722]))}
    metrics["geometry"][name] = entry

for stage, previous in [("r1", FIG / "ch03-03c-cand-branch.png"),
                        ("r2", OUT / "ch03-05b-r1.png"), ("r3", OUT / "ch03-05b-r2.png")]:
    current = np.asarray(Image.open(OUT / ("ch03-05b-" + stage + ".png"))).astype(int)
    before = np.asarray(Image.open(previous)).astype(int)
    difference = np.abs(current - before).max(2) > 15
    metrics["revision_differences"][stage] = {"changed_pixels_percent": float(difference.mean() * 100),
                                            "top_row_changed_percent": float(difference[:300].mean() * 100),
                                            "threshold": "max absolute RGB channel difference > 15/255"}

counts = collections.Counter(r["key"] for r in records if "alias_of" not in r)
assert max(counts.values()) <= 3
assert len(inspection["notes"]) == len(records)
assert metrics["images"]["figures/ch03/ch03-05b-v3-revised.png"]["sha256"] == metrics["images"]["provenance/ch03/ch03-05b-r3.png"]["sha256"]
main = [r for r in records if r["file"].startswith("figures/") and "-alt" not in r["file"]]
assert len(main) == 8
(OUT / "generation-manifest.json").write_text(json.dumps(records, ensure_ascii=False, indent=2) + "\n")
(OUT / "measurements.json").write_text(json.dumps(metrics, ensure_ascii=False, indent=2) + "\n")

geometry_output = json.dumps(metrics["geometry"], ensure_ascii=False, indent=2)
diff_output = json.dumps(metrics["revision_differences"], ensure_ascii=False, indent=2)
measured_output = ("$ ls -l " + str(FIG) + "/\n" + ls_output
                   + "\n$ PNG pixel dimensions (Pillow read + verify)\n" + "\n".join(sorted(size_lines))
                   + "\n\n$ Geometry measurement\n" + geometry_output
                   + "\n\n$ Revision pixel comparison\n" + diff_output + "\n")
(OUT / "verification-output.txt").write_text(measured_output)

intro = f"""# 第 03 章 codex-image 生成与核验记录

核验日期：{date}。状态：8 张规定路径底图均已保存；**部分验收未通过，不能当作全章已合格终稿**。

## 范围、工具与诚信说明

- 只交付 FIG 03-02a/b/c、03-03a/b/c、03-05b、03-06 的 PNG 底图；未制作 TikZ、文字标签、章节或非 codex-image 图。
- 实际工具：{tool}。具体模型：{model}
- 21 次图像生成调用；22 个 PNG 文件 = 8 张正文路径文件 + 7 张 figures 下备选 + 7 张 provenance 下中间版/备选。05b 正文图复制 r3，不额外调用生成。
- 每张草图、候选及每个修订阶段最多 3 次。修改失败时回到上一阶段选定版重试；每条参考图路径见下文。未运行子 agent，未 commit/push。
- 02a/b/c 是模型模拟铅笔草图。所有图都是教学示意，不是实验图或数据。
- 图像均逐张进行了模型视觉检查，没有观察到文字、字母、数字或伪文字；没有执行 OCR（本机未找到 tesseract），也没有真人同事测试或基因编辑同行签名复核。RNA 发夹、DNA 横档、箭头和 indel 标记按图形对象判断，不当作标签。
- 图片没有手工修图、裁切、插值放大或补画；只复制原始输出。工具自动在自身 generated_images 缓存中落盘，交付副本及本任务手动写入文件仅在 figures/ch03 和 provenance/ch03。逐张源路径保存在 generation-manifest.json。
- 规划 prompt 逐字保留，公共开头与布局段用空行连接；候选图依规划将 LAYOUT 占位符替换为 A/B/C 对应原文。重试追加说明逐条列出，**不是所有调用都与规划字符串完全相同**，且三张候选的最终文字不完全相同。不能沿用“只换草图、提示词完全相同”的图注表述。

## 总体验收和需交回作者的差异

| 项目 | 实测/结论 |
|---|---|
| 正文路径 | 8/8 已保存；所有 PNG 可解码 |
| 像素尺寸 | 全部 1672×941，未达到 ≥2400 px；原生宽高比 1.776833，较 16:9 偏差约 0.0531% |
| 提高分辨率尝试 | 02b 第 1 次追加 2560×1440 和 ≥2400 px，仍未生效；工具没有独立尺寸参数；未插值冒充高分辨率 |
| 无字 | 逐张视觉检查未见文字；不等于 OCR 或真人校对 |
| 02c | 分支各到一条通道；框仍不等高，RNA 双描线，风格与 A/B 非严格一致 |
| 03b | 最终候选箭头两进两出，但 NHEJ/PAM 细节位置漂移及额外 PAM 未解决；不通过全部科学/画面验收 |
| 03c 实际问题 | 缺口两侧重复 PAM、153/198 px 不等高框；没有漂浮/重复供体，没有细胞核；DNA 端点已基本对齐 |
| 05b | 单侧 PAM、唯一 HDR 供体及两种结果保留；端点误差 0.224% <2%，框高仍差 5.96% |
| 06 | 端点误差 0.224% <2%；框高差 5.71%；右 30% 的纯空白高度约 32%，目标约35%，连接线侵入预定插图区域下缘 |
| 平涂风格 | 候选和后续图含轻微蓝色纹理及橙色高光，未严格满足 no gradients/no highlights/no texture |
| 修改 4 | 无多余细胞核/背景对象，按 §3.8 条件跳过；没有 r4.png，不伪造“四步全执行” |
| 标签/插图/最终尺寸 | 本轮只做底图，标签不压对象、6.5 pt 字号、174 mm 排版及精确 PAM 插图未验证 |
| 阅读顺序/同行复核 | 未做真人测试；编号只能写“作者预期”，不能虚构同事测试或领域审核 |

## 终稿 C1–C9 视觉核验

| 关系 | 结论 | 观察 |
|---|---|---|
| C1 sgRNA–Cas9 | ✓ | 第一步橙 RNA 与蓝灰 Cas9 接触；发夹可辨 |
| C2 PAM 识别 | ✓ 示意层面 | 第二步蛋白/RNA 复合物邻近黄色段 |
| C3 靶链配对/R 环 | ? | 有橙线和置换轮廓，但横档、双描边使配对对象含混，不能据此验证靶链身份 |
| C4 PAM 非靶链位置 | 部分 | 第三步黄色段在上链、缺口右侧；精确方向/碱基几何需另行 TikZ 插图 |
| C5 双链断裂 | ✓ 简化 | 两条链在同一 x 位置有缺口，右侧黄段相邻；3 bp 距离未在底图表达 |
| C6/C7 NHEJ | ✓ 示意层面 | 上通道无模板，结果有单一红紫 indel 标记；“可能”须由标签/图注说明 |
| C8/C9 HDR | 部分 | 下通道有唯一短供体及青绿写入段，中心接近；两段青绿长度不严格相等，没有画修复中间步骤 |
| 阅读路径 | 模型检查通过，真人未测 | 上排三步→同一右侧分叉→上下两结果；选定 06 第2次，未使用分叉脱节的第3次 |
| 禁止项 | 视觉检查通过 | 无细胞核、剪刀、闪电、发光及文字；轻微高光属于风格未达标，已另列 |
| 同行科学复核 | 未完成 | 未请基因编辑同行复核，不填写虚构签名 |

## 每次修改的副作用

| 阶段 | 尝试次数 | 处理与实际结果 |
|---|---:|---|
| PAM r1 | 2 | 原文第1次无效；第2次追加定位后删除左侧重复 PAM；细线/色纹再渲染 |
| 供体 r2 | 2 | 第1次删掉供体，弃用；回到 r1 后重试，保留并略下移唯一供体 |
| 对齐 r3 | 3 | 第1次删除供体并混合两结果颜色，弃用；第2次仍不等高；第3次框高差减小但未消除，下通道连带下移 |
| 删除背景 r4 | 0 | 条件不成立，跳过 |
| 终稿留白 | 3 | 第1次留白不足且路径脱节；第2次连通、留白高度稍不足；第3次留白增加但分叉脱节，弃用，选第2次 |

## 每个文件的完整调用和逐条视觉结论
"""
parts = [intro]
for record in records:
    filename = pathlib.Path(record["file"]).name
    reason = inspection["reasons"].get(filename, "未追加/改写规划英文 prompt；仅作规划要求的公共段拼接或 LAYOUT 占位替换。")
    references = ", ".join(record["reference"]) or "无；从文字生成"
    notes = inspection["notes"][filename]
    detail = (f"\n### {record['file']}\n\n"
              f"- 工具：{tool}\n- 模型：{model}\n- 日期：{date[:10]}\n"
              f"- 本阶段第几次：{record['attempt']}\n- 参考图：{references}\n"
              f"- 输出：1672×941，RGB PNG；SHA-256：`{record['sha256']}`\n"
              f"- prompt 改动原因：{reason}\n- 人工图像修改：无。\n\n"
              "画面内容 / 核验要点逐条检查：\n\n"
              + "\n".join("- " + note for note in notes)
              + "\n- 共通核验：未见文字；像素宽度未达2400；约16:9；未真人复核。\n\n"
              "实际完整 prompt（保留换行）：\n\n```text\n" + record["prompt"] + "\n```\n")
    parts.append(detail)
    (OUT / (pathlib.Path(filename).stem + ".txt")).write_text(detail.lstrip())
parts.append("\n## 实测输出\n\n以下为脚本直接读取文件所得，不是规划预期值。几何测量采用明确 ROI 的深色像素阈值；边框中心取覆盖率超过90%的行均值。差值统计包含图像重绘纹理，不等价于对象语义变化。\n\n```text\n" + measured_output + "```\n")
(OUT / "codex-images.md").write_text("\n".join(parts))
print(measured_output)
print(f"Verified {len(records)} PNG records; {len(main)} main images; {sum(counts.values())} generation calls; each stage <=3 attempts.")
print("Saved codex-images.md, same-name TXT files, measurements.json and verification-output.txt.")
