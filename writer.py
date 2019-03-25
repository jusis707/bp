from flask import Flask, request, jsonify
from datetime import datetime
import threading

app = Flask(__name__, static_url_path='')
mydate = datetime.datetime.now()

@app.route('/writetofile', methods=['POST']) 
def printit():
  threading.Timer(5.0, printit).start()
  f=open("/mnt/acs.txt",'a')
  f.write(datetime.datetime.strftime(mydate, '%Y, %m, %d, %H, %M, %S'))
  f.write ("heloo-"+'\t')

printit()

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = False)
