#!/usr/bin/env python3

import sys
import os

import argparse

if __name__ == "__main__":

  args = argparse.ArgumentParser(description='SysStat Control Script',
                                epilog='Copyright 2011 Nicholas Steicke')
  parser.add_argument('module', metavar='MODULE', type=str, nargs=1, 
                     help="Monitor, Communicator or UI")
  parser.add_argument('-c', '--config', metavar='PATH', type=str, nargs=1,
                     help="Path to the config file")

  config_path = os.path.realpath(os.getenv('SYSSTAT', sys.path[0])) + os.sep

  
  config_path = os.path.realpath(sys.argv[2]) + os.sep

  if not os.path.exists("%s%s.cfg" % (config_path, sys.argv[1])):
    print('The config file could not be found.', sys.stderr)
    print('  Please specify it as the 2nd argument,', sys.stderr)
    print('  or set the SYSSTAT environment variable', sys.stderr)
    print('  or create it along side the executable.', sys.stderr)

  if sys.argv[1] == 'monitor':
    import monitor
    main = monitor.Main(config_path)
    main.run()

  elif sys.argv[1] == 'communicator':
    import communicator
    main = communicator.Main(config_path)
    main.run()

  elif sys.argv[1] == 'ui':
    import ui
    main = ui.Main(config_path)
    main.run()
