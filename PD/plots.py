import plotly
import pandas as pd
import plotly.graph_objects  as go
import plotly.express as px
import json
from datas import fullframe,featureframe,rateframe
from collections import Counter
from nltk.corpus import stopwords

def EDA_Type1():
    dfx = fullframe()
    fig1 = go.Figure(data=go.Heatmap(z = dfx.corr().values, x = dfx.corr().index, y = dfx.corr().index))  
    fig1_json = json.dumps(fig1, cls=plotly.utils.PlotlyJSONEncoder)
    return fig1_json

def EDA_Type2():
    dfx = fullframe()
    x0 = dfx['minimum_nights']
    x1 = dfx['maximum_nights']

    fig2 = go.Figure()
    fig2.add_trace(go.Histogram(
        x=x0,
        name='Minimum Stay Period', # name used in legend and hover labels
        xbins=dict( # bins used for histogram
            size=500
        ),
        marker_color='#EB89B5',
        opacity=1
    ))
    fig2.add_trace(go.Histogram(
        x=x1,
        name='Maximum Stay Period',
        xbins=dict(
            size=500
        ),
        marker_color='#330C73',
        opacity=1
    ))

    fig2.update_layout(
        title_text='Period of Stay Comparison', # title of plot
        xaxis_title_text= 'Allowed Period', # xaxis label
        yaxis_title_text= 'Occurence', # yaxis label
    )

    fig2_json = json.dumps(fig2, cls=plotly.utils.PlotlyJSONEncoder)
    return fig2_json

def EDA_Type3():
    dfx = fullframe() 
    fig3 = px.histogram(dfx, x = 'property_type', color = 'bed_type')
    fig3.update_layout(
    title_text='Melbourne Airbnb Asset Type', # title of plot
    xaxis_title_text= 'Property and Bed Type ', # xaxis label
    yaxis_title_text= 'Assets', # yaxis label
)
    fig3_json = json.dumps(fig3, cls=plotly.utils.PlotlyJSONEncoder)
    return fig3_json

def EDA_Type4():
    dfx = fullframe()
    labels = list(dfx['room_type'].value_counts().index)
    values = list(dfx['room_type'].value_counts().values)
    fig4 = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.5)])
    fig4_json = json.dumps(fig4, cls=plotly.utils.PlotlyJSONEncoder)
    return fig4_json

def EDA_Type5():
    fig5 = go.Figure(data=go.Scatterpolar(
    r=[9000, 8000, 4445, 2400, 2050],
    theta=['Apartment','Town House','House', 'Villa',
            'Boutique Hotel'],
    fill='toself'
    ))

    fig5.update_layout(
    polar=dict(
        radialaxis=dict(
        visible=True
        ),
    ),
    showlegend=False
    )
    fig5_json = json.dumps(fig5, cls=plotly.utils.PlotlyJSONEncoder)
    return fig5_json

def EDA_Type6():
    dfx = fullframe()
    fig6 = px.scatter_geo(dfx,lat='latitude',lon='longitude',animation_frame='property_type',projection='natural earth')
    fig6_json = json.dumps(fig6, cls=plotly.utils.PlotlyJSONEncoder)
    return fig6_json

def EDA_Type7(x):
    sw = stopwords.words("english")
    all_words = ' '.join(list(x))
    list_all_words = all_words.split()
    word_count = Counter(list_all_words)
    word_count_series = pd.Series(word_count)
    word_stopwords = []
    for item in word_count_series.index:
        if(item not in sw):
            word_stopwords.append(item)
    word_count_series = word_count_series.loc[word_stopwords]
    most_appeared_word = word_count_series.sort_values(ascending = False).head(20)
    word_frame = pd.DataFrame(most_appeared_word).reset_index()
    word_frame.columns = ['Important Words', 'Word Counts']
    fig7 = px.bar(word_frame, x ='Important Words', y ='Word Counts')
    fig7_json = json.dumps(fig7, cls=plotly.utils.PlotlyJSONEncoder)
    return fig7_json






    

