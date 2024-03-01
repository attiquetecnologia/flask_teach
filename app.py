from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
app.secret = "Random string"

@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0")