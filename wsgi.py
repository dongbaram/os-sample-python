from flask import Flask
application = Flask(__name__)

@application.route("/test/")

def hello():
    return "OpenShift Hello World! test"

if __name__ == "__main__":
    application.run()
