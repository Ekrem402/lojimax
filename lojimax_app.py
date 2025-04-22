import streamlit as st
import pandas as pd

st.set_page_config(page_title="LOJIMAX ÖZET", layout="wide")

st.title("📊 LOJIMAX - ÖZET (Google Sheets üzerinden)")

# Google Sheets ID (Paylaştığın dosyadan alındı)
sheet_id = "1iU-Q96InL-DPi3OcrjbG8XnU_mcx_Tv_"

# CSV formatında veri çek
sheet_url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv"

# Google Sheets verisini oku (önbellekleme açık)
@st.cache_data
def oku_sheet():
    return pd.read_csv(sheet_url)

try:
    df = oku_sheet()

    # İlk 9 sütun (0–8) ve 17–21 arası sütunları al
    df_secili = pd.concat([df.iloc[:, :9], df.iloc[:, 17:22]], axis=1)

    st.subheader("📄 ÖZET - Seçilen Sütunlar")
    st.dataframe(df_secili, use_container_width=True)

except Exception as e:
    st.error(f"❌ Veri okunamadı: {e}")
