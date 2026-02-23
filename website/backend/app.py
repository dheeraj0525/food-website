from flask import Flask
from flask_cors import CORS

from routes.auth_routes import auth_bp
from routes.food_routes import food_bp
from routes.order_routes import order_bp

app = Flask(__name__)
CORS(app)

@app.route("/api/health")
def health():
    return {"status": "Backend is running"}

app.register_blueprint(auth_bp, url_prefix="/api")
app.register_blueprint(food_bp, url_prefix="/api")
app.register_blueprint(order_bp, url_prefix="/api")

if __name__ == "__main__":
    app.run(debug=True)