import streamlit as st
import csv
import xml.etree.ElementTree as ET
import time
import pandas as pd
import lxml


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


xml_data_in_valid = """<?xml version="1.0" encoding="UTF-8"?>
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

xml_data_in_NOT_valid = """<?xml version="1.0" encoding="UTF-8"?>
<invoice>
  <header>
    <customer>ABC s.r.o</customer>
    <total_sum>33333.00</total_sum>
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

# Frontend part

st.write("------")

st.write("# 1) Predefined file - sum matches")
st.image("Pictures/XML 2.png")

if st.download_button("Download",data = xml_data_in_valid  , file_name="XML_sum matching.xml"):
    st.info("Download will happen in few seconds")

st.write("------")

st.write("# 2) Predefined file - sum does not match")
st.image("Pictures/XML 3.png")
if st.download_button("Download",data = xml_data_in_NOT_valid  , file_name="XML_sum not matchining.xml"):
    st.info("Download will happen in few seconds")

st.write("------")

st.write("# 3) XML template with no values")
st.image("Pictures/XML 1.png")
if st.download_button("Download",data = xml_data_empty , file_name="XML_empty_template.xml"):
    st.info("Download will happen in few seconds")

st.write("------")