from flask import Blueprint, current_app
from flask import jsonify
from flask_cors import cross_origin

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

    # Quando abrimos o arquivo .json encontramos na verdade uma string
    # que precisa ser tratada removendo espaços em branco (strip) e linhas (\n)
    dados = dados.strip().replace("\n", "")
    dados = json.loads(dados) # depois precisa convertê-la em dicionarios python (loads)
    # return dados
    return {"results":dados}