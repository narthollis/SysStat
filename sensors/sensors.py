
import simplejson
import datetime
import dateutil.tz

def encode_datetime(obj):
  if isinstance(obj, datetime.datetime):
    return obj.isoformat()
  elif type(obj) == bytes:
    return obj.decode()
  raise TypeError(repr(obj) + " is not JSON serializable")

class Sensor:
  config = None

  def __init__(self, config):
    self.config = config
    self.data = {}

  def reset(self):
    self.data['time'] = datetime.datetime.now(tz=dateutil.tz.tzlocal())
    self.data = {}

  def run(self):
    pass

  def __str__(self):
    return simplejson.dumps(self.data, default=encode_datetime)
