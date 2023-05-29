# OTC Trade Management System

This Trade Portfolio Management System is a Python implementation that allows you to manage a collection of trades and calculate their present value and profit and loss (P&L).

## Features

- Create individual trades with unique identifiers, underlying assets, notional amounts, and maturity dates.
- Calculate the present value of each trade based on the current date and time to maturity.
- Calculate the P&L of each trade based on the previous present value.
- Create a portfolio to manage multiple trades.
- Add trades to the portfolio and calculate the aggregate present value and P&L.
- Easily extend the system by adding new trades and customizing calculations.

## Getting Started

To get started with the OTC Trade Management System, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/madsdia293/otc-trade-management-system.git
   
2. Navigate to the project directory:
   
   cd otc-trade-management-system
   
3. Install the required dependencies. Ensure that you have Python (version 3.11) and pip installed. Then run:

   pip install -r requirements.txt
   
4. Open the main.py file and modify it according to your trade requirements.

5. Run thr code:

   python main.py
 
 
## Steps left to finish:  
   
- Add additional trade attributes such as trade date, settlement date, trade type, etc.
- Implement data persistence by storing trades and portfolios in a database.
- Integrate with external APIs (polygon.io) for real-time market data.
- Integrate with external APIs (exchangeratesapi.io) for currency exchange rate data.
- Implement risk calculations and risk metrics.
- Add a user interface for easier interaction and visualization of trade and portfolio data.
