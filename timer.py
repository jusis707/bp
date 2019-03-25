import threading
import datetime

def printit():
  threading.Timer(5.0, printit).start()
  f=open("/tmp/acs.txt",'a')
  f.write ("heloo"+'\t')
  f.write(datetime.datetime.now().ctime())

printit()
