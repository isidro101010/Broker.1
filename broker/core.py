from __future__ import annotations
from dataclasses import dataclass
from typing import Dict, Optional, Protocol
import time


@dataclass
class Order:
    symbol: str
    side: str          # "BUY" or "SELL"
    qty: float
    limit_price: Optional[float] = None
    ts: float = time.time()


@dataclass
class Fill:
    symbol: str
    side: str
    qty: float
    price: float
    ts: float


class PriceFeed(Protocol):
    def last(self, symbol: str) -> float:
        ...


class ExecutionVenue(Protocol):
    def place_order(self, order: Order) -> Fill:
        ...


class RiskManager:
    def __init__(self, max_pos_usd: float = 10_000, max_order_usd: float = 2_000):
        self.max_pos_usd = max_pos_usd
        self.max_order_usd = max_order_usd

    def check(self, order: Order, last_price: float, positions: Dict[str, float]) -> None:
        notional = order.qty * last_price
        if notional > self.max_order_usd:
            raise ValueError("Order size exceeds max allowed")

        pos_qty = positions.get(order.symbol, 0.0)
        new_qty = pos_qty + (order.qty if order.side == "BUY" else -order.qty)
        new_notional = abs(new_qty * last_price)

        if new_notional > self.max_pos_usd:
            raise ValueError("Position size exceeds max allowed")


class Portfolio:
    def __init__(self, cash: float = 100_000):
        self.cash = cash
        self.positions: Dict[str, float] = {}

    def on_fill(self, fill: Fill)_



