import streamlit as st
from PIL import Image, ImageOps


def load_fixed_image(path):
    img = Image.open(path)
    return ImageOps.exif_transpose(img)


st.title("Box 4. Large: October 9 - October 23")

text_c, pic_c = st.columns(2)

with text_c:
    st.subheader("Opened October 5: Documentation")

    st.write("Materials:")
    
    st.write("- Box #4: Looks like some sort of candy cane jet pack.")
    st.write("- 1 large roll of orange yarn")
    st.write("- 1 small roll of tan yarn")
    st.write("- 1 package of stuffing")
    st.write("- 1 yellow 4.0 mm crochet hook")
    st.write("- 1 envelope of information...")

    st.write("Envelope contents:")
    st.write("- 1 extra small roll of black yarn")
    st.write("- 1 tapestry needle")
    st.write("- 3 eye attachments")
    st.write("- 1 informational card:")
    st.write("- 'LANA THE ALPACA'")
    st.write("- 'EMPLOYEE ID CARD'")
    st.write("- 'NAME: Lana'")
    st.write("- 'ROLE: Head Packer'")
    st.write("- 'TO MAKE GO TO: thewoobles.com/start'")
    st.write("- 'PASSWORD: SJ7Z-64FP'")

    st.subheader("Timeline")

    st.write("HEAD & BODY")
    st.write("✅ 20 rounds")
    st.write("✅ 10/5: Rounds 1-4")
    st.write("✅ 10/6: Rounds 5-8")
    st.write("✅ 10/7: Rounds 9-12")
    st.write("✅ 10/8: Rounds 13-16")
    st.write("✅ 10/9: Rounds 17-20")

    st.write("SNOUT")
    st.write("✅ 3 rounds")
    st.write("✅ 10/10: Rounds 1-3")

    st.write("EARS")
    st.write("✅ 2 rounds x2")
    st.write("✅ 10/11: First Ear")
    st.write("✅ 10/12: Second Ear")

    st.write("LEGS")
    st.write("✅ 2 rounds (x4)")
    st.write("✅ 10/13: First Leg")
    st.write("✅ 10/14: Second Leg")
    st.write("✅ 10/15: Third Leg")
    st.write("✅ 10/16: Fourth Leg")

    st.write("NOSE & MOUTH")
    st.write("✅ 5 steps")
    st.write("✅ 10/17: Steps 1-5")

    st.write("HAIR")
    st.write("- 2 rows")
    st.write("✅ 10/18: Row 1")
    st.write("- 10/19: Row 2")

    st.subheader("Completed on ")


    with pic_c:
        st.image(load_fixed_image("xmas_2025/pictures/box_4_top.jpeg"), width='stretch')
        st.image(load_fixed_image("xmas_2025/pictures/box_4_front.jpeg"), width='stretch')
        st.image(load_fixed_image("xmas_2025/pictures/box_4_sides.jpeg"), width='stretch')
        st.image(load_fixed_image("xmas_2025/pictures/box_4_lid.jpeg"), width='stretch')
        st.image(load_fixed_image("xmas_2025/pictures/box_4_contents.jpeg"), width='stretch')
        st.image(load_fixed_image("xmas_2025/pictures/lana_card_front.jpeg"), width='stretch')
        st.image(load_fixed_image("xmas_2025/pictures/lana_card_back.jpeg"), width='stretch')