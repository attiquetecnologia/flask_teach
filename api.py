from flask import Blueprint, current_app
from flask import jsonify

bp = Blueprint("api", __name__)

@bp.route("/api", methods=("POST", "GET"))
async def index():
    return ""

@bp.route("/api/randon_data")
async def randon_data():
    import os
    import json

    dados = {}
    with open(os.path.join(current_app.root_path, "database","random_data.json"), "r") as file:
        dados = file.read()

    dados = json.dumps(dados) 
    dados = dados.strip()
    return dados