#!/usr/bin/env python3
"""Transparent example calculator for the research note; not an order simulator.

Run: python tools/tp_accounting_example.py
The 0.07 fee rate is an illustrative assumption from the reviewed report/prototype.
"""
from math import sqrt

STAKE = 1.00
ENTRY_PRICE = 0.20
FEE_RATE = 0.07
TARGET_NET_PROFIT = 0.95
STARTING_BALANCE = 4.77

shares = STAKE / ENTRY_PRICE
entry_fee = shares * FEE_RATE * ENTRY_PRICE * (1 - ENTRY_PRICE)
initial_cash_outflow = STAKE + entry_fee
required_net_sale_proceeds = initial_cash_outflow + TARGET_NET_PROFIT

# Net sale proceeds = shares*q - shares*fee_rate*q*(1-q)
# Solve fee_rate*q**2 + (1-fee_rate)*q - entry_price*required_net_sale_proceeds = 0.
a = FEE_RATE
b = 1 - FEE_RATE
c = -ENTRY_PRICE * required_net_sale_proceeds
exit_price = (-b + sqrt(b * b - 4 * a * c)) / (2 * a)
gross_sale_proceeds = shares * exit_price
exit_fee = shares * FEE_RATE * exit_price * (1 - exit_price)
net_sale_proceeds = gross_sale_proceeds - exit_fee
net_pnl = net_sale_proceeds - initial_cash_outflow
ending_balance = STARTING_BALANCE - initial_cash_outflow + net_sale_proceeds
full_loss_if_position_settles_worthless = initial_cash_outflow
break_even_win_rate = full_loss_if_position_settles_worthless / (full_loss_if_position_settles_worthless + TARGET_NET_PROFIT)

print(f"Shares: {shares:.4f}")
print(f"Entry fee: {entry_fee:.4f} USDC")
print(f"Initial cash outflow: {initial_cash_outflow:.4f} USDC")
print(f"Required net sale proceeds (after exit fees): {required_net_sale_proceeds:.4f} USDC")
print(f"Modelled exit price under the stated fee formula: {exit_price:.6f}")
print(f"Gross sale proceeds: {gross_sale_proceeds:.6f} USDC")
print(f"Exit fee: {exit_fee:.6f} USDC")
print(f"Net sale proceeds: {net_sale_proceeds:.4f} USDC")
print(f"Net P&L: {net_pnl:+.4f} USDC")
print(f"Balance: {STARTING_BALANCE:.4f} -> {ending_balance:.4f} USDC")
print(f"Simplified binary payoff break-even win rate: {break_even_win_rate:.4%}")

assert abs(entry_fee - 0.056) < 1e-9
assert abs(initial_cash_outflow - 1.056) < 1e-9
assert abs(required_net_sale_proceeds - 2.006) < 1e-9
assert abs(net_pnl - TARGET_NET_PROFIT) < 1e-9
assert abs(ending_balance - 5.72) < 1e-9
assert abs(break_even_win_rate - 0.52642) < 0.0001
