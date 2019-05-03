from flask import Flask
app = Flask(__name__)

@app.route("/")
def run():
    return "Main!!"

@app.route("/test/")
def test():
    return "test"

@app.route("/test2/")
def test2():
    return "test2"

if __name__ == "__main__":
    app.run()
