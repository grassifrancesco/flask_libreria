import sqlite3

from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


# Database connection
def get_db_connection():
    conn = sqlite3.connect("libri.sqlite3")
    conn.row_factory = sqlite3.Row
    return conn


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
    conn = get_db_connection()
    libri = conn.execute("SELECT * FROM libro").fetchall()
    conn.close()

    return jsonify(
        {
            "success": True,
            "data": [dict(libro) for libro in libri],
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

    # Validazione dell'anno
    try:
        anno_num = int(libro["anno"])
        import datetime

        current_year = datetime.datetime.now().year
        if anno_num < 0:
            return jsonify(
                {"success": False, "error": "L'anno non può essere negativo"}
            ), 400
        if anno_num > current_year + 1:
            return jsonify(
                {
                    "success": False,
                    "error": f"L'anno non può essere maggiore di {current_year + 1}",
                }
            ), 400
    except ValueError:
        return jsonify(
            {"success": False, "error": "L'anno deve essere un numero valido"}
        ), 400

    conn = get_db_connection()
    cursor = conn.execute(
        "INSERT INTO libro (titolo, autore, anno, genere) VALUES (?, ?, ?, ?)",
        (libro["titolo"], libro["autore"], libro["anno"], libro["genere"]),
    )
    nuovo_id = cursor.lastrowid
    conn.commit()
    conn.close()

    nuovo_libro = {
        "id": nuovo_id,
        "titolo": libro["titolo"],
        "autore": libro["autore"],
        "anno": libro["anno"],
        "genere": libro["genere"],
    }

    return jsonify({"success": True, "data": nuovo_libro}), 201


@app.route("/")
def index():
    return "INDEX DELLA API, VAI SU /api/libri PER OTTENERE DEI LIBRI"


@app.route("/api/libri/<int:id>", methods=["DELETE"])
def delete_libro(id):
    conn = get_db_connection()
    cursor = conn.execute("DELETE FROM libro WHERE id = ?", (id,))
    conn.commit()
    conn.close()

    if cursor.rowcount == 0:
        return jsonify({"success": False, "error": "Libro non trovato"}), 404

    return jsonify({"success": True, "message": "Libro eliminato"})


@app.route("/api/libri", methods=["DELETE"])
def delete_all_libri():
    conn = get_db_connection()
    conn.execute("DELETE FROM libro")
    conn.commit()
    conn.close()

    return jsonify({"success": True, "message": "Tutti i libri eliminati"})


if __name__ == "__main__":
    app.run("0.0.0.0", 12346, debug=True)
