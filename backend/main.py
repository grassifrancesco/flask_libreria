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

@app.route("/api/libri", methods=["GET"])
def get_libri():
    libri = []
    
    for i in range(20):
        libro = {
            "id": str(uuid.uuid4()),
            "titolo": fake.sentence(nb_words=3).rstrip('.').title(),
            "autore": fake.name(),
            "anno": fake.year(),
            "genere": fake.random_element(elements=("M", "F"))
        }

        libri.append(libro)

    return jsonify({
        "success": True,
        "data": libri
    })

if __name__ == "__main__":
    app.run("0.0.0.0", 12346, debug=True)
