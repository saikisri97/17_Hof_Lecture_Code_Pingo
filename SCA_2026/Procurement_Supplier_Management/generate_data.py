"""Deterministic synthetic procurement case. Run from the chapter directory."""
from pathlib import Path
import pandas as pd
ROOT=Path(__file__).resolve().parent
OUT=ROOT/'data';OUT.mkdir(exist_ok=True)
patterns={'A':[9,9,10,10,10,10,11,11,11,12], 'B':[5,6,7,8,9,9,10,11,12,13], 'C':[7,8,9,10,10,11,12,13,14,16]}
price={'A':9.,'B':10.,'C':9.5};promise={'A':11,'B':12,'C':10};freight={'A':1.2,'B':.2,'C':.6};inspection={'A':.3,'B':.1,'C':.2}
rows=[]
for supplier in 'ABC':
 for i in range(60):
  date=pd.Timestamp('2026-01-02')+pd.Timedelta(days=i*2)
  qty=[400,500,600][i%3];short=20 if i<{'A':3,'B':1,'C':6}[supplier] else 0;received=qty-short
  flagged=i<{'A':12,'B':6,'C':18}[supplier];defective=({'A':6,'B':30,'C':20}[supplier] if flagged else 0)
  actual=date+pd.Timedelta(days=patterns[supplier][i%10]);promised=date+pd.Timedelta(days=promise[supplier])
  rows.append(dict(PO_ID=f'{supplier}-{i+1:03}',Supplier=supplier,Product_Code='VALVE20',Product='20 mm brass valve',Unit='piece',Currency='EUR',PO_Date=str(date.date()),Promised_Date=str(promised.date()),Actual_Receipt_Date=str(actual.date()),Status='Closed',Ordered_Qty=qty,Received_Qty=received,Inspected_Qty=received,Defective_Qty=defective,Unit_Price_EUR=price[supplier],Freight_EUR=round(received*freight[supplier],2),Inspection_Cost_EUR=round(received*inspection[supplier],2),Rework_Cost_EUR=defective*8))
 for j,(status,order,promised) in enumerate([('Open','2026-06-01','2026-06-15'),('Open','2026-06-25','2026-07-08'),('Receipt_unconfirmed','2026-05-20','2026-06-02')],61):
  rows.append(dict(PO_ID=f'{supplier}-{j:03}',Supplier=supplier,Product_Code='VALVE20',Product='20 mm brass valve',Unit='piece',Currency='EUR',PO_Date=order,Promised_Date=promised,Actual_Receipt_Date=None,Status=status,Ordered_Qty=500,Received_Qty=None,Inspected_Qty=None,Defective_Qty=None,Unit_Price_EUR=price[supplier],Freight_EUR=None,Inspection_Cost_EUR=None,Rework_Cost_EUR=None))
d=pd.DataFrame(rows);d.to_csv(OUT/'procurement_orders.csv',index=False)
pd.DataFrame([['A','Approved',8000],['B','Approved',6000],['C','Conditional',12000]],columns=['Supplier','Qualification','Available_Capacity_July_units']).to_csv(OUT/'supplier_profile.csv',index=False)
print(f'Created {len(d)} synthetic order records; review date 2026-06-30.')
