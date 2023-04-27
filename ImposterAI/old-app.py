import os
import dash
import dash_bootstrap_components as dbc
from dash import dcc
from dash import html

# Import layouts
from frontend import header, body1, messenger_layout

# import openai

def load_openai_api_key():
    try:
        with open("API_KEY") as f:
            file_contents = f.read()
        os.environ["OPENAI_API_KEY"] = file_contents
    except:
        pass

# Load the API Key
load_openai_api_key()

# Initialize the Dash app with Bootstrap
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Set the app's title
app.title = "Imposter.AI"

# Import callbacks from other files
from callbacks.callbacks import register_callbacks
register_callbacks(app)

# Disable handling exceptions in callbacks
# app.config.suppress_callback_exceptions = True

# Expose the server instance for running the app
server = app.server

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

# If running this script directly, run the server
if __name__ == "__main__":
    app.run_server(debug=True)