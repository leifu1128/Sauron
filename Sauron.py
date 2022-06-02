class Event(object):
    pass


class MarketEvent(Event):
    def __init__(self):
        self.type = 'MARKET'
