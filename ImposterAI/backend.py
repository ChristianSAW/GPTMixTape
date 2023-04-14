import pandas as pd
import openai
import os
import sys

saved_messages = []

def system_message(sys_message):
    # print("System Message Called")
    # sys_message = request.form['system_message']
    save_message({"role": "system", "content": sys_message})
    chat_gpt_response = send_message_to_chat_gpt()
    return jsonify(chat_gpt_response)

def user_message(user_message):
    # user_message = request.form['user_message']
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

# def send_message_to_chat_gpt(sys_message, user_message):
#     try:
#         response = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo",
#         messages=[
#                 # {"role": "system", "content": sys_message},
#                 {"role": "user", "content": "Hi"}
#             ]
#         )
#         # print(response)
#         message = response.choices[0].message.content
#         print(message)
#         return {'status': 'success', 'message': message}

    # except Exception as e:
    #     return {'status': 'error', 'message': str(e)}