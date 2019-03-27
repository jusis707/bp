from flask import Flask
import datetime
import threading

app = Flask(__name__, static_url_path='')

def printit():
  threading.Timer(10.0, printit).start()
  f=open("/mnt/stamp.txt",'a')
  f.write ("\nHello-BP\n")
  f.write(datetime.datetime.now().ctime())
printit()

@app.route("/") 
def hello(): 
    return "Hello BP!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = False)
