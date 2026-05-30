import streamlit as st
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

# --- 1. LOGIKA PENCARIAN FOLDER CORE ---
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

# --- 2. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="Daftar Barang - E-VENTARIS", layout="wide")

st.title("Daftar Inventaris Paskibra")
st.write("Data barang tersimpan secara transparan di database.")

# Mengambil data
df = fetch_data()

if df.empty:
    st.warning("Gudang data masih kosong.")
else:
    # --- 3. FITUR PENCARIAN ---
    search = st.text_input("Cari Nama Barang", placeholder="Ketik nama barang untuk mencari...")
    
    if search:
        df = df[df['nama_barang'].str.contains(search, case=False)]

  # --- 4. TAMPILAN TABEL RATA TENGAH (VERSI UPDATE) ---
    st.markdown("""
        <style>
        /* 1. Paksa teks di sel dan header ke tengah */
        [data-testid="stDataFrame"] td, 
        [data-testid="stDataFrame"] th {
            text-align: center !important;
        }

        /* 2. Paksa angka (yang biasanya di dalam div flex) ke tengah */
        [data-testid="stDataFrame"] div[data-testid="stTable"] div,
        [data-testid="stDataFrame"] div[class*="st-"] {
            justify-content: center !important;
            text-align: center !important;
            width: 100%;
        }

        /* 3. Menghilangkan padding berlebih agar benar-benar simetris */
        [data-testid="stDataFrame"] td > div {
            padding-right: 0px !important;
        }
        </style>
        """, unsafe_allow_html=True)
        
    st.dataframe(
        df, 
        use_container_width=True, 
        hide_index=True,
        column_config={
            "id": st.column_config.NumberColumn("ID", format="%d", width="small"),
            "nama_barang": st.column_config.TextColumn("Nama Barang", width="medium"),
            "kategori": st.column_config.TextColumn("Kategori", width="small"),
            "jumlah": st.column_config.NumberColumn("Jumlah", format="%d", width="small"),
            "kondisi": st.column_config.TextColumn("Kondisi", width="small"),
            "status": st.column_config.TextColumn("Status", width="small"),
        }
    )

    # --- 5. STATISTIK ---
    st.markdown("---")
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Jenis", len(df))
    col2.metric("Total Unit", int(df['jumlah'].sum()))
    col3.metric("Kondisi Baik", len(df[df['kondisi'] == 'Baik']))
