from flask import Flask, render_template, request, jsonify
from dash import Dash, html, dcc, callback
from dash.dependencies import Input, Output, State
from frontend import body1, header
from callbacks import save_message, send_message_to_chat_gpt
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
        header,
        body1
        ]
    )
   
    

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

if __name__ == '__main__':
    app.run_server(debug=True)
