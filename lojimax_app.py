import streamlit as st
import pandas as pd
import os

# Dosya yolu
dosya_yolu = r"C:\Users\asus\Desktop\LOJIMAX_MALIYET_16022025-havlupan düzeltmesi.xlsx"

# Dosya kontrolü
if not os.path.exists(dosya_yolu):
    st.error("❌ Dosya bulunamadı.")
    st.stop()

# ÖZET sayfasını oku (önbellekle)
@st.cache_data
def oku_ozet():
    return pd.read_excel(dosya_yolu, sheet_name="ÖZET")

try:
    df = oku_ozet()

    # İlk 9 sütun (0–8) ve 17–21 arası sütunları al
    df_secili = pd.concat([df.iloc[:, :9], df.iloc[:, 18:22]], axis=1)

    st.title("📌 LOJIMAX - ÖZET (Filtrelenmiş Sütunlar)")
    st.dataframe(df_secili)

except ValueError:
    st.error("❌ Excel dosyasında 'ÖZET' sayfası bulunamadı.")
