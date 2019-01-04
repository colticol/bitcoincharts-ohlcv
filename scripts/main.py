# data source : https://api.bitcoincharts.com/v1/csv/
# wget "http://api.bitcoincharts.com/v1/trades.csv?symbol=bitstampUSD"
import sys
from date_assignor import Assignor
from candlestick import Candlestick


def fill_blank(now, candlestick, assignor):
  date = assignor.nextDate(candlestick.getDate())
  out = ''
  while now != date:
    cs = Candlestick(date, candlestick.getClose())
    out += cs.toString()
    date = assignor.nextDate(date)
  return out


def make_csv(f_input, f_output, frequency='1m'):
  assignor = Assignor(frequency)
  candlestick = None
  f_w = open(f_output, 'w')
  for line in open(f_input, 'r'):
    unixtime, price, volume = map(float, line.strip().split(','))
    date = assignor.convertUnixtime(unixtime)
    if candlestick is None:
      candlestick = Candlestick(date)
    elif date != candlestick.getDate():
      f_w.write(candlestick.toString())
      f_w.write(fill_blank(date, candlestick, assignor))
      candlestick = Candlestick(date, candlestick.getClose())
    candlestick.set(price, volume)
  f_w.write(candlestick.toString())
  f_w.close()


if __name__ == '__main__':
  if len(sys.argv) != 4:
    print ('usage : python3 bitcoincharts.py inputfile outputfile frequency')
    print ('You can choose frequencies that is [1m, 3m, 5m, 15m, 30m, 1h, 2h, 4h, 8h, 12h, 1d]')
    sys.exit(1)
  make_csv(sys.argv[1], sys.argv[2], sys.argv[3])
