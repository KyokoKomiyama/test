import streamlit as st
import time
import pandas as pd
from PIL import Image

#TOPページタブ 
image = Image.open('cat.png')
st.set_page_config(
    page_title="A素敵な部屋づくり", 
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

#ページタイトル
import base64

def image_to_base64(image_path):
    with open(image_path, 'rb') as f:
        img_bytes = f.read()
        return base64.b64encode(img_bytes).decode()
st.markdown('<p style="font-family:HGP創英角ﾎﾟｯﾌﾟ体; color:DeepPink ; font-size: 40px;"><img src="data:image/png;base64,{}" alt="猫の画像" style="width:40px;height:40px;"> 素敵な部屋づくり</p>'.format(image_to_base64("cat.png")),
            unsafe_allow_html=True)

# CSVファイルからデータを読み込む
df = pd.read_csv("./おすすめサイト選択肢.csv", encoding='utf-8', index_col=None)

# リンク列にリンクを追加する
df["リンク"] = df["URL"].apply(lambda url: f'<a href="{url}" target="_blank">{url}</a>')
df = df.drop('リンク', axis=1)

# インデックスを表示しないように設定する
html = df.to_html(escape=False, index=False)

# スペースを空けるためのdiv
st.write("<div></div>", unsafe_allow_html=True) 

# ユーザーが選択した部屋タイプとアイテムを取得する
# 部屋タイプ
st.markdown('<p style="font-family:HGP創英角ﾎﾟｯﾌﾟ体; color:DeepPink; font-size: 25px;">どんな部屋にしたいにゃ🐾</p>', unsafe_allow_html=True)

# 画像のパスをリストで用意する
image_paths = ["image6.png", "image7.png", "image8.png",
               "image9.png", "image10.png", "image11.png"]

# 画像を5つずつ分割する
image_chunks = [image_paths[i:i+6] for i in range(0, len(image_paths), 6)]

# 画像を表示する
for image_chunk in image_chunks:
    cols = st.columns(len(image_chunk))
    for col, image_path in zip(cols, image_chunk):
        image = Image.open(image_path)
        col.image(image, use_column_width=True)


# # メニュー名を表示する_ 部屋タイプを取得
selected_room_types = None
def my_function():
    global selected_room_types
    selected_room_types = st.multiselect('🐠好みのタイプを選んでにゃん♪', df['room-type'].unique())
my_function()

# スペースを空けるためのdiv
st.write("<div></div>", unsafe_allow_html=True) 

# アイテム
st.markdown('<p style="font-family:HGP創英角ﾎﾟｯﾌﾟ体; color:DeepPink; font-size: 25px;">探しているアイテムは何だにゃ🐾</p>', unsafe_allow_html=True)

# 5つの画像を開く
img1 = Image.open("image1.png")
img2 = Image.open("image2.png")
img3 = Image.open("image3.png")
img4 = Image.open("image4.png")
img5 = Image.open("image5.png")

# 5つの画像を横に並べるコンテナを作成
col1, col2, col3, col4, col5 = st.columns(5)

# 5つの画像をコンテナ内に表示
with col1:
    st.image(img1, width=80, caption="インテリア")
with col2:
    st.image(img2, width=80, caption="ペット用品")
with col3:
    st.image(img3, width=80, caption="ファブリック")
with col4:
    st.image(img4, width=80, caption="電化製品")
with col5:
    st.image(img5, width=80, caption="食器")

# メニュー名を表示する_ アイテムを取得
selected_items = st.multiselect('🐠アイテムを選んでにゃん♪', df['item'].unique())

# スペースを空けるためのdiv
st.write("<div></div>", unsafe_allow_html=True) 

# メニュー名を表示する_ おすすめサイト提示
st.markdown('<p style="font-family:HGP創英角ﾎﾟｯﾌﾟ体; color:DeepPink; font-size: 25px;">あなたにおススメのサイトはこれにゃ🐾</p>', unsafe_allow_html=True)
st.write('🐠ここから探してみるにゃん♪')

# フィルタリングされたデータを表示する
filtered_df = df[(df['room-type'].isin(selected_room_types)) & (df['item'].isin(selected_items))]
if filtered_df.empty:
    st.warning('該当するデータはありません')
else:
    filtered_df['URL'] = filtered_df['URL'].apply(lambda url: f'<a href="{url}" target="_blank">{url}</a>')
    st.write(filtered_df.to_html(index=False, escape=False), unsafe_allow_html=True)

# スペースを空けるためのdiv
st.write("<div></div>", unsafe_allow_html=True) 

# テキストにリンクを設定
st.markdown(
f'<a href="http://localhost:8501/BPockets_&_Wallet" target="_blank" rel="noopener noreferrer" '
'style="font-family:HGP創英角ﾎﾟｯﾌﾟ体; color:DeepPink ; font-size: 18px; '
'text-decoration:none;" '
'onmouseover="this.style.color=\'red\';" '
'onmouseout="this.style.color=\'Magenta\';">'
'🐾B Pockets&Wallet はこちらから</a>',
unsafe_allow_html=True
)

# サイドバーにロゴ表示する
# 画像ファイルの読み込み
img = Image.open("nyanrogo.png")

# サイドバーに画像を表示する
st.sidebar.image(img, caption="", use_column_width=True)