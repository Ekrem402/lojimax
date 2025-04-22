import gdown
import pandas as pd
import streamlit as st

# Başlık
st.title("LOJIMAX - ÖZET (Google Drive Üzerinden Excel)")

# Google Drive dosya linki
url = "https://drive.google.com/uc?id=1iU-Q96InL-DPi3OcrjbG8XnU_mcx_Tv_"
output = "lojimax_maliyet.xlsx"

# Dosyayı indir (varsa tekrar indirme)
gdown.download(url, output, quiet=False)

# Excel'in "ÖZET" sayfasını oku (başlık 2. satırda)
df = pd.read_excel(output, sheet_name="ÖZET", header=1)

# İlk 8 satırı ve 17–21. sütunlar arasını al
df_first8 = df.head(8)
df_selected_columns = df_first8.iloc[:, 17:22]

# Alt başlık
st.subheader("📌 ÖZET - Seçilen Sütunlar")

# Tabloyu göster
st.dataframe(df_selected_columns)
