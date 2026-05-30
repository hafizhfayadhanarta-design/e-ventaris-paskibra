import streamlit as st
from core.database import tampilkan_sidebar

# 1. Konfigurasi Halaman (Harus Paling Atas!)
st.set_page_config(page_title="Home | E-VENTARIS", layout="wide")

# 2. TEMBAK CSS LANGSUNG DI SINI (Memaksa Warna Aplikasi)
st.markdown("""
    <style>
    /* Latar belakang halaman utama wajib putih */
    .stApp {
        background-color: #ffffff !important;
    }
    
    /* Semua teks di konten utama wajib Navy */
    .stApp h1, .stApp h2, .stApp h3, .stApp h4, .stApp p, .stApp span, .stApp label {
        color: #001f3f !important;
    }
    
    /* Paling Penting: Paksa warna background SIDEBAR jadi Navy gelap */
    [data-testid="stSidebar"] {
        background-color: #001f3f !important;
    }
    
    /* Paksa semua teks di dalam SIDEBAR jadi putih bersih */
    [data-testid="stSidebar"] *, [data-testid="stSidebar"] p, [data-testid="stSidebar"] span {
        color: #ffffff !important;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Panggil fungsi database untuk memuat logo dan menu
tampilkan_sidebar()

# --- HEADER APLIKASI ---
st.markdown("""
    <div style="text-align: center; margin-top: 30px; margin-bottom: 40px;">
        <h1 style="font-size: 3.2rem; font-weight: 800; letter-spacing: -1px; margin-bottom: 5px; color: #001f3f !important;">E-VENTARIS</h1>
        <p style="font-size: 1.2rem; font-style: italic; opacity: 0.85; color: #001f3f !important;">Sistem Informasi Inventaris Paskibra Berbasis Platform Digital</p>
    </div>
""", unsafe_allow_html=True)

st.divider()

# --- KONTEN UTAMA: PILAR UTAMA SISTEM ---
st.markdown("""
    <div style="text-align: center; margin-bottom: 25px;">
        <h3 style="display: inline-block; border-bottom: 3px solid #FFD700; padding-bottom: 8px; font-weight: 700; color: #001f3f !important;">
            Pilar Utama Sistem
        </h3>
    </div>
""", unsafe_allow_html=True)

# Membuat 3 kolom sejajar
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
        <div style="text-align: center; padding: 10px;">
            <h4 style="margin-bottom: 8px; color: #001f3f !important;">🔍 Transparansi</h4>
            <p style="font-size: 1rem; line-height: 1.4; color: #001f3f !important;">Kemudahan akses pantau kondisi dan ketersediaan logistik secara terbuka.</p>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div style="text-align: center; padding: 10px;">
            <h4 style="margin-bottom: 8px; color: #001f3f !important;">💡 Akurasi</h4>
            <p style="font-size: 1rem; line-height: 1.4; color: #001f3f !important;">Pencatatan jumlah dan mutasi barang secara real-time ke pusat data.</p>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
        <div style="text-align: center; padding: 10px;">
            <h4 style="margin-bottom: 8px; color: #001f3f !important;">⚡ Efisiensi</h4>
            <p style="font-size: 1rem; line-height: 1.4; color: #001f3f !important;">Memangkas rekapitulasi manual menjadi digital yang cepat dan aman.</p>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)
st.divider()

# --- FOOTER ---
st.markdown("""
    <div style="text-align: center; opacity: 0.7; font-size: 0.95rem; color: #001f3f !important;">
        💡 <i>Gunakan menu navigasi di sebelah kiri untuk mulai mengelola atau memantau data inventaris.</i>
    </div>
""", unsafe_allow_html=True)