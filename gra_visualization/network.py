import plotly.graph_objects as go
def plot_graph(edges):
    fig = go.Figure(data=[go.Scatter(x=[0,1], y=[0,1], mode='lines')])
    return fig
