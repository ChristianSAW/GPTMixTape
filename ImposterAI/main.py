from flask import Flask, render_template, request, jsonify
from dash import Dash, html, dcc, callback
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import pandas as pd
import openai
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

#app = Flask(__name__)
app = Dash(__name__)
current_prompt = ""


try:
    with open("API_KEY") as f:
        file_contents = f.read()

    print(file_contents)
    os.environ["OPENAI_API_KEY"] = file_contents
except:
    from SecureKeys import gpt_api_key
    openai.api_key = gpt_api_key



#region Basic Dash App
app.layout = html.Div([
    html.H1(children='Title of Dash App', style={'textAlign':'center'}),
    html.Div(
        className="chat-container",
        children=[
            dbc.Form(
                id='system-form',
                # autocomplete="off",
                children=[
                    html.P(
                        id="sys-window-output"
                    ),
                    dbc.Input(
                        id="system-input",
                        class_name="chat-input",
                        type="text",                        
                        placeholder="Type your system message here..."
                    ),
                    dbc.Button(
                        id="system-input-button",
                        class_name="chat-submit",
                        type="submit",
                        children="Send"
                    )                   
                ]
            ),
            html.Div(
                id="chat-window",
                className="chat-window",
                children=[
                    dbc.Form(
                        id="user-form",
                        children=[
                            dbc.Input(
                                id="user-input",
                                class_name="chat-input",
                                type="text",                        
                                placeholder="Type your chat message here..."
                            ),
                            dbc.Button(
                                id="user-input-button",
                                class_name="chat-submit",
                                type="submit",
                                children="Send"
                            ),
                            html.P(
                                id="chat-window-output"
                            )                               
                        ]
                    )
                ]
            )
        ]
    )
    # html.Div(
    #     [
    #         dbc.Input(id="input", placeholder="Type something...", type="text"),
    #         html.Br(),
    #         html.P(id="output"),
    #     ]
    # ),
    # html.Div(
    #     [
    #         dbc.Button("Send", id="send-button", color="primary", className="me-1")            
    #     ]
    # ),
    # html.Div(
    #     [
    #         dbc.Input(id="sys-input", placeholder="Type something...", type="text"),
    #         html.Br(),
    #         html.P(id="output"),
    #     ]
    # ),
    # html.Div(
    #     [
    #         dbc.Button("Update", id="update-button", color="primary", className="me-1")            
    #     ]
    # ),
    ])

'''
Send system message
'''
@app.callback(
        Output("chat-window-output", "children", allow_duplicate=True),
        Input('system-input-button', 'n_clicks'),
        State("system-input", "value"),
        prevent_initial_call=True
    )
def send_sys_message(n_clicks, system_input):
    if n_clicks and n_clicks > 0:
        save_message({"role": "system", "content": system_input})
        chat_gpt_response = send_message_to_chat_gpt()
        return chat_gpt_response['message']
    else:
        resp = ""
    return resp

@app.callback(
        Output("chat-window-output", "children"),
        Input('user-input-button', 'n_clicks'),
        State("user-input", "value"),
        prevent_initial_call=True
    )
def send_user_message(n_clicks, user_input):
    global current_prompt
    if n_clicks and n_clicks > 0:
        save_message({"role": "user", "content": user_input})
        chat_gpt_response = send_message_to_chat_gpt()
        return chat_gpt_response["message"]
    else:
        resp = current_prompt
    return resp
#endregion Basic Dash App

'''
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

'''
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


if __name__ == '__main__':
    app.run_server(debug=True)
