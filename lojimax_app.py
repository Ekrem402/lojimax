import gdown
import pandas as pd
import streamlit as st

# Başlık
st.title("LOJIMAX - ÖZET (Google Drive Üzerinden Excel)")

# Google Drive dosya linki
url = "https://drive.google.com/uc?id=1iU-Q96InL-DPi3OcrjbG8XnU_mcx_Tv_"
output = "lojimax_maliyet.xlsx"

# Dosyayı indir
gdown.download(url, output, quiet=False)

# Excel dosyasının "ÖZET" sayfasını oku (başlık 2. satırda)
df = pd.read_excel(output, sheet_name="ÖZET", header=1)

# İlk 8 satırı al
df_first8 = df.head(8)

# İlk 9 sütun (0-8) ve 17-21 arası sütunları birleştir
df_selected = pd.concat([df_first8.iloc[:, 0:9], df_first8.iloc[:, 17:22]], axis=1)

# Alt başlık
st.subheader("📌 ÖZET - Seçilen Sütunlar")

# Tabloyu göster
st.dataframe(df_selected)
