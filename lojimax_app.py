import streamlit as st
import pandas as pd
import requests
from io import BytesIO

st.set_page_config(page_title="LOJIMAX ÖZET", layout="wide")
st.title("📊 LOJIMAX - ÖZET (Google Drive üzerinden Excel)")

# Google Drive dosya ID'si
file_id = "1iU-Q96InL-DPi3OcrjbG8XnU_mcx_Tv_"
url = f"https://drive.google.com/uc?id={file_id}"

@st.cache_data
def load_excel():
    response = requests.get(url)
    return pd.read_excel(BytesIO(response.content), sheet_name="ÖZET", engine="openpyxl")

try:
    df = load_excel()

    # Sadece 0–8 ve 17–21. sütunlar (10–16 arası gizlenmiş olacak)
    df_secili = pd.concat([df.iloc[:, :9], df.iloc[:, 17:22]], axis=1)

    st.subheader("📄 ÖZET - Seçilen Sütunlar")
    st.dataframe(df_secili, use_container_width=True)

except Exception as e:
    st.error(f"❌ Veri okunamadı: {e}")
