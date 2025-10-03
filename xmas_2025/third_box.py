import streamlit as st
from PIL import Image, ImageOps


def load_fixed_image(path):
    img = Image.open(path)
    return ImageOps.exif_transpose(img)


st.title("Box 3. Small: October 6 - October 9")

text_c, pic_c = st.columns(2)

with text_c:
    st.subheader("Opened October 2: Documentation")

    st.write("Materials:")

    st.write("- Box #3: Looks like a work bench.")
    st.write("- 1 small roll of blue yarn")
    st.write("- 1 extra small roll of white yarn")
    st.write("- Informational Card:")
    st.write("- 'TINY YO-YO'")
    st.write("- 'MAKE THIS TINY YO-YO'")
    st.write("- 'Go to: thewoobles.com/start'")
    st.write("- 'Type in the password: S6NR-AT3Q'")

    st.subheader("Timeline")



    st.subheader("Completed on ")


with pic_c:
    st.image(load_fixed_image("xmas_2025/pictures/box_3_top.jpeg"), width="stretch")
    st.image(load_fixed_image("xmas_2025/pictures/box_3_sides.jpeg"), width="stretch")
    st.image(load_fixed_image("xmas_2025/pictures/yoyo_card_front.jpeg"), width="stretch")
    st.image(load_fixed_image("xmas_2025/pictures/yoyo_card_back.jpeg"), width="stretch")
    