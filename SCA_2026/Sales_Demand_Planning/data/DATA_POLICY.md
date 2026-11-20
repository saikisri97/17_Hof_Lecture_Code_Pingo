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

Forecasts use preceding calendar weeks only, with no filled actual targets. Candidates are fixed as naïve, MA3 and MA6. Validation is 11 August–27 October 2024 (12 weeks), final audit is 3 November–22 December 2024 (8 weeks). Compare common eligible dates per SKU. A has 12/12 validation and 8/8 final dates; B has 2/12 and 0/8. Select A using validation only; report the locked choice and naïve on final data without reselection. The minimum-eight-validation-observations guard is a teaching convention, not a statistical reliability guarantee.

The last two examples concern demand planning only. A fixed150.333333 weekly reference is repeated for one/four weeks to illustrate units and period. This does not claim multi-step forecasting accuracy. The final review keeps original150.333333 and assumed-adjusted180.4 fixed, and compares them with hypothetical actuals150/190. These are not later observed source data. No inventory, transport, cost or service-policy model is included.
