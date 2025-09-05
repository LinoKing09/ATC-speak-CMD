import colorArt as c

def red(text):
  print(c.color.RED + str(text) + c.color.END)

def yellow(text):
  print(c.color.YELLOW + str(text) + c.color.END)

def green(text):
  print(c.color.GREEN + str(text) + c.color.END)

def cyan(text):
  print(c.color.CYAN + str(text) + c.color.END)

def blue(text,ende="\n"):
  print(c.color.BLUE + str(text) + c.color.END,end=f"{ende}")

def bold(text):
  print(c.color.BOLD + str(text) + c.color.END)