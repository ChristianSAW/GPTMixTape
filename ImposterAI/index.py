# Import required libraries
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

# Import app and layouts
from app import app
from frontend import header, body1

# Define the app's layout
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(
        id='page-content', 
        children=[
            header,
            body1
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

# Import callbacks from other files
# from callbacks import callbacks1, callbacks2

# Run the server
if __name__ == '__main__':
    app.run_server(debug=True)
