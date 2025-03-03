import streamlit as st
import csv
import xml.etree.ElementTree as ET
import time
import pandas as pd
import lxml


xml_upload = st.file_uploader("Nahraj: ",type = "xml")

if xml_upload is not None:
    st.success("Cau")

if xml_upload is None:
    st.info("Nahraj")




