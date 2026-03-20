from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Fake database
users = {}
balance = 0

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/buy_policy', methods=['POST'])
def buy_policy():
    global balance
    plan = request.json['plan']

    if plan == "basic":
        premium = 20
    else:
        premium = 50

    balance -= premium

    return jsonify({
        "message": f"Policy activated! ₹{premium} deducted",
        "balance": balance
    })

@app.route('/simulate_rain', methods=['POST'])
def simulate_rain():
    global balance

    rain = random.randint(50, 100)

    if rain > 70:
        payout = random.randint(200, 500)
        balance += payout
        return jsonify({
            "status": "CLAIM TRIGGERED",
            "payout": payout,
            "balance": balance
        })
    else:
        return jsonify({
            "status": "No disruption",
            "rain": rain
        })

if __name__ == '__main__':
    app.run(debug=True)