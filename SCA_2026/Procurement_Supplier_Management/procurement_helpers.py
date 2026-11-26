"""Calculations for the synthetic Hof procurement case."""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from IPython.display import display
REVIEW_DATE=pd.Timestamp('2026-06-30')

def prepare(orders):
    d=orders.copy()
    for col in ['PO_Date','Promised_Date','Actual_Receipt_Date']:
        d[col]=pd.to_datetime(d[col],errors='raise')
    d['Lead_Days']=(d.Actual_Receipt_Date-d.PO_Date).dt.days
    d['Days_After_Promise']=(d.Actual_Receipt_Date-d.Promised_Date).dt.days
    return d

def completed(orders):
    return orders.loc[orders.Status.eq('Closed') & orders.Actual_Receipt_Date.notna()].copy()

def supplier_metrics(orders):
    rows=[]
    for supplier,g in completed(orders).groupby('Supplier'):
        received=g.Received_Qty.sum();inspected=g.Inspected_Qty.sum()
        purchase=(g.Received_Qty*g.Unit_Price_EUR).sum()
        extra=g[['Freight_EUR','Inspection_Cost_EUR','Rework_Cost_EUR']].sum().sum()
        rows.append({'Supplier':supplier,'Completed POs':len(g),'Mean days':g.Lead_Days.mean(),
          'Std days':g.Lead_Days.std(ddof=1),'Promised-date OTD %':g.Days_After_Promise.le(0).mean()*100,
          'In-full %':g.Received_Qty.ge(g.Ordered_Qty).mean()*100,
          'Flagged POs':int(g.Defective_Qty.gt(0).sum()),'Flagged PO %':g.Defective_Qty.gt(0).mean()*100,
          'Inspected units':int(inspected),'Defective units':int(g.Defective_Qty.sum()),
          'Defective unit %':g.Defective_Qty.sum()/inspected*100,
          'Purchase EUR/unit':purchase/received,'Recorded cost EUR/unit':(purchase+extra)/received})
    return pd.DataFrame(rows).set_index('Supplier')

def baseline(orders,profiles):
    display(orders.head(3));display(profiles)
    print('Review date: 30 June 2026. Synthetic case: VALVE20, 20 mm brass valve, pieces, EUR.')
    table=orders.groupby(['Supplier','Status']).size().unstack(fill_value=0);display(table)
    open_orders=orders[orders.Status.eq('Open')]
    print(f'Open overdue: {int(open_orders.Promised_Date.lt(REVIEW_DATE).sum())}; open not yet due: {int(open_orders.Promised_Date.ge(REVIEW_DATE).sum())}; receipt unconfirmed: {int(orders.Status.eq("Receipt_unconfirmed").sum())}.')
    print('The completed-order scorecard uses 60 orders per supplier. Open and unconfirmed orders remain in this separate status view.')

def show_delivery(orders,supplier='A'):
    if supplier not in ['A','B']:raise ValueError('Choose A or B.')
    g=completed(orders);m=supplier_metrics(orders)
    display(m.loc[['A','B'],['Completed POs','Mean days','Std days']].round(2))
    fig,ax=plt.subplots(figsize=(8,3));vals=g.loc[g.Supplier.eq(supplier),'Lead_Days']
    ax.hist(vals,bins=np.arange(4.5,14.6,1),color='#5B9BD5',edgecolor='white');ax.set(xlabel='Calendar days from order to receipt',ylabel='Completed orders',title=f'Supplier {supplier}: 60 completed orders',xlim=(4.5,14.5),ylim=(0,26));plt.tight_layout();plt.show()
    print('Both runs use the same date range and fixed plot scales. Standard deviation summarises spread around the mean in days.')
    return m.loc[supplier]

def show_target(orders,target_days=10):
    if target_days not in [10,12]:raise ValueError('Choose 10 or 12 days.')
    g=completed(orders);m=supplier_metrics(orders)
    count=g.groupby('Supplier').Lead_Days.apply(lambda x:int(x.le(target_days).sum()))
    result=pd.DataFrame({'Completed POs':m['Completed POs'],'Within internal target':count,'Within target %':count/m['Completed POs']*100,'Promised-date OTD %':m['Promised-date OTD %']})
    display(result.round(2));result[['Within target %','Promised-date OTD %']].plot.bar(figsize=(8,3),ylim=(0,100),color=['#5B9BD5','#ED7D31']);plt.ylabel('Completed orders (%)');plt.title(f'Internal target: {target_days} calendar days');plt.xticks(rotation=0);plt.tight_layout();plt.show()
    print('The internal target is a hypothetical reporting rule. Original promised dates and actual receipts stay unchanged.')
    return result

def show_quality(orders,view='orders'):
    if view not in ['orders','units']:raise ValueError('Choose orders or units.')
    m=supplier_metrics(orders);display(m[['Completed POs','Flagged POs','Flagged PO %','Inspected units','Defective units','Defective unit %']].round(2))
    col='Flagged PO %' if view=='orders' else 'Defective unit %'
    m[col].plot.bar(figsize=(7,3),color='#5B9BD5',ylim=(0,35 if view=='orders' else 1.4));plt.ylabel(col);plt.title('Orders with any defect' if view=='orders' else 'Defective units among inspected units');plt.xticks(rotation=0);plt.tight_layout();plt.show()
    print('All received units in the closed orders were inspected. A flagged order may contain one or many defective units. Read the axis: the two charts use different scales.')
    return m

def show_cost(orders,basis='purchase'):
    if basis not in ['purchase','recorded']:raise ValueError('Choose purchase or recorded.')
    m=supplier_metrics(orders);display(m[['Purchase EUR/unit','Recorded cost EUR/unit']].round(3))
    col='Purchase EUR/unit' if basis=='purchase' else 'Recorded cost EUR/unit'
    m[col].plot.bar(figsize=(7,3),color='#5B9BD5',ylim=(0,12));plt.ylabel('EUR per received unit');plt.title('Purchase price' if basis=='purchase' else 'Recorded procurement cost');plt.xticks(rotation=0);plt.tight_layout();plt.show()
    print('Recorded cost = purchase + freight + inspection + rework, divided by received units. These case records exclude downtime, financing, administration and later lifecycle costs.')
    return m

def screen_suppliers(orders,profiles,max_defective_pct=1.0):
    if max_defective_pct not in [1.0,.5]:raise ValueError('Choose 1.0 or 0.5 percent.')
    m=supplier_metrics(orders).join(profiles.set_index('Supplier'))
    m['Approved']=m.Qualification.eq('Approved');m['Delivery passes']=m['Promised-date OTD %'].ge(85);m['Quality passes']=m['Defective unit %'].le(max_defective_pct)
    m['Eligible']=m[['Approved','Delivery passes','Quality passes']].all(axis=1)
    display(m[['Qualification','Promised-date OTD %','Defective unit %','Available_Capacity_July_units','Delivery passes','Quality passes','Eligible']].round(2))
    capacity=int(m.loc[m.Eligible,'Available_Capacity_July_units'].sum());need=9000
    print(f'July requirement: {need:,} units. Eligible capacity: {capacity:,}. Capacity gap: {max(0,need-capacity):,}.')
    print('Hypothetical buyer rules: Approved, promised-date OTD at least 85%, and the chosen defective-unit ceiling. Capacity is assumed available for July, not an allocation recommendation.')
    print('A follow-up should identify the failed criterion, request evidence and agree a measurable review. Changing a rule does not improve a supplier.')
    return m
