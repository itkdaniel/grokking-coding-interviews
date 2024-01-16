# vim: set comments=sb\:\"\"\",mb\:##\ \ \ ,ex-3\:\"\"\",fb\:\*,fb\:-,\:##:
# vim: set fo=tcq1rowapn:

import colorama
import random
import time
import sys

colored = colorama.Fore
paint = colorama.Back
colors = [paint.WHITE + colored.BLACK, colored.RED, colored.LIGHTRED_EX, colored.GREEN, colored.LIGHTGREEN_EX, colored.YELLOW, colored.LIGHTYELLOW_EX, colored.BLUE, colored.LIGHTBLUE_EX, colored.MAGENTA, colored.LIGHTMAGENTA_EX, colored.CYAN, colored.LIGHTCYAN_EX, colored.WHITE]

def load(length=25,speed=0.05,factor=4,rand=False):
     """
     Calculating factor:
        if length is 25, then factor is 100/25=4.
        if length is 50, then factor is 100/50=2.
     """
     print(colored.LIGHTYELLOW_EX,'Loading...',colored.RESET)
     for i in range(100):
          time.sleep(speed)
          width = (i+1)//factor
          if rand:
              bar = "[" + random.choice(colors) + "#" * width + " " * (length-width) + colored.RESET + paint.RESET + "]"
          else:
              bar = "[" + colored.LIGHTMAGENTA_EX + "#" * width + " " * (length-width) + colored.RESET + "]"
          sys.stdout.write(u'\x1b[1000D' + bar)
          sys.stdout.write(str(i+1) + "%")
          sys.stdout.flush()
     bar = "[" + colored.LIGHTGREEN_EX + "#" * length + colored.RESET + "]"
     sys.stdout.write(u'\x1b[1000D')
     sys.stdout.write(u'\x1b[0K')
     sys.stdout.write(bar + "100%")
     print()
