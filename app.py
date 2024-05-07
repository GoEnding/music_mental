import streamlit as st
from streamlit_option_menu import option_menu
import streamlit.components.v1 as html
import matplotlib.pyplot as plt
from  PIL import Image
import numpy as np
import pandas as pd 
import plotly.express as px
import io

from matplotlib import font_manager, rc
import platform
plt.rcParams['axes.unicode_minus'] = False
if platform.system() == 'Linux':
    rc('font', family='NanumGothic')

from home import home_st
from eda import eda_st
from ml import ml_st

def main():
    with st.sidebar:
        choose = option_menu("음악과 정신", ["메인화면", "EDA", "머신 러닝"],
                            icons=['house', 'kanban', 'bi bi-reddit'],
                            menu_icon="bi bi-music-note-beamed", default_index=0,
                            styles={
            "container": {"padding": "5!important", "background-color": "#fafafa"},
            "icon": {"color": "black", "font-size": "25px"}, 
            "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
            "nav-link-selected": {"background-color": "#02ab21"},
        }
        )
    if choose == '메인화면':
        home_st()
    elif choose == 'EDA':
        eda_st()

    elif choose == '머신 러닝':
        ml_st()

    # 선택된 메뉴에 따라 함수 호출
if __name__ == '__main__':
    main()