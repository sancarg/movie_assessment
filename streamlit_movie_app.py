import streamlit as st
import numpy as np
import pandas as pd
import altair as alt

# Set the page configuration 
st.set_page_config(page_title="Movie Insights Analyzer", page_icon="📽", layout="wide")

st.header('Movie Assessment App')
st.info('This is a machine learning app for TMDB 3000+ Movie Dataset!')

st.markdown('**What can you do with this app?**')
st.info('This application demonstrates the capabilities of Pandas for data manipulation, Altair for visualizing charts, and an interactive dataframe for user engagement.')
st.markdown('**How to use the app?**')
st.warning('To engage with the app, 1. Select genres of your interest in the drop-down selection box and then 2. Select the year duration from the slider widget. As a result, this should generate an updated editable DataFrame and line plot.')

# Question header
st.subheader('Which Movie Genre performs ($) best at the box office?')
# Load data - Read CSV into a Pandas DataFrame
# Convert the Relesa_Date column to datetime format:
df['Release_Date'] = pd.to_datetime(df['Release_Date'], format='%m/%d/%Y')
# Extract the year and convert it to integer:
df['Year'] = df['Release_Date'].dt.year
# Ensure the 'Year' column is of integer type:
df['Year'] = df['Year'].astype(int)

# Extract unique genres from the DataFrame 
genres_list = df['genre'].unique() 
# Create a multiselect dropdown menu for genre selection 
genres_selection = st.multiselect( 
  label='Select genres', # Dropdown label 
  options=genres_list, # List of genres to choose from 
  default=['Action', 'Adventure', 'Biography', 'Comedy', 'Drama', 'Horror'] # Default selected genres 
)
