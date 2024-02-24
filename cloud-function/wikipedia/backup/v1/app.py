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

    url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{object_of_interest}?redirect=true"
    headers = {'accept': 'application/json'}
    r = requests.get(url, headers=headers)

    if r.status_code != 200:
        return jsonify({"message": "Error fetching Wikipedia summary"}), r.status_code

    data = json.loads(r.content)
    summary = data.get('extract')

    return jsonify({"summary": summary}), 200

if __name__ == '__main__':
    app.run(debug=True)
