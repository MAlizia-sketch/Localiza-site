from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)


# ==========================================
# SERVIR O SITE
# ==========================================

@app.route("/", methods=["GET"])
def inicio():

    pasta = os.path.dirname(os.path.abspath(__file__))

    return send_from_directory(
        pasta,
        "localiza.html"
    )


# ==========================================
# RECEBER LOCALIZAÇÃO
# ==========================================

@app.route("/localizacao", methods=["POST"])
def receber_localizacao():

    dados = request.get_json()

    if not dados:

        return jsonify({
            "status": "erro",
            "mensagem": "Nenhum dado recebido"
        }), 400

    latitude = dados.get("latitude")
    longitude = dados.get("longitude")
    precisao = dados.get("precisao")
    horario = dados.get("horario")

    print()
    print("=" * 50)
    print("       NOVA LOCALIZAÇÃO RECEBIDA")
    print("=" * 50)

    print("Latitude :", latitude)
    print("Longitude:", longitude)
    print("Precisão :", precisao, "metros")
    print("Horário  :", horario)

    print("=" * 50)

    mapa = (
        "https://www.google.com/maps?q="
        f"{latitude},{longitude}"
    )

    print("Mapa:")
    print(mapa)

    print()

    return jsonify({
        "status": "ok",
        "mensagem": "Localização recebida",
        "latitude": latitude,
        "longitude": longitude,
        "precisao": precisao,
        "horario": horario,
        "mapa": mapa
    })


# ==========================================
# EXECUÇÃO LOCAL
# ==========================================

if __name__ == "__main__":

    porta = int(os.environ.get("PORT", 10000))

    print("=" * 50)
    print("       SERVIDOR DE LOCALIZAÇÃO")
    print("=" * 50)

    print(f"Servidor rodando na porta: {porta}")
    print("Aguardando localização...")

    print("=" * 50)

    app.run(
        host="0.0.0.0",
        port=porta,
        debug=False
    )
