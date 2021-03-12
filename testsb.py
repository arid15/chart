import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv('C:/Users/ASUS/Pictures/Silsilah_Update.csv')

fig = go.Figure(go.Sunburst(
        ids = df.ids,
        labels = df.labels,
        parents = df.parents))
fig.update_layout(
    autosize=False,
    width=1500,
    height=1500,)
fig.show()