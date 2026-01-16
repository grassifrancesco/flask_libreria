from flask import Flask, jsonify
from markupsafe import escape
from faker import Faker
from flask_cors import CORS
from flask import request
import uuid

app = Flask(__name__)
CORS(app)

fake = Faker()

@app.route('/')
def index():
    return 'INDEX DELLA API, VAI SU /api/libri PER OTTENERE DEI LIBRI'

libri = []                  # INIZIALIZZO IL VETTORE LIBRI (SAREBBE MEGLIO USARE UN DATABASE)

@app.route("/api/libri", methods=["GET"])
def get_libri():   
    for i in range(20):     # CREO 20 LIBRI
        libro = {
            "id": str(uuid.uuid4()),
            "titolo": fake.sentence(nb_words=3).rstrip('.').title(),
            "autore": fake.name(),
            "anno": fake.year(),
            "genere": fake.random_element(elements=("M", "F"))
        }

        libri.append(libro) # AGGIUNGO IL LIBRO CREATO AL VETTORE (MA SAREBBE MEGLIO AGGIUNGERLO AD UN DATABASE)

    return jsonify({        # PRENDO UN FILE .json CONTENENTE I LIBRI
        "success": True,
        "data": libri
    })

@app.route("/api/libri", methods=["POST"])
def post_libro():
    libro = request.get_json()

    if not libro or "titolo" not in libro or "autore" not in libro or "anno" not in libro or "genere" not in libro:
        return jsonify({"success": False, "error": "Dati mancanti"}), 400
    
    nuovo_libro = {
        "id": str(uuid.uuid4()),
        "titolo": libro["titolo"],
        "autore": libro["autore"],
        "anno": libro["anno"],
        "genere": libro["genere"]
    }
    
    libri.append(nuovo_libro)

    return jsonify({
        "success": True,
        "data": nuovo_libro
    }), 201

if __name__ == "__main__":
    app.run("0.0.0.0", 12346, debug=True)
