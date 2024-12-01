import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title("Streamlit 入門")

st.write('Interactive Widgets')

# サイドバーに追加 st.sidebar.
text = st.sidebar.text_input('あなたの趣味を教えて')
'あなたの趣味：', text
condition = st.sidebar.slider('あなたの今の調子は？', 0, 100, 50)
'コンディション：', condition

# 2カラムレイアウト
left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラムです')

expander1 = st.expander('問い合わせ1')
expander1.write('問い合わせ1の回答')
expander2 = st.expander('問い合わせ2')
expander2.write('問い合わせ2の回答')
expander3 = st.expander('問い合わせ3')
expander3.write('問い合わせ3の回答')