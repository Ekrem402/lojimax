import pandas as pd
import streamlit as st

# Google Sheets CSV bağlantısı
sheet_id = "1BnZd9fGTb2yGnn8H1fzEi32df_jKJEZ9"
sheet_name = "Sayfa1"  # Gerekirse değiştir
csv_url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"

# Veriyi oku
df = pd.read_csv(csv_url)

st.title("📊 Ürün Sorgulama Paneli")

# 🔍 Filtre bileşenleri
col1, col2, col3 = st.columns(3)

with col1:
    urun_adlari = [""] + sorted(df['Ürün Adı'].dropna().unique().astype(str).tolist())
    selected_urun = st.selectbox("🔎 Ürün Adı", urun_adlari)

with col2:
    yukseklikler = [""] + sorted(df['Yükseklik'].dropna().unique().astype(str).tolist())
    selected_yukseklik = st.selectbox("📏 Yükseklik", yukseklikler)

with col3:
    renkler = [""] + sorted(df['Renk'].dropna().unique().astype(str).tolist())
    selected_renk = st.selectbox("🎨 Renk", renkler)

# 📌 Filtre uygulama
filtered_df = df.copy()
if selected_urun:
    filtered_df = filtered_df[filtered_df['Ürün Adı'].astype(str) == selected_urun]

if selected_yukseklik:
    filtered_df = filtered_df[filtered_df['Yükseklik'].astype(str) == selected_yukseklik]

if selected_renk:
    filtered_df = filtered_df[filtered_df['Renk'].astype(str) == selected_renk]

# 📋 Sonuçları göster
st.subheader("🔎 Filtrelenmiş Ürünler")
st.dataframe(filtered_df, use_container_width=True)
