
import streamlit as st
import pandas as pd
import sys
import os

st.set_page_config(page_title="Daftar Barang | E-VENTARIS", layout="wide")

# --- SUNTIKAN CSS ---
st.markdown("""
    <style>
    .stApp { background-color: #ffffff !important; }
    .stApp h1, .stApp h2, .stApp h3, .stApp h4, .stApp p, .stApp span, .stApp label, th, td {
        color: #001f3f !important;
    }
    [data-testid="stSidebar"] { background-color: #001f3f !important; }
    [data-testid="stSidebar"] *, [data-testid="stSidebar"] p, [data-testid="stSidebar"] span { color: #ffffff !important; }
    </style>
""", unsafe_allow_html=True)

# Mencari alamat folder utama (WEB_AKHIR)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# --- LOGIKA PENCARIAN FOLDER CORE ---
def add_core_to_path():
    current_path = os.path.abspath(os.path.dirname(__file__))
    while current_path != os.path.dirname(current_path):
        if 'core' in os.listdir(current_path):
            if current_path not in sys.path:
                sys.path.append(current_path)
            return True
        current_path = os.path.dirname(current_path)
    return False

add_core_to_path()
from core.database import fetch_data, get_connection

st.set_page_config(page_title="Kelola Barang - E-VENTARIS", layout="wide")

st.title("Kelola Inventaris")
st.write("Gunakan halaman ini untuk memperbarui data atau menghapus barang yang sudah tidak ada.")

df = fetch_data()

if df.empty:
    st.info("Belum ada data untuk dikelola.")
else:
    # Pilih Barang yang akan diolah
    list_barang = df['nama_barang'].tolist()
    pilih_barang = st.selectbox("Pilih Nama Barang yang ingin diubah/hapus:", list_barang)
    
    # Ambil data spesifik barang yang dipilih
    data_detail = df[df['nama_barang'] == pilih_barang].iloc[0]
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Edit Data")
        with st.form("form_edit"):
            new_nama = st.text_input("Nama Barang", value=data_detail['nama_barang'])
            new_kat = st.selectbox("Kategori", ["Seragam", "Kostum", "Alat Komando", "Lainnya"], 
                                   index=["Seragam", "Kostum", "Alat Komando", "Lainnya"].index(data_detail['kategori']))
            new_jml = st.number_input("Jumlah", value=int(data_detail['jumlah']))
            new_kon = st.radio("Kondisi", ["Baik", "Rusak Ringan", "Rusak Berat"], 
                               index=["Baik", "Rusak Ringan", "Rusak Berat"].index(data_detail['kondisi']))
            new_stat = st.selectbox("Status", ["Tersedia", "Dipinjam", "Hilang"],
                                    index=["Tersedia", "Dipinjam", "Hilang"].index(data_detail['status']))
            
            btn_update = st.form_submit_button("Simpan Perubahan")
            
            if btn_update:
                conn = get_connection()
                curr = conn.cursor()
                curr.execute("""
                    UPDATE inventaris SET nama_barang=?, kategori=?, jumlah=?, kondisi=?, status=?
                    WHERE id=?
                """, (new_nama, new_kat, new_jml, new_kon, new_stat, int(data_detail['id'])))
                conn.commit()
                conn.close()
                st.success("Data berhasil diperbarui!")
                st.rerun()

    with col2:
        st.subheader("Hapus Barang")
        st.warning(f"Apakah kamu yakin ingin menghapus '{pilih_barang}'?")
        if st.button(f"Ya, Hapus {pilih_barang}", type="primary"):
            conn = get_connection()
            curr = conn.cursor()
            curr.execute("DELETE FROM inventaris WHERE id=?", (int(data_detail['id']),))
            conn.commit()
            conn.close()
            st.error("Barang telah dihapus!")
            st.rerun()
            
            st.sidebar.image("static/logo_paskibra.jpg", use_container_width=True)
