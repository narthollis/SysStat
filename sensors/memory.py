
import subprocess
import re
from .sensors import Sensor

class Memory(Sensor):
  freeRe = re.compile(b'^(?P<name>\w+):\s+(?P<total>\d+)\s+(?P<used>\d+)\s+(?P<free>\d+).*$')

  def run(self):
    free = subprocess.Popen(['/usr/bin/free'], stdout=subprocess.PIPE)
    
    free.wait()
    
    for line in free.stdout:
      result = self.freeRe.match(line)

      if result:
        name = 'memory' if result.group('name') == b'Mem' else 'swap'

        self.data[name] = {
          'free': result.group('free'),
          'used': result.group('used'),
          'total': result.group('total'),
        }

if __name__ == "__main__":
  m = Memory({})
  m.run()
  print(m.data)
  print(m)
