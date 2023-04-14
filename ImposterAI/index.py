# Import required libraries
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

# Import app and layouts
from app import app
from frontend import header, body1, messenger_layout

# Import callbacks from other files
from callbacks.callbacks import send_sys_message, send_user_message

import openai
import os

try:
    with open("API_KEY") as f:
        file_contents = f.read()
    os.environ["OPENAI_API_KEY"] = file_contents
except:
    from SecureKeys import gpt_api_key
    openai.api_key = gpt_api_key

# Define the app's layout
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(
        id='page-content', 
        children=[
            header,
            body1,
            messenger_layout
        ]
    )
])

# Define the app's callback for switching between pages
# @app.callback(
#     Output('page-content', 'children'),
#     [Input('url', 'pathname')]
# )
# def display_page(pathname):
#     if pathname == '/page1':
#         return page1_layout
#     elif pathname == '/page2':
#         return page2_layout
#     else:
#         return home_layout



# Run the server
if __name__ == '__main__':
    print("Starting the server")
    app.run_server(debug=True)
