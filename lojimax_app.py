import gdown
import pandas as pd
import streamlit as st

# Başlık
st.title("LOJIMAX - Ürün Sorgulama Paneli")

# Google Drive'dan dosyayı indir
url = "https://drive.google.com/uc?id=1iU-Q96InL-DPi3OcrjbG8XnU_mcx_Tv_"
output = "lojimax_maliyet.xlsx"
gdown.download(url, output, quiet=False)

# Excel'den ÖZET sayfasını oku
df = pd.read_excel(output, sheet_name="ÖZET", header=1)
df = df.dropna(how='all')  # Tamamen boş satırları at

# Kullanıcı sorgusu
st.subheader("🔍 Sorgu Yapınız")

with st.expander("Sorgu Yapmak İçin Tıklayın"):
    urun_adi = st.text_input("Ürün Adı (4. sütun)", "")
    yukseklik = st.text_input("Yükseklik (6. sütun, örn: 600)", "")
    dilim_sayisi = st.text_input("Dilim Sayısı (7. sütun, örn: 3)", "")

# Filtrele
filtered_df = df.copy()

if urun_adi:
    filtered_df = filtered_df[filtered_df.iloc[:, 3].astype(str).str.contains(urun_adi, case=False, na=False)]

if yukseklik:
    filtered_df = filtered_df[filtered_df.iloc[:, 5].astype(str) == yukseklik]

if dilim_sayisi:
    filtered_df = filtered_df[filtered_df.iloc[:, 6].astype(str) == dilim_sayisi]

# Sadece gerekli sütunları al (4, 6, 7, 18–21)
final_df = filtered_df.iloc[:, [3, 5, 6, 17, 18, 19, 20]].copy()

# Sütun adlarını güncelle
final_df.columns = ["Ürün Adı", "Yükseklik", "Dilim Sayısı", "Fiyat 1", "Fiyat 2", "Fiyat 3", "Fiyat 4"]

# Fiyat sütunlarını 2 ondalık basamakla göster
for col in ["Fiyat 1", "Fiyat 2", "Fiyat 3", "Fiyat 4"]:
    final_df[col] = pd.to_numeric(final_df[col], errors="coerce").round(2)

# Sonuçları göster
st.subheader("📄 Sorgu Sonuçları")

if not final_df.empty:
    st.dataframe(final_df)
else:
    st.warning("❗ Sonuç bulunamadı. Lütfen filtre kriterlerini kontrol edin.")
