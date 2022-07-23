import streamlit as st
import pandas as pd


st.title('Eye tracking raw export transformator')

st.subheader('Prerequisites')

st.markdown("Export from Gazeviewer is not possible until you import the zones. Upon importing the zones, you'll have the **Export** button.")
st.markdown("As described in the Scribehow tutorial, please download all the necessary files from the Gazeviewer by selecting the following options:")
#st.image("https://github.com/jkomazec/streamlithelloworld/blob/main/gv_options.png")
htp5= 'https://raw.githubusercontent.com/jkomazec/streamlithelloworld/main/gv_options.png'
st.image(htp5, caption= 'Gazeviewer options', width=1000)

st.markdown("Please import your `.csv` files. Please import either **SHELF** or **STANDALONE** files per session.")

st.subheader('Enter the cutoff seconds')
st.markdown("Standalone: 3 and 7")
st.markdown("Shelf:      5 and 10")

break1 = st.number_input("Shorter breakpoint", min_value = 1, max_value = 15, value = 3, step = 1)
break2 = st.number_input("Longer breakpoint", min_value = 7, max_value = 15, value = 7, step = 1)

uploaded_file = st.file_uploader("Choose ET files", accept_multiple_files = True)

if uploaded_file:
	#df = pd.read_csv(uploaded_file)
	et_raw = pd.concat([pd.read_csv(f, sep=';', keep_default_na=False) for f in uploaded_file])
	#et_raw = st.file_uploader("Choose a file")

	#cell derivation from the project name
	et_raw['cell_id'] = et_raw['cell_id'].astype(str)
	et_raw['cell_num'] = et_raw.cell_id.str.extract(r'(cell\d+)')
	et_raw['cell_num'] = et_raw['cell_num'].astype(str)
	et_raw['cell'] = et_raw.cell_num.str.extract(r'(\d+)')

	#breakpoint columns calc
	et_raw['break1'] = np.where(et_raw['time_stamp'] == break1, 1, 0)
	et_raw['break2'] = np.where(et_raw['time_stamp'] == break2, 1, 0)

	st.subheader('DataFrame')
	st.write(et_raw)
	st.subheader('Descriptive Statistics')
	st.write(et_raw.describe())
  
	@st.cache
	def convert_df(df):
    		return df.to_csv().encode('utf-8')


  	csv = convert_df(et_raw)

  	st.download_button(
		"Press to Download",
		csv,
		"file.csv",
		"text/csv",
		key='download-csv'
  	)
  	
else:
  st.info('☝️ Upload a CSV file')
