import streamlit as st
import xml.etree.ElementTree as ET
import time
import plotly.express as px
import pandas as pd
import math


st.write("# Upload XML:")

object_from_upload = st.file_uploader("")

if object_from_upload is None:
    st.info("When a file uploaded, application will start")
        

if object_from_upload is not None:
    st.success("Upload complete")

    # Data import 
    tree_element_data = ET.parse(object_from_upload)

    root = tree_element_data.getroot()
    print(f"root identified as {root}")

    # Data parsing from header
    value_customer = root[0][0].text
    value_total_sum = root[0][1].text

        
   
    # Data parsing from detail
    value_category_list = []
    for detail_category in root.findall('detail'):
        category = detail_category.find('category').text
        value_category_list.append(category)

    # 04-March - to be deleted
    # c_value_1 = value_category_list[0]
    # c_value_2 = value_category_list[1]
    # c_value_3 = value_category_list[2]
   
    value_product_name_list = []
    for detail_product_name in root.findall('detail'):
        product_name = detail_product_name.find('product_name').text
        value_product_name_list.append(product_name)

    # 04-March - to be deleted
    # produ_value_1 = value_product_name_list[0]
    # produ_value_2 = value_product_name_list[1]
    # produ_value_3 = value_product_name_list[2]
    

    value_price_list = []
    for detail_price in root.findall('detail'):
        product_price = detail_price.find('price').text
        value_price_list.append(product_price)
        
    # 04-March - to be deleted
    # pri_value_1 = value_price_list[0]
    # pri_value_2 = value_price_list[1]
    # pri_value_3 = value_price_list[2]

    value_attribut = []
    for detail_id in root.findall('detail'):
        ids = detail_id.get('id')
        value_attribut.append(ids)

    #Sum of prices - type change string -> float for calculation
    value_price_list_float = list(map(float, value_price_list)) 
    sum_price = math.fsum(value_price_list_float)
    
    # Data validation - sum = pri_values Y/N 
    value_total_sum_fl = float(value_total_sum)

    # 04-March - to be deleted
    # pri_value_1_fl = float(pri_value_1)
    # pri_value_2_fl = float(pri_value_2)
    # pri_value_3_fl = float(pri_value_3)

    result_validation = []
    def data_validation(value_total_sum, sum_price):
        result = value_total_sum - sum_price
        st.write("---------")
        st.write("#### Validation process:")
        
        if result < 0 or result > 0:
            st.warning("Validation not passed - summary does not equeal to line values. You can either continue with existing file or adjust the input file and upload it again.")
            st.write(f"** Total sum in the XML invoice is: '{value_total_sum}' but summary of prices in detail lines / per product is: '{sum_price}'.")
            outcome = ("Not passed")
            result_validation.append(outcome)

        else:
            st.success("Validation passed")
            outcome = ("Passed")
            result_validation.append(outcome)

    data_validation(value_total_sum_fl, sum_price)

    result_obj_outcome = result_validation[0]

    # Buttons to show values

    st.write("------")
    st.write("#### Check your data:")

    if st.button("Summary overview"):
        st.write(f"Receiver of the invoice: {value_customer}")
        st.write(f"Total sum: {value_total_sum} Kc")

    if st.button("Detail overview"):

        # 04-March - to be deleted
        # st.write(f"Item 1: Product: {produ_value_1}, Category - {c_value_1}, Price: {pri_value_1} Kc.")
        # st.write(f"Item 2: Product: {produ_value_2}, Category - {c_value_2}, Price: {pri_value_2} Kc.")
        # st.write(f"Item 3: Product: {produ_value_3}, Category - {c_value_3}, Price: {pri_value_3} Kc.")

        # Transformation of Data to table -> not editable
        data_table = pd.DataFrame({
                    "Order" : value_attribut,
                    "Product" : value_product_name_list,
                    "Price" : value_price_list,
                    "Category" : value_category_list
                                     
                    })
        
        # This is adjusting the table
        data_table_2 = st.dataframe(data=data_table, hide_index=True, use_container_width=True)
        

         

        # Pie chart
        data = pd.DataFrame({
        "Product" : value_product_name_list,
        "Price" : value_price_list
        })


        fig_pie = px.pie(
            data, 
            names = "Product",
            values = "Price",
            title = "Pie chart - ratio of the total sum"
        )

        st.plotly_chart(fig_pie)

        fig_bar = px.bar(
            data, 
            x="Product",
            y="Price",
            title= "Bar chart   "
        )

        st.plotly_chart(fig_bar)

    # final outcome for print - using server time

    st.write("------")
    st.write("#### Download of .txt:")
    st.write('''Here is short summary of the original XML invoice, including result of validation and date.''')

    st.image("Pictures/outcome txt picture.png")
    st.write(" ")
    st.image("Pictures/Validation passed picture txt.png")
    st.write(" ")
    st.image("Pictures/Validation NOT passed picture txt.png")
    st.write(" ")

    # backend part
    time_objects = time.localtime()
    year, month, day, hour, minute, second, weekday, yearday, daylight = time_objects  

    date_custom = str("Date: %02d-%02d-%04d" % (day,month,year))
    time_custom = str("Time: %02d:%02d:%02d" % (hour,minute,second))
    day_custom = str(("Mon","Tue","Wed","Thu","Fri","Sat","Sun") [weekday])
    day_custom_2 = str("Day: "+ day_custom)
    full_date_outcome = str(date_custom +", " + day_custom_2 +", " + time_custom )

    final_outcome = (f"{full_date_outcome} - Validation: {result_obj_outcome} --- Receiver: {value_customer}, price to pay {value_total_sum} Kc.")


    if st.download_button("Download", data= final_outcome, file_name="Summary.txt"):
        
        file = open("print.txt","w")

        file.write(final_outcome)
        file.close()
        st.info("download will start in few seconds")

    st.write("------")