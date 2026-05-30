import sqlite3
import pandas as pd
import os
import streamlit as st

# --- LOGIKA ALAMAT DATABASE ---
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "data", "paskibra.db")

def get_connection():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    return conn

def tampilkan_sidebar():
    import os
    import streamlit as st

    # --- KUNCI CSS GLOBAL (Memastikan warna seragam di semua halaman) ---
    st.markdown("""
        <style>
        /* Latar belakang halaman utama wajib putih */
        .stApp { background-color: #ffffff !important; }
        
        /* Semua teks di konten utama wajib Navy */
        .stApp h1, .stApp h2, .stApp h3, .stApp h4, .stApp h5, .stApp h6, .stApp p, .stApp span, .stApp label, th, td {
            color: #001f3f !important;
        }
        
        /* Angka statistik di Dashboard agar Navy */
        div[data-testid="stMetricValue"] > div { color: #001f3f !important; }
        div[data-testid="stMetricLabel"] > div { color: #001f3f !important; opacity: 0.8; }
        
        /* Paksa warna background SIDEBAR jadi Navy gelap */
        section[data-testid="stSidebar"] { background-color: #001f3f !important; }
        
        /* Paksa semua teks di dalam SIDEBAR jadi putih bersih */
        section[data-testid="stSidebar"] *, section[data-testid="stSidebar"] p, section[data-testid="stSidebar"] span {
            color: #ffffff !important;
        }
        
        /* Warna ikon panah kecil di paling atas sidebar agar tetap Putih */
        section[data-testid="stSidebar"] button svg { fill: #ffffff !important; }

        /* Warna garis pembatas (Divider) menjadi Navy tipis */
        hr { border-color: #001f3f !important; opacity: 0.2 !important; }
        </style>
    """, unsafe_allow_html=True)

    # --- KONTEN SIDEBAR (Tanpa Logo Gambar) ---
    st.sidebar.markdown("### 🇮🇩 E-VENTARIS")
    
    # Menambahkan garis pembatas tipis di sidebar
    st.sidebar.divider()
    
    # Menampilkan tulisan yang kamu inginkan di setiap halaman web
    st.sidebar.markdown("### Sistem Inventaris Paskibra")
    
# --- FUNGSI DATABASE UTAMA ---
def create_table():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS inventaris (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nama_barang TEXT NOT NULL,
            kategori TEXT,
            jumlah INTEGER,
            kondisi TEXT,
            status TEXT
        )
    ''')
    conn.commit()
    conn.close()

def fetch_data():
    conn = get_connection()
    df = pd.read_sql_query("SELECT * FROM inventaris", conn)
    conn.close()
    return df

def add_data(nama, kategori, jumlah, kondisi, status):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO inventaris (nama_barang, kategori, jumlah, kondisi, status)
        VALUES (?, ?, ?, ?, ?)
    ''', (nama, kategori, jumlah, kondisi, status))
    conn.commit()
    conn.close()

# Membuat tabel secara otomatis saat di-import
create_table()
