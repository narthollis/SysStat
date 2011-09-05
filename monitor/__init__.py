#!/usr/bin/env python3

import sys
import os
from configparser import SafeConfigParser

from .server import Server
from .dispatcher import Dispatcher

class Main:
  default_config = "%s%smonitor%sdefault.cfg" % (
                      os.path.realpath(sys.path[0]),
                      os.sep,
                      os.sep
                    )


  def __init__(self, config_path):
    self.config_path = config_path

    self.config = SafeConfigParser(allow_no_value=True)

    self.config.read(self.default_config)
    self.config.read(self.config_path + 'monitor.cfg')

  def run(self):
    self.server = Server(self.config, Dispatcher)
    try:
      self.server.serve_forever()
    except KeyboardInterrupt:
      self.server.shutdown()


__all__ = [Main, Server, Dispatcher]

if __name__ == '__main__':

  config_path = os.path.realpath(os.getenv('SYSSTATS', sys.path[0])) + os.sep

  main = Main(config_path);
  main.run()

