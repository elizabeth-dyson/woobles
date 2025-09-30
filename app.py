import streamlit as st


xmas_overview = st.Page("xmas_2025/overview.py", title="Kit Overview", icon=":material/ac_unit:")
first_box = st.Page("xmas_2025/first_box.py", title="Box #1", icon=":material/redeem:")
second_box = st.Page("xmas_2025/second_box.py", title="Box #2", icon=":material/redeem:")
third_box = st.Page("xmas_2025/third_box.py", title="Box #3", icon=":material/redeem:")
fourth_box = st.Page("xmas_2025/fourth_box.py", title="Box #4", icon=":material/redeem:")
fifth_box = st.Page("xmas_2025/fifth_box.py", title="Box #5", icon=":material/redeem:")
sixth_box = st.Page("xmas_2025/sixth_box.py", title="Box #6", icon=":material/redeem:")
seventh_box = st.Page("xmas_2025/seventh_box.py", title="Box #7", icon=":material/redeem:")
eighth_box = st.Page("xmas_2025/eighth_box.py", title="Box #8", icon=":material/redeem:")
ninth_box = st.Page("xmas_2025/ninth_box.py", title="Box #9", icon=":material/redeem:")
tenth_box = st.Page("xmas_2025/tenth_box.py", title="Box #10", icon=":material/redeem:")
eleventh_box = st.Page("xmas_2025/eleventh_box.py", title="Box #11", icon=":material/redeem:")
twelfth_box = st.Page("xmas_2025/twelfth_box.py", title="Box #12", icon=":material/redeem:")


nav = {
    "Christmas Toy to the World Advent 2025": [
        xmas_overview, 
        first_box, second_box, third_box, fourth_box,
        fifth_box, sixth_box, seventh_box, eighth_box,
        ninth_box, tenth_box, eleventh_box, twelfth_box
    ]
}

pg = st.navigation(nav)

st.set_page_config(page_title="Woobles Tracking", page_icon=":material/pets:", layout="wide")

pg.run()