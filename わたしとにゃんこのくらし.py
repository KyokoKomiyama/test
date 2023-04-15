import streamlit as st
import time
import pandas as pd
from PIL import Image

#TOPページタブ 
image = Image.open('nyantech.png')
st.set_page_config(
    page_title="わたしとにゃんこのくらし", 
    page_icon=image, 
    layout="wide", 
    initial_sidebar_state="auto"
)

#サイトアイコンの表示
image = Image.open("ロゴベージュ.png")
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
image = Image.open("ロゴベージュ.png")

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

st.markdown('<p style="font-family:メイリオ; color:DarkSlateGray ; font-size: 20px;">わたしとにゃんこのくらし ではにゃんこ好きな人もそうでない人も、わたしだけのおしゃれな素敵なお部屋づくりを目指す女性を応援しています♪ あなたとにゃんこの暮らしが心ゆたかでありますように🐾</p>',
            unsafe_allow_html=True)

# スペースを空けるためのdiv
st.write("<div></div>", unsafe_allow_html=True) 

#メニュー
import base64

def image_to_base64(image_path):
    with open(image_path, 'rb') as f:
        img_bytes = f.read()
        return base64.b64encode(img_bytes).decode()
st.markdown('<p style="font-family:HGP創英角ﾎﾟｯﾌﾟ体; color:DeepPink ; font-size: 40px;"><img src="data:image/png;base64,{}" alt="猫の画像" style="width:40px;height:40px;"> メニュー</p>'.format(image_to_base64("nyantech.png")),
            unsafe_allow_html=True)

#メニュー画像ファイルの読み込み
import streamlit as st
import pathlib

col1, col2 = st.columns(2)

with col1:
    # ファイルのパスを取得
    file_path = pathlib.Path("pages/A素敵な部屋づくり.py").resolve().as_uri()
    
    # テキストにリンクを設定
    st.markdown(
    f'<a href="http://localhost:8501/A素敵な部屋づくり" target="_blank" rel="noopener noreferrer" '
    'style="font-family:HGP創英角ﾎﾟｯﾌﾟ体; color:HotPink ; font-size: 30px; '
    'text-decoration:none;" '
    'onmouseover="this.style.color=\'red\';" '
    'onmouseout="this.style.color=\'Magenta\';">'
    '素敵な部屋にしたい🐾</a>',
    unsafe_allow_html=True
)
    
    st.image("図1.png", use_column_width=True)

with col2:
    # テキストにリンクを設定
    st.markdown(
        f'<a href="http://localhost:8501/A素敵な部屋づくり" target="_blank" rel="noopener noreferrer" '
        'style="font-family:HGP創英角ﾎﾟｯﾌﾟ体; color:HotPink ; font-size: 30px; '
        'text-decoration:none;" '
        'onmouseover="this.style.color=\'red\';" '
        'onmouseout="this.style.color=\'Magenta\';">'
        "街の情報が知りたい🐾</a>",
        unsafe_allow_html=True
    )
    
    st.image("図2.png", use_column_width=True)

# サイドバーにロゴ表示する
# 画像ファイルの読み込み
img = Image.open("nyanrogo.png")

# サイドバーに画像を表示する
st.sidebar.image(img, caption="", use_column_width=True)