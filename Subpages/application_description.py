import streamlit as st

st.write("ArchiMate diagram:")
st.image("Pictures/Parsing-archimate-diagram-MINI.png")

if st.download_button("Download",data = "Pictures/Parsing-archimate-diagram.png"  , file_name="Archimate.jpeg"):
    st.info("Download will happen in few seconds")