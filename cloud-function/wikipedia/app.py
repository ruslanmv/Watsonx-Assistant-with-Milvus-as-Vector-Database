import json
import requests
from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/cloud-function', methods=['POST'])
def main():
    """Retrieves and summarizes Wikipedia information based on the provided object of interest.

    This function handles POST requests with a JSON payload containing the `object_of_interest` key.
    It fetches the Wikipedia summary for the specified object and returns it as a JSON response.

    Returns:
        A JSON response containing the summary or an error message if unsuccessful.
    """

    if request.content_type != 'application/json':
        return jsonify({"message": "Invalid content type. Expected application/json"}), 400

    try:
        params = request.get_json()
        object_of_interest = params.get('object_of_interest')

        if not object_of_interest:
            return jsonify({"message": "Missing 'object_of_interest' parameter"}), 400

        url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{object_of_interest}?redirect=true"
        headers = {'accept': 'application/json'}
        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            return jsonify({"message": f"Error fetching Wikipedia summary: {response.status_code}"}), response.status_code

        data = response.json()
        summary = data.get('extract')

        if not summary:
            return jsonify({"message": "No summary found for the specified object of interest"}), 404

        return jsonify({"summary": summary}), 200
    except Exception as e:
        return jsonify({"message": f"An error occurred: {e}"}), 500
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)