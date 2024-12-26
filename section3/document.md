# stremlitの準備
## インストール
pythonが使える環境にて、pip installを行う
```
pip install streamlit
```

## デモ
インストール後、下記のコマンドを入力することによってブラウザでStreamlitのデモを実際に動かすことができる。
```
streamlit hello
```

## ドキュメント
[公式サイト](https://docs.streamlit.io/)にて、Stremlitのリファレンスを参照できる。


# streamlitの基本的な使い方
## インポート
pythonプログラム上で、streamlitをインポートする。asとすることで、別名として使うことができる。
```
import streamlit as st
```

## タイトル
st.title()で、タイトルを表示できる。
```
st.title('タイトル')
```

## テキスト
st.write()で、テキストの表示ができる。
```
st.write('テキスト')
```

## 表
### write
st.write()で表の表示もできる。
```
import pandas as pd

df = pd.DataFrame({
    '1列目':[1, 2, 3, 4],
    '2列目':[10, 20, 30, 40]
})

st.write(df)
```

### dataframe
st.dataframe()でも表示が可能
```
st.dataframe(df)
```
こっちは、引数でいろいろな指定が可能
```
# 幅と高さを指定
st.dataframe(df, width=100, height=100)

# 列での最大値をハイライト
st.dataframe(df.style.highlight_max(axis=0))
```

### table
st.table()で静的な表を表示可能（ソート等ができない）
```
st.table(df)
```

## インタラクティブなウィジェット
### チェックボックス
st.checkbox()とすることで、チェックボックスの表示が可能
```
# checkboxの状態(true or false)によって、画像の表示非表示を切り替える
if st.checkbox("Show Image") :
    img = Image.open('../src/sample.jpg')

    # st.image()は画像の表示が可能
    st.image(img, caption='NCS logo', use_container_width=True)
```

### セレクトボックス
st.selectbox()でプルダウンを表示できる
```
# selectboxの結果をoptionに代入
option = st.selectbox(
    # セレクトボックスのタイトル
    'あなたが好きな数字を教えてください',
    # セレクトボックスの選択肢
    list(range(1, 11))
)
# セレクトボックスで選んだ値を表示
'あなたの好きな数字は，', option, 'です'
```

### スライダー
st.sliderでスライダーを表示できる
```
# st.slider(タイトル, 最小値, 最大値, 初期値)
condition = st.slider('あなたの今の調子は？', 0, 100, 50)
# スライダーで選んだ値を表示
'コンディション：', condition
```

## サイドバー
st.sidebar.〇〇〇とすることで、任意のアイテムをサイドバーに追加できる。
```
# textに、text_inputで入力した文字列を代入
text = st.sidebar.text_input('あなたの趣味を教えて')
'あなたの趣味：', text

# conditionに、sliderで入力した値を代入
condition = st.sidebar.slider('あなたの今の調子は？', 0, 100, 50)
'コンディション：', condition
```

## 2カラムレイアウト
st.columns()を使うことで、Webページ状で列に分割して表示できる
```
# 2カラムの左側と右側をそれぞれleft_column, right_columnとして扱う
left_column, right_column = st.columns(2)
# 左カラムにボタンを追加する
button = left_column.button('右カラムに文字を表示')
# 左カラムのボタンが押されたとき、右カラムにテキストを表示する
if button:
    right_column.write('ここは右カラムです')
```

## プログレスバー
st.progress()とすることで、プログレスバーを表示できる
```
# プログレスバー定義
latest_interation = st.empty()
bar = st.progress(0)

# プログレスバー更新処理
for i in range(100):
    ## 現在の状況をテキスト表示
    latest_interation.text(f'Iteration {i+1}')
    ## プログレスバーにてfor文のiを表示する
    bar.progress(i + 1)
    ## 0.1秒スリープ
    time.sleep(0.1)
    
# プログレスバーの処理が終了次第、テキストを表示
'Done !!!!!'
```