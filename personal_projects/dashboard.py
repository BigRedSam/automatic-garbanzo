import dash
from dash import dcc
from dash import html
import plotly.express as px
import pandas as pd

app = dash.Dash()

long_df = px.data.medals_long()

fig = px.bar(long_df, x="nation", y="count",
             color="medal", title="Long-Form Input")
fig.show()

# df = pd.read_csv("~/Downloads/MOCK_DATA_2.csv")

# fig = px.scatter(
#     df,
#     x="weight",
#     y="life_expectency",
#     size="id",
#     color="country_of_origin",
#     hover_name="common_name",
#     #log_x=True,
#     size_max=60,
# )

# app.layout = html.Div([dcc.Graph(id="life-exp-vs-gdp", figure=fig)])


# if __name__ == "__main__":
#     app.run_server(debug=True)