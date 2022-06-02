class Event(object):
    pass


class MarketEvent(Event):
    def __init__(self):
        self.type = 'MARKET'


class OrderEvent(Event):
    def __init__(self, asset_type, ticker, order_type, quantity, price, direction, underlying):
        """
        Parameters:
        :param asset_type: Type of asset, Equity: 'E', Option: 'O', Future: 'F'
        :param ticker: Ticker symbol of asset
        :param order_type: Type of order, Market: 'MKT', Limit: 'LMT'
        :param quantity: Quantity traded, non-negative integer
        :param price: Price at which order was placed
        :param direction: Direction of trade, Long: 'BUY', Short: 'SELL'
        :param underlying: If derivative, ticker of underlying asset
        """

        self.type = 'ORDER'
        self.asset_type = asset_type
        self.ticker = ticker
        self.order_type = order_type
        self.quantity = quantity
        self.price = price
        self.direction = direction
        self.underlying = underlying

    def print_order(self):
        if self.asset_type == "E":
            print("Order: %s %s %s %s" % (self.ticker, self.order_type, self.quantity, self.direction))

        else:
            print("Order: %s %s %s %s %s" % \
                  (self.ticker, self.order_type, self.quantity, self.direction, self.underlying))


class FillEvent(Event):
    def __init__(self, time_index, ticker, quantity, price, type):
        """
        Parameters:
        :param time_index: The bar-resolution when the order was filled
        :param ticker: The ticker that was filled
        :param quantity: The quantity that was filled
        :param price: The price at which the order was filled
        :param type: Type of liquidity effect, Added: 'ADD', Removed: 'TAKE'
        """
        self.type = 'FILL'
        self.time_index = time_index
        self.ticker = ticker
        self.quantity = quantity
        self.price = price
        self.type = type
