import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title("Interactive Widgets")
# チェックボックスによる画像の表示制御
if st.checkbox("Show Image") :
    img = Image.open('../src/sample.jpg')
    st.image(img, caption='NCS logo', use_container_width=True)

# セレクトボックス
option = st.selectbox(
    'あなたが好きな数字を教えてください',
    list(range(1, 11))
)
## テキストの表示
'あなたの好きな数字は，', option, 'です'


# テキスト入力
option_text = st.text_input('あなたの趣味を教えてください')
'あなたの趣味：', option_text


# スライダー
## st.slider(text，最小値，最大値，初期値)
condition = st.slider('あなたの今の調子は？', 0, 100, 50)
'コンディション：', condition