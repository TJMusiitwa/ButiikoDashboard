import pandas as pd
import plotly.express as px
import streamlit as st
from gsheetsdb import connect


def app():
    st.title('The Butiiko Clan')

    con = connect()

    @st.cache(ttl=700)
    def fetch_clan(query):
        rows = con.execute(query,headers=1)
        return rows


    sheets_url = st.secrets["clan_url"]
    rows = fetch_clan(f'SELECT * FROM "{sheets_url}"')


    clan = pd.DataFrame(rows)
    #st.table(clan)

    fig = px.treemap(clan, 
    path=[px.Constant("Omutaka Gunju"),'Essiga','Omutuba','Nyiriri'],
     color_discrete_map={'Essiga':'gold','Omutuba':'red','(?)':'darkblue'},
     width=1000, height=600
   )
    fig.update_traces(root_color="royalblue",pathbar_textfont_size=20,textfont_size=18)
    fig.update_layout(
        treemapcolorway = ["gold", "darkblue"],
        margin = dict(t=25, l=0, r=15, b=0))

    st.plotly_chart(fig,use_container_width=False)
