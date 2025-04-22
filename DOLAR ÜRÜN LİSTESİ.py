import pandas as pd
import streamlit as st

# Sheet URL'yi CSV çıktısı olarak al
sheet_id = "1BnZd9fGTb2yGnn8H1fzEi32df_jKJEZ9"
sheet_name = "Sayfa1"  # Eğer ad farklıysa güncelle
csv_url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"

# Veriyi oku
df = pd.read_csv(csv_url)

st.title("Ürün Sorgulama Paneli")
st.dataframe(df)
