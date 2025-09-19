import streamlit as st


xmas_overview = st.Page("xmas_2025/overview.py", title="Kit Overview", icon=":material/ac_unit:")
first_box = st.Page("xmas_2025/first_box.py", title="Box #1", icon=":material/redeem:")


nav = {
    "Christmas Toy to the World Advent 2025": [
        xmas_overview, first_box
    ]
}

pg = st.navigation(nav)

st.set_page_config(page_title="Woobles Tracking", page_icon=":material/pets:", layout="wide")

pg.run()