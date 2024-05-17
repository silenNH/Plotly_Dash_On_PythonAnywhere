
from dash import  html, dcc, callback, Input, Output, State, no_update
import dash_bootstrap_components as dbc
#import plotly.express as px
import dash


dash.register_page(__name__)

layout = dbc.Container([
    
    
    dcc.Location(id="ATool"),
    html.H1(children='Allocation Tool/ UpTime-izer'),
    html.Hr(),


    html.H2(children='Upload Section:'),
    dcc.Upload(
        id='upload-data',
        children=html.Div([
            'Drag and Drop or ',
            html.A('Select Files')
        ]),
        style={
            'width': '100%',
            'height': '60px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '10px'
        },
        # Allow multiple files to be uploaded
        multiple=True
    ),
    
    html.Br(),
    html.Br(),
    html.Hr(),
    html.H2(children='Define Run Parameters:'), 
    
    html.Br(),
    html.Br(),
    dbc.Row([
        dbc.Col([
            dcc.Dropdown(
                ['s3://DOC-EXAMPLE-BUCKET/FOLDER/uploadFile1', 's3://DOC-EXAMPLE-BUCKET/FOLDER/uploadFile2', 's3://DOC-EXAMPLE-BUCKET/FOLDER/uploadFile3'],
                 id="S3FileDropDown", 
                clearable=False
                ),
            ]),
        dbc.Col([
            html.H4(children='Please select the S3 file in the given S3 Bucket which should be used during execution'),      
        ], width=6)],
          className='mb-1'),

    html.Br(),
    html.Br(),
    html.Hr(),
    html.H2(children='Run on DMC'), 
    dbc.Row([
            dbc.Col([
            dbc.Button("Click to execute on DMC", color="primary", id='my-button', className="me-1",n_clicks=0),    
            ])

    ]),
    dbc.Row([
    dbc.Alert("", color="Primary", id="Alert1"),
        ]),

    html.Br(),
    html.Br(),
    html.Hr(),
    html.H2(children='Download Results'), 
    dbc.Row([
        dbc.Col([
            dcc.Dropdown(
                ['s3://DOC-EXAMPLE-BUCKET/FOLDER/resultFile1', 's3://DOC-EXAMPLE-BUCKET/FOLDER/resultFile2', 's3://DOC-EXAMPLE-BUCKET/FOLDER/resultFile3'],
                 id="S3FileDropDownDownload", 
                clearable=False
                ),
            ]),
        dbc.Col([
            html.H4(children='Please select the S3 result file in the given S3 Bucket for downloading'),      
        ], width=6)],
          className='mb-1'),
    
    dbc.Row([
        dbc.Col([
            html.H4(children='The presigned URL link is:')
        ]),
        dbc.Col([
            dbc.Alert("", color="Primary", id="Alert2"),
        ]),
        ]),
    

])

@callback(
    Output(component_id='Alert1', component_property="children"),
    Input(component_id='my-button', component_property='n_clicks'),
    State(component_id='S3FileDropDown', component_property='value'), 
    )
def execute_dmc(button, inputtext1):
    return inputtext1   

@callback(
    Output('Alert2', 'children'), 
    Input('S3FileDropDownDownload', 'value'))
def create_presigned_url(file_path):
    return file_path

