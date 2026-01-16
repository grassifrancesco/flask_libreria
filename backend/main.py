from flask import Flask, jsonify
from markupsafe import escape
from faker import Faker
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

faker = Faker()

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'

@app.route('/user/<username>')
def show_user_profile(username):
    return f'User {escape(username)}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f'Post {post_id}'

@app.route("/fake")
def fake_profile():
    profile = {
        "nome": faker.name(),
        "email": faker.email(),
        "indirizzo": faker.address().replace("\n", ", "),
        "telefono": faker.phone_number(),
        "azienda": faker.company(),
        "lavoro": faker.job(),
        "data_nascita": faker.date_of_birth(minimum_age=18, maximum_age=70).isoformat(),
        "username": faker.user_name(),
        "avatar": faker.image_url(width=128, height=128)
    }

    return jsonify({
        "success": True,
        "data": profile
    })

if __name__ == "__main__":
    app.run("0.0.0.0", 12346, debug=True)
