import streamlit as st
import pandas as pd
import gdown

# Google Drive'dan dosyayı indir
url = "https://drive.google.com/uc?id=1iU-Q96InL-DPi3OcrjbG8XnU_mcx_Tv_"
output = "lojimax_maliyet.xlsx"
gdown.download(url, output, quiet=False)

# Excel dosyasını oku
df = pd.read_excel(output)

# Başlık
st.title("Lojimax Maliyet Tablosu")

# İlk 5 satırı göster
st.subheader("İlk 5 Satır")
st.dataframe(df.head())

# Tüm veriyi gösterme butonu
if st.checkbox("Tüm veriyi göster"):
    st.dataframe(df)

# Kolon bilgilerini göster
st.subheader("Kolonlar")
st.write(df.columns.tolist())

# Eksik verileri göster
st.subheader("Eksik Değerler")
st.write(df.isnull().sum())
