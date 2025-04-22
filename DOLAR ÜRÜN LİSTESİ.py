import streamlit as st
import pandas as pd
import requests
from io import BytesIO

st.set_page_config(page_title="Ürün Sorgulama Paneli", layout="wide")

st.markdown("## 📊 Ürün Sorgulama Paneli")

# Google Sheet Excel dosyasını indirme
xlsx_url = "https://docs.google.com/spreadsheets/d/1BnZd9fGTb2yGnn8H1fzEi32df_jKJEZ9/export?format=xlsx"
response = requests.get(xlsx_url)
df = pd.read_excel(BytesIO(response.content), engine='openpyxl')

# Sayısal sütunları tek ondalığa yuvarla (float tipindekiler)
numeric_cols = df.select_dtypes(include=['float', 'int']).columns
df[numeric_cols] = df[numeric_cols].applymap(lambda x: round(x, 1) if pd.notnull(x) else x)

# Filtreler
col1, col2, col3 = st.columns(3)

with col1:
    urun_adlari = df.iloc[:, 2].dropna().unique()
    selected_urun = st.selectbox("🔎 Ürün Adı (C sütunu)", [""] + list(urun_adlari))

with col2:
    yukseklikler = df.iloc[:, 4].dropna().unique()
    selected_yukseklik = st.selectbox("📐 Yükseklik (E sütunu)", [""] + list(map(str, sorted(yukseklikler))))

with col3:
    dilim_sayilari = df.iloc[:, 5].dropna().unique()
    selected_dilim = st.selectbox("🌟 Dilim Sayısı (F sütunu)", [""] + list(map(str, sorted(dilim_sayilari))))

# Filtreleme
filtered_df = df.copy()
if selected_urun:
    filtered_df = filtered_df[filtered_df.iloc[:, 2] == selected_urun]
if selected_yukseklik:
    filtered_df = filtered_df[filtered_df.iloc[:, 4].astype(str) == selected_yukseklik]
if selected_dilim:
    filtered_df = filtered_df[filtered_df.iloc[:, 5].astype(str) == selected_dilim]

# Sonuçları göster
st.dataframe(filtered_df, use_container_width=True)
