import streamlit as st
from dotenv import load_dotenv
from langchain_community.document_loaders import WebBaseLoader

from chains import Chain
from utils import cleanText

load_dotenv()

st.set_page_config(layout="wide", page_title="Article To Tweet", page_icon="📰")
chain = Chain()

st.title('Article To Tweet')
url_input = st.text_input("Enter a URL:", value="https://www.nbcnews.com/news/weather/live-blog/storm-helene-live-updates-rcna173120")
submit_button = st.button("Submit")

if submit_button:
    try:
        loader = WebBaseLoader([url_input])
        data = cleanText(loader.load().pop().page_content)
        res = chain.summarizeArticle(data)
        st.code(res)
    except Exception as e:
        st.error(f"An Error Occurred: {e}")
    