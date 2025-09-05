import logln
mode =True

def write(*message, type="info"):
  if mode == True:
    message_str = " ".join(str(msg) for msg in message)
    if type == "info":
      logln.yellow(message_str)
    elif type == "debug":
      logln.blue(message_str)
    elif type == "error":
      logln.red(message_str)