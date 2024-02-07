import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import requests

# e-Stat APIから日本の人口データを取得する関数
def fetch_population_data(api_key, stats_data_id):
    API_URL = 'https://api.e-stat.go.jp/rest/3.0/app/json/getStatsData'
    params = {
        'appId': api_key,
        'lang': 'J',
        'statsDataId': stats_data_id,
        'metaGetFlg': 'Y',
        'cntGetFlg': 'N',
        'sectionHeaderFlg': '1',
    }
    response = requests.get(API_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        # ここでデータをパースしてDataFrameに変換する処理を追加
        # 以下はダミーのDataFrameを返す例
        df = pd.DataFrame({
            '年': [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019],
            '人口': [128057352, 127833000, 127629000, 127445000, 127276000, 127141000, 126994511, 126785797, 126529100, 126264931]
        })
        return df
    else:
        return pd.DataFrame()

# メイン関数
def main():
    st.title('日本の人口ダッシュボード')

    # e-Stat APIキーと統計データIDを設定
    API_KEY = 'あなたのAPIキー'
    STATS_DATA_ID = '統計データID'

    df = fetch_population_data(API_KEY, STATS_DATA_ID)

    st.write("### 日本の人口データ (2010-2019)")
    st.dataframe(df)

    st.write("### 人口推移グラフ")
    fig, ax = plt.subplots()
    ax.plot(df['年'], df['人口'], marker='o')
    ax.set_xlabel('年')
    ax.set_ylabel('人口')
    ax.set_title('日本の人口推移 (2010-2019)')
    st.pyplot(fig)

if __name__ == "__main__":
    main()