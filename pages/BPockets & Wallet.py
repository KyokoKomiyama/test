import streamlit as st
import pandas as pd
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from PIL import Image
import csv

# Bページタブ 
image = Image.open('fish.png')
st.set_page_config(
    page_title="BPockets & Wallet", 
    page_icon=image, 
    layout="wide", 
    initial_sidebar_state="auto"
)

#サイトアイコンの表示
image = Image.open("ロゴベージュ2.png")
st.markdown(
    """
    <style>
    .img-container {
        position: fixed;
        top: 10px;
        right: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 画像を読み込む
image = Image.open("ロゴベージュ2.png")

# 画像を表示する
st.image(
    image,
    caption="",
    use_column_width=True,  # ページの幅に合わせる
)

# スタイルを適用する
st.markdown(
    """
    <style>
    .stApp {
        max-width: 100%;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
# スペースを空けるためのdiv
st.write("<div></div>", unsafe_allow_html=True)  

#メニュー名を表示する
import base64

def image_to_base64(image_path):
    with open(image_path, 'rb') as f:
        img_bytes = f.read()
        return base64.b64encode(img_bytes).decode()
st.markdown('<p style="font-family:HGP創英角ﾎﾟｯﾌﾟ体; color:DeepPink ; font-size: 40px;"><img src="data:image/png;base64,{}" alt="魚の画像" style="width:40px;height:40px;"> Pockets （欲しいものリスト）</p>'.format(image_to_base64("fish.png")),
            unsafe_allow_html=True)

# 商品情報をスクレイピングする関数
def scrape_product_info(url):
    """
    商品情報をスクレイピングする関数
    :param url: スクレイピングする商品ページのURL
    :return: スクレイピング結果を格納したDataFrame
    """
    try:
        # ChromeDriverManagerを使用してWebブラウザを起動する
        browser = webdriver.Chrome(ChromeDriverManager().install())

        # 商品情報をスクレイピングするコードをここに書く
        browser.get(url)

        # 商品名を取得
        name_elem = browser.find_element(By.ID, "_name")
        product = name_elem.text
        print("商品名: ", product)

        # 価格を取得
        price_xpath = '//span[contains(.,"¥")]'
        price_elem = browser.find_element(By.XPATH, price_xpath)
        price = price_elem.text
        print("価格: ", price)

        # Webブラウザを終了する
        browser.quit()

        # 商品情報をDataFrameに格納する
        df = pd.DataFrame({
            "商品名": [product],
            "価格": [price]
        })

        return df
    except Exception as e:
        st.error(f"エラーが発生しました：{e}")
        
# Streamlitアプリ
def main():
    # CSVファイルのパス
    csv_file_path = "./nyantech_pockets.csv"

    # CSVファイルからデータを読み込み
    def read_csv_file(file_path):
        """
        CSVファイルを読み込んでPandasデータフレームに変換する関数
        :param file_path: 読み込むCSVファイルのパス
        :return: CSVファイルの内容を格納したPandasデータフレーム
        """
        try:
            csv_df = pd.read_csv(file_path)
            return csv_df
        except Exception as e:
            st.error(f"エラーが発生しました：{e}")

    # スペースを空けるためのdiv
    st.write("<div></div>", unsafe_allow_html=True) 

    #メニュー名を表示する
    st.markdown('<p style="font-family:HGP創英角ﾎﾟｯﾌﾟ体; color:DeepPink; font-size: 25px;">気になるアイテムがあったらここに入れるにゃ🐾</p>', unsafe_allow_html=True)    
    
    # スクレイピングするURLを入力
    url = st.text_input("商品のURLを入力してにゃん♪")

    # スクレイピング開始ボタンが押されたらスクレイピングを実行
    if st.button("Pocketsに追加するにゃー"):
        df = scrape_product_info(url)
        if df is not None:
            # スクレイピング結果をテーブルに表示
            df.index += 1  # インデックスを1から始める
            st.write(df)

            # CSVファイルに追記保存
            with open(csv_file_path, mode="a", encoding="utf-8", newline="") as f:
                df.to_csv(f, header=f.tell() == None, index=False)
            st.success("Pocketsに追加したにゃん♪")

    # CSVファイルからデータを読み込み
    csv_df = read_csv_file(csv_file_path)

    # インデックスを1から始める
    csv_df.index += 1

    # スペースを空けるためのdiv
    st.write("<div></div>", unsafe_allow_html=True) 

    # 読み込んだデータを表示
    if csv_df is not None:
        st.markdown('<p style="font-family:HGP創英角ﾎﾟｯﾌﾟ体; color:DeepPink; font-size: 25px;">あなたの選んだ商品はこれにゃ🐾</p>', unsafe_allow_html=True)
        st.write(csv_df)

if __name__ == "__main__":
    main()

# スペースを空けるためのdiv
st.write("<div></div>", unsafe_allow_html=True) 

#メニュー名を表示する
st.markdown('<p style="font-family:HGP創英角ﾎﾟｯﾌﾟ体; color:DeepPink ; font-size: 40px;"><img src="data:image/png;base64,{}" alt="魚の画像" style="width:40px;height:40px;"> Wallet (予算管理)</p>'.format(image_to_base64("fish.png")),
            unsafe_allow_html=True)

#メニュー名を表示する
st.markdown('<p style="font-family:HGP創英角ﾎﾟｯﾌﾟ体; color:DeepPink; font-size: 25px;">あなたの予算と比較してみるにゃん🐾</p>', unsafe_allow_html=True)


# データを読み込む
data = pd.read_csv('./nyantech_pockets.csv')

# データの前処理
data['価格'] = data['価格'].str.replace('¥', '').str.replace(',', '').fillna(0).astype(int)
data = data.dropna(subset=['価格']) # NaNを含む行を削除

# 予算額を入力するUIの作成
# budget = st.number_input('予算額を入力してにゃ🐾', value=0)
budget = int(st.text_input('予算額を入力してにゃ♪', value=0))

if budget > 0:
    # 予算関連の情報を計算する
    if st.session_state.get('selected_products') is None or st.session_state['selected_products'].empty:
        if not st.session_state.get('remaining_budget', None):
            st.session_state['remaining_budget'] = budget
    else:
        selected_products = st.session_state['selected_products']
        remaining_budget = budget - selected_products['価格'].sum()
        st.session_state['remaining_budget'] = max(0, remaining_budget)
        
    # メニュー名を表示する 
    st.markdown('<p style="font-family:HGP創英角ﾎﾟｯﾌﾟ体; color:DeepPink; font-size: 25px;">おさいふのなかみにゃん🐾</p>', unsafe_allow_html=True)

    # 画像を表示する
    image_path = 'ad.png'
    close_button = ""
    if not st.session_state.get('close_button_clicked', False):
        st.image(image_path, caption='', width=600)

        # 画像を閉じる
        # st.write('closeをクリックで画像が閉じます')
        close_button = st.button('close')

    if close_button:
        st.session_state['close_button_clicked'] = True
        st.experimental_rerun()

    if not st.session_state.get('close_button_clicked', False):
        # 画像が閉じられていない場合は、ここで処理を終了する
        pass
    else:
        # 予算関連の情報を表示する
        st.write('🐠予算額', budget, '円にゃ🐾')
        selected_products = data[data['価格'] <= st.session_state['remaining_budget']]
        remaining_budget = st.session_state['remaining_budget'] 
        remaining_budget -=selected_products['価格'].sum()
        st.session_state['remaining_budget'] = max(0, remaining_budget)

        # 選択商品価格合計額を表示する
        st.write(f"🐠選択した商品の合計額：{selected_products['価格'].sum()} 円にゃ🐾")

        # 残りの予算を表示する
        st.write(f"🐠残りの予算：{remaining_budget} 円にゃ🐾")

        if remaining_budget < 0:
            st.session_state['remaining_budget'] = 0

# スペースを空けるためのdiv
st.write("<div></div>", unsafe_allow_html=True) 

# テキストにリンクを設定
st.markdown(
f'<a href="http://localhost:8501/A素敵な部屋づくり" target="_blank" rel="noopener noreferrer" '
'style="font-family:HGP創英角ﾎﾟｯﾌﾟ体; color:DeepPink ; font-size: 18px; '
'text-decoration:none;" '
'onmouseover="this.style.color=\'red\';" '
'onmouseout="this.style.color=\'Magenta\';">'
'🐾A 素敵な部屋づくり はこちらから</a>',
unsafe_allow_html=True
)

# サイドバーにロゴ表示する
# 画像ファイルの読み込み
img = Image.open("nyanrogo.png")

# サイドバーに画像を表示する
st.sidebar.image(img, caption="", use_column_width=True)