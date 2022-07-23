import streamlit as st
import pandas as pd

st.title('Eye tracking raw export transformator')

st.subheader('Prerequisites')
#st.markdown('As described in the Scribehow tutorial, please download all the necessary files from the Gazeviewer by selecting the following options:')
#st.image("https://github.com/jkomazec/streamlithelloworld/blob/main/gv_options.png")
htp5= 'https://github.com/jkomazec/streamlithelloworld/blob/main/gv_options.png'
st.image(htp5, caption= 'Gazeviewer options', width=300)

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
