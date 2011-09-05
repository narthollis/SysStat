
import subprocess
import re
from .sensors import Sensor

class Cpu(Sensor):
  mpstatRe = re.compile(b'^.*all\s+(?P<usr>\d+\.\d+)\s+(?P<nice>\d+\.\d+)\s+' \
                 b'(?P<sys>\d+\.\d+)\s+(?P<iowait>\d+\.\d+)\s+(?P<irq>\d+' \
                 b'\.\d+)\s+(?P<soft>\d+\.\d+)\s+(?P<steal>\d+\.\d+)\s+' \
                 b'(?P<guest>\d+\.\d+)\s+(?P<idle>\d+\.\d+).*$')

  uptimeRe = re.compile(b'^.*load average:\s+(?P<one>\d+\.\d+),\s+(?P<ten>\d+'\
                 b'\.\d+),\s+(?P<fifteen>\d+\.\d+).*$')

  def run(self):
    mpstat = subprocess.Popen(['/usr/bin/mpstat'], stdout=subprocess.PIPE)
    uptime = subprocess.Popen(['/usr/bin/uptime'], stdout=subprocess.PIPE)
    
    mpstat.wait()
    uptime.wait()
    
    for line in mpstat.stdout:
      result = self.mpstatRe.match(line)

      if result:
        self.data['usr'] = result.group('usr')
        self.data['nice'] = result.group('nice')
        self.data['sys'] = result.group('sys')
        self.data['iowait'] = result.group('iowait')
        self.data['irq'] = result.group('irq')
        self.data['soft'] = result.group('soft')
        self.data['steal'] = result.group('steal')
        self.data['guest'] = result.group('guest')
        self.data['idle'] = result.group('idle')

    for line in uptime.stdout:
      result = self.uptimeRe.match(line)

      if result:
        self.data['loadavg_1'] = result.group('one')
        self.data['loadavg_5'] = result.group('ten')
        self.data['loadavg_15'] = result.group('fifteen')

if __name__ == "__main__":
  c = Cpu({})
  c.run()
  print(c.data)
  print(c)
