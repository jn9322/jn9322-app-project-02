import streamlit as st

# --- SHARED ON ALL PAGES ---
st.logo("Pictures/Logo2.png", size='large')


# Pages as objects
testuju = st.Page(
    "Subpages/testuju.py",
    title="TESTUJU"
    )

app_purpose = st.Page(
    "Subpages/Purpose_of_app.py",
    title="Purpose of this application"
    )

app_description_ArM = st.Page(
    "Subpages/application_description_archimate.py",
    title="Description Archimate"
    )

app_description_BPMN = st.Page(
    "Subpages/application_description_BPMN.py",
    title="Description BPMN"
    )

download = st.Page(
    "Subpages/XML_dowload.py",
    title="1. XML - Download"
    )

xsd = st.Page(
    "Subpages/XML_XSD_schema.py",
    title="Description - XSD, XML Schema"
    )

parsing = st.Page(
    "Subpages/XML_parsing_to_txt_outcome.py",
    title="2. XML - Parsing, Validation, Vizualization"
    )


# Navigation
pg = st.navigation(
    {
        "About this application": [app_purpose , app_description_ArM , app_description_BPMN , xsd],
        #"Testuju": [testuju],
        "Application functions": [download , parsing]
    }
)
pg.run()




