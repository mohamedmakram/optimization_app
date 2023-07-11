import streamlit as st
import pandas as pd
import plotly.express as px
import itertools
import plotly.graph_objects as go
from plotly.subplots import make_subplots


st.title('Optimizing Trading Strategies')

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
   


   fig = px.line(df, x='TimeStamp', y='Closed P/L', color='MagicNo.', markers=True)
   fig = go.Figure(data=go.Scatter(x=df['TimeStamp'], y=df['Closed P/L'], ))

   fig = go.Figure()
   negative_profit = go.Figure() 
   for i in strategy:
      df_strategy = df[df['MagicNo'] == i]
      fig.add_trace(go.Scatter(x=df_strategy['TimeStamp'], y=df_strategy['ClosedP/L'],
         name=str(i),

      ))

      # Edit the layout
      fig.update_layout(title='strategy Comparison',
                  xaxis_title='TimeStamp',
                  yaxis_title='Closed P/L')

   st.plotly_chart(fig)

      #  Magic No 6835025
   negative_profit = df.groupby('MagicNo')['FloatingProfit'].agg('min')
   lastpl = df.groupby('MagicNo')['ClosedP/L'].agg('last')
 
   # strategies = [str(s) for s in negative_profit.index]
   strategies = ['0', '4750', '47100', '47200', '475025', '475050', '4750200']

   plot = go.Figure(data=[go.Bar(
      x = strategies, 
      y= negative_profit.values,
     name='Negative Profit'),
   go.Bar(
      x = strategies, 
      y= lastpl.values,
      name = 'Last PL')
       
   ], )

   st.plotly_chart(plot)