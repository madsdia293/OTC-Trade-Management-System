import numpy as np
import pandas as pd
from datetime import datetime

class Trade:
    def __init__(self, trade_id, underlying, notional, maturity_date):
        self.trade_id = trade_id
        self.underlying = underlying
        self.notional = notional
        self.maturity_date = maturity_date

    def present_value(self):
        current_date = datetime.now().date()
        maturity_date = datetime.strptime(self.maturity_date, "%Y-%m-%d").date()
        time_to_maturity = (maturity_date - current_date).days / 365.25
        present_value = self.notional * 0.95 
        
        return present_value

    def calculate_pnl(self):
        previous_present_value = 1000000 
        current_present_value = self.present_value()
        pnl = current_present_value - previous_present_value

        return pnl

class TradePortfolio:
    def __init__(self):
        self.trades = []

    def add_trade(self, trade):
        self.trades.append(trade)

    def present_value(self):
        pv = 0
        for trade in self.trades:
            pv += trade.present_value()
        return pv

    def calculate_pnl(self):
        pnl = 0
        for trade in self.trades:
            pnl += trade.calculate_pnl()
        return pnl

portfolio = TradePortfolio()

trade1 = Trade("T1", "ABC Stock", 1000000, "2023-12-31")
trade2 = Trade("T2", "XYZ Stock", 500000, "2024-06-30")

portfolio.add_trade(trade1)
portfolio.add_trade(trade2)

portfolio_pv = portfolio.present_value()
portfolio_pnl = portfolio.calculate_pnl()

print("Portfolio Present Value:", portfolio_pv)
print("Portfolio Profit and Loss:", portfolio_pnl)
