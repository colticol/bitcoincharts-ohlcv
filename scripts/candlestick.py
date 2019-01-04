class Candlestick(object):
  """CandleStick"""
  def __init__(self, date, prev=None):
    self.date   = date
    self.open   = None
    self.high   = None
    self.low    = None
    self.close  = None
    self.volume = 0.0
    self.prev   = prev

  def set(self, price, volume):
    if self.open is None:
      self.open = price
    if self.high is None or self.high < price:
      self.high = price
    if self.low is None or self.low > price:
      self.low = price
    self.close = price
    self.volume += volume

  def getDate(self):
    return self.date

  def getClose(self):
    return self.close

  def toString(self):
    if self.open is not None:
      return '{0},{1},{2},{3},{4},{5}\n'.format(self.date, self.open, self.high, self.low, self.close, self.volume)
    elif self.prev is not None:
      return '{0},{1},{2},{3},{4},{5}\n'.format(self.date, self.prev, self.prev, self.prev, self.prev, self.volume)
    else:
      return ''
