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
    sys_message = request.form['custom_text']
    # message = custom_text + user_message
    chat_gpt_response = send_message_to_chat_gpt(sys_message, user_message)
    return jsonify(chat_gpt_response)

def send_message_to_chat_gpt(sys_message, user_message):
    try:
        # response = openai.ChatCompletion.create(
        #     model="gpt-3.5-turbo",
        #     messages=[
        #         {"role": "system", "content": prompt},
        #     ]
        # )
        print(sys_message)
        response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
                {"role": "system", "content": sys_message},
                {"role": "user", "content": user_message}
            ]
        )
        # print(response)
        message = response.choices[0].message.content
        return {'status': 'success', 'message': message}

    except Exception as e:
        return {'status': 'error', 'message': str(e)}


if __name__ == '__main__':
    app.run(debug=True)
