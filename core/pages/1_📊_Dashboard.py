import streamlit as st
import pandas as pd
import plotly.express as px
import sys
import os
from core.database import tampilkan_sidebar, fetch_data

# 1. Seting Halaman (Harus paling atas)
st.set_page_config(page_title="Dashboard | E-VENTARIS", layout="wide")

# 2. Suntikan CSS Kunci Warna (Agar tetap putih-navy)
st.markdown("""
    <style>
    .stApp { background-color: #ffffff !important; }
    .stApp h1, .stApp h2, .stApp h3, .stApp h4, .stApp p, .stApp span, .stApp label, div[data-testid="stMetricValue"] > div, div[data-testid="stMetricLabel"] > div {
        color: #001f3f !important;
    }
    [data-testid="stSidebar"] { background-color: #001f3f !important; }
    [data-testid="stSidebar"] *, [data-testid="stSidebar"] p, [data-testid="stSidebar"] span { color: #ffffff !important; }
    </style>
""", unsafe_allow_html=True)

# Mencari alamat folder utama (WEB_AKHIR)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Menggabungkan alamat folder utama dengan folder static dan nama file

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
from core.database import fetch_data

st.set_page_config(page_title="Dashboard - E-VENTARIS", layout="wide")

st.title("Dashboard Inventaris Paskibra")
st.write("Ringkasan data barang secara real-time")

# Ambil data dari database
df = fetch_data()

if df.empty:
    st.info("Belum ada data untuk ditampilkan. Silakan isi data di menu Tambah Barang.")
else:
    # --- BARIS 1: RINGKASAN ANGKA ---
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total Barang", len(df))
    with col2:
        st.metric("Total Unit", int(df['jumlah'].sum()))
    with col3:
        st.metric("Kondisi Baik", len(df[df['kondisi'] == 'Baik']))
    with col4:
        st.metric("Barang Tersedia", len(df[df['status'] == 'Tersedia']))

    st.markdown("---")

    # --- BARIS 2: GRAFIK VISUAL ---
    left_column, right_column = st.columns(2)

    with left_column:
        st.subheader("Persentase Kondisi Barang")
        fig_kondisi = px.pie(df, names='kondisi', hole=0.4, 
                             color_discrete_sequence=px.colors.qualitative.Pastel)
        st.plotly_chart(fig_kondisi, use_container_width=True)

    with right_column:
        st.subheader("Distribusi Kategori")
        fig_kategori = px.bar(df, x='kategori', y='jumlah', color='kategori',
                              text_auto=True, title="Jumlah Unit per Kategori")
        st.plotly_chart(fig_kategori, use_container_width=True)
