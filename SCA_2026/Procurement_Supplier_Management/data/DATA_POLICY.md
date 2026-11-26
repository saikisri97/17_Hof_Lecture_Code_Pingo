# Dataset policy and assumptions

This is a deterministic synthetic classroom case, version 1.0. It does not represent a real company or suppliers. The earlier procurement_po_data.csv is preserved separately as a source reference and is not used in the new exercises.

## Population and timing
The snapshot is at 30 June 2026. One order purchases VALVE20, a 20 mm brass valve, in pieces, EUR. There are 189 unique orders:60 closed per supplier plus one open overdue, one open not yet due and one receipt-unconfirmed record per supplier. Closed order dates span 2 January–30 April 2026. Receipt is a single final delivery. On short closed orders, the unreceived balance is cancelled. This case has no partial-delivery event history.

Supplier A’s lead-time pattern is 9,9,10,10,10,10,11,11,11,12 days; B’s is 5,6,7,8,9,9,10,11,12,13; C’s is 7,8,9,10,10,11,12,13,14,16. Each pattern repeats six times. Promised lead times are 11,12,10 calendar days respectively. These engineered patterns support comparisons; they are not fitted distributions or forecasts.

## Quantities and quality
Ordered quantities cycle 400,500,600. A’s first 3, B’s first 1 and C’s first 6 orders are 20 units short. All received units in closed orders are inspected. The first 12 A orders have 6 defective units each; the first 6 B orders have 30 each; the first 18 C orders have 20 each. The arrangement deliberately separates incident frequency from defective-unit proportion. Defects are first-inspection failures, all successfully reworked in this case. There are no refunds or scrapped units. Outcomes of open/unconfirmed orders remain blank, not zero.

## Cost boundary
Prices are EUR 9.00(A),10.00(B),9.50(C) per received piece. Freight rates are 1.20,0.20,0.60 and inspection rates 0.30,0.10,0.20 per received piece. Rework costs EUR 8 per defective unit. Amount columns are per order and do not include each other. Recorded cost is total purchase plus freight, inspection and rework divided by total received units. Purchase means are quantity-weighted. The case excludes taxes, downtime, financing, administration and lifecycle costs; it is not a full total-cost-of-ownership measure. These costs are scenario inputs, not market benchmarks.

## Delivery and status denominators
Completed-order OTD is closed known receipts on/before their own promised date divided by closed known receipts. In-full compares received and ordered quantities. The common internal 10/12-day target is a separate buyer rule and never overwrites promised dates. The three open overdue records need action and are shown separately; completed-order OTD is not a measure of all outstanding commitments. Unconfirmed records require source follow-up.

## Supplier screening
A/B are Approved and C is Conditional for this component. Hypothetical July available capacities are 8,000/6,000/12,000 units. No other commitments reduce those available quantities in the scenario. The buyer’s 9,000-unit need is a separate hypothetical requirement, not mechanically derived from the previous chapter’s sales dataset. Screening requires Approved status, at least 85% completed-order promised-date OTD and at most the chosen defective-unit percentage. The quality ceiling changes 1.0→0.5 percent, not a fraction. Historical performance, approval and capacity do not change. Capacity is summed only over eligible suppliers. No order allocation is optimised or recommended.

## Reproducibility
Run generate_data.py from any directory to reproduce both CSVs. The notebooks embed identical CSV text as a standalone fallback. They use adjacent data files when present. Raw records are copied before derivation. All task variants read the same prepared data independently.
