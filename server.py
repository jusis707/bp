import time
starttime=time.time()
while True:
  print "Hello world"
  time.sleep(3.0 - ((time.time() - starttime) % 3.0))
