import plotly.plotly as py
import plotly.graph_objs as go

import pandas as pd
from datetime import datetime
from IPython.display import IFrame

df = pd.read_csv('https://raw.githubusercontent.com/asahi-nino/clutch_players/master/clutch_fg.csv')

trace_dnowitski = go.Scatter(
    x=df.Date,
    y=df['Dirk Nowitski'],
    name = "Dirk Nowitski",
    line = dict(color = '#173bcf'),
    opacity = 0.8)

trace_ljames = go.Scatter(
    x=df.Date,
    y=df['Lebron James'],
    name = "Lebron James",
    line = dict(color = '#cf5417'),
    opacity = 0.8)

trace_kirving = go.Scatter(
    x=df.Date,
    y=df['Kyrie Irving'],
    name = "Kyrie Irving",
    line = dict(color = '#2c7f13'),
    opacity = 0.8)

trace_kdurant = go.Scatter(
    x=df.Date,
    y=df['Kevin Durant'],
    name = "Kevin Durant",
    line = dict(color = '#279cbc'),
    opacity = 0.8)

trace_scurry = go.Scatter(
    x=df.Date,
    y=df['Stephen Curry'],
    name = "Stephen Curry",
    line = dict(color = '#0c62b2'),
    opacity = 0.8)

trace_dlillard = go.Scatter(
    x=df.Date,
    y=df['Damian Lillard'],
    name = "Damian Lillard",
    line = dict(color = '#ad0a0a'),
    opacity = 0.8)

trace_kleonard = go.Scatter(
    x=df.Date,
    y=df['Kawhi Leonard'],
    name = "Kawhi Leonard",
    line = dict(color = '#514f4f'),
    opacity = 0.8)

trace_kbryant = go.Scatter(
    x=df.Date,
    y=df['Kobe Bryant'],
    name = "Kobe Bryant",
    line = dict(color = '#750b7c'),
    opacity = 0.8)

trace_jharden = go.Scatter(
    x=df.Date,
    y=df['James Harden'],
    name = "James Harden",
    line = dict(color = '#db0a0a'),
    opacity = 0.8)

data = [trace_dnowitski, trace_ljames, trace_kirving, trace_kdurant, trace_scurry, trace_dlillard, trace_kleonard, trace_kbryant, trace_jharden]

updatemenus = list([
    dict(active=-1,
         buttons=list([   
            dict(label = 'Dirk Nowitski',
                 method = 'update',
                 args = [{'visible': [True, False, False, False, False, False, False, False, True]},
                         {'title': 'Dirk Nowitski'}]),
            dict(label = 'Lebron James',
                 method = 'update',
                 args = [{'visible': [False, True, False, False, False, False, False, False, True]},
                         {'title': 'Lebron James'}]),
            dict(label = 'Kyrie Irving',
                 method = 'update',
                 args = [{'visible': [False, False, True, False, False, False, False, False, True]},
                         {'title': 'Kyrie Irving'}]),
            dict(label = 'Kevin Durant',
                 method = 'update',
                 args = [{'visible': [False, False, False, True, False, False, False, False, True]},
                         {'title': 'Kevin Durant'}]),
            dict(label = 'Stephen Curry',
                 method = 'update',
                 args = [{'visible': [False, False, False, False, True, False, False, False, True]},
                         {'title': 'Stephen Curry'}]),
            dict(label = 'Damian Lillard',
                 method = 'update',
                 args = [{'visible': [False, False, False, False, False, True, False, False, True]},
                         {'title': 'Damian Lillard'}]),
            dict(label = 'Kawhi Leonard',
                 method = 'update',
                 args = [{'visible': [False, False, False, False, False, False, True, False, True]},
                         {'title': 'Kawhi Leonard'}]),
            dict(label = 'Kobe Bryant',
                 method = 'update',
                 args = [{'visible': [False, False, False, False, False, False, False, True, True]},
                         {'title': 'Kobe Bryant'}]),
            dict(label = 'James Harden',
                 method = 'update',
                 args = [{'visible': [False, False, False, False, False, False, False, False, True]},
                         {'title': 'James Harden'}]),
            dict(label = 'All',
                 method = 'update',
                 args = [{'visible': [True, True, True, True, True, True, True, True, True]},
                         {'title': 'All'}])
        ]),
    )
])

layout = dict(title='Is James Harden Clutch?', showlegend=False,
              updatemenus=updatemenus)

# layout = dict(
#     title = "NBA Clutchness",
#     xaxis = dict(
#         range = ['2001-07-01','2019-07-01'])
# )



fig = dict(data=data, layout=layout)

py.iplot(fig, filename = "Is James Harden Clutch?", fileopt = 'new')

IFrame(src= "https://dash-simple-apps.plotly.host/nba-clutchness/", width="100%", height="750px", frameBorder="0")


