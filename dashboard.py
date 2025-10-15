import streamlit as st
import pandas as pd
import sqlite3

@st.cache_data
def load_data():
    conn = sqlite3.connect('baseball.db')
    df = pd.read_sql('SELECT * FROM events', conn)
    conn.close()

    return df

st.set_page_config(page_title = 'Baseball History Dashboard', layout = 'wide')
st.title('Baseball History Dashboard')

df = load_data()

years = sorted(df['Year'].unique())
selected_year = st.selectbox('Select Year', years)
filtered = df[df['Year'] == selected_year]

st.subheader('Events in', selected_year)
st.dataframe(filtered)

stat_counts = filtered[1].value_counts().reset_index()
stat_counts.columns = [1, 'Count']

st.bar_chart(stat_counts.set_index(1))
st.write(df.head())
