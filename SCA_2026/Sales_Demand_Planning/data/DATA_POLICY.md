# Sales history policy

The source is a supplied teaching CSV, not an independently authenticated operational record. The previous treated CSV is preserved at its original path and is not used as ground truth.

1. Preserve the raw snapshot. The notebook verifies its SHA-256 whether loaded from the data folder or its embedded copy.
2. Under an explicit teaching assumption, remove three exact repeated export rows. This assumes they are duplicate exports, not legitimate transactions.
3. Quarantine the invalid-date record. Do not infer its week or silently count it as zero.
4. Quarantine both records for the conflicting SKU_A/2024-01-14 key. Do not sum -5 and166 or invent the authoritative correction.
5. Reindex each SKU to104 Sunday-labelled weeks. Retain gaps as unknown; a Sunday label does not establish a formal business week-ending convention.
6. Treat the remaining negative sales as unknown pending returns/error interpretation. Preserve their original values in the raw data.
7. Retain recorded large promotion events. Do not cap sales or fill prices/promotion status. No revenue/profit calculation is attempted because price currency/basis are not supplied.

Outcome:208 calendar SKU/weeks,198 known sales values,10 unknowns. The quarantine contains one invalid-date record and two conflicting records. Preparation adds no recovered sales evidence.

Forecasts use preceding calendar weeks only. Never fill unknown actuals to create evaluation targets. Both windows and the naive benchmark use the same eligible final20-week dates per SKU; A has20 scored dates, B only2. The small B sample is a substantive limitation.

The stock rule is a declared SKU_A scenario, not a calibrated service policy: immediate replenishment before the next selling week, weekly review, no on-order/backlog, no capacity/pack-size constraints. The latest3-week forecast is150.33 units. The buffer uses observed sales SD from the pre-evaluation period. Factors1/1.65 do not imply guaranteed service. Order quantities alone are rounded up to whole units.
