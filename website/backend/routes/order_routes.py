from flask import Blueprint, request, jsonify

from utils.jwt_handler import verify_token
from model.order import create_order, add_order_item

order_bp = Blueprint("order", __name__)

@order_bp.route("/order", methods=["POST"])
def place_order():
    token = request.headers.get("Authorization")

    if not token:
        return jsonify({"error": "Token required"}), 401

    user_id = verify_token(token)
    if not user_id:
        return jsonify({"error": "Invalid token"}), 401

    data = request.json

    # create order (matches order.py exactly)
    order_id = create_order(user_id, data["total"])

    # save order items
    for item in data["items"]:
        add_order_item(
            order_id,
            item["food_id"],
            item["quantity"]
        )

    return jsonify({
        "message": "Order placed successfully",
        "order_id": order_id
    }), 201