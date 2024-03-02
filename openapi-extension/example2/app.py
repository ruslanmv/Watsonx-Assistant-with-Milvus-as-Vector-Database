from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return jsonify({'message': 'Hello, world!'})

@app.route('/cloud-function', methods=['POST'])
def cloud_function():
    data = request.get_json()
    
    if 'object_of_interest' not in data:
        return jsonify({'message': 'Missing required parameter: object_of_interest'}), 400
    
    object_of_interest = data['object_of_interest']
    summary = f"Summary about {object_of_interest}."
    
    return jsonify({
        'object_of_interest': object_of_interest,
        'summary': summary
    })

if __name__ == '__main__':
    app.run(debug=True, port=8080)
