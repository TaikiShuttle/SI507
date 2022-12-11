import plotly.graph_objects as go

import pandas as pd

def plot_restaurant():
    df = pd.read_json('restaurant_info.json')

    fig = go.Figure(data=go.Scattergeo(
            name = df['name'],
            lon = df['coordinates']['logitude'],
            lat = df['coordinates']['latitude'],
            ))

    fig.update_layout(
            title = 'Most trafficked US airports<br>(Hover for airport names)',
            geo_scope='new york',
        )
    
    fig.save_html('restaurant.html')

if __name__ == "__main__":
    plot_restaurant()