# Case provenance / 案例来源

- mechanism-prompt.txt: the exact instruction sent to Codex's built-in image generation.
- mechanism-review.json: output hash, semantic checks, observed style deviation, and generator disclosure.
- paired-data-check.json: counts, means, and direction checks produced by the deterministic plotting script.

The mechanism output was generated in Codex, not SciDraw AI. The actual prompt uses letter labels only and moves relation definitions to the caption, a documented presentation choice relative to the fuller drawing brief.

No exact model name, seed, or hidden setting was returned by the generation tool. The repository therefore makes no claim of pixel-identical regeneration. The original output is included to make the case inspectable.

中文：保留实际输入、原始输出与核验记录。机制案例由 Codex 生成，模型细节未返回，不自行补写。数据图可以按源数据和脚本复现；不同运行环境的字体或 PDF 元数据可能不同。
