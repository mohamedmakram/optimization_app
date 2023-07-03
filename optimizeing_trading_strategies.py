import streamlit as st
import pandas as pd
import plotly.express as px
import itertools
import plotly.graph_objects as go
from plotly.subplots import make_subplots


st.title('Optimizeing Trading Strategies')

upload_files = st.file_uploader('Choose a CSV file', type='csv', accept_multiple_files=True)

if upload_files:
   df = pd.DataFrame()

   for file in upload_files: 
      df_list = pd.read_csv(file)
      df = pd.concat([df_list, df], axis=0)

   # Merge the DataFrames into one DataFrame
   # data = pd.merge(*df_list, on='SequenceNo', how='inner')

   strategy = df['MagicNo'].unique()
# convert TimeStamp column to datetime type
   df['TimeStamp'] = pd.to_datetime(df['TimeStamp'])

   df.rename(columns={'Closed P/L': 'ClosedP/L', 'Profit': 'FloatingProfit'}, inplace=True)
   


   # fig = px.line(df, x='TimeStamp', y='Closed P/L', color='MagicNo.', markers=True)
   # fig = go.Figure(data=go.Scatter(x=df['TimeStamp'], y=df['Closed P/L'], ))

   fig = go.Figure()

   for i in strategy:
      df_strategy = df[df['MagicNo'] == i]
      fig.add_trace(go.Scatter(x=df_strategy['TimeStamp'], y=df_strategy['ClosedP/L'],
         name=str(i),

      ))

      # Edit the layout
      fig.update_layout(title='strategy Comparison',
                  xaxis_title='TimeStamp',
                  yaxis_title='Closed P/L')



   # # Magic No 6835025
   # trace1_hourly_profit = go.Bar(
   #    x = hourly_profit.index, 
   #    y=hourly_profit['Profit'],
   #    name = 'Profit Close'
   # )

   # figures_hourly_profit = [trace1_hourly_profit]
   # layout = go.Layout(barmode = 'group')
   # fig_hourly_profit = go.Figure(data = figures_hourly_profit, layout = layout)


   # fig_hourly_profit.update_layout(title=dict(text=f"P/L hourly {strategy}"),
   #    xaxis = dict(
   #       tickmode = 'linear')
   # )

   st.plotly_chart(fig)

