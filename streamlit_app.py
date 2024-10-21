import streamlit as st
import pandas as pd

# Judul aplikasi
st.title('Tampilan Grafik Dataset')

# Input untuk nama dan NIM
nama = st.text_input("Masukkan Nama Anda")
nim = st.text_input("Masukkan NIM Anda")

# Jika nama dan NIM sudah diisi
if nama and nim:
    st.write(f"Nama: {nama}")
    st.write(f"NIM: {nim}")
    
    # Input untuk memasukkan file dataset
    uploaded_file = st.file_uploader("Upload dataset Anda (format CSV)", type=['csv'])

    # Jika dataset diupload
    if uploaded_file is not None:
        # Membaca dataset dengan encoding latin1
        try:
            df = pd.read_csv(uploaded_file, encoding='latin1')  # Bisa coba 'latin1' atau 'iso-8859-1'
        except UnicodeDecodeError:
            st.error("Gagal membaca file, coba format encoding lain.")
        
        # Menampilkan dataset
        st.write("Dataset yang diupload:")
        st.dataframe(df)

        # Input multi select untuk memilih kolom
        columns = st.multiselect('Pilih kolom yang ingin ditampilkan:', df.columns)

        # Input untuk memilih jenis grafik
        chart_type = st.selectbox('Pilih jenis grafik:', ['Bar Chart', 'Line Chart', 'Area Chart'])

        # Plot grafik berdasarkan jenis dan kolom yang dipilih
        for col in columns:
            st.write(f"Grafik untuk kolom: {col}")

            if chart_type == 'Bar Chart':
                st.bar_chart(df[col])

            elif chart_type == 'Line Chart':
                st.line_chart(df[col])

            elif chart_type == 'Area Chart':
                st.area_chart(df[col])
    else:
        st.write("Silakan upload file dataset (format CSV) untuk memulai.")
else:
    st.write("Silakan masukkan nama dan NIM Anda untuk memulai.")