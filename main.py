import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

col1, col2, col3 = st.columns([2.5, 5, 2.5])

with col2:
  st.title("Terrain profile")

col4, col5, col6 = st.columns([2, 6, 2])

with col5:
  st.markdown('Prepare the csv file with x and y columns as below')

col7, col8, col9 = st.columns([3.5, 3, 3.5])
with col8:
  df = pd.read_csv('test_df.csv')
  st.dataframe(df)

col10, col11, col12 = st.columns([3.2, 3.6, 3.2])
with col11:
  st.markdown('Upload your **CSV file** below')

uploaded_file = st.file_uploader("Choose a CSV file", type=['csv'])
if uploaded_file is not None:
  #read csv
  df1=pd.read_csv(uploaded_file)

  min = df1['y'].min() - 1
  max = df1['y'].max() + 1

  maxx = df1['x'].max()

  #st.dataframe(df1)
  fig = go.Figure()

  WATERlevel = float(st.number_input(f"**Set the water level in meters above the sea level** (range between {min} and {max})", min_value = min, max_value = max))
  TITLE = st.text_input("**Set tittle of your graph**")
  #Choosing language
  # Define a list of language options
  language_options = ['Polish', 'English', 'Spanish']

  # Display a selectbox for the user to choose a language
  selected_language = st.selectbox('Select a language [PL, ENG, ESP]', language_options)

  fig.add_trace(go.Scatter(x = [df1['x'].max(), df1['x'].min()], y = [WATERlevel, WATERlevel] , fill = 'tonexty', mode='lines', line_color='rgb(52,128,242)'))
  fig.add_trace(go.Scatter(x=df1['x'], y=df1['y'], fill='tozeroy', fillcolor='rgb(223,142,35)', mode='lines', line_color='orange'))

  if selected_language == 'Polish':
    fig.update_layout(
      yaxis_range=(min, max),
      title=TITLE, title_x=0.5,
      xaxis=dict(title='odległość [m]'),
      yaxis=dict(title='wysokość [m n.p.m.]'),
      showlegend=False
    )
  elif selected_language == 'English':
    fig.update_layout(
      yaxis_range=(min, max),
      title=TITLE,
      xaxis=dict(title='distance [meters]'),
      yaxis=dict(title='elevation [meters above sea level]'),
      showlegend=False
    )
  elif selected_language == 'Spanish':
    fig.update_layout(
      yaxis_range=(min, max),
      title=TITLE,
      xaxis=dict(title='distancia [metros]'),
      yaxis=dict(title='altitud [metros sobre el nivel del mar]'),
      showlegend=False
    )
  st.plotly_chart(fig)

else:
  st.warning('You need to upload a csv file above')

