import streamlit as st
from PIL import Image
import base64

avatar = Image.open("media/5350_3d-removebg_small.png")
#fav_icon = Image.open("media/")

# App Title
app_title = "Piper's Links "
app_description = ""

# Page Config
st.set_page_config(
    page_title = app_title, 
    #page_icon = fav_icon, 
    #layout = "wide",
    #initial_sidebar_state="collapsed"
    )

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-position: right bottom;
        background-repeat: no-repeat;
    }}
    </style>
    """,
    unsafe_allow_html=True
    )

def img_to_bytes(img_path):
    img_bytes = Path(img_path).read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded

def create_button(title, link, icon):

    st.markdown(
    f"""
    <div class="">
        {icon} <a href="{link}">{title}</a>
    </div>
    """,
    unsafe_allow_html=True
    )

# styles.css
with open('styles.css') as style:
    st.markdown(f'<style>{style.read()}</style>', unsafe_allow_html=True)

add_bg_from_local('media/5350_3d-removebg.png') 

# content


col1, col2, col3 = st.columns(3)
with col1:
    header_html = "<img src='data:image/png;base64,{}' id='avatar' />".format(img_to_bytes("header.png"))
    st.markdown(
        header_html, unsafe_allow_html=True,
    )
    st.header('Piper')

st.subheader('On-chain Data Analyst, Flipside Crypto Community Moderator')

st.text('')
st.text('')



st.markdown(f"""🐦 twitter: <a href=\"https://twitter.com/der_piper\" target=\"_blank\"> piper</a>""", unsafe_allow_html=True)

st.text('')
st.text('')

#footer
col1,col2 = st.columns(2)
with col2:
   st.text('© 2022 - Made with ❤️ in Potsdam')