from flask import Flask, request, jsonify 
import json
import os

app = Flask(__name__)

def salvar_arquivo(usuarios):
 with open("usuarios.json", "w") as arquivo_json:
        json.dump(usuarios  , arquivo_json, indent=4)

def carregar_arquivo():
    if os.path.exists("usuarios.json"):
        with open("usuarios.json", "r") as arquivo_json:
            return json.load(arquivo_json)
    else:
        return []



@app.route('/usuario/<int:cpf>',methods=['GET'])
def consultar_usuario(cpf):
    usuarios = carregar_arquivo()
    for usuario in usuarios:
        if usuario.get('cpf') == cpf:
            return jsonify(usuario)

    return jsonify("Não Encontrado")

@app.route('/usuario/',methods=['POST'])
def criar_usuario():
    usuarios = carregar_arquivo()
    print(usuarios)
    novo_usuario = request.get_json()
    usuarios.append(novo_usuario)
    salvar_arquivo(usuarios)
    return("Usuario Cadastrado")

app.run(port=5000, host='localhost', debug=True)

