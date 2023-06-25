import streamlit as st
import pandas as pd
import plotly.express as px
import itertools
import plotly.graph_objects as go
from plotly.subplots import make_subplots


st.title('Optimizeing Trading Strategies')

upload_files = st.file_uploader('Choose a CSV file', type='csv', accept_multiple_files=True)

if upload_files:

    # Read each file into a DataFrame
   # df = pd.DataFrame()
   try:

      for file in upload_files:
         df = pd.read_csv(file)
         # df = pd.concat([df_list, df], axis=0)

      # Merge the DataFrames into one DataFrame
      # data = pd.merge(*df_list, on='SequenceNo', how='inner')

         strategy = df['MagicNo'].unique()
      # convert TimeStamp column to datetime type
         df['Open Time'] = pd.to_datetime(df['Open Time'])

         # Parameters
         # extract hours
         df['hourly'] = df['Open Time'].dt.hour
         # extract days
         df['days'] = df['Open Time'].dt.day_name()

         # profit data to plot
         # hours profit
         
         hourly_profit = df.groupby(['hourly'])[['Profit']].agg('sum')
         
         # Magic No 6835025
         trace1_hourly_profit = go.Bar(
            x = hourly_profit.index, 
            y=hourly_profit['Profit'],
            name = 'Profit Close'
         )

         figures_hourly_profit = [trace1_hourly_profit]
         layout = go.Layout(barmode = 'group')
         fig_hourly_profit = go.Figure(data = figures_hourly_profit, layout = layout)


         fig_hourly_profit.update_layout(title=dict(text=f"P/L hourly {strategy}"),
            xaxis = dict(
               tickmode = 'linear')
         )

         st.plotly_chart(fig_hourly_profit)
   except:
      print('this is Open file ')
