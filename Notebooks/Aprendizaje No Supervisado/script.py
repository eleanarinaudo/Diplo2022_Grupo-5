import time
import plotly.graph_objects as go

def show_scatter(df, skill_1, skill_2, color=None):
    start = time.time()
    kmean_clusters = go.Scatter(
        x=df[skill_1], 
        y=df[skill_2],
                               mode='markers',
        text=df["player_positions"] + ": " + df['short_name'],
                               marker=dict(
                                    #size=2,
                                    color = color, #set color equal to a variable
                                    colorscale='Portland',
                                    showscale=False)
                               )

    data=[kmean_clusters]
    layout = go.Layout(title="Clustering K means ",titlefont=dict(size=20),
                    xaxis=dict(title=skill_1),
                    yaxis=dict(title=skill_2),
                    autosize=False, width=1000,height=650)

    fig = go.Figure(data=data, layout=layout)
    fig.show()
    end = time.time()
    t=end-start
    print('time:',round(t,2))