# DC UPS/Power Inspection (lite)

## English

A free slice of the UPS inspection pack: eight checklist rows from the EXAMPLE-DC1 visit, and a calculator that covers N and N+1 only.

## Purpose

Show the shape of the inspection and the load / headroom alert without the full workbook.

## Deliverables

- `deliverables/inspection_checklist_short.md` — eight filled checks, including the three failures.
- `deliverables/ups_capacity_lite.py` — load ratio, N and N+1 headroom, and the same 70/80 and 25/15 alert bands.
- `examples/sample_capacity.csv` — three UPS rows that land on OK, WARN, and CRITICAL.

## Quick start

```text
python3 deliverables/ups_capacity_lite.py --input examples/sample_capacity.csv
```

2N, the formula workbook, the Chinese checklist, and the full 18-item visit are in the paid pack.

## 中文

这是完整巡检包的免费部分：EXAMPLE-DC1 巡检里的八项，外加只支持 N 和 N+1 的容量计算。

## 交付物

- 八项已填写的检查清单，含三次不通过。
- 计算负载率和 N / N+1 余量的脚本。
- 三行示例，分别落在正常、预警和严重。

完整版还有 2N、带公式和颜色的工作簿、中文清单，以及全部 18 项巡检。

Full version: GUMROAD_URL

## Delivery time / 交付时间

- Lite (this repo): free, available now. / 精简版（本仓库）：免费，立即可用。
- Full version: instant download after purchase (GUMROAD_URL). / 完整版：购买后即时下载（GUMROAD_URL）。
