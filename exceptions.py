
class Error(Exception):
  code    = None
  name    = None
  message = None

  def __str__(self):
    return "ERROR: %s %s\n%s" % (
              self.code.decode(),
              self.name.decode(),
              self.message.decode()
           )

class UnknownCommand(Error):
  code    = b"000"
  name    = b"UNKNOWN COMMAND"
  message = b"The requested command is not understood by the server."

class UnknownModule(Error):
  code    = b"100"
  name    = b"UNKNOWN MODULE"
  message = b"The requested module can not be found."

class UnknownList(Error):
  code    = b"200"
  name    = b"UNKNOWN LIST"
  message = b"The requested list could not be found."

class ListNotSupported(Error):
  code    = b"210"
  name    = b"LIST NOT SUPPORTED"
  message = b"The specified module does not suppor the list command."

__all__ = [
  UnknownCommand,
  UnknownModule,
  UnknownList,
  ListNotSupported
]

