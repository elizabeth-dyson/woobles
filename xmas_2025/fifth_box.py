import streamlit as st
from PIL import Image, ImageOps


def load_fixed_image(path):
    img = Image.open(path)
    return ImageOps.exif_transpose(img)


st.title("Box 5. Medium: October 23 - October 27")

text_c, pic_c = st.columns(2)

with text_c:
    st.subheader("Opened October 31: Documentation")

    st.write("Materials:")

    st.write("- Box #5: Looks like ...")
    st.write("- Contains a small bag:")
    st.write("- 'TINY SPINNING TOP'")

    st.write("- Inside the small bag:")
    st.write("- 1 small roll of red yarn")
    st.write("- 1 small roll of yellow yarn")
    st.write("- 1 small roll of blue yarn")
    st.write("- a small amount of stuffing")
    st.write("- 1 card:")
    st.write("- 'MAKE THIS TINY SPINNING TOP'")
    st.write("- 'Go to: thewoobles.com/start'")
    st.write("- 'Type in the password: SQWK-T6GC'")

    st.subheader("Completed on November 1")

with pic_c:
    st.image(load_fixed_image("xmas_2025/pictures/spinning_top_card.jpeg"), width='stretch')
    st.image(load_fixed_image("xmas_2025/pictures/spinning_top_front.jpeg"), width='stretch')
    st.image(load_fixed_image("xmas_2025/pictures/spinning_top_angle.jpeg"), width='stretch')