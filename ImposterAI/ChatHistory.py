

class Message:

    def __init__(self):
        """
        """

class ChatHistory():

    def __init__(self):
        """ Stores history of chat """
        self.message_history = []

from flask import Flask, render_template, request, jsonify
import openai
import os

app = Flask(__name__)

with open("API_KEY") as f:
    file_contents = f.read()

print(file_contents)
os.environ["OPENAI_API_KEY"] = file_contents
saved_messages = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/system-message', methods=['POST'])
def system_message():
    # print("System Message Called")
    sys_message = request.form['system_message']
    save_message({"role": "system", "content": sys_message})
    chat_gpt_response = send_message_to_chat_gpt()
    return jsonify(chat_gpt_response)

@app.route('/user-message', methods=['POST'])
def user_message():
    user_message = request.form['user_message']
    save_message({"role": "user", "content": user_message})
    chat_gpt_response = send_message_to_chat_gpt()
    return jsonify(chat_gpt_response)

def save_message(msg):
    saved_messages.append(msg)

def send_message_to_chat_gpt():
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=saved_messages
        )
        chat_gpt_response = response.choices[0].message.content
        save_message({"role": "assistant", "content": chat_gpt_response})
        # print(saved_messages)
        return {'status': 'success', 'message': chat_gpt_response}

    except Exception as e:
        return {'status': 'error', 'message': str(e)}


if __name__ == '__main__':
    app.run(debug=True)
