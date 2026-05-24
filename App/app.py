import streamlit as st


st.title("ASL Sign language recognition app")
st.write("Streamlit test")

img_file = st.camera_input("photo")


if st.button("button"):
    st.balloons()
    st.write("works")
