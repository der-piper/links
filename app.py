import streamlit as st
from PIL import Image
import base64

background_img = Image.open("media/5350_3d-removebg.png")
#fav_icon = Image.open("media/")

# App Title
app_title = "Piper's Links "
app_description = ""

# Page Config
st.set_page_config(
    page_title = app_title, 
    #page_icon = fav_icon, 
    layout = "wide",
    initial_sidebar_state="collapsed"
    )

# styles.css

with open('styles.css') as style:
    st.markdown(f'<style>{style.read()}</style>', unsafe_allow_html=True)

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('media/5350_3d-removebg.png') 


st.header('Piper')
st.subheader('On-chain Data Analyst, Flipside Crypto Community Moderator')

st.text('')
st.text('')

st.markdown(f"""🐦 twitter: <a href=\"https://twitter.com/der_piper\" target=\"_blank\"> piper</a>""", unsafe_allow_html=True)

st.text('')
st.text('')

col1,col2 = st.columns(2)
with col2:
   st.text('© 2022 - Made with ❤️ in Potsdam')