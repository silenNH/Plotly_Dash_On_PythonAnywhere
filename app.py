import dash
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import dash_auth

# Keep this out of source code repository - save in a file or a database
VALID_USERNAME_PASSWORD_PAIRS = {
    'hello': 'world'
}
app = Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.SOLAR])
auth = dash_auth.BasicAuth(
    app,
    VALID_USERNAME_PASSWORD_PAIRS
)

app.layout = html.Div([
    html.Br(),
    dbc.Row([
        dbc.Col([

        ]),
        dbc.Col([
               html.H1('Master Analytics Platform - Our Solutions Catalog'),    
        ]),
        dbc.Col([

        ]),
    ]),
    
    html.Br(),
    dbc.NavbarSimple(
    dbc.DropdownMenu(
        [
            dbc.DropdownMenuItem(page["name"], href=page["path"])
            for page in dash.page_registry.values()
            if page["module"] != "pages.not_found_404"
        ],
        nav=True,
        label="More Pages",
    ),
    brand="Chose the solution you need",
    color="primary",
    dark=True,
    className="mb-2",
    ),

    dash.page_container
])
if __name__ == '__main__':
    app.run(debug=True)