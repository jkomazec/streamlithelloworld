import streamlit as st
import pandas as pd
#import xlsxwriter
from io import BytesIO
from pyxlsb import open_workbook as open_xlsb

st.title('Eye tracking raw export transformator')

st.subheader('Prerequisites')

st.markdown("Export from Gazeviewer is not possible until you import the zones. Upon importing the zones, you'll have the **Export** button.")
st.markdown("As described in the Scribehow tutorial, please download all the necessary files from the Gazeviewer by selecting the following options:")
#st.image("https://github.com/jkomazec/streamlithelloworld/blob/main/gv_options.png")
htp5= 'https://raw.githubusercontent.com/jkomazec/streamlithelloworld/main/gv_options.png'
st.image(htp5, caption= 'Gazeviewer options', width=1000)

st.markdown("Please import your `.csv` files. Please import either **SHELF** or **STANDALONE** files per session.")

uploaded_file = st.file_uploader("Choose ET files", accept_multiple_files = True)

if uploaded_file:
  #df = pd.read_csv(uploaded_file)
  et_raw = pd.concat([pd.read_csv(f, sep=';', keep_default_na=False) for f in uploaded_file])
  #et_raw = st.file_uploader("Choose a file")

  st.subheader('DataFrame')
  st.write(et_raw)
  st.subheader('Descriptive Statistics')
  st.write(et_raw.describe())
else:
  st.info('☝️ Upload a CSV file')

def to_excel(df):
    output = BytesIO()
    writer = pd.ExcelWriter(output, engine='xlsxwriter')
    df.to_excel(writer, index=False, sheet_name='Sheet1')
    workbook = writer.book
    worksheet = writer.sheets['Sheet1']
    format1 = workbook.add_format({'num_format': '0.00'}) 
    worksheet.set_column('A:A', None, format1)  
    writer.save()
    processed_data = output.getvalue()
    return processed_data
df_xlsx = to_excel(et_raw)
st.download_button(label='📥 Download Current Result',
                                data=df_xlsx ,
                                file_name= 'df_test.xlsx')
