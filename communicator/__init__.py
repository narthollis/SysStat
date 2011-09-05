#!/usr/bin/env python3

import os
from configparser import SafeConfigParser
import oursql

from .host import Host

class Main:
  config = None
  db     = None
  hosts  = []

  def __init__(self, config_path):

    self.config = SafeConfigParser(allow_no_value=False)
    self.config.read(config_path + os.sep + 'communicator.cfg')

    self.db = oursql.Connection(
                                host=self.config.get('database', 'host'),
                                port=self.config.getint('database', 'port'),
                                user=self.config.get('database', 'username'),
                                passwd=self.config.get('database', 'password'),
                                db=self.config.get('database', 'dbname'),
                                charset="utf8")

  def getHosts(self):
    with self.db.cursor() as cur:
      cur.execute(b'SELECT `id`, `name`, `address`, `port`, `key`, `uuid`' +
                  b' FROM `host` WHERE `active`', plain_query=True)

      for row in cur:
        self.hosts.append(Host(
                          row[0],
                          row[1],
                          (row[2], row[3]),
                          row[4],
                          row[5],
                          self.db)
                    )

  def run(self):
    self.getHosts()


if __name__ == "__main__":
  from os.path import dirname, realpath
  main = Main(realpath('../'))
  main.run()
