import dash
import dash_bootstrap_components as dbc

# Initialize the Dash app with Bootstrap
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Set the app's title
app.title = "Imposter.AI"

# Disable handling exceptions in callbacks
# app.config.suppress_callback_exceptions = True

# Expose the server instance for running the app
server = app.server

# If running this script directly, run the server
if __name__ == "__main__":
    app.run_server(debug=True)