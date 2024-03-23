from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
app.config["secret"] = "Random string"

@app.route("/meu_ip")
def meu_ip():
    return render_template("meu_ip.html")

@app.route("/")
def dashboard():
    return render_template("NiceAdmin/index.html")

@app.route("/<string:page>")
def page(page):
    return page

from api import bp
app.register_blueprint(bp)

if __name__ == "__main__":
    app.run(host="0.0.0.0")