import plotly.plotly as py
import plotly.graph_objs as go
from plotly.offline import iplot


df['claps'].iplot(kind='hist', xTitle='claps',
        yTitle='count', title='Claps Distr')
