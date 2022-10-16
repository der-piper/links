import streamlit as st
from PIL import Image
import base64
from pathlib import Path

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

def create_button(prefix, title, link):

    st.markdown(
    f"""
    <div class="link-list" >
        {prefix}: <a href="{link}" target="_blank">{title}</a>
    </div>
    """,
    unsafe_allow_html=True
    )

# styles.css
with open('styles.css') as style:
    st.markdown(f'<style>{style.read()}</style>', unsafe_allow_html=True)

add_bg_from_local('media/5350_3d-removebg.png') 

# content
col1,col2,col3 = st.columns([1,1,6])
with col1:
    header_html = "<img src='data:image/png;base64,{}' class='avatar' id='avatar' />".format(img_to_bytes("media/5350_3d-removebg_small.png"))
    st.markdown(
        header_html, unsafe_allow_html=True,
    )
with col2:
    st.header('Piper')
with col3:
    st.text('')

st.write('On-chain Data Analyst, Flipside Crypto Community Moderator')

st.info('Just a guy who is interested in web3, nft and data analysis 📊 📈 📉 ... ')

st.text('')
st.text('')

create_button('🐦 twitter', '@der_piper','https://twitter.com/der_piper')

create_button('📝 medium', '@der_piper','https://medium.com/@der_piper')

create_button('📝 Flipside Crypto Discord', 'piper#6707','https://discord.gg/enrH6bPA')

create_button('📝 GitHub', 'der-piper','https://github.com/https://github.com/der-piper')



st.text('')
st.text('')

#footer
st.text('© 2022 - Made with ❤️ in Potsdam')