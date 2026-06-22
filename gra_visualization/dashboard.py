import dash
from dash import html

class Dashboard:
    def __init__(self):
        self.app = dash.Dash(__name__)
        self.app.layout = html.Div("GRA-X Dashboard")
    def run(self):
        self.app.run_server(debug=True)
