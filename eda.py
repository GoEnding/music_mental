import streamlit as st
import pandas as pd


def eda_st():
    df = pd.read_csv('music_mental.csv')
    df = df.iloc[ : , 1 : ]
    st.dataframe(df)



if __name__ == '__main__':
    eda_st()