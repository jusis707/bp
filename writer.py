from datetime import datetime
import datetime
import threading
import logging

app = Flask(__name__, static_url_path='')

@@ -12,5 +13,10 @@ def printit():
  f.write(datetime.datetime.now().ctime())
printit()

@app.route('/hello')
def printMsg():
    app.logger.info('testing info log')
    return "HELLO-BP!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = False)
