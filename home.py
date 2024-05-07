import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from  PIL import Image
from matplotlib import font_manager, rc
import platform
plt.rcParams['axes.unicode_minus'] = False
if platform.system() == 'Linux':
    rc('font', family='NanumGothic')


def home_st():
    st.title('음악이 정신건강에 미치는 영향')
    st.write('###### 음악치료(MT)는 개인의 스트레스, 기분,전반적인 정신 건강을 개선하기 위해 음악을 사용하는 것입니다')
    st.write('###### MT는 또한 음악을 옥시토신과 같은 "행복한" 호르몬의 촉매제로 사용하는 증거 기반 실천으로 인정받고 있습니다.')
    st.link_button('출처입니다',url='https://www.kaggle.com/datasets/catherinerasgaitis/mxmh-survey-results/data',use_container_width=True)
    st.image('https://cdn.mediafine.co.kr/news/photo/201508/3271_4634_292.jpg',width= 700.0)

if __name__ == '__main__':
    home_st()