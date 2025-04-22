import streamlit as st
import pandas as pd

# Başlık
st.set_page_config(page_title="Ürün Sorgulama Paneli", layout="wide")
st.title("📊 Ürün Sorgulama Paneli")

# Google Sheets bağlantısı (CSV formatında dışa aktarım linki)
sheet_url = "https://docs.google.com/spreadsheets/d/1BnZd9fGTb2yGnn8H1fzEi32df_jKJEZ9/export?format=csv&gid=0"

# Veriyi oku
df = pd.read_csv(sheet_url)

# Sütun isimlerini düzelt (bazı unnamed'ler olabilir)
df.columns = df.columns.str.strip()

# Gerekli sütunları seç
selected_columns = list(df.columns[:9]) + list(df.columns[17:22])
df = df[selected_columns]

# Sayısal sütunları 1 ondalığa yuvarla
numeric_cols = df.select_dtypes(include='number').columns
df[numeric_cols] = df[numeric_cols].round(1)

# Sorgu formu
with st.form("sorgu_formu"):
    col1, col2, col3 = st.columns(3)
    with col1:
        urun_adi = st.text_input("🔍 Ürün Adı (C sütunu)")
    with col2:
        yukseklik = st.text_input("📏 Yükseklik (E sütunu)")
    with col3:
        dilim_sayisi = st.text_input("🍰 Dilim Sayısı (F sütunu)")
    
    sorgula = st.form_submit_button("✅ Sorgu Yap")

# Sorgulama
if sorgula:
    # Filtreleme
    df_filtered = df.copy()
    if urun_adi:
        df_filtered = df_filtered[df_filtered.iloc[:, 2].astype(str).str.contains(urun_adi, case=False, na=False)]
    if yukseklik:
        df_filtered = df_filtered[df_filtered.iloc[:, 4].astype(str) == yukseklik]
    if dilim_sayisi:
        df_filtered = df_filtered[df_filtered.iloc[:, 5].astype(str) == dilim_sayisi]
    
    # Sonuçları göster
    st.subheader("🔎 Sorgu Sonuçları")
    st.dataframe(df_filtered, use_container_width=True)
