import streamlit as st
import pandas as pd
import gdown

st.set_page_config(page_title="Ürün Sorgulama", layout="wide")

@st.cache_data
def load_data():
    url = "https://drive.google.com/uc?id=1BnZd9fGTb2yGnn8H1fzEi32df_jKJEZ9"
    output = "yeni_excel.xlsx"
    gdown.download(url, output, quiet=True)
    
    df = pd.read_excel(output, sheet_name="ÖZET", header=1)
    df = df.dropna(how='all')
    return df

df = load_data()

st.title("📊 Ürün Sorgulama Paneli")

# Filtre Alanları
col1, col2, col3 = st.columns(3)

with col1:
    urun_adi = st.text_input("🔍 Ürün Adı (C sütunu)")
with col2:
    yukseklik = st.text_input("📏 Yükseklik (E sütunu)")
with col3:
    dilim_sayisi = st.text_input("🔢 Dilim Sayısı (F sütunu)")

# Filtreleme
filtered_df = df.copy()

if urun_adi:
    filtered_df = filtered_df[filtered_df.iloc[:, 2].astype(str).str.contains(urun_adi, case=False, na=False)]

if yukseklik:
    filtered_df = filtered_df[filtered_df.iloc[:, 4].astype(str).str.contains(yukseklik, case=False, na=False)]

if dilim_sayisi:
    filtered_df = filtered_df[filtered_df.iloc[:, 5].astype(str).str.contains(dilim_sayisi, case=False, na=False)]

# Sayısal sütunları 1 basamaklı göster
numeric_cols = filtered_df.select_dtypes(include=['float', 'int']).columns
filtered_df[numeric_cols] = filtered_df[numeric_cols].applymap(lambda x: round(x, 1))

# Tabloda göster
st.dataframe(filtered_df, use_container_width=True)
