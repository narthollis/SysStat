
class SysStatError(Exception):
  code    = b"000"
  name    = b"UNKNOWN COMMAND"
  message = b"The requested command is not understood by the server"

  def __str__(self):
    return "ERROR: %s %s\n%s" % (
              self.code.decode(),
              self.name.decode(),
              self.message.decode()
           )

class SysStat
