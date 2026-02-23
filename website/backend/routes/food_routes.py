from flask import Blueprint, jsonify
from model.food import get_all_foods

food_bp = Blueprint("food", __name__)

@food_bp.route("/foods", methods=["GET"])
def foods():
    foods = get_all_foods()
    return jsonify(foods), 200