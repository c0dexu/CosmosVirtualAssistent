from flask import Flask, request, jsonify
from flask_cors import CORS
from chat_bot import chat

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})

@app.route("/", methods=['GET'])
def hello_world():
    response = jsonify({'response': 'Hello, World!'})
    return response


@app.route("/chat", methods=['GET'])
def read_item():
    message = chat(request.args.get('message'))
    response = jsonify({'response': message})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == "__main__":
    app.run(debug=True)
