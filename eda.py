import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
from matplotlib import font_manager, rc
import platform
plt.rcParams['axes.unicode_minus'] = False
if platform.system() == 'Linux':
    rc('font', family='NanumGothic')

def eda_st():
    df = pd.read_csv('music_mental.csv')
    df =    df.iloc[ : , 1 : ]
    

    tab1, tab2= st.tabs(['데이터 살펴보기' , '장르가 정서에 미치는 영향'])

    with tab1: 

        data_de = ['데이터 전체보기','통계치']
        radio_data = st.radio('버튼을 선택해 주세요',data_de)
        if radio_data == data_de[0]:
            st.write('#### 음악 장르에 따른 청취 빈도')  
            st.info('Never:절대   Rarely:드물게   Sometimes:때때로   Very frequently:매우 자주')
            st.write('#### 불안, 우울증, 불면증 및 OCD를 0~10점 척도로 평가')
            st.info('0에 가까울 수록 증상이 없고, 10에 가까울 수록 증상이 매우 심함을 나타냄')
            st.dataframe(df)
        elif radio_data == data_de[1]:
            st.dataframe(df.describe())



        st.title('설문에 참여한 나이 분포도')
        bins = [10, 20, 30, 40, 50, 60,70]
        labels = ['10대', '20대', '30대', '40대', '50대', '60대']

        # 'Age_group' 열 생성
        df['나이 그룹'] = pd.cut(df['나이'], bins=bins, labels=labels)
        # 'Age_group'에 따른 빈도수 계산
        age_counts_ = df.groupby(['나이 그룹']).size()
        # 막대 그래프 생성
        fig, ax = plt.subplots()
        age_counts_.plot(kind='bar', color=['black', 'red', 'pink', 'orange', 'blue', 'skyblue'], ax=ax)
        # 그래프 크기 조정
        fig.set_size_inches(10, 5)
        # 그래프를 Streamlit에 표시
        st.pyplot(fig)


        color1 = sb.color_palette("magma",3)

    # 그래픽 차트 생성
        st.subheader('작업 중 스트리밍을 듣는 횟수 및 비율')
        fig1, axes = plt.subplots(1, 2, figsize=(15, 10))

        # 작업 중 스트리밍에 대한 countplot
        sb.countplot(data=df, x="작업 중 스트리밍", palette=color1, ax=axes[0])

        # 작업 중 스트리밍에 대한 파이 차트 
        axes[1].pie(df["작업 중 스트리밍"].value_counts(), colors=color1, labels=["Yes", "No"], autopct="%0.1f%%")
        axes[1].legend()

        # 그래프를 Streamlit에 표시
        st.pyplot(fig1)




        st.write('#### 장르 분포도')
        fig2, ax1 = plt.subplots(figsize=(15, 5))

        # 선호 음악 장르에 대한 countplot
        sb.countplot(data=df, x="선호 음악 장르", ax=ax1)
        plt.xticks(rotation=45)

        st.pyplot(fig2)





if __name__ == '__main__':
    eda_st()