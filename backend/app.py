from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import sqlite3, jwt, datetime
from werkzeug.security import check_password_hash
from dss_logic import recommend_products

app = Flask(__name__)
CORS(app)

SECRET_KEY = "secret123"
DB_PATH = "cosmetics.db"

# ------------------ LOGIN ------------------
@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT password FROM users WHERE email=?", (email,))
    row = cursor.fetchone()
    conn.close()

    if row and check_password_hash(row[0], password):
        token = jwt.encode(
            {"email": email, "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)},
            SECRET_KEY,
            algorithm="HS256"
        )
        return jsonify({"token": token})
    return jsonify({"error": "Sai email hoặc mật khẩu"}), 401

# ------------------ DSS ------------------
@app.route("/recommend", methods=["POST"])
def recommend():
    token = request.headers.get("Authorization")
    if not token:
        return jsonify({"error": "Thiếu token"}), 401

    try:
        jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
    except:
        return jsonify({"error": "Token không hợp lệ"}), 401

    data = request.get_json()
    skin_type = data.get("skin_type")
    problem = data.get("problem")
    budget = data.get("budget")

    recommendations = recommend_products(DB_PATH, skin_type, problem, budget)
    return jsonify(recommendations)

# ------------------ SERVE IMAGES ------------------
@app.route('/images/<path:filename>')
def serve_image(filename):
    return send_from_directory("static/images", filename)

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Backend is running 🚀"})

if __name__ == "__main__":
    app.run(debug=True)
