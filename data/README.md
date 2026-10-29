# Simulated paired data / 模拟配对数据

paired-example.csv was manually constructed for this book. It describes no patients, experiment, or published study.

| Field | Meaning |
| --- | --- |
| sample_id | Unique fictional object, SIM01–SIM08; the pairing key |
| before | First measurement, arbitrary units (a.u.) |
| after | Second measurement, arbitrary units (a.u.) |

There are 8 objects and 16 observations, with no missing values or exclusions. SIM04 decreases from 18 to 17; the other seven increase. Means are 13.125 and 16.5. No inferential test is part of the exercise.

中文：本文件是模拟教学数据，不支持真实研究或因果结论。8 个对象的两次测量不能表述为 16 个独立对象。保留配对键，图题或图注注明“模拟教学数据”。数据图由脚本读取原值绘制，不生成、删改观测值。

License: CC BY 4.0, within the scope defined in the repository LICENSE.
