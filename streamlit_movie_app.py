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
df = pd.read_csv('Movies_dataset_cleaned.csv')
# Extract unique genres from the DataFrame 
genres_list = df['Genres'].unique() 
# Create a multiselect dropdown menu for genre selection 
genres_selection = st.multiselect( 
  label='Select Genres', # Dropdown label 
  options=genres_list, # List of genres to choose from 
  default=['Mystery', 'Adventure', 'Thriller', 'Comedy', 'Drama', 'Horror', 'Science Fiction'] # Default selected genres 
)
# Year selection - Create slider for year range selection
year_list = df.Year.unique()
year_selection = st.slider('Select year duration', 1932, 2023, (2000, 2023))
year_selection_list = list(np.arange(year_selection[0], year_selection[1]+1))

# Subset data - Filter DataFrame based on selections
df_selection = df[df.Genres.isin(genres_selection) & df['Year'].isin(year_selection_list)]
reshaped_df = df_selection.pivot_table(index='Year', columns='Genres', values='Revenue', aggfunc='sum', fill_value=0)
reshaped_df = reshaped_df.sort_values(by='Year', ascending=False)
# Apply custom formatting to the DataFrame 
styled_df = reshaped_df.style.format({"Year": "{:.0f}"}) # Format only the Year column
# Display the DataFrame with 
st.dataframe(styled_df, height=212, use_container_width=True)
# Display the DataFrame 
#st.write(reshaped_df)

# Data preparation - Prepare data for charting 
df_chart = pd.melt(reshaped_df.reset_index(), id_vars='Year', var_name='Genres', value_name='Revenue') 

# Display line chart 
chart = alt.Chart(df_chart).mark_line().encode( 
  x=alt.X('Year:N', title='Year'), 
  y=alt.Y('Revenue:Q', title='Revenue Amount ($)'), 
  color='Genres:N').properties(height=320) 
st.altair_chart(chart, use_container_width=True)
