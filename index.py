from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
    return "Hello World!"
    fo= open("test.txt", "w")
    filebuffer = ["brave new world"]
    fo.writelines(filebuffer)
    fo.close()
    


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("5000"), debug=True)
