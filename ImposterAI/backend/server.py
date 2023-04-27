import os
import openai
from flask import Flask, request, jsonify
from flask_cors import CORS

import datetime

x = datetime.datetime.now()

app = Flask(__name__)
CORS(app)

def load_openai_api_key():
    try:
        with open("API_KEY") as f:
            file_contents = f.read()
        os.environ["OPENAI_API_KEY"] = file_contents
    except:
        pass

# Load the API Key
load_openai_api_key()

@app.route("/api/send_user_message", methods=['POST'])
def send_user_message():
    print("clicked")
    # Get the user's input
    data = request.json
    print(data)
    user_input = request.args.get("input")

    # Send the user's input to the ChatGPT API
    openai.api_key = os.getenv("OPENAI_API_KEY")

    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": data['newQuestion']}
    ]
    )

    print(completion.choices[0].message)
    # Return the ChatGPT's response
    return completion.choices[0].message

@app.route('/api/some_function', methods=['POST'])
def some_function():
    data = request.json
    # Process the data and perform the desired function
    result = {'result': 'Hello, ' + data['name']}
    return jsonify(result)

@app.route("/data")
def get_time():
    return{
        'Name':"Tim",
        'Age':"29",
        'Date':x,
        "Programming":"Python"
    }

if __name__ == "__main__":
    app.run(debug=True)
