import plotly.graph_objects as go
from src.visualizer import create_sunburst_figure
from src.data_generator import generate_construction_data

def test_create_sunburst_figure_returns_figure():
    """
    Tests if the create_sunburst_figure function returns a Plotly Figure object.
    """
    df = generate_construction_data()
    fig = create_sunburst_figure(df)
    assert isinstance(fig, go.Figure)

def test_create_sunburst_figure_has_title():
    """
    Tests if the generated figure has the expected title.
    """
    df = generate_construction_data()
    fig = create_sunburst_figure(df)
    assert fig.layout.title.text == "<b>Residential Construction: Hierarchical Cost Explorer</b>"

def test_create_sunburst_figure_has_correct_traces():
    """
    Tests if the generated figure has the correct number of traces.
    """
    df = generate_construction_data()
    fig = create_sunburst_figure(df)
    assert len(fig.data) == 1
    assert fig.data[0].type == 'sunburst'