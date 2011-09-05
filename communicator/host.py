import uuid
import importlib
import sensors

class Host:
  dbid = 0
  host = ('localhost', 37585)
  name = 'Localhost'
  uuid = uuid.uuid1()
  key  = 'LocalHostIsASecureHost'

  db = None

  modules = []

  def __init__(self, dbid, name, host, key, uuidstr, database):
    self.dbid = dbid
    self.name = name
    if not (type(host) == tuple or type(host) == list):
      raise TypeError("Host should be a tuple containing address and port.")
    if not type(host[1]) == int:
      raise TypeError("Port should be an int.")
    self.host = tuple(host)

    self.uuid = uuid.UUID(uuidstr)
    self.key  = key

    self.db = database

    self.getModules()

  def getModules(self):
    with self.db.cursor() as cur:
      cur.execute(b"SELECT `module`, `status` FROM `enalbed_module`" +
                  b" WHERE `host_id` = ? ", (self.dbid,))

      for row in cur:
        print(row)

        if row[1]:
          try:
            importlib.import_module(row[0], 'sensors')

            print(row[2])
          except Exception as e:
            print(e)
