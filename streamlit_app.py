import streamlit as st


pages = {
    "Content": [
        st.Page("Subpages/welcome.py", title="Welcome"),
        st.Page("Subpages/XML_parsing_to_txt_outcome.py", title="XML parsing")
    ]
}

pg = st.navigation(pages)
pg.run()


