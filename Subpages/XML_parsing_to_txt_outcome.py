import streamlit as st
import csv
import xml.etree.ElementTree as ET
import time

# Data import 
tree_element_data = ET.parse("Data/Source_file.xml")

root = tree_element_data.getroot()
print(f"root identified as {root}")

# Data parsing from header
value_customer = root[0][0].text
value_total_sum = root[0][1].text
st.write(value_customer)
st.write(value_total_sum)

# Data parsing from detail
value_category_list = []
for detail_category in root.findall('detail'):
    category = detail_category.find('category').text
    value_category_list.append(category)

print(value_category_list)
c_value_1 = value_category_list[0]
c_value_2 = value_category_list[1]
c_value_3 = value_category_list[2]
print(c_value_1)
st.write(c_value_1)


value_product_name_list = []
for detail_product_name in root.findall('detail'):
    product_name = detail_product_name.find('product_name').text
    value_product_name_list.append(product_name)

print(value_product_name_list)
produ_value_1 = value_product_name_list[0]
produ_value_2 = value_product_name_list[1]
produ_value_3 = value_product_name_list[2]
st.write(produ_value_1)

value_price_list = []
for detail_price in root.findall('detail'):
    product_price = detail_price.find('price').text
    value_price_list.append(product_price)

print(value_price_list)
pri_value_1 = value_price_list[0]
pri_value_2 = value_price_list[1]
pri_value_3 = value_price_list[2]
st.write(f"zde {pri_value_1}")


# nejaky tlacitko na praci s tema hodnotama

if st.button("Summary overview"):
    st.write(f"Receiver of the invoice: {value_customer}")
    st.write(f"Total sum: {value_total_sum} Kc")

if st.button("Detail overview"):
    st.write(f"Item 1: Product: {produ_value_1}, Category - {c_value_1}, Price: {pri_value_1} Kc.")
    st.write(f"Item 2: Product: {produ_value_2}, Category - {c_value_2}, Price: {pri_value_2} Kc.")
    st.write(f"Item 3: Product: {produ_value_3}, Category - {c_value_3}, Price: {pri_value_3} Kc.")

# final outcome for print - using server time
time_objects = time.localtime()
year, month, day, hour, minute, second, weekday, yearday, daylight = time_objects  

date_custom = str("Date: %02d-%02d-%04d" % (day,month,year))
time_custom = str("Time: %02d:%02d:%02d" % (hour,minute,second))
day_custom = str(("Mon","Tue","Wed","Thu","Fri","Sat","Sun") [weekday])
day_custom_2 = str("Day: "+ day_custom)
full_date_outcome = str(date_custom +", " + day_custom_2 +", " + time_custom )

final_outcome = (f"{full_date_outcome} - Receiver: {value_customer}, price to pay {value_total_sum} Kc.")


if st.download_button("Print/Download - Summary overview", data= final_outcome, file_name="Summary.txt"):
    
    file = open("print.txt","w")

    file.write(final_outcome)
    file.close()

    
    