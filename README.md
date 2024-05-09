# 음악이 정신건강에 미치는 영향에 대한 데이터 분석



## 출처
streamlit 사이드바 꾸밀 때 사용한 코드
https://luvris2.tistory.com/121

데이터 세트
https://www.kaggle.com/code/dikshaaswal/music-and-mental-health-analysis

예측 할때 이미지 사진 출처
https://m.health.chosun.com/svc/news_view.html?contid=2023110102356

메인화면 음악사진 출처
https://www.mediafine.co.kr/news/articleView.html?idxno=3271

## 1.프로젝트 소개
음악은 스트레스를 완화시키며, 우리의 기분을 고조시켜 우울증이나 불안을 극복하게 합니다.  
하지만 어떠한 경우에는 음악을 들어도 오히려 역효과가 나타 날 수 있고, 효과가 없을 수도 있습니다.  
이 프로젝트는 음악이 정서적으로 어떤 영향을 미치는지에 대해 알기 위해 진행하였습니다.

## 2. 개발 일련 과정

#### 환경 설정
- 크롬에서 아나콘다 및 파이썬을 다운로드하여 설치합니다.
- 데이터 가공 및 인공지능 개발을 위해 쥬피터 노트북을 설치합니다.

#### 깃허브 레포지토리 생성

- 깃허브 레포지토리를 생성합니다.
- 깃허브 데스크탑을 설치하지 않은 경우 설치합니다.

#### 로컬에서 클론

- 깃허브에서 Desktop을 통해 클론하거나 직접 깃허브 데스크탑에서 파일 경로를 복사하여 클론합니다.
- 클론한 경로로 이동한 후 데이터를 저장할 새 폴더(data)를 생성합니다.

#### 데이터 가공

- 아나콘다 프롬프트를 열고 해당 경로로 이동합니다.
- 쥬피터 노트북을 실행합니다.
- 데이터를 가공합니다.

#### 가상환경 설정

- 새로운 가상환경을 생성하고 필요한 라이브러리를 설치합니다.
  ```bash
  conda create -n 가상환경이름 python=3.10 openssl numpy scipy matplotlib ipython scikit-learn pandas pillow jupyter seaborn

 - 가상환경을 활성화합니다.
 - conda activate 가상환경이름
- Visual Studio Code(VSC)를 열고 해당 가상환경으로 전환합니다.

#### Streamlit 설치
- 가상환경에서 Streamlit을 설치합니다. (예: pip install streamlit)
- 파일을 생성하고 Streamlit을 실행하여 정상 작동을 확인합니다. (예: streamlit run 파일이름)