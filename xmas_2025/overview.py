import streamlit as st
from PIL import Image, ImageOps


def load_fixed_image(path):
    img = Image.open(path)
    return ImageOps.exif_transpose(img)


st.title("Christmas 2025 Kit Overview")

text_c, pic_c = st.columns(2)

with text_c:
    st.page_link("xmas_2025/first_box.py", label="#1 - Large: September 18 - October 2 (Serge the Beaver)")
    st.page_link("xmas_2025/second_box.py", label="#2 - Small: October 2 - October 6")
    st.page_link("xmas_2025/third_box.py", label="#3 - Small: October 6 - October 9")
    st.page_link("xmas_2025/fourth_box.py", label="#4 - Large: October 9 - October 23")
    st.page_link("xmas_2025/fifth_box.py", label="#5 - Medium: October 23 - October 27")
    st.page_link("xmas_2025/sixth_box.py", label="#6 - Small: October 27 - October 30")
    st.page_link("xmas_2025/seventh_box.py", label="#7 - Large: October 30 - November 13")
    st.page_link("xmas_2025/eighth_box.py", label="#8 - Medium: November 13 - November 17")
    st.page_link("xmas_2025/ninth_box.py", label="#9 - Small: November 17 - November 20")
    st.page_link("xmas_2025/tenth_box.py", label="#10 - Large: November 20 - December 4")
    st.page_link("xmas_2025/eleventh_box.py", label="#11 - Medium: December 4 - December 8")
    st.page_link("xmas_2025/twelfth_box.py", label="#12 - Medium: December 8 - December 11")

with pic_c:
    st.image(load_fixed_image("xmas_2025/pictures/box_lid.jpeg"), width="stretch")
    st.image(load_fixed_image("xmas_2025/pictures/box_flaps.jpeg"), width="stretch")
    st.image(load_fixed_image("xmas_2025/pictures/box_open.jpeg"), width="stretch")
    st.image(load_fixed_image("xmas_2025/pictures/open_first_box.jpeg"), width="stretch")