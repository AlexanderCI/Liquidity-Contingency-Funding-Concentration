### Wholesale Funding Concentration and Liquidity Runoff Model

Hey guys, this project applies concentration metrics and runoff probability frameworks to wholesale banking liquidity risk management. As you can probably tell, I have a strong interest in Liquidity!

The model evaluates a structural banking book exposure where an institution is reliant on highly concentrated wholesale funding blocks, and simulates a sudden liquidity crisis where those sources refuse to roll over short-term liabilities.

### Important notes:
* Computes a Herfindahl-Hirschman Index (HHI) value to quantify the bank's funding source concentration.
* Models specific cash runoff percentages across different wholesale funding counterparty types during a market freeze.
* Compares the aggregated stress cash drain against emergency cash reserves to test if Contingency Funding Plans (CFP) are triggered.

