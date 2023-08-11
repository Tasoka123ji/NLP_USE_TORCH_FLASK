from flask import Flask, render_template, request
from flask_ngrok import run_with_ngrok
from chat import chat
from time import sleep
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get", methods=["POST"])
def chatbot_response():

    msg = request.form["msg"]
    foo = chat(msg)
    sleep(2)
    return foo

if __name__ == "__main__":
    app.run()

