import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title("Streamlit 入門")

st.write('プログレスバーの表示')
'Start!'

# プログレスバー定義
latest_interation = st.empty()
bar = st.progress(0)

# プログレスバー更新処理
for i in range(100):
    # bar.progress(i)
    latest_interation.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)
    
'Done !!!!!'

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