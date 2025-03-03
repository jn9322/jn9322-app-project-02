import streamlit as st
import xml.etree.ElementTree as ET

# Firstly - data options/XML structures -> objects
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


xml_data_summatch = """<?xml version="1.0" encoding="UTF-8"?>
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

xml_data_sumnotmatch = """<?xml version="1.0" encoding="UTF-8"?>
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

st.set_page_config(page_title="XML download")
st.write("# XML download")
st.write(
    '''
Here you can download XML which can be used for parsing. There are 3 options from which to select.
'''
)

st.write("------")

# Option 1
st.write("#### 1) Predefined file - sum matches")
st.write(
    '''
Simple scenario where <total_sum> field matches the sum of <price> in detail elements.
'''
)
st.image("Pictures/XML 2.png")

if st.download_button("Download",data = xml_data_summatch  , file_name="XML_sum matching.xml"):
    st.info("Download will happen in few seconds")

st.write("------")


# Option 2
st.write("#### 2) Predefined file - sum does not match")
st.write(
    '''
Scenario where <total_sum> field does not matches the sum of <price> in detail elements. Which will be seen in the parsing data step where there is validation of values built.
'''
)
st.image("Pictures/XML 3.png")
if st.download_button("Download",data = xml_data_sumnotmatch  , file_name="XML_sum not matchining.xml"):
    st.info("Download will happen in few seconds")

st.write("------")

# Option 3
st.write("#### 3) XML template with no values")
st.write(
    '''
There can be data filled into templete. Just XML structure to be downloaded.
'''
)
st.image("Pictures/XML 1.png")
if st.download_button("Download",data = xml_data_empty , file_name="XML_empty_template.xml"):
    st.info("Download will happen in few seconds")

st.write("------")