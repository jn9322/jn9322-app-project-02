import streamlit as st

st.set_page_config(page_title="XSD, XML Schema")

st.write("# XSD, XML Schema")
st.write(
    '''
Description of XML structure with which this application works.

'''
)

st.write("----")
st.write("#### Diagram:")
st.image("Pictures/V2_pictures/Schema diagram.png")

st.write("#### Diagram with element properties:")
st.write("*For better visibility - put cursor on the picture and click on the icon in the right upper corner")
st.write("Header:")
st.image("Pictures/V2_pictures/header properties.png")
st.image("Pictures/V2_pictures/xsd_header.png")
st.write("Detail:")
st.image("Pictures/V2_pictures/detail properties.png")
st.image("Pictures/V2_pictures/xsd_detail.png")

st.write("----")

st.write("#### Principle of XML:")
st.write("*For better visibility - put cursor on the picture and click on the icon in the right upper corner")
st.image("Pictures/V2_pictures/Principle.png")
st.write(
    '''

    PŘEPSAT !!!!!!!!!!!!!!!!!!!!!
XML structure is based on 2 main elements:

1) <header> - header of invoice, including <customer> name and <total_sum> of <price> values from <detail level>.

    ** The application has validation mechanism to see whether it matches or not

2) <detail> - element can be 1 to N times in the message (depending on how many products have been bought). Includes child elements <category>, <product_name> and <price>

'''
)

st.write("#### Principle in context of data parsing:")
st.write("*For better visibility - put cursor on the picture and click on the icon in the right upper corner")
st.image("Pictures/V2_pictures/Principle in context of parsing4.png")
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
							<xs:element name="invoice_number">
								<xs:simpleType>
									<xs:restriction base="xs:string">
										<xs:minLength value="10"/>
										<xs:maxLength value="10"/>
										<xs:pattern value="[I]{1}[N]{1}[V]{1}[-]{1}[0-9]{6}"/>
									</xs:restriction>
								</xs:simpleType>
							</xs:element>
							<xs:element name="date">
								<xs:simpleType>
									<xs:restriction base="xs:date">
										<xs:minInclusive value="2025-03-10"/>
									</xs:restriction>
								</xs:simpleType>
							</xs:element>
							<xs:element name="price">
								<xs:complexType>
									<xs:sequence>
										<xs:element name="total_sum" default="0.01">
											<xs:simpleType>
												<xs:restriction base="xs:decimal">
													<xs:fractionDigits value="2"/>
													<xs:minInclusive value="0.01"/>
												</xs:restriction>
											</xs:simpleType>
										</xs:element>
										<xs:element name="total_sum_services">
											<xs:simpleType>
												<xs:restriction base="xs:decimal">
													<xs:minInclusive value="0.00"/>
													<xs:fractionDigits value="2"/>
												</xs:restriction>
											</xs:simpleType>
										</xs:element>
										<xs:element name="currency">
											<xs:simpleType>
												<xs:restriction base="xs:string">
													<xs:pattern value="euro|US dollar|Kč"/>
												</xs:restriction>
											</xs:simpleType>
										</xs:element>
									</xs:sequence>
								</xs:complexType>
							</xs:element>
						</xs:sequence>
					</xs:complexType>
				</xs:element>
				<xs:element name="detail" maxOccurs="unbounded">
					<xs:complexType>
						<xs:sequence>
							<xs:element name="category">
								<xs:simpleType>
									<xs:restriction base="xs:string">
										<xs:pattern value="PC|TV|Gaming|Mobile phones|Tablets|Major Appliances|Households"/>
									</xs:restriction>
								</xs:simpleType>
							</xs:element>
							<xs:element name="product_name" type="xs:string"/>
							<xs:element name="price_amount">
								<xs:simpleType>
									<xs:restriction base="xs:decimal">
										<xs:minInclusive value="0.00"/>
										<xs:fractionDigits value="2"/>
									</xs:restriction>
								</xs:simpleType>
							</xs:element>
							<xs:element name="additional_service">
								<xs:complexType>
									<xs:sequence>
										<xs:element name="service" default="N">
											<xs:simpleType>
												<xs:restriction base="xs:string">
													<xs:length value="1"/>
													<xs:pattern value="Y|N"/>
												</xs:restriction>
											</xs:simpleType>
										</xs:element>
										<xs:element name="service_type" default="None">
											<xs:simpleType>
												<xs:restriction base="xs:string">
													<xs:pattern value="None|extended varanty|insurance"/>
												</xs:restriction>
											</xs:simpleType>
										</xs:element>
										<xs:element name="service_price" default="0.00">
											<xs:simpleType>
												<xs:restriction base="xs:decimal">
													<xs:minInclusive value="0.00"/>
													<xs:fractionDigits value="2"/>
												</xs:restriction>
											</xs:simpleType>
										</xs:element>
									</xs:sequence>
								</xs:complexType>
							</xs:element>
						</xs:sequence>
						<xs:attribute name="id" type="xs:integer" use="required" id="yes"/>
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