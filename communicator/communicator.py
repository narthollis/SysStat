#!/usr/bin/env python3

class Main:
  def __init__(self):
    self.config_path = os.path.realpath(os.getenv('SYSSTATS', sys.path[0]))
    self.config_path+= os.sep

    self.config = SafeConfigParser(allow_no_value=True)
    self.config.read(os.path.realpath(sys.path[0]) + os.sep + 'default.cfg')
    self.config.read(self.config_path + 'sysstats.cfg')

  def run(self):
    pass


if __name__ == "__main__":
  main = Main()
  main.run()

