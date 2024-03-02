import json
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    params = request.get_json()
    message = params.get('message')
    history = params.get('history', [])

    if not message:
        return jsonify({"message": "Missing 'message' parameter"}), 400

    history, chat_history = custom_chat_function(message, history)

    response_data = {
        "message": message,
        "response": chat_history[-1][1],
        "history": chat_history
    }

    return jsonify(response_data), 200

def custom_chat_function(message, history):
    # Implement your custom chat function here
    # For example, using a simple echo response:
    response = f"Echo: {message}"
    history.append((message, response))
    return history, history

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
