from flask import Blueprint, request, jsonify
from werkzeug.security import check_password_hash

# correct imports based on your project structure
from model.user import create_user, get_user_by_email
from utils.validator import validate_register, validate_login
from utils.jwt_handler import create_token

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.json

    error = validate_register(data)
    if error:
        return jsonify({"error": error}), 400

    # check if user already exists
    existing_user = get_user_by_email(data["email"])
    if existing_user:
        return jsonify({"error": "Email already registered"}), 400

    # IMPORTANT:
    # pass RAW password
    # hashing is already done inside create_user()
    create_user(
        data["name"],
        data["email"],
        data["password"]
    )

    return jsonify({"message": "User registered successfully"}), 201


@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json

    error = validate_login(data)
    if error:
        return jsonify({"error": error}), 400

    user = get_user_by_email(data["email"])

    if not user:
        return jsonify({"error": "Invalid credentials"}), 401

    if not check_password_hash(user["password_hash"], data["password"]):
        return jsonify({"error": "Invalid credentials"}), 401

    token = create_token(user["id"])

    return jsonify({
        "token": token,
        "user": {
            "id": user["id"],
            "name": user["name"],
            "email": user["email"]
        }
    }), 200