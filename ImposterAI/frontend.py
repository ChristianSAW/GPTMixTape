from flask import Flask, render_template, request, jsonify
from dash import Dash, html, dcc, callback
import dash_bootstrap_components as dbc


header = html.H1(children='Imposter AI', style={'textAlign':'center'})
body1 = html.Div(
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

messenger_layout = html.Div([
    dbc.Row([
        dbc.Col([
            html.Div(className='chat-container', children=[
                html.Div(id='message-container', className='message-container'),
                dcc.Input(
                    id='input-message',
                    placeholder='Type your message here...',
                    type='text',
                    value='',
                    className='input-message'
                ),
                dbc.Button('Send', id='submit-message', color='primary', className='send-button')
            ])
        ], width={'size': 6, 'offset': 3})
    ], className='main-row')
])


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