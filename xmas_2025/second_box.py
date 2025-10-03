import streamlit as st
from PIL import Image, ImageOps


def load_fixed_image(path):
    img = Image.open(path)
    return ImageOps.exif_transpose(img)


st.title("Box 2. Small: October 2 - October 6")

text_c, pic_c = st.columns(2)

with text_c:
    st.subheader("Opened September 30: Documentation")

    st.write("Materials:")

    st.write("- Box #2: Looks like a desk with letters to Santa on it.")
    st.write("- Contains a small bag:")
    st.write("- 'TINY TOY CANDY'")
    st.write("- 'FESTIVE THINGS COME IN TEENY TINY PACKAGES'")

    st.write("- Inside the small bag:")
    st.write("- 1 small roll of green yarn")
    st.write("- 1 small roll of white yarn")
    st.write("- 1 extra small roll of red yarn")
    st.write("- a small amount of stuffing")
    st.write("- 1 card:")
    st.write("- 'TINY TOY CANDY'")
    st.write("- 'MAKE THIS TINY TOY CANDY'")
    st.write("- 'Go to: thewoobles.com/start'")
    st.write("- 'Type in the password: SYZX-A32W'")

    st.subheader("Timeline")

    st.write("CANDY:")
    st.write("✅ 7 rounds")
    st.write("✅ 10/1: Rounds 1-7 (apparently)")

    st.write("WRAPPERS:")
    st.write("✅ 10/2: First wrapper")
    st.write("✅ 10/3: Second wrapper")

    st.write("STRIPES:")
    st.write("✅ 10/4: Both stripes")

    st.subheader("Completed on October 2")

with pic_c:
    st.image(load_fixed_image("xmas_2025/pictures/box_2_top.jpeg"), width="stretch")
    st.image(load_fixed_image("xmas_2025/pictures/box_2_sides.jpeg"), width="stretch")
    st.image(load_fixed_image("xmas_2025/pictures/candy_card_front.jpeg"), width="stretch")
    st.image(load_fixed_image("xmas_2025/pictures/candy_card_back.jpeg"), width="stretch")
    st.image(load_fixed_image("xmas_2025/pictures/candy_front.jpeg"), width="stretch")
    st.image(load_fixed_image("xmas_2025/pictures/candy_angle.jpeg"), width="stretch")