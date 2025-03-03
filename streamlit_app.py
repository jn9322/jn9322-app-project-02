import streamlit as st


# pages = {
#     "XML Parsing": [
#         #st.Page("Subpages/welcome.py", title="Welcome"),
#         st.Page("Subpages/XML_dowload.py", title="XML download"),
#         st.Page("Subpages/XML_parsing_to_txt_outcome.py", title="XML parsing"),
#         #st.Page("Subpages/testuju.py", title="TESTUJU")
#     ]
# }

# pg = st.navigation(pages)
# pg.run()

# --- SHARED ON ALL PAGES ---
st.logo("Pictures/Logo2.png", size='large')

testuju = st.Page("Subpages/testuju.py", title="TESTUJU")
app_description = st.Page("Subpages/application_description.py", title="Application Description")
download = st.Page("Subpages/XML_dowload.py", title="Download")
parsing = st.Page("Subpages/XML_parsing_to_txt_outcome.py", title="XML parsing")

pg = st.navigation(
    {
        "Welcome": [app_description],
        #"Testuju": [testuju],
        "Parsing": [parsing,download]
    }
)
pg.run()




