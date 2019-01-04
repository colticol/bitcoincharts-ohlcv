import sys
from datetime import datetime, timedelta


class Assignor(object):
  """Date(index) Assignor"""
  def __init__(self, frequency):
    self.frequency_unit = frequency[-1]
    self.frequency_num = int(frequency[:-1])
    if 'm' in self.frequency_unit:
      self.timeformat = '%Y-%m-%d %H:%M'
    elif 'h' in self.frequency_unit:
      self.timeformat = '%Y-%m-%d %H:00'
    elif 'd' in self.frequency_unit:
      self.timeformat = '%Y-%m-%d 00:00'
    else:
      print ('invalid frequency [{0}]'.format(frequency))
      sys.exit(1)

  def convertUnixtime(self, unixtime):
    t = datetime.fromtimestamp(unixtime)
    if 'm' in self.frequency_unit:
      out = datetime(t.year, t.month, t.day, t.hour, int(t.minute / self.frequency_num) * self.frequency_num)
    elif 'h' in self.frequency_unit:
      out = datetime(t.year, t.month, t.day, int(t.hour / self.frequency_num) * self.frequency_num)
    elif 'd' in self.frequency_unit:
      out = datetime(t.year, t.month, int(t.day / self.frequency_num) * self.frequency_num)
    else:
      print ('invalid frequency unit [{0}]'.format(self.frequency_unit))
      sys.exit(1)
    return out.strftime(self.timeformat)

  def nextDate(self, date):
    t = datetime.strptime(date, self.timeformat)
    if 'm' in self.frequency_unit:
      out = t + timedelta(minutes=self.frequency_num)
    elif 'h' in self.frequency_unit:
      out = t + timedelta(hours=self.frequency_num)
    elif 'd' in self.frequency_unit:
      out = t + timedelta(days=self.frequency_num)
    else:
      print ('invalid frequency unit [{0}]'.format(self.frequency_unit))
      sys.exit(1)
    return out.strftime(self.timeformat)
