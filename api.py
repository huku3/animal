from flask import Flask
from flask import render_template
from flask import request

# flaskから引っ張ってくる
import json
import requests

# requestから引っ張ってくる
import secrets

app = Flask(__name__)

app.secret_key = secrets.token_urlsafe(32)


@app.route("/")
def show_form():
    return render_template("index.html")


@app.route("/post", methods=["POST"])
def post():
    if request.form["animal"] == "cat":
        res = requests.get("https://api.thecatapi.com/v1/images/search")
        outfile = json.loads(res.text)[0]["url"]
    elif request.form["animal"] == "dog":
        res = requests.get("https://dog.ceo/api/breeds/image/random")
        outfile = json.loads(res.text)["message"]
    elif request.form["animal"] == "fox":
        res = requests.get("https://randomfox.ca/floof/")
        outfile = json.loads(res.text)["image"]
    # 配列の０
    return render_template("upload.html", outfile=outfile)


if __name__ == "__main__":
    app.run(debug=True)
