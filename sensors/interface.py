
import subprocess
import re
from .sensors import Sensor
from configparser import NoOptionError

class Interface(Sensor):
  ifconfigRe = re.compile(b'^(?P<name>[a-z][a-z:]+[0-9]*)\s+(.*\n)+?\s+RX bytes:' \
                          b'\s*(?P<in>\d+).*TX bytes:(?P<out>\d+).*$', re.M)

  def __init__(self, config):
    self.config = config
    self.data = {}

  def run(self):
    ifconfig = subprocess.Popen(['/sbin/ifconfig'], stdout=subprocess.PIPE)

    ifconfig.wait()

    interfaces = []

    current = b''
    for line in ifconfig.stdout:
      if line == b'\n':
        interfaces.append(current)
        current = b''
      else:
        current+=line

    for interface in interfaces:
      result = self.ifconfigRe.match(interface)
      
      if result:
        name = result.group('name').decode()
        try:
          self.config.get('interface', name)
          self.data[name] = {'in': result.group('in'), 'out': result.group('out')}
        except NoOptionError:
          pass

  def getlist(self):
    return self.config.options('interface')

if __name__ == "__main__":
  from configparser import SafeConfigParser
  config = SafeConfigParser(allow_no_value=True)
  config.read_string("""
    [interface]
    eth0
    """)
  i = Interface(config)
  i.run()
  print(i.data)
  print(i)
