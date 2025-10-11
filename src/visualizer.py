import plotly.express as px

def create_sunburst_figure(df):
    """Creates the styled, interactive sunburst figure from the DataFrame."""
    color_map = {
        "Construction": "#5D6D7E",
        "Management": "#5499C7",
        "Project Design": "#48C9B0",
        '(?)': '#F4F6F6'
    }
    fig = px.sunburst(
        df,
        path=['pillar', 'area', 'service', 'task'], values='cost',
        color='pillar', color_discrete_map=color_map, custom_data=['cost']
    )
    fig.update_layout(
        title_text="<b>Residential Construction: Hierarchical Cost Explorer</b>",
        title_x=0.5, font=dict(family="Arial, sans-serif", size=16),
        margin=dict(t=80, l=40, r=40, b=40),
    )
    fig.update_traces(
        textinfo='label+percent root',
        hovertemplate=("<b>%{label}</b><br><br><b>Cost:</b> $%{customdata[0]:,.0f}<br><b>Contribution:</b> %{percentParent:.2%}<extra></extra>"),
        insidetextorientation='radial', textfont_size=12,
        marker_line=dict(color='#ffffff', width=3)
    )
    return fig