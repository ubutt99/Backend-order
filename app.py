from flask import Flask, jsonify
import requests

app = Flask(__name__)


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"service": "Order Service", "status": "UP"})


@app.route("/orders", methods=["GET"])
def get_orders():
    return jsonify({"message": "Order Service is working"})


@app.route("/products", methods=["GET"])
def get_products():

    response = requests.get(
        "http://127.0.0.1:5001/products"
    )

    return jsonify(response.json())


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5002)