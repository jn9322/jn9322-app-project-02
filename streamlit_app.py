import streamlit as st

# --- SHARED ON ALL PAGES ---
st.logo("Pictures/Logo2.png", size='large')


# Pages as objects
testuju = st.Page(
    "Subpages/testuju.py",
    title="TESTUJU"
    )

app_description_ArM = st.Page(
    "Subpages/application_description_archimate.py",
    title="Application Description Archimate"
    )

app_description_BPMN = st.Page(
    "Subpages/application_description_BPMN.py",
    title="Application Description BPMN"
    )

download = st.Page(
    "Subpages/XML_dowload.py",
    title="XML - Download"
    )

xsd = st.Page(
    "Subpages/XML_XSD_schema.py",
    title="XML - XSD, XML Schema"
    )

parsing = st.Page(
    "Subpages/XML_parsing_to_txt_outcome.py",
    title="XML - Parsing"
    )


# Navigation
pg = st.navigation(
    {
        "Welcome": [app_description_ArM , app_description_BPMN],
        "Testuju": [testuju],
        "XML Data Parsing": [xsd , download , parsing]
    }
)
pg.run()




