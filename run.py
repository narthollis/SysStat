#!/usr/bin/env python3

import sys
import os

import argparse

if __name__ == "__main__":

  parser = argparse.ArgumentParser(
                                   prog='SysStats',
                                   description='SysStat Control Script',
                                   epilog='Copyright 2011 Nicholas Steicke')
  parser.add_argument('module',
                      metavar='MODULE',
                      type=str,
                      nargs=1,
                      help="Monitor, Communicator or UI")
  parser.add_argument('-c',
                      '--config',
                      metavar='PATH',
                      type=str,
                      nargs=1,
                      help="Path to the config file")

  args = parser.parse_args()
    
  if not args.config:
    config_path = os.path.realpath(os.getenv('SYSSTAT', sys.path[0])) + os.sep
  else:
    config_path = os.path.realpath(args.config) + os.sep

  if not os.path.exists("%s%s.cfg" % (config_path, sys.argv[1])):
    print('The config file could not be found.', file=sys.stderr)
    print('  Please specify it as the 2nd argument,', file=sys.stderr)
    print('  or set the SYSSTAT environment variable', file=sys.stderr)
    print('  or create it along side the executable.', file=sys.stderr)

  if args.module[0] == 'monitor':
    import monitor
    main = monitor.Main(config_path)
    main.run()

  elif args.module[0] == 'communicator':
    import communicator
    main = communicator.Main(config_path)
    main.run()

  elif args.module[0] == 'ui':
    import ui
    main = ui.Main(config_path)
    main.run()
