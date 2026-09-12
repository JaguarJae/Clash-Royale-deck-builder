from flask import Flask, request, jsonify
from flask_cors import CORS
from cr_api import get_top_decks
from main import get_user_valid_decks

app = Flask(__name__)
CORS(app)

@app.get('/api/top-decks')
def get_top_decks_route():
    top_decks = get_top_decks()
    return jsonify(top_decks)

@app.post('/api/fetch-decks')
def fetch_decks():
    data = request.get_json()
    user_tag = data.get('user_tag')
    if not user_tag:
        return jsonify({"error": "User tag is required"}), 400
    try:
        decks = get_user_valid_decks(user_tag=user_tag)
        return jsonify(decks)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(port=5000, debug=True)