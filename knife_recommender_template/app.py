from flask import Flask, request, jsonify
from flask_cors import CORS
from recommend import recommend_knives

app = Flask(__name__)
CORS(app)

@app.route("/recommend", methods=["POST"])
def recommend():
    user_info = request.get_json()
    result = recommend_knives(user_info)
    return jsonify({"recommendations": result})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
