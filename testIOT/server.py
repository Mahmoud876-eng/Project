from flask import Flask, request, jsonify
from flask_cors import CORS  # Add this import
import requests

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Your Telegram Bot details
TOKEN = "7574204510:AAHDO7BlbgTVLJGNSyoBIxXQoGfqSWwd4yg"
CHAT_ID = "5944518463"

def send_telegram_message(message):
    """ Sends a message to the Telegram bot """
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }
    response = requests.post(url, json=payload)
    return response.json()

@app.route("/send", methods=["POST"])
def send_message():
    data = request.get_json()
    message = data.get("message", "")

    if not message:
        return jsonify({"status": "error", "message": "No message provided"}), 400

    response = send_telegram_message(message)
    return jsonify({"status": "success", "telegram_response": response})

if __name__ == "__main__":
    app.run(debug=True)
