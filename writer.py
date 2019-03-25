from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__, static_url_path='')

@app.route('/writetofile', methods=['POST']) 
def log_feedback():
    with open("/mnt/hello-bp.txt","a") as fo:
        fo.write(request.data.decode("utf-8"))
        print(request.data.decode("utf-8"))
        fo.write('\n')
    return 'Got it!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = False)
