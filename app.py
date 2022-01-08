import pandas as pd
import streamlit as st

import clan
import family_tree

st.set_page_config(page_icon="🍄", page_title="Butiiko Clan",
layout="wide", 
menu_items={
         'Get Help': None,
         'Report a bug': None,
         'About': "# This is a header. This is an *extremely* cool app!"
     })

Pages ={
    "Clan" : clan,
    "Family Tree": family_tree
}

st.sidebar.title("🍄")

page_selected = st.sidebar.selectbox('Navigation',list(Pages.keys()))
app_page = Pages[page_selected]

app_page.app()
