# Yahoo!Financeから株価取得
## インポート
以下のライブラリをインポートする
```
import yfinance as yf
```

## データの取得
yf.Ticker(企業リスト)とすることで、各企業の株価を取得できる
```
# tickersに企業のティッカーシンボルを格納
tickers = {
    'apple': 'AAPL',
    'facebook': 'META',
    'google': 'GOOGL',
    'microsoft': 'MSFT',
    'netflix': 'NFLX',
    'amazon': 'AMZN'
}

# for文を回し、企業ごとに取り出す
for company in tickers.keys():
    # tkrにcompanyの株価を格納
    tkr = yf.Ticker(tickers[company])
```

yf.Ticker().histroy(period=期間)とすることで、任意の期間分取り出せる
```
# 5日分
days = 5

for company in tickers.keys():
    # tkrにcompanyの株価を格納
    tkr = yf.Ticker(tickers[company])
    # histにdays分の株価を格納
    hist = tkr.history(period=f'{days}d')
    # '日 月 年'の形の値をhistのインデックスとする
    hist.index = hist.index.strftime('%d %B %Y')
    # 終値を取得する
    hist = hist[['Close']]
```


# Altairによるグラフの可視化
## インポート
以下のライブラリをインポートする
```
import altair as alt 
```

## グラフの設定
表示するグラフの設定をする必要がある。
```
chart = (
    # alt chartに数値のリスト(data)を渡す
    alt.Chart(data)
    # ラインの設定
    .mark_line(opacity = 0.8, clip = True)
    .encode(
        # x軸の設定
        x = "Date:T",
        # y軸の設定
        y = alt.Y("Stock Prices(USD):Q", stack = None, scale = alt.Scale(domain=[ymin, ymax])),
        color = 'Name:N'
    )
)
```

## グラフの表示
st.altair_chart(グラフの設定)とすることで、Streamlitを用いて簡単にグラフを表示することができる。
```
# グラフの設定を渡す。コンテンツに合うように幅を調整する。
st.altair_chart(chart, use_container_width = True) 
```