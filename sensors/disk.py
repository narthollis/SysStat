
import subprocess
import re
from .sensors import Sensor
from configparser import NoOptionError

class Disk(Sensor):
  dfRe = re.compile(b'^(?P<device>.*?)\s?\s+\d+\s+(?P<used>\d+)\s+' \
                    + b'(?P<free>\d+)\s+\d+%\s+(?P<mount>.*)$')

  def __init__(self, config):
    self.config = config
    self.data = {}

  def run(self):
    df = subprocess.Popen(['/bin/df'], stdout=subprocess.PIPE)

    df.wait()

    for line in df.stdout:
      result = self.dfRe.match(line)
      
      if result:
        try:
          name = result.group('mount').decode()
          self.config.get('disk', name)
          self.data[name] = {'used': result.group('used'), 'free': result.group('free')}
        except NoOptionError:
          pass

  def getlist(self):
    return self.config.options('disk')

if __name__ == "__main__":
  from configparser import SafeConfigParser
  config = SafeConfigParser(allow_no_value=True)
  config.read_string("""
    [disk]
    /
    """)
  d = Disk(config)
  d.run()
  print(d.data)
  print(d)
