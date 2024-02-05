from dash import Dash, html, dcc, callback, Output, Input, State
import plotly.express as px
import pandas as pd
import requests
import os
from dotenv import load_dotenv
from openai import AzureOpenAI
import time

app = Dash(__name__)

# Add CSS for pre-loader animation
app.css.append_css({
    "external_url": "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"
})

# Add skeleton pre-loader
skeleton_loader = html.Div(
    className="skeleton-loader",
    children=[
        html.Div(className="skeleton-image"),
        html.Div(className="skeleton-text"),
    ],
)

def generate_image_from_prompt(prompt):  
    try:
        # ... (existing code remains unchanged)

        # Return the URL for the generated image
        return image_url

    except Exception as ex:
        print(ex)

# ... (existing generate_prompt function remains unchanged)

app.layout = html.Div([
    html.H1(children='My Awesome Image Generation App', style={'textAlign':'center'}),
    dcc.Input(
        id="basic-prompt-input",
        type="text",
        placeholder="Type your basic prompt here",
        size="100",
    ),
    html.Button('Submit', id='submit-button', n_clicks=0),
    html.Div(id='image-generation-output',
             children=skeleton_loader),  # Show skeleton loader initially
    html.Img(id="generated-image")
])

# Add CSS for skeleton loader
app.css.append_css({
    "external_url": "path_to_your_custom_css_file.css"
})

@callback(
    Output('generated-image', 'src'),
    Input('submit-button', 'n_clicks'),
    State('basic-prompt-input', 'value'),
    prevent_initial_call=True
)
def generate_image(n_clicks, value):
    image_url = generate_prompt(value)

    return image_url

if __name__ == '__main__':
    app.run(debug=True)
