import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

st.header('st.write')

#텍스트와 마크다운 형식의 텍스트 표시
st.write('Hello, *World!* :sunglasses:')
#숫자와 같은 다른 데이터 형식 표시
st.write(1234)
#Dataframe 표시
df =  pd.DataFrame({
    '첫번째 칼럼': [1, 2, 3, 4],
    '두번째 칼럼': [10, 20, 30, 40]})
st.write(df)
#여러 인수 전달
st.write('아래는 데이터 프레임이다:', df, '위에는 데이터 프레임이다.')

df2 = pd.DataFrame(
    np.random.randn(200, 3),
    columns=['a', 'b', 'c'])
c = alt.Chart(df2).mark_circle().encode(
    x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c)
