from flask import Flask, request, jsonify
from datetime import datetime
import datetime
import threading

app = Flask(__name__, static_url_path='')

def printit():
  threading.Timer(5.0, printit).start()
  f=open("/mnt/stamp.txt",'a')
  f.write ("\nHello-BP\n")
  f.write(datetime.datetime.now().ctime())

  
printit()

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = False)
