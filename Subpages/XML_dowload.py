import streamlit as st
import xml.etree.ElementTree as ET

xml_data_empty = """<?xml version="1.0" encoding="UTF-8"?>
<invoice>
  <header>
    <customer></customer>
    <total_sum></total_sum>
  </header>
  <detail>
    <category></category>
    <product_name></product_name>
    <price></price>
  </detail>
  <detail>
    <category></category>
    <product_name></product_name>
    <price></price>
  </detail>
  <detail>
    <category></category>
    <product_name></product_name>
    <price></price>
  </detail>
</invoice>
"""


xml_data_in = """<?xml version="1.0" encoding="UTF-8"?>
<invoice>
  <header>
    <customer>ABC s.r.o</customer>
    <total_sum>54290.00</total_sum>
  </header>
  <detail>
    <category>PC</category>
    <product_name>HP ProBook</product_name>
    <price>24000.00</price>
  </detail>
  <detail>
    <category>TV</category>
    <product_name>Philips The One</product_name>
    <price>30000.00</price>
  </detail>
  <detail>
    <category>Gaming</category>
    <product_name>Plastation 5 Pro</product_name>
    <price>20290.00</price>
  </detail>
</invoice>
"""



if st.download_button("Download - XML template empty",data = xml_data_empty , file_name="XML_empty_template.xml"):
    st.info("Download will happen in few seconds")

if st.download_button("Download - XML template with data",data = xml_data_in  , file_name="XML_template.xml"):
    st.info("Download will happen in few seconds")
