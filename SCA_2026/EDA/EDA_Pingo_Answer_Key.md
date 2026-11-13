# EDA Pingo answer key — instructor use

| Question | Correct option in source order | Explanation |
|---|---|---|
| EDA01 | B — Confirm the row definition and whether S002 is an export duplicate | The case defines one shipment per row and confirms one exact repeated export row. A repeated ID alone would not establish duplication. |
| EDA02 | C — Labels may split one carrier, and the repeated shipment affects row counts | Grouping changes the view only. Confirm the A/a mapping and duplicate rule before interpreting counts as workload. |
| EDA03 | B — The shipment records: labels are consistent and double counting is removed | The same retained shipment times remain. The edit corrects their representation, not delivery performance. |
| EDA04 | C — Unknown pending delivery evidence, with reasons for follow-up retained | Missing and invalid durations do not establish either an on-time or a late outcome. Both shipments remain visible. |
| EDA05 | B — The estimates imply two late classifications; the actual outcomes remain unknown | The 15-hour estimate is not delivery evidence. The reviewed report remains 9/10 known outcomes on time, with 2/12 unknown. |
| EDA06 | C — Retain the confirmed 72-hour delay and investigate the operational event | An IQR flag requests investigation. It is not proof of a recording error. Statistical fences do not replace business validity rules. |
| EDA07 | B — The recorded duration and its classification | Only the recorded duration and resulting service classification changed. Keep the uncapped reviewed data for the evidence-based report. |
| EDA08 | C — Follow up B's two unknown outcomes and the customs event before a carrier decision | The groups are small and differ in coverage; route/SLA context also matters. A PASS check cannot recover missing evidence or establish causation. |

Pingo may shuffle answers; identify the answer text rather than relying on its displayed letter. EDA07 covers the cap comparison; the wrap-up slide shows the access QR. Use EDA01–EDA08 after the notebook exercises. XML structure checked locally; live import remains to be confirmed.