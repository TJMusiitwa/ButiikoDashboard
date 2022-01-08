import pandas as pd
import plotly.express as px
import streamlit as st
from gsheetsdb import connect


def app():
    st.title('The Butiiko Family Tree')

    con = connect()


    @st.cache(ttl=700)
    def fetch_family_tree(query):
        rows = con.execute(query,headers=1)
        return rows

    sheets_url = st.secrets["family_tree_url"]
    rows = fetch_family_tree(f'SELECT * FROM "{sheets_url}"')   

    tree = pd.DataFrame(rows)
    
    st.dataframe(tree)
