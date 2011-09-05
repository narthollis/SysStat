
import socketserver
import ssl

class Server(socketserver.TCPServer):

  def __init__(self, config, dispatcher, bind_and_activate=True):

    self.config  = config
    self.modules = {}

    server_address = (
      self.config.get('listen', 'host'),
      self.config.getint('listen', 'port')
    )

    socketserver.TCPServer.__init__(self,
                                    server_address,
                                    dispatcher,
                                    bind_and_activate=False)

    if config.getboolean('ssl', 'use'):
      self.socket = ssl.wrap_socket(self.socket,
                                    certfile = self.config.get('ssl', 'cert'),
                                    keyfile  = self.config.get('ssl', 'key'),
                                    ssl_version=ssl.PROTOCOL_TLSv1)

    if bind_and_activate:
      self.server_bind()
      self.server_activate()

  def server_activate(self):
    if self.config.getboolean('modules', 'cpu'):
      from sensors.cpu import Cpu
      self.modules['cpu'] = Cpu(self.config)

    if self.config.getboolean('modules', 'disk'):
      from sensors.disk import Disk
      self.modules['disk'] = Disk(self.config)

    if self.config.getboolean('modules', 'interface'):
      from sensors.interface import Interface
      self.modules['interface'] = Interface(self.config)

    if self.config.getboolean('modules', 'memory'):
      from sensors.memory import Memory
      self.modules['memory'] = Memory(self.config)

    socketserver.TCPServer.server_activate(self)
