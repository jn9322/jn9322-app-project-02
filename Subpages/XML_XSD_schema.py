import streamlit as st

st.set_page_config(page_title="XSD, XML Schema")

st.write("# XSD, XML Schema")
st.write(
    '''
Description of XML structure with which this application works.

'''
)

st.write("----")
st.write("#### Diagram:"
)

st.write("*For better visibility - put cursor on the picture and click on the icon in the right upper corner")
st.image("Pictures/XSD diagram.png")

st.write("----")

st.write("#### Principle:")
st.write("*For better visibility - put cursor on the picture and click on the icon in the right upper corner")
st.image("Pictures/XSD diagram XML context.png")
st.write(
    '''
XML structure is based on 2 main elements:

1) <header> - header of invoice, including <customer> name and <total_sum> of <price> values from <detail level>.

    ** The application has validation mechanism to see whether it matches or not

2) <detail> - element can be 1 to N times in the message (depending on how many products have been bought). Includes child elements <category>, <product_name> and <price>

'''
)

st.write("------")


# Download of XSD
xsd_structure = '''<?xml version="1.0" encoding="UTF-8"?>
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema" elementFormDefault="qualified" attributeFormDefault="unqualified">
	<xs:element name="invoice">
		<xs:complexType>
			<xs:sequence>
				<xs:element name="header">
					<xs:complexType>
						<xs:sequence>
							<xs:element name="customer" type="xs:string"/>
							<xs:element name="total_sum" type="xs:decimal"/>
						</xs:sequence>
					</xs:complexType>
				</xs:element>
				<xs:element name="detail" maxOccurs="unbounded">
					<xs:complexType>
						<xs:sequence>
							<xs:element name="category" type="xs:string"/>
							<xs:element name="product_name" type="xs:string"/>
							<xs:element name="price">
								<xs:simpleType>
									<xs:restriction base="xs:decimal">
										<xs:fractionDigits value="2"/>
									</xs:restriction>
								</xs:simpleType>
							</xs:element>
						</xs:sequence>
						<xs:attribute name="id" type="xs:integer" use="required"/>
					</xs:complexType>
				</xs:element>
			</xs:sequence>
		</xs:complexType>
	</xs:element>
</xs:schema>
'''

st.write("#### XSD - download as .txt:")
if st.download_button("Download",data = xsd_structure  , file_name="XML Schema.txt"):
    st.info("Download will happen in few seconds")

st.write("------")