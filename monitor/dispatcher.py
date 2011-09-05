import hashlib
from configparser import NoOptionError
from socketserver import StreamRequestHandler
from datetime import datetime

class Dispatcher(StreamRequestHandler):
  def log(self, msg):
    print("%s %s" % (datetime.now().isoformat(), msg))

  def boundry(self, item):
    data = "%s-%s-%s" % (datetime.now(), self.client_address[0], item.decode())

    return hashlib.sha1(data.encode()).hexdigest()

  def handle(self):
    self.log("New Connection from %s" % (self.client_address[0],))
    self.active = True

    # Receive the greeting and process it, fail if its wrong
    self.data = self.rfile.readline().strip()
    if not self.data.startswith(b'HELLO'): return

    # Find out who the client claims to be
    (junk, identifier) = self.data.split(b' ')


    self.log("%s identified as %s" % (
                                        self.client_address[0],
                                        identifier.decode())
                                      )

    # Recieve the access code, fail if its wrong or if the cleint didnt ident
    # with as a valid client
    self.data = self.rfile.readline().strip()

    try:
      if not self.server.config.get('authorization', identifier.decode()) == \
             self.data.decode():
        return
    except NoOptionError:
      return

    self.wfile.write(b'OK\n')
    self.wfile.flush()

    while self.active:
      self.data = self.rfile.readline().strip()

      if self.data == b'CLOSE': return
      elif self.data.startswith(b'GET'):
        (junk, item) = self.data.split(b' ')

        key = item.decode().lower()
        if key in self.server.modules.keys():
          self.server.modules[key].reset()
          self.server.modules[key].run()

          boundry = self.boundry(item)

          response = "SENDING %s ----%s----\n" % (key, boundry)
          response+= "%s" % (self.server.modules[key],)
          response+= "\n----%s---- FINISHED\n" % (boundry, )

          self.wfile.write(response.encode())
          self.wfile.flush()
        else:
          self.wfile.write(b'ERROR 100 --- UNKNOWN MODULE\n')
          self.wfile.flush()
      elif self.data.startswith(b'LIST'):
        try:
          (junk, item) = self.data.split(b' ')
        except ValueError:
          self.wfile.write(b'ERROR 200 --- UNKNOWN LIST\n')
        if item == b'ALL':
          boundry = self.boundry(b'list all')

          response = "LIST ALL ----%s----\n" % (boundry, )
          response+= "\n".join(self.server.modules.keys())
          response+= "\n----%s---- FINISHED\n" % (boundry, )

          self.wfile.write(response.encode())
          self.wfile.flush()
        elif item.decode().lower() in self.server.modules.keys():
          boundry = self.boundry(('list %s' % item).encode())

          key = item.decode().lower()

          try:
            response = "LIST %s ----%s----\n" % (key, boundry)
            response+= "\n".join(self.server.modules[key].getlist())
            response+= "\n----%s---- FINISHED\n" % (boundry, )
            self.wfile.write(response.encode())
          except AttributeError as e:
            print(e)
            self.wfile.write(b'ERROR 210 --- MODULE DOSE NOT SUPPORT LIST\n')
          finally:
            self.wfile.flush()
        else:
          self.wfile.write(b'ERROR 200 --- UNKNOWN LIST\n')
          self.wfile.flush()
      else:
        self.wfile.write(b'ERROR 000 -- UNKNOWN COMMAND\n')
        self.wfile.flush()
