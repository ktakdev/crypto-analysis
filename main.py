from google.cloud import bigquery
import plotly.express as px


client = bigquery.Client()

query = """
    SELECT *
    FROM `btcdataanalysis.binance.daily_summary`
"""

df = client.query(query).to_dataframe()
fig = px.line(df, x="date", y="price_gc_rate_7_25_usdt")
fig.update_xaxes(dtick="D1")
fig.update_yaxes(range=[0, 1])

fig.show()
