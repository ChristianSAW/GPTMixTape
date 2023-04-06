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
        [
            dbc.Input(id="input", placeholder="Type something...", type="text"),
            html.Br(),
            html.P(id="output"),
        ]
    ),
    html.Div(
        [
            dbc.Button("Send", id="send-button", color="primary", className="me-1")
        ]
    )
    ])

@app.callback(
        Output("output", "children"),
        Input('send-button', 'n_clicks'),
        State("input", "value")
    )
def output_text(n_clicks, value):
    sys_message ="Respond as if your best friend."
    out = send_message_to_chat_gpt(sys_message, value)
    return out
    
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
def send_message_to_chat_gpt(sys_message, user_message):
    try:
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
    app.run_server(debug=True)
