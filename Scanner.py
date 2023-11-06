import streamlit as st
import re


trigger_words = [
    "xunux.ch",
    "http://steamcommumity.ru/=gift&7854901254",
    "chappiz.com",
    "http://freenitro.gift/",
    "ww1.steamcommunidy.com"
]


# Function to check if a domain name is present in the trigger words list
def is_phishing_website(url):
    for word in trigger_words:
        if re.search(word, url):
            return True
    return False


# User interface
st.title('Cyber Safe Clicks')

url = st.text_input('Enter URL:')

if url:
    result = is_phishing_website(url)

    if result:
        st.error('WARNING: The link you uploaded is a PHISHING!')
    else:
        st.success('The link you uploaded is a SAFE!')