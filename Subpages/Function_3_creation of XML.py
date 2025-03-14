import streamlit as st
import xml.etree.ElementTree as ET
import string
import random
import time



# Function for pretty print of XML elements
def prettify(element, indent='  '):
    queue = [(0, element)]  # (level, element)
    while queue:
        level, element = queue.pop(0)
        children = [(level + 1, child) for child in list(element)]
        if children:
            element.text = '\n' + indent * (level+1)  # for child open
        if queue:
            element.tail = '\n' + indent * queue[0][0]  # for sibling open
        else:
            element.tail = '\n' + indent * (level-1)  # for parent close
        queue[0:0] = children  # prepend so children come before siblings



# Function for generating random 6 digits for invoice number
def id_generator(size=6, chars=string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

a = id_generator()
invoice_number_generated = 'INV-' + a



# Generation of date for <date> element
now = time.localtime()
print(now)
date_input = time.strftime("%Y-%m-%d", now)

with st. expander("Buyer"):
    customer_input = st.text_input(
        "Customer:",
        help = "Write a customer name"
        )

with st. expander("Product"):

    product_name_inp = st.text_input(
        "Product name:",
        help = "Write a product name"
        )

    category_selb = st.selectbox(
        "Category" ,
        index = None,
        placeholder= "Select category...",
        options=["PC","TV","Gaming","Mobile phones","Tablets","Major Appliances","Households"],
        help = "Select category from which the product is"
         )

with st. expander("Price"):
    currency_selb = st.selectbox(
        "Currency" ,
        index = None,
        placeholder= "Select currency...",
        options=["euro","US dollar","Kč"],
        help = "Select one from the predefined currencies"
        )
    
    price = st.number_input(
        "Price",
        min_value=0.00,
        step = 10.00,
        help = "You can either click on the +- icons or write the input using numbers. *The step is step +- 10.00 -> i case of diferent values in decimals wrrte it."
        )


with st. expander("Extra purchase"):

    add_service_select = st.selectbox(
        "Additional service" ,
        options=["No additional service","Insurance","Extended varanty"],
        help = "Select one of the options"
         )

    if add_service_select == 'Insurance':
        st.info("costs 15% from product price")
    
    if add_service_select == 'Extended varanty':
        st.info("costs 10% from product price")


price_str = str(price)


# logika pro additional service

def fun_add_service_1(option):
    
    if option == 'No additional service':
        return 'None'

    elif option == 'Insurance':
        return 'insurance'
    
    elif option == 'Extended varanty':
        return 'extended varanty'

service_type_fn = fun_add_service_1(add_service_select)

def fun_add_service_2(option, price):
    
    if option == 'No additional service':
        return '0.00'

    elif option == 'Insurance':
        ins = price * 0.15
        ins = str(ins)
        return ins
    
    elif option == 'Extended varanty':
        extv = price * 0.1
        extv = str(extv)
        return extv

service_price_fn = fun_add_service_2(add_service_select, price)



def fun_add_service_3(option):
    
    if option == 'No additional service':
        return 'N'

    else:
        return 'Y'
       

service_fn = fun_add_service_3(add_service_select)


if customer_input == '' or product_name_inp == '' or category_selb == '' or currency_selb == '' or price == '' or add_service_select == '':
    st.warning("One of the inputs is still not available")

else:
    st.success("Fulfiled properly")



if st.button("submit"):
    st.write("Jane ty jsi genius")
    

    st.write(f" - Customer name: {customer_input}")
    ''
    st.write(f" - Product name: {product_name_inp}")
    st.write(f" - Category: {category_selb}")
    st.write(f" - Price: {price:.2f} {currency_selb}")
    ''
    st.write(f" - Extra service: {add_service_select}")
    st.write(f" - Price for the extra service: {service_price_fn} {currency_selb}")

    st.info("If this is what you expect you can proceed with Download button which will create XML file. If not, you can go up and change your inputs and then use the Submit button again.")
    
    
       
   
    xml_doc = ET.Element("invoice")
    header = ET.SubElement(xml_doc, 'header')
    customer = ET.SubElement(header, 'customer').text = customer_input
    invoice_number = ET.SubElement(header, 'invoice_number').text = invoice_number_generated
    date = ET.SubElement(header, 'date').text = date_input
    price = ET.SubElement(header, 'price')
    total_sum = ET.SubElement(price, 'total_sum').text = price_str
    total_sum_services = ET.SubElement(price, 'total_sum_services').text = service_price_fn
    currency = ET.SubElement(price, 'currency').text = currency_selb

    detail = ET.SubElement(xml_doc, 'detail', id = '1')
    category= ET.SubElement(detail, 'category').text = category_selb
    product_name = ET.SubElement(detail, 'product_name').text = product_name_inp
    price_amount = ET.SubElement(detail, 'price_amount').text = price_str
    addtional_service = ET.SubElement(detail, 'additional_service')
    service = ET.SubElement(addtional_service, 'service'). text = service_fn
    service_type = ET.SubElement(addtional_service, 'service_type').text = service_type_fn
    service_price = ET.SubElement(addtional_service, 'service_price').text = service_price_fn

    prettify(xml_doc)

    tree = ET.ElementTree(xml_doc)
    # xml_declaration=Tru -> generuje XML prolog
    tree.write('person.xml', encoding='UTF-8', xml_declaration=True)
 

file_name_fstring = f"{invoice_number_generated}.xml"

with open('Data/Function_3_do NOT delete.xml') as f:
    if st.download_button('Download', f, file_name = file_name_fstring):
        st.info("download will start in few seconds")