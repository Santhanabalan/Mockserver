from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

PAYMENT_SERVICE_URL = os.getenv('PAYMENT_SERVICE_URL')

# Route to create an order
@app.route('/createOrder', methods=['POST'])
def create_order():
    data = request.get_json()
    
    order_id = data.get('orderId')
    amount = data.get('amount')
    
    if not order_id or not amount:
        return jsonify({"error": "Invalid input"}), 400
    
    # Send payment request to the Payment Service
    payment_response = requests.post(PAYMENT_SERVICE_URL, json={"orderId": order_id, "amount": amount})
    
    if payment_response.status_code == 201:
        payment_data = payment_response.json()
        if payment_data.get("status") == "success":
            return jsonify({
                "orderId": order_id,
                "status": "confirmed",
                "message": f"Order {order_id} has been confirmed with transaction ID {payment_data['transactionId']}."
            })
        else:
            return jsonify({
                "orderId": order_id,
                "status": "failed",
                "message": f"Order {order_id} could not be confirmed: {payment_data.get('error')}."
            })
    else:
        return jsonify({"error": "Payment Service is unavailable"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
