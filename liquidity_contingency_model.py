# This is my academic project in Funding Concentration and Liquidity Runoff.
# Tried applying Actuarial Science risk theory to wholesale banking liquidity stress testing:

import numpy as np
import pandas as pd

def analyze_liquidity_contingency():
    # pull in the basic csv data file we made
    try:
        df = pd.read_csv('funding_sources.csv')
    except:
        print("Error: cant find the csv file anywhere")
        return

    print("--- Running Funding Concentration and Liquidity Contingency Model ---")
    
    total_funding = df['Committed_Amount'].sum()
    herfindahl_index = 0.0
    total_stress_outflow = 0.0
    
    # baseline cash we keep under the mattress for emergencies (HQLA)
    emergency_cash_reserve = 550000000 

    for idx, row in df.iterrows():
        provider = row['Funding_Provider']
        amount = row['Committed_Amount']
        runoff_rate = row['Stress_Runoff_Pct']
        
        # find the percentage share of total funding for this specific group
        funding_share = amount / total_funding
        
        # calculate HHI index to check for bad concentration
        # if this score gets too high it means we rely way too much on just 1 or 2 guys
        herfindahl_index += (funding_share * 100) ** 2
        
        # figure out how much money vanishes if a market freeze hits tomorrow
        provider_outflow = amount * runoff_rate
        total_stress_outflow += provider_outflow

    # see what cash is left over after the big panic run
    net_liquidity_position = emergency_cash_reserve - total_stress_outflow

    # print the metrics to screen
    print(f"Total Wholesale Funding Portfolio:  ${total_funding:,.2f}")
    print(f"Calculated Funding Concentration HHI: {herfindahl_index:.2f}")
    print(f"Initial Emergency Cash Reserve:     ${emergency_cash_reserve:,.2f}")
    print("---------------------------------------------------------")
    print(f"Stress Scenario: Systemic Liquidity Contingency Event")
    print(f"Total Simulated Cash Runoff (Drain): ${total_stress_outflow:,.2f}")
    print(f"Net Post-Stress Cash Surplus/Deficit: ${net_liquidity_position:,.2f}")
    print("---------------------------------------------------------")
    
    if herfindahl_index > 2500:
        print("Risk Alert: Portfolio is highly concentrated. Vulnerable to single-funder flight.")
    else:
        print("Concentration Profile: Well diversified across funding structures.")
        
    if net_liquidity_position < 0:
        print("Contingency Signal: Emergency cash depleted. Contingency Funding Plan (CFP) must activate.")
    else:
        print("Contingency Signal: Emergency cash cushion successfully absorbed the runoff shock.")

if __name__ == "__main__":
    analyze_liquidity_contingency()
