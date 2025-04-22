import streamlit as st
import pandas as pd

# Başlık
st.markdown("## 📊 Ürün Sorgulama Paneli")

# Google Sheets'teki veriyi oku
sheet_url = "https://docs.google.com/spreadsheets/d/1BnZd9fGTb2yGnn8H1fzEi32df_jKJEZ9/export?format=xlsx"
df = pd.read_excel(sheet_url, sheet_name="ÖZET", header=0)

# Sütun isimlerini temizle
df.columns = df.columns.str.strip()

# Filtrelenecek sütunlar
df_filtered = df.copy()

# Arayüz - Sorgu seçenekleri
col1, col2, col3 = st.columns(3)

with col1:
    urun_adi = st.text_input("🔍 Ürün Adı (C sütunu)")
with col2:
    yukseklik = st.text_input("📏 Yükseklik (E sütunu)")
with col3:
    dilim_sayisi = st.text_input("🧩 Dilim Sayısı (F sütunu)")

# Sorguya göre filtrele
if urun_adi:
    df_filtered = df_filtered[df_filtered.iloc[:, 2].astype(str).str.contains(urun_adi, case=False, na=False)]
if yukseklik:
    df_filtered = df_filtered[df_filtered.iloc[:, 4].astype(str) == yukseklik]
if dilim_sayisi:
    df_filtered = df_filtered[df_filtered.iloc[:, 5].astype(str) == dilim_sayisi]

# Gösterilecek sütunlar: 0–8 + 9–14 (sayısal olanlar)
selected_columns = list(df.columns[:9]) + list(df.columns[9:15])
df_filtered = df_filtered[selected_columns]

# Sayısal sütunları sadece 1 ondalık hane ile göster
numeric_cols = df_filtered.select_dtypes(include='number').columns
df_filtered[numeric_cols] = df_filtered[numeric_cols].applymap(lambda x: round(x, 1))

# Sonuçları göster
st.dataframe(
    df_filtered.style.format({col: "{:.1f}" for col in numeric_cols}),
    use_container_width=True
)
