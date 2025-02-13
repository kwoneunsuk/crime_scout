import streamlit as st

#  기계학습 모델 파일 로드(모델명 : _______)
import joblib
model = joblib.load('crime_scout_LinearRegression_model.pkl')

# 만든 모델로 테스트 데이터에 대해 예측하기
st.title('안심스카우트정책 기반 범죄 발생 건수 예측하기')

col1, col2 = st.columns(2)

with col1:
      st.subheader(' 1. 기계학습 모델 제작과정 ')
      st.write(' - 기계학습 알고리즘 : 선형회귀 ')
      st.write(' - 학습 데이터 출처 : https://www.kaggle.com/')
      st.write(' - 훈련    데이터 : 90건')
      st.write(' - 테스트 데이터 : 9건')
with col2:
      st.subheader('2. 기계학습 모델의  성능')
      image_path = '/content/prediction.png' # 로컬 이미지 파일 경로
      st.image(image_path )   # 이미지 불러오기

st.subheader('예측 연도')
st.write('범죄발생 건수를 예측하여 알려드립니다.')

# 사용자 입력
a = st.number_input("예측연도(2025~2028)", min_value=0)

# 예측 버튼 만들기
if st.button("예측하기"):
        input_data = [[a]]
        p = model.predict(input_data)
         # 단순 조건문으로 예측 결과 출력
        if p[0] == 1:
              st.success('인공지능 분류 결과는 합격입니다........... 그러나, 방심은 금물입니다!')
        else:
              st.success('인공지능 분류 결과는 불합격입니다............... 더 열심히 공부하면 됩니다!')
