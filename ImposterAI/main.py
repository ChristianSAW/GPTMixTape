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
                                placeholder="Type your system message here..."
                            ),
                            dbc.Button(
                                id="user-input-button",
                                class_name="chat-submit",
                                type="submit",
                                children="Send"
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

@app.callback(
        Output("chat-window", "children"),
        Input('user-input-button', 'n_clicks'),
        State("user-input", "value")
    )

def output_text(n_clicks, value):
    global current_prompt
    if n_clicks and n_clicks > 0:
        sys_message ="Respond as if your best friend."
        out = send_message_to_chat_gpt(sys_message, value)
        resp = out['message']
        current_prompt = resp
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
def send_message_to_chat_gpt(sys_message, user_message):
    try:
        response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
                # {"role": "system", "content": sys_message},
                {"role": "user", "content": "Hi"}
            ]
        )
        # print(response)
        message = response.choices[0].message.content
        print(message)
        return {'status': 'success', 'message': message}

    except Exception as e:
        return {'status': 'error', 'message': str(e)}


if __name__ == '__main__':
    app.run_server(debug=True)
