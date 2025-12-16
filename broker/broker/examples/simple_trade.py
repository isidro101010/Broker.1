from broker.core import BrokerEngine, RiskManager, Portfolio, Order
from broker.paper import DictPriceFeed, PaperVenue

feed = DictPriceFeed({
    "AAPL": 200.0,
    "MSFT": 350.0,
})

venue = PaperVenue(feed, slippage_bps=1.0)
risk = RiskManager(max_pos_usd=20_000, max_order_usd=5_000)
portfolio = Portfolio(cash=50_000)

broker = BrokerEngine(feed, venue, risk, portfolio)

order = Order(symbol="AAPL", side="BUY", qty=10)
fill = broker.submit(order)

print("FILL:", fill)
print("CASH:", portfolio.cash)
print("POSITIONS:", portfolio.positions)
print("EQUITY:", portfolio.equity(feed))
