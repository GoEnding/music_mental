import streamlit as st
import pandas as pd
import joblib
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import MinMaxScaler
def ml_st():
    df = pd.read_csv('music_mental.csv')
    df = df.iloc[ : , 1: ]
    st.subheader('정신건강에 음악이 효과가 있을지 예측하기')
    #  <일단 입력 받아야 할 값(컬럼)을 전부 나열해주기>
    # '나이', '하루 스트리밍 시간', '작업 중 스트리밍', '악기 연주', '작곡가', '선호 음악 장르', '음악 탐색',
    # '외국어 가사', 'BPM', '클래식 음악 빈도', '미국 음악 빈도', 'EDM 빈도', '민요 빈도',
    # '기독교 음악 빈도', '힙합 빈도', '재즈 빈도', 'K-pop 빈도', '라틴 음악 빈도', 'Lofi 청취 빈도',
    # '메탈 청취 빈도', '팝 빈도', 'R&B 빈도', '랩 빈도', '락 빈도', '게임 음악 빈도', '불안 장애',
    # '우울증', '불면증', '강박증'


    st.write('###### 나이를 입력해 주세요.')
    age = st.number_input('나이 입력', min_value=18, max_value=80, value= 24)

    st.write('###### 하루에 음악을 몇시간 들으시나요?')
    day_hours = st.slider('데이터 선택', 0.0, 24.0, 0.0, 0.5)


    job_music_key = "job_music"
    inst_key = "inst"
    compose_key = 'compose'
    quest_key = 'quest'
    language_key = 'language'
    key = ['Yes','No']
    # st.radio()를 호출할 때마다 다른 키를 사용합니다.
    job_music = st.radio('일을 하실 때 노래를 들으시면서 하시나요?', key=job_music_key, options=key)
    if job_music == 'Yes':
        job_music = 1
    elif job_music == 'No':
        job_music = 0

    inst = st.radio('응답자는 정기적으로 악기를 연주하는 편인가요?', key=inst_key, options=key)
    if inst == 'Yes':
        inst = 1
    elif inst == 'No':
        inst = 0

    compose = st.radio('응답자는 작곡을 하시나요?', key=compose_key, options=key)
    if compose == 'Yes':
        compose = 1
    elif compose == 'No':
        compose = 0

    music_select = ['Classical','Country','EDM','Folk','Gospel','Hip hop','Jazz','K pop','Latin','Lofi','Metal','Pop','R&B','Rap','Rock','Video game music']
    my_choice = st.selectbox('가장 좋아하는 장르 한개를 선택해 주세요',music_select)
    print(my_choice)
    st.info(f'가장 좋아하는 장르는{my_choice}입니다')
    
    quest = st.radio('응답자는 새로운 아티스트/장르를 적극적으로 탐색하나요?', key=quest_key, options=key)
    if quest == 'Yes':
        quest = 1
    elif quest == 'No':
        quest = 0
    
    language = st.radio('자신이 유창하지 않은 언어로 가사가 있는 음악을 정기적으로 듣나요?', key=language_key, options=key)
    if language == 'Yes':
        language = 1
    elif quest == 'No':
        language = 0

    st.write('###### 주로 듣는 노래들의 BPM이 몇인지 입력해주세요.')
    bpm = st.number_input('BPM 입력', min_value=0, max_value=200, value= 120)

    st.subheader('※장르별 음악을 얼마나 자주 듣는지 골라주시면 됩니다.')
    st.info('Never:절대   Rarely:드물게   Sometimes:때때로   Very frequently:매우 자주')
    fre_select = ['Never', 'Rarely', 'Sometimes', 'Very frequently']
    my_select1 = st.select_slider('클래식 음악을 얼마나 들으시나요?',fre_select)

    my_select2 = st.select_slider('미국 음악을 얼마나 들으시나요?',fre_select)

    my_select3 = st.select_slider('EDM 음악을 얼마나 들으시나요?',fre_select)
    
    my_select4 = st.select_slider('민요를 얼마나 들으시나요?',fre_select)

    my_select5 = st.select_slider('기독교 음악을 얼마나 들으시나요?',fre_select)

    my_select6 = st.select_slider('힙합을 얼마나 들으시나요?',fre_select)

    my_select7 = st.select_slider('재즈를 얼마나 들으시나요?',fre_select)

    my_select8 = st.select_slider('K-pop을 얼마나 들으시나요?',fre_select)

    my_select9 = st.select_slider('라틴 음악을 얼마나 들으시나요?',fre_select)

    my_select10 = st.select_slider('lofi음악을 얼마나 들으시나요?',fre_select)

    my_select11 = st.select_slider('메탈 음악을 얼마나 들으시나요?',fre_select)

    my_select12 = st.select_slider('팝송을 얼마나 들으시나요?',fre_select)

    my_select13 = st.select_slider('R&B 음악을 얼마나 들으시나요?',fre_select)

    my_select14 = st.select_slider('랩을 얼마나 들으시나요?',fre_select)

    my_select15 = st.select_slider('락을 얼마나 들으시나요?',fre_select)

    my_select16 = st.select_slider('게임음악을 얼마나 들으시나요?',fre_select)

    st.write('#### 불안, 우울증, 불면증 및 OCD를 0~10점 척도로 평가')
    st.info('0에 가까울 수록 증상이 없고, 10에 가까울 수록 증상이 매우 심함을 나타냄')
    anx = st.slider('불안장애가 있나요?', 0.0, 10.0, 0.0, 1.0)
    dep = st.slider('우울증이 있나요?', 0.0, 10.0, 0.0, 1.0)
    slp = st.slider('불면증이 있나요?', 0.0, 10.0, 0.0, 1.0)
    ocd = st.slider('강박증이 있나요?', 0.0, 10.0, 0.0, 1.0)

    if st.button('예측하기'):
        classifier = joblib.load('classifier.pkl')
        print(classifier)
        ct = joblib.load('ct1.pkl')
 
        # 범주형 변수를 One-hot encoding하여 새로운 열을 생성
        
        
        new_data = [age, day_hours, job_music, inst, compose,my_choice, quest, language, bpm, my_select1, my_select2, my_select3, my_select4,
                    my_select5, my_select6, my_select7, my_select8, my_select9, my_select10, my_select11, my_select12, my_select13,
                    my_select14, my_select15, my_select16, anx, dep, slp, ocd]
        
        print(new_data)

        new_data = np.array(new_data).reshape(1, -1)
        print(new_data)
        new_data = ct.transform(new_data)
        print(new_data)
        y_pred = classifier.predict(new_data)
        print(y_pred)
        st.text(f'{y_pred}')


if __name__ == '__main__':
    ml_st()