import gdown
import pandas as pd
import streamlit as st

# Başlık
st.title("LOJIMAX - ÖZET (Veri Görselleştirme)")

# Google Drive dosya linki (sadece dosya ID kısmını aldık)
url = "https://drive.google.com/uc?id=1iU-Q96InL-DPi3OcrjbG8XnU_mcx_Tv_"
output = "lojimax_maliyet.xlsx"

# Dosyayı indir (zaten varsa tekrar indirmez)
gdown.download(url, output, quiet=False)

# Excel dosyasının 'ÖZET' sayfasını oku, başlık 2. satırda (index 1)
df = pd.read_excel(output, sheet_name="ÖZET", header=1)

# Sadece dolu olan satırları filtrele
df = df.dropna(how='all')

# İlk 9 sütun (0-8) ve 17–21 arası sütunları birleştir
df_selected = pd.concat([df.iloc[:, 0:9], df.iloc[:, 17:22]], axis=1)

# Alt başlık
st.subheader("📌 ÖZET Sayfası - Seçilen Sütunlar (Tüm Satırlar)")

# Tabloyu göster
st.dataframe(df_selected)
