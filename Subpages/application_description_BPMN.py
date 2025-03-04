import streamlit as st

st.write("### BPMN diagrams:")
st.write("*For better visibility - put cursor on the picture and click on the icon in the right upper corner")

st.write("-----")
st.write("#### Application process flow:")
st.image("Pictures/BPMN flow.png")
st.write(" 5 stages of process - high level")


st.write("-----")
st.write("##### Data parsing process:")
st.image("Pictures/BPMN data parsing.png")
st.write("Principle of data parsing process from XML")

st.write("-----")
st.write("##### Data validation process:")
st.image("Pictures/BPMN Validation process.png")
st.write("The application includes validation of the data <sum_total> (Invoice summary of price) against price per item <price>. If match, application displays green success note, If not match, application displays warrning message and providing correct summary calculated. In BOTH CASES application ALLOWS to continue to data vizualization step.")

st.write("-----")
st.write("##### Data vizualization process:")
st.image("Pictures/BPMN data visualization.png")
st.write("Posibility of data visualization from the parsed data. Either simple overview of header info or table of items including pie chart and bar chart. It can be switched between these 2 options/buttons.")