import json
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/cloud-function', methods=['POST'])
def main():
    params = request.get_json()
    object_of_interest = params.get('object_of_interest')

    if not object_of_interest:
        return jsonify({"message": "Missing 'object_of_interest' parameter"}), 400

    response_data = {"object_of_interest": object_of_interest}

    try:
        url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{object_of_interest}?redirect=true"
        headers = {'accept': 'application/json'}
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        data = json.loads(response.content)
        summary = data.get('extract')
        response_data["summary"] = summary

    except requests.exceptions.RequestException as e:
        response_data["message"] = f"Error fetching Wikipedia summary: {str(e)}"

    return jsonify(response_data), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
