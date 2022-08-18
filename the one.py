import savReaderWriter as spss
import pandas as pd
import json
from PIL import Image, ImageDraw
import streamlit as st 

st.title('Click mapper')

uploaded_db = st.file_uploader("Upload SPSS database")
images = st.file_uploader("Upload JPGs", type="jpg")

if uploaded_db:
	st.write("Brao")

	@st.cache

else:
	st.info('Upload a database')

