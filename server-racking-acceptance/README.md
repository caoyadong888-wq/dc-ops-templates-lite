# Server racking acceptance (lite)

## English

## Purpose

Score a delivery carton. The full pack adds racking, the four-role sign-off, the formula workbook, and the worked three-server batch.

## Deliverables

- `deliverables/score_delivery.py` — fails a row when the serial, seal, packaging, or shock indicator is wrong.
- `deliverables/delivery_acceptance_short.md` — two filled cartons, one pass and one shock-indicator failure.
- `deliverables/racking_checklist_short.md` — the racking gates, listed but not the full worked batch.
- `examples/sample_delivery.csv` — the two cartons the script scores.

## Quick start

```text
python3 deliverables/score_delivery.py --input examples/sample_delivery.csv
```

You should see one pass and one fail.

## 中文

## 目的

只判断到货纸箱。完整版还有上架、四角色会签、带公式的工作簿，以及三台服务器的完整例子。

## 交付物

- 到货打分脚本。
- 两台纸箱的短清单：一台通过，一台冲击指示器变红。
- 上架闸门列表。
- 供脚本读取的 CSV。

Full version: GUMROAD_URL
