import time
from typing import Dict
from .core import Order, Fill


class DictPriceFeed:
    def __init__(self, prices: Dict[str, float]):
        self.prices = prices

    def last(self, symbol: str) -> float:
        return float(self.prices[symbol])


class PaperVenue:
    def __init__(self, feed: DictPriceFeed, slippage_bps: float = 2.0):
        self.feed = feed
        self.slippage_bps = slippage_bps

    def place_order(self, order: Order) -> Fill:
        px = self.feed.last(order.symbol)

        slip = px * (self.slippage_bps / 10_000.0)
        px = px + slip if order.side == "BUY" else px - slip

        return Fill(
            symbol=order.symbol,
            side=order.side,
            qty=order.qty,
            price=px,
            ts=time.time(),
        )
