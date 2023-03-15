from flask import Flask, render_template, request, jsonify
import openai
import os

app = Flask(__name__)

with open("API_KEY") as f:
    file_contents = f.read()

print(file_contents)
os.environ["OPENAI_API_KEY"] = file_contents

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/message', methods=['POST'])
def message():
    user_message = request.form['message']
    chat_gpt_response = send_message_to_chat_gpt(user_message)
    return jsonify(chat_gpt_response)

def send_message_to_chat_gpt(message):
    try:
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=f"User: {message}\nAssistant:",
            temperature=0.7,
            max_tokens=150,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            stop=["\n"]
        )

        response_text = response.choices[0].text.strip()
        return {'status': 'success', 'message': response_text}

    except Exception as e:
        return {'status': 'error', 'message': str(e)}


if __name__ == '__main__':
    app.run(debug=True)
