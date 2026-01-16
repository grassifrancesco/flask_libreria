import random
import sqlite3
import uuid

from faker import Faker
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

fake = Faker()


@app.route("/")
def index():
    return "INDEX DELLA API, VAI SU /api/libri PER OTTENERE DEI LIBRI"


libri = []  # INIZIALIZZO IL VETTORE LIBRI (TODO: SOSTITUIRE CON UN DATABASE)
generi = [
    "Fantasy",
    "Horror",
    "Thriller",
    "Romanzo",
    "Storico",
    "Fantascienza",
    "Biografia",
]


@app.route("/api/libri", methods=["GET"])
def get_libri():
    # for i in range(20):  # CREO 20 LIBRI
    #     libro = {
    #         "id": str(uuid.uuid4()),
    #         "titolo": fake.sentence(nb_words=3).rstrip(".").title(),
    #         "autore": fake.name(),
    #         "anno": fake.year(),
    #         "genere": fake.random_element(elements=("M", "F")),
    #     }

    #     libri.append(
    #         libro
    #     )  # AGGIUNGO IL LIBRO CREATO AL VETTORE (TODO: SOSTITUIRE CON UN DATABASE)

    return jsonify(
        {  # RITORNO UN FILE .json CONTENENTE TUTTI I LIBRI PRESENTI NEL VETTORE (TODO: SOSTITUIRE CON UN DATABASE)
            "success": True,
            "data": libri,
        }
    )


@app.route("/api/libri", methods=["POST"])
def post_libro():
    libro = request.get_json()

    # CONTROLLO SE IL LIBRO CHE VOGLIO CREARE CONTIENE TUTTI I DATI NECESSARI
    if (
        not libro
        or "titolo" not in libro
        or "autore" not in libro
        or "anno" not in libro
        or "genere" not in libro
    ):
        return jsonify({"success": False, "error": "Dati mancanti!!!!!!"}), 400

    nuovo_libro = {
        "id": str(uuid.uuid4()),  # COME FACCIO A GENERARE UN ID USANDO IL DATABASE?
        "titolo": libro["titolo"],
        "autore": libro["autore"],
        "anno": libro["anno"],
        "genere": libro["genere"],
    }

    libri.append(nuovo_libro)  # TODO: SOSTITUIRE CON UN DATABASE

    return jsonify({"success": True, "data": nuovo_libro}), 201


if __name__ == "__main__":
    app.run("0.0.0.0", 12346, debug=True)
