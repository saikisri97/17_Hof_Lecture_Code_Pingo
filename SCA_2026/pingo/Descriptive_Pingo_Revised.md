# Descriptive analytics: revised Pingo questions

Instructor copy. These questions refer to the adapted notebook, seed 42, and the specified target settings. Classroom OTIF means meeting SLA; completeness is not modeled. All scenarios independently start from the original baseline. Correct answer positions remain **A, B, B, B, C**, matching the supplied PDF. Upload/update these manually in Pingo; the live question bank has not been changed.

## Q1 — Mode mix
After changing Road/Air/Sea probabilities from 60%/15%/25% to 35%/40%/25%, what happens to **overall average lead time and average cost per shipment in this simulation**?

A. Average lead time decreases and average cost increases.
B. Average lead time increases and average cost decreases.
C. Both average lead time and average cost decrease.
D. Neither average lead time nor average cost changes.

**Correct: A.** Air replaces some Road probability, while Sea probability is fixed. The executed simulation determines the reported result. This is not a guarantee for every transport network, and it does not imply that OTIF improves.

## Q2 — Road SLA
In the provided dataset, Road SLA changes from 6 to 5 days while actual lead times and costs remain fixed. What happens to **overall simplified OTIF**?

A. It increases because Road shipments become faster.
B. It decreases because some previously on-time Road shipments miss the stricter deadline.
C. It stays unchanged because SLA is not used in the calculation.
D. It becomes 100% because the deadline is shorter.

**Correct: B.** The threshold changes; physical delivery performance does not. Shipments with lead time >5 and <=6 days change classification. In other datasets, tightening SLA could leave OTIF unchanged if no shipment crosses the threshold.

## Q3 — Cost volatility
Each shipment's cost is multiplied by an independently sampled factor between 0.8 and 1.2. Lead times, SLAs and transport modes remain fixed. Which statement is correct?

A. Average cost must increase by exactly 20%.
B. Shipment costs change, but average cost need not rise by 20%; lead time and OTIF stay unchanged.
C. Deliveries become up to 20% faster.
D. The share of Air shipments must increase.

**Correct: B.** Positive and negative percentage shocks are possible. The finite-sample average cost can increase or decrease. This exercise models cost uncertainty; it does not change service performance.

## Q4 — Lead-time cap
In the provided baseline, we replace each lead time with `min(original lead time, 10 days)` and recompute simplified OTIF using each mode's unchanged SLA. What happens?

A. Overall OTIF decreases.
B. Overall OTIF increases, although this artificial transformation does not establish a feasible operational improvement.
C. Overall OTIF remains unchanged.
D. Lead-time records become missing.

**Correct: B.** Some late Sea shipments become on-time. Road and Air still have SLAs below 10 days, so the cap does not guarantee 100% overall OTIF. Raw lead times are retained separately. No resource or extra cost model justifies the transformation as a real intervention.

## Q5 — Rail
We keep the original 600 shipments and add 120 Rail shipments using a cost rate of EUR 0.80/km, base lead time of 8 days and SLA of 10 days. Which conclusion is justified?

A. The experiment proves total transport spending falls.
B. The experiment proves Rail is best for every shipment.
C. Rail has an intermediate assumed cost/speed profile relative to Road and Sea, but adding volume does not isolate the effect of replacing an existing mode.
D. The dataset remains at 600 shipments.

**Correct: C.** The dataset grows to 720. Total spend includes the additional shipments. Use per-shipment and per-mode measures to describe the enlarged portfolio. Keep shipment volume and shipment characteristics fixed in a separate substitution comparison.

## Classroom use

Complete the baseline and Experiments 1–5 in order. Then use Pingo Q1–Q5 to review the corresponding experiments. Students should see each experiment before answering its question.
