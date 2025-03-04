import streamlit as st
import xml.etree.ElementTree as ET

# Firstly - data options/XML structures -> objects
xml_data_empty = """<?xml version="1.0" encoding="UTF-8"?>
<invoice>
  <header>
    <customer></customer>
    <total_sum></total_sum>
  </header>
  <detail id = "1">
    <category></category>
    <product_name></product_name>
    <price></price>
  </detail>
  <detail id = "2">
    <category></category>
    <product_name></product_name>
    <price></price>
  </detail>
  <detail id = "3">
    <category></category>
    <product_name></product_name>
    <price></price>
  </detail>
    <detail id = "4">
    <category></category>
    <product_name></product_name>
    <price></price>
  </detail>
  <detail id = "5">
    <category></category>
    <product_name></product_name>
    <price></price>
  </detail>
  <detail id = "6">
    <category></category>
    <product_name></product_name>
    <price></price>
  </detail>
</invoice>
"""


xml_data_summatch = """<?xml version="1.0" encoding="UTF-8"?>
<invoice>
  <header>
    <customer>ABC s.r.o.</customer>
    <total_sum>115960.00</total_sum>
  </header>
  <detail id = "1">
    <category>PC</category>
    <product_name>HP ProBook</product_name>
    <price>24000.00</price>
  </detail>
  <detail id = "2">
    <category>TV</category>
    <product_name>Philips The One</product_name>
    <price>30000.00</price>
  </detail>
  <detail id = "3">
    <category>Gaming</category>
    <product_name>Playstation 5 Pro</product_name>
    <price>20290.00</price>
  </detail>
    <detail id = "4">
    <category>PC</category>
    <product_name>MacBook Air 13</product_name>
    <price>18390.00</price>
  </detail>
  <detail id = "5">
    <category>Mobile phones</category>
    <product_name>Xiaomi Pad 7</product_name>
    <price>9990.00</price>
  </detail>
  <detail id = "6">
    <category>Gaming</category>
    <product_name>Playstation 5</product_name>
    <price>13290.00</price>
  </detail>
</invoice>
"""

xml_data_sumnotmatch = """<?xml version="1.0" encoding="UTF-8"?>
<invoice>
  <header>
    <customer>ABC s.r.o.</customer>
    <total_sum>74290.00</total_sum>
  </header>
  <detail id = "1">
    <category>PC</category>
    <product_name>HP ProBook</product_name>
    <price>24000.00</price>
  </detail>
  <detail id = "2">
    <category>TV</category>
    <product_name>Philips The One</product_name>
    <price>30000.00</price>
  </detail>
  <detail id = "3">
    <category>Gaming</category>
    <product_name>Playstation 5 Pro</product_name>
    <price>20290.00</price>
  </detail>
    <detail id = "4">
    <category>PC</category>
    <product_name>MacBook Air 13</product_name>
    <price>18390.00</price>
  </detail>
  <detail id = "5">
    <category>Mobile phones</category>
    <product_name>Xiaomi Pad 7</product_name>
    <price>9990.00</price>
  </detail>
  <detail id = "6">
    <category>Gaming</category>
    <product_name>Playstation 5</product_name>
    <price>13290.00</price>
  </detail>
</invoice>
"""

xml_data_12_sumnmatches = """<?xml version="1.0" encoding="UTF-8"?>
<invoice>
  <header>
    <customer>ABC s.r.o.</customer>
    <total_sum>210930.00</total_sum>
  </header>
  <detail id = "1">
    <category>PC</category>
    <product_name>HP ProBook</product_name>
    <price>24000.00</price>
  </detail>
  <detail id = "2">
    <category>TV</category>
    <product_name>Philips The One</product_name>
    <price>30000.00</price>
  </detail>
  <detail id = "3">
    <category>Gaming</category>
    <product_name>Playstation 5 Pro</product_name>
    <price>20290.00</price>
  </detail>
    <detail id = "4">
    <category>PC</category>
    <product_name>MacBook Air 13</product_name>
    <price>18390.00</price>
  </detail>
  <detail id = "5">
    <category>Mobile phones</category>
    <product_name>Xiaomi Pad 7</product_name>
    <price>9990.00</price>
  </detail>
  <detail id = "6">
    <category>Gaming</category>
    <product_name>Playstation 5</product_name>
    <price>13290.00</price>
  </detail>
  <detail id = "7">
    <category>Mobile phones</category>
    <product_name>Xiaomi 15 Ultra 5G</product_name>
    <price>34000.00</price>
  </detail>
  <detail id = "8">
    <category>Mobile phones</category>
    <product_name>Xiaomi 15 Ultra </product_name>
    <price>32000.00</price>
  </detail>
  <detail id = "9">
    <category>Gaming</category>
    <product_name>Xbox Series S</product_name>
    <price>7190.00</price>
  </detail>
    <detail id = "10">
    <category>Gaming</category>
    <product_name>Kingdom Come: Deliverance 2</product_name>
    <price>1890.00</price>
  </detail>
  <detail id = "11">
    <category>Tablets</category>
    <product_name>iPad 10.9</product_name>
    <price>9990.00</price>
  </detail>
  <detail id = "12">
    <category>Tablets</category>
    <product_name>Samsung Galaxy Tab S9</product_name>
    <price>9900.00</price>
  </detail>
</invoice>
"""
# Frontend part

st.set_page_config(page_title="XML download")
st.write("# XML download")
st.write(
    '''
Here you can download XML which can be used for parsing. There are 5 options from which to select. 

1) Predefind file - sum matches - 6 detail levels
2) Predefind file - sum does not match - 6 detail levels
3) Empty file - just XML structure, no values - 6 detail levels
4) Predefind file - sum matches - 12 detail levels
5) Customized file - There can be how many detail levels you want. (Only what needs to be kept is XML structer and XML rules). More details in section 'XML - XSD, XML Schema' in the navigation bar.

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
st.image("Pictures/XML 1 w attributes.png")

if st.download_button("Download",data = xml_data_summatch  , file_name="XML_sum matching.xml"):
    st.info("Download will happen in few seconds")

st.write("------")


# Option 2
st.write("#### 2) Predefined file - sum does not match")
st.write(
    '''
Scenario where <total_sum> field does not match the sum of <price> in detail elements. This will be seen in the parsing data step - validation is built.
'''
)
st.image("Pictures/XML 2 w attributes.png")
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
st.image("Pictures/XML 3 w attributes.png")
if st.download_button("Download",data = xml_data_empty , file_name="XML_empty_template.xml"):
    st.info("Download will happen in few seconds")

st.write("------")


# Option 4
st.write("#### 4) Predefined file - 12 detail lines - sum matches")
st.write(
    '''
Application can work with many <detail> elements, it is not limited. Here example of 12 detail levels -> The data parsing and data visualization work the same way due to python for cycle
'''
)
st.image("Pictures/XML 4 w attributes.png")
if st.download_button("Download",data = xml_data_12_sumnmatches , file_name="XML_12 details_sum matchining.xml"):
    st.info("Download will happen in few seconds")

st.write("------")