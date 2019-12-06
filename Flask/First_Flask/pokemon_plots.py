import plotly
import plotly.graph_objects  as go
from pokemon_data import data_pokemon
import json

def count_type1():
    df = data_pokemon()
    df_group= df['Type 1'].value_counts()
    
    fig = go.Figure([
        go.Bar(x=df_group.index , y= df_group.values)
    ])
    fig_json = json.dumps(fig , cls=plotly.utils.PlotlyJSONEncoder)
    return fig_json
    # fig.show()

def sum_type2():
    df = data_pokemon()
    df_aduh = df.groupby('Type 1').sum()['Total'].sort_values(ascending = False)
    df_aduh2 = df.groupby('Type 2').sum()['Total'].sort_values(ascending = False)

    fig2 = go.Figure()
    fig2.add_trace(go.Bar(
    x = df_aduh.index , 
    y = df_aduh.values, 
    name = 'Total Type 1', 
    marker_color='indianred'
    ))
    fig2.add_trace(go.Bar(
    x = df_aduh2.index , 
    y = df_aduh2.values, 
    name = 'Total Type 2', 
    marker_color='lightsalmon'
    ))
    fig2_json = json.dumps(fig2 , cls=plotly.utils.PlotlyJSONEncoder)
    return fig2_json
