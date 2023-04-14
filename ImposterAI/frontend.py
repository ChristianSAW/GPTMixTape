from flask import Flask, render_template, request, jsonify
from dash import Dash, html, dcc, callback
import dash_bootstrap_components as dbc


header = html.H1(children='Title of Dash App', style={'textAlign':'center'})
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