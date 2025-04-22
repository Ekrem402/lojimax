import streamlit as st
import pandas as pd
import os
import gdown

# Sayfa başlığı ve yapılandırma
st.set_page_config(page_title="LOJIMAX - ÖZET", layout="wide")
st.title("📄 LOJIMAX - ÖZET (Google Drive Üzerinden Excel)")

# Google Drive dosya ID'si ve indirme yolu
file_id = "1Ui-QD5lRrD2baojcrJBGXwh_mcx_Tv"
output_file = "lojimax_ozet.xlsx"
url = f"https://drive.google.com/uc?id={file_id}"

# Excel dosyasını indir ve yükle
@st.cache_data
def download_and_load_excel():
    if not os.path.exists(output_file):
        gdown.download(url, output_file, quiet=False)
    df = pd.read_excel(output_file, sheet_name="ÖZET", engine="openpyxl")
    return df

# Veri yükleme ve gösterme
try:
    df = download_and_load_excel()

    # 0-8 ve 17-21. sütunları birleştir
    df_secili = pd.concat([df.iloc[:, :9], df.iloc[:, 17:22]], axis=1)

    st.subheader("📌 ÖZET - Seçilen Sütunlar")
    st.dataframe(df_secili, use_container_width=True)

except Exception as e:
    st.error(f"❌ Veri okunamadı: {e}")
