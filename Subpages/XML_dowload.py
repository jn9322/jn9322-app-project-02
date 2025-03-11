import streamlit as st
import xml.etree.ElementTree as ET

# Firstly - data options/XML structures -> objects
xml_data_euro = """<?xml version="1.0" encoding="UTF-8"?>
<invoice>
	<header>
		<customer>ABC s.r.o.</customer>
		<invoice_number>INV-123456</invoice_number>
		<date>2025-03-10</date>
		<price>
			<total_sum>3291.00</total_sum>
			<total_sum_services>168.00</total_sum_services>
			<currency>euro</currency>
		</price>
	</header>
	<detail id="1">
		<category>PC</category>
		<product_name>HP ProBook</product_name>
		<price_amount>240.00</price_amount>
		<additional_service>
			<service>Y</service>
			<service_type>extended varanty</service_type>
			<service_price>9.00</service_price>
		</additional_service>
	</detail>
	<detail id="2">
		<category>TV</category>
		<product_name>Philips The One</product_name>
		<price_amount>300.00</price_amount>
		<additional_service>
			<service>N</service>
			<service_type>None</service_type>
			<service_price>0.00</service_price>
		</additional_service>
	</detail>
	<detail id="3">
		<category>Gaming</category>
		<product_name>Playstation 5 Pro</product_name>
		<price_amount>202.00</price_amount>
		<additional_service>
			<service>Y</service>
			<service_type>insurance</service_type>
			<service_price>25.00</service_price>
		</additional_service>
	</detail>
	<detail id="4">
		<category>PC</category>
		<product_name>MacBook Air 13</product_name>
		<price_amount>183.00</price_amount>
		<additional_service>
			<service>Y</service>
			<service_type>insurance</service_type>
			<service_price>15.00</service_price>
		</additional_service>
	</detail>
	<detail id="5">
		<category>Mobile phones</category>
		<product_name>Xiaomi Pad 7</product_name>
		<price_amount>99.00</price_amount>
		<additional_service>
			<service>N</service>
			<service_type>None</service_type>
			<service_price>0.00</service_price>
		</additional_service>
	</detail>
	<detail id="6">
		<category>Gaming</category>
		<product_name>Playstation 5</product_name>
		<price_amount>132.00</price_amount>
		<additional_service>
			<service>N</service>
			<service_type>None</service_type>
			<service_price>0.00</service_price>
		</additional_service>
	</detail>
	<detail id="7">
		<category>Mobile phones</category>
		<product_name>Xiaomi 15 Ultra 5G</product_name>
		<price_amount>340.00</price_amount>
		<additional_service>
			<service>N</service>
			<service_type>None</service_type>
			<service_price>0.00</service_price>
		</additional_service>
	</detail>
	<detail id="8">
		<category>Mobile phones</category>
		<product_name>Xiaomi 15 Ultra </product_name>
		<price_amount>320.00</price_amount>
		<additional_service>
			<service>N</service>
			<service_type>None</service_type>
			<service_price>0.00</service_price>
		</additional_service>
	</detail>
	<detail id="9">
		<category>Gaming</category>
		<product_name>Xbox Series S</product_name>
		<price_amount>71.00</price_amount>
		<additional_service>
			<service>Y</service>
			<service_type>insurance</service_type>
			<service_price>4.00</service_price>
		</additional_service>
	</detail>
	<detail id="10">
		<category>Gaming</category>
		<product_name>Kingdom Come: Deliverance 2</product_name>
		<price_amount>18.00</price_amount>
		<additional_service>
			<service>N</service>
			<service_type>None</service_type>
			<service_price>0.00</service_price>
		</additional_service>
	</detail>
	<detail id="11">
		<category>Tablets</category>
		<product_name>iPad 10.9</product_name>
		<price_amount>99.00</price_amount>
		<additional_service>
			<service>Y</service>
			<service_type>extended varanty</service_type>
			<service_price>5.00</service_price>
		</additional_service>
	</detail>
	<detail id="12">
		<category>Tablets</category>
		<product_name>Samsung Galaxy Tab S9</product_name>
		<price_amount>99.00</price_amount>
		<additional_service>
			<service>N</service>
			<service_type>None</service_type>
			<service_price>0</service_price>
		</additional_service>
	</detail>
	<detail id="13">
		<category>Major Appliances</category>
		<product_name>GORENJE NRK61CS2XL4</product_name>
		<price_amount>990.00</price_amount>
		<additional_service>
			<service>Y</service>
			<service_type>insurance</service_type>
			<service_price>100.00</service_price>
		</additional_service>
	</detail>
	<detail id="14">
		<category>Households</category>
		<product_name>BOSCH MUM58364</product_name>
		<price_amount>109.00</price_amount>
		<additional_service>
			<service>N</service>
			<service_type>None</service_type>
			<service_price>0</service_price>
		</additional_service>
	</detail>
	<detail id="15">
		<category>Gaming</category>
		<product_name>Meta Quest 3S 128GB</product_name>
		<price_amount>89.00</price_amount>
		<additional_service>
			<service>Y</service>
			<service_type>insurance</service_type>
			<service_price>10.00</service_price>
		</additional_service>
	</detail>
</invoice>
"""


xml_data_koruna = """<?xml version="1.0" encoding="UTF-8"?>
<invoice>
	<header>
		<customer>ABC s.r.o.</customer>
		<invoice_number>INV-123456</invoice_number>
		<date>2025-03-10</date>
		<price>
			<total_sum>210930.00</total_sum>
			<total_sum_services>6169.00</total_sum_services>
			<currency>Kč</currency>
		</price>
	</header>
	<detail id="1">
		<category>PC</category>
		<product_name>HP ProBook</product_name>
		<price_amount>24000.00</price_amount>
		<additional_service>
			<service>Y</service>
			<service_type>extended varanty</service_type>
			<service_price>990.00</service_price>
		</additional_service>
	</detail>
	<detail id="2">
		<category>TV</category>
		<product_name>Philips The One</product_name>
		<price_amount>30000.00</price_amount>
		<additional_service>
			<service>N</service>
			<service_type>None</service_type>
			<service_price>0.00</service_price>
		</additional_service>
	</detail>
	<detail id="3">
		<category>Gaming</category>
		<product_name>Playstation 5 Pro</product_name>
		<price_amount>20290.00</price_amount>
		<additional_service>
			<service>Y</service>
			<service_type>insurance</service_type>
			<service_price>2500.00</service_price>
		</additional_service>
	</detail>
	<detail id="4">
		<category>PC</category>
		<product_name>MacBook Air 13</product_name>
		<price_amount>18390.00</price_amount>
		<additional_service>
			<service>Y</service>
			<service_type>insurance</service_type>
			<service_price>1590.00</service_price>
		</additional_service>
	</detail>
	<detail id="5">
		<category>Mobile phones</category>
		<product_name>Xiaomi Pad 7</product_name>
		<price_amount>9990.00</price_amount>
		<additional_service>
			<service>N</service>
			<service_type>None</service_type>
			<service_price>0.00</service_price>
		</additional_service>
	</detail>
	<detail id="6">
		<category>Gaming</category>
		<product_name>Playstation 5</product_name>
		<price_amount>13290.00</price_amount>
		<additional_service>
			<service>N</service>
			<service_type>None</service_type>
			<service_price>0.00</service_price>
		</additional_service>
	</detail>
	<detail id="7">
		<category>Mobile phones</category>
		<product_name>Xiaomi 15 Ultra 5G</product_name>
		<price_amount>34000.00</price_amount>
		<additional_service>
			<service>N</service>
			<service_type>None</service_type>
			<service_price>0.00</service_price>
		</additional_service>
	</detail>
	<detail id="8">
		<category>Mobile phones</category>
		<product_name>Xiaomi 15 Ultra </product_name>
		<price_amount>32000.00</price_amount>
		<additional_service>
			<service>N</service>
			<service_type>None</service_type>
			<service_price>0.00</service_price>
		</additional_service>
	</detail>
	<detail id="9">
		<category>Gaming</category>
		<product_name>Xbox Series S</product_name>
		<price_amount>7190.00</price_amount>
		<additional_service>
			<service>Y</service>
			<service_type>insurance</service_type>
			<service_price>499.00</service_price>
		</additional_service>
	</detail>
	<detail id="10">
		<category>Gaming</category>
		<product_name>Kingdom Come: Deliverance 2</product_name>
		<price_amount>1890.00</price_amount>
		<additional_service>
			<service>N</service>
			<service_type>None</service_type>
			<service_price>0.00</service_price>
		</additional_service>
	</detail>
	<detail id="11">
		<category>Tablets</category>
		<product_name>iPad 10.9</product_name>
		<price_amount>9990.00</price_amount>
		<additional_service>
			<service>Y</service>
			<service_type>extended varanty</service_type>
			<service_price>590.00</service_price>
		</additional_service>
	</detail>
	<detail id="12">
		<category>Tablets</category>
		<product_name>Samsung Galaxy Tab S9</product_name>
		<price_amount>9900.00</price_amount>
		<additional_service>
			<service>N</service>
			<service_type>None</service_type>
			<service_price>0</service_price>
		</additional_service>
	</detail>
</invoice>
"""

xml_data_usdollar = """<?xml version="1.0" encoding="UTF-8"?>
<invoice>
	<header>
		<customer>ABC s.r.o.</customer>
		<invoice_number>INV-123456</invoice_number>
		<date>2025-03-10</date>
		<price>
			<total_sum>2000.00</total_sum>
			<total_sum_services>50.00</total_sum_services>
			<currency>US dollar</currency>
		</price>
	</header>
	<detail id="1">
		<category>PC</category>
		<product_name>HP ProBook</product_name>
		<price_amount>240.00</price_amount>
		<additional_service>
			<service>Y</service>
			<service_type>extended varanty</service_type>
			<service_price>9.00</service_price>
		</additional_service>
	</detail>
	<detail id="2">
		<category>TV</category>
		<product_name>Philips The One</product_name>
		<price_amount>300.00</price_amount>
		<additional_service>
			<service>N</service>
			<service_type>None</service_type>
			<service_price>0.00</service_price>
		</additional_service>
	</detail>
	<detail id="3">
		<category>Gaming</category>
		<product_name>Playstation 5 Pro</product_name>
		<price_amount>202.00</price_amount>
		<additional_service>
			<service>Y</service>
			<service_type>insurance</service_type>
			<service_price>25.00</service_price>
		</additional_service>
	</detail>
	<detail id="4">
		<category>PC</category>
		<product_name>MacBook Air 13</product_name>
		<price_amount>183.00</price_amount>
		<additional_service>
			<service>Y</service>
			<service_type>insurance</service_type>
			<service_price>15.00</service_price>
		</additional_service>
	</detail>
	<detail id="5">
		<category>Mobile phones</category>
		<product_name>Xiaomi Pad 7</product_name>
		<price_amount>99.00</price_amount>
		<additional_service>
			<service>N</service>
			<service_type>None</service_type>
			<service_price>0.00</service_price>
		</additional_service>
	</detail>
	<detail id="6">
		<category>Gaming</category>
		<product_name>Playstation 5</product_name>
		<price_amount>132.00</price_amount>
		<additional_service>
			<service>N</service>
			<service_type>None</service_type>
			<service_price>0.00</service_price>
		</additional_service>
	</detail>
	<detail id="7">
		<category>Mobile phones</category>
		<product_name>Xiaomi 15 Ultra 5G</product_name>
		<price_amount>340.00</price_amount>
		<additional_service>
			<service>N</service>
			<service_type>None</service_type>
			<service_price>0.00</service_price>
		</additional_service>
	</detail>
	<detail id="8">
		<category>Mobile phones</category>
		<product_name>Xiaomi 15 Ultra </product_name>
		<price_amount>320.00</price_amount>
		<additional_service>
			<service>N</service>
			<service_type>None</service_type>
			<service_price>0.00</service_price>
		</additional_service>
	</detail>
	<detail id="9">
		<category>Gaming</category>
		<product_name>Xbox Series S</product_name>
		<price_amount>71.00</price_amount>
		<additional_service>
			<service>Y</service>
			<service_type>insurance</service_type>
			<service_price>4.00</service_price>
		</additional_service>
	</detail>
	<detail id="10">
		<category>Gaming</category>
		<product_name>Kingdom Come: Deliverance 2</product_name>
		<price_amount>18.00</price_amount>
		<additional_service>
			<service>N</service>
			<service_type>None</service_type>
			<service_price>0.00</service_price>
		</additional_service>
	</detail>
	<detail id="11">
		<category>Tablets</category>
		<product_name>iPad 10.9</product_name>
		<price_amount>99.00</price_amount>
		<additional_service>
			<service>Y</service>
			<service_type>extended varanty</service_type>
			<service_price>5.00</service_price>
		</additional_service>
	</detail>
	<detail id="12">
		<category>Tablets</category>
		<product_name>Samsung Galaxy Tab S9</product_name>
		<price_amount>99.00</price_amount>
		<additional_service>
			<service>N</service>
			<service_type>None</service_type>
			<service_price>0</service_price>
		</additional_service>
	</detail>
</invoice>
"""

xml_empty_template = """<?xml version="1.0" encoding="UTF-8"?>
<invoice>
	<header>
		<customer/>
		<invoice_number/>
		<date/>
		<price>
			<total_sum>0.01</total_sum>
			<total_sum_services/>
			<currency/>
		</price>
	</header>
	<detail id="1">
		<additional_service>
			<service>N</service>
			<service_type>None</service_type>
			<service_price>0.00</service_price>
		</additional_service>
	</detail>
	<detail id="2">
		<additional_service>
			<service>N</service>
			<service_type>None</service_type>
			<service_price>0.00</service_price>
		</additional_service>
	</detail>
	<detail id="3">
		<additional_service>
			<service>N</service>
			<service_type>None</service_type>
			<service_price>0.00</service_price>
		</additional_service>
	</detail>
	<detail id="4">
		<additional_service>
			<service>N</service>
			<service_type>None</service_type>
			<service_price>0.00</service_price>
		</additional_service>
	</detail>
	<detail id="5">
		<additional_service>
			<service>N</service>
			<service_type>None</service_type>
			<service_price>0.00</service_price>
		</additional_service>
	</detail>
	<detail id="6">
		<additional_service>
			<service>N</service>
			<service_type>None</service_type>
			<service_price>0.00</service_price>
		</additional_service>
	</detail>
	<detail id="7">
		<additional_service>
			<service>N</service>
			<service_type>None</service_type>
			<service_price>0.00</service_price>
		</additional_service>
	</detail>
	<detail id="8">
		<additional_service>
			<service>N</service>
			<service_type>None</service_type>
			<service_price>0.00</service_price>
		</additional_service>
	</detail>
	<detail id="9">
		<additional_service>
			<service>N</service>
			<service_type>None</service_type>
			<service_price>0.00</service_price>
		</additional_service>
	</detail>
	<detail id="10">
		<additional_service>
			<service>N</service>
			<service_type>None</service_type>
			<service_price>0.00</service_price>
		</additional_service>
	</detail>
	<detail id="11">
		<additional_service>
			<service>N</service>
			<service_type>None</service_type>
			<service_price>0.00</service_price>
		</additional_service>
	</detail>
	<detail id="12">
		<additional_service>
			<service>N</service>
			<service_type>None</service_type>
			<service_price>0</service_price>
		</additional_service>
	</detail>
</invoice>
"""
# Frontend part

st.set_page_config(page_title="XML download")
st.write("# XML download")
st.write(
    '''
Here you can download XMLs which can be used for parsing:

1) Predefind file - sum matches - currency: euro - 15 detail lines
2) Predefind file - sum matches - currency: koruna - 12 detail lines
3) Predefind file - sum does not match - currency: US dollar - 15 detail lines
4) XML Template
'''
)

st.write("------")

# Option 1
st.write("#### 1) Predefined file - sum matches - currency: euro - 15 detail lines")
st.write(
    '''
Scenario where <total_sum> and <total_sum_services> values match the sum of <price> and sum of <service_price> in detail elements. Validation in application will be passed.
'''
)
st.image("Pictures/V2_pictures/XML download - scenario 1.png")

if st.download_button("Download",data = xml_data_euro  , file_name="XML_euro_sum matches.xml"):
    st.info("Download will happen in few seconds")

st.write("------")


# Option 2
st.write("#### 2) Predefind file - sum matches - currency: koruna - 12 detail lines")
st.write(
    '''
Scenario where <total_sum> field does not match the sum of <price> in detail elements. This will be seen in the parsing data step - validation is built.
'''
)
st.image("Pictures/XML 2 w attributes.png")
if st.download_button("Download",data = xml_data_koruna  , file_name="XML_koruna_sum matches.xml"):
    st.info("Download will happen in few seconds")

st.write("------")

# Option 3
st.write("#### 3) redefind file - sum does not match - currency: US dollar - 15 detail lines")
st.write(
    '''
There can be data filled into templete. Just XML structure to be downloaded.
'''
)
st.image("Pictures/XML 3 w attributes.png")
if st.download_button("Download",data = xml_data_usdollar , file_name="XML_usdollar_sum not match.xml"):
    st.info("Download will happen in few seconds")

st.write("------")


# Option 4
st.write("#### 4) XML Template")
st.write(
    '''
Application can work with many <detail> elements, it is not limited. Here example of 12 detail levels -> The data parsing and data visualization work the same way due to python for cycle
'''
)
st.image("Pictures/XML 4 w attributes.png")
if st.download_button("Download",data = xml_empty_template , file_name="XML_empty_template.xml"):
    st.info("Download will happen in few seconds")

st.write("------")