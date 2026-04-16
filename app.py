import streamlit as st

st.title("Note Summary and Quiz Generator")
st.markdown("upload upto 3 images to generate note summary and Quizzes")
st.divider()

with st.sidebar:
    st.header("Controls")
    img = st.file_uploader(
        "upload the photos of your note",
        type = ['jpg','jpeg','png'],
        accept_multiple_files=True
    )

    if img:
        if len(img)>3:
            st.error("upload at max 3 img")
        else:
            col = st.columns(len(img))

            st.subheader("your uploaded image")

            for i,img in enumerate(img):
                with col[i]:
                    st.image(img)
                    