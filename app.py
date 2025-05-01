import streamlit as st
import mysql.connector
import hashlib
import base64

# Koneksi ke database
def create_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="18sy1dei",
        database="db_streamlit"
    )

# Enkripsi password
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Login user
def login_user(email, password):
    conn = create_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE email = %s AND password = %s"
    hashed_pw = hash_password(password)
    cursor.execute(query, (email, hashed_pw))
    result = cursor.fetchone()
    conn.close()
    return result

# Registrasi user baru
def register_user(email, full_name, password):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        query = "INSERT INTO users (email, full_name, password) VALUES (%s, %s, %s)"
        hashed_pw = hash_password(password)
        cursor.execute(query, (email, full_name, hashed_pw))
        conn.commit()
        return True
    except Exception as e:
        st.error(f"Gagal daftar: {e}")
        return False
    finally:
        conn.close()

# Fungsi untuk encode gambar ke base64
def load_base64_image(path):
    try:
        with open(path, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except FileNotFoundError:
        st.error(f"Gambar tidak ditemukan: {path}")
        return ""

# Tambahkan CSS background ke Streamlit
def set_background():
    hijau = load_base64_image("assets/icon_hijau.png")
    ungu = load_base64_image("assets/icon_ungu.png")
    pink = load_base64_image("assets/icon_pink.png")

    if not hijau or not ungu or not pink:
        st.warning("Sebagian gambar background tidak ditemukan. Background tidak ditampilkan.")
        return

    st.markdown(f"""
    <style>
    body {{
        background-color: #f9fafb;
    }}
    .stApp {{
        background-image: url("data:image/png;base64,{hijau}"), 
                          url("data:image/png;base64,{pink}"), 
                          url("data:image/png;base64,{ungu}");
        background-position: top left, bottom 30px right 60px, bottom right;
        background-size: 300px, 260px, 420px;
        background-repeat: no-repeat, no-repeat, no-repeat;
        position: relative;
    }}
    .custom-container {{
        background: #f5f5ff;
        padding: 2rem;
        border-radius: 20px;
        border: 1px solid #8d8ff9;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
        max-width: 400px;
        margin: auto;
    }}
    h2 span.selamat {{ color: #4043e9; }}
    h2 span.datang {{ color: #e9509d; }}
    h2 span.kembali {{ color: #38dda6; }}
    .small-text {{ font-size: 13px; color: black; text-align: left; margin-bottom: 1rem; }}
    .signup a {{ color: #e9509d; text-decoration: none; }}
    .signup a:hover {{ text-decoration: underline; }}
    </style>
    """, unsafe_allow_html=True)

# UI utama
def main():
    st.set_page_config(page_title="Login App", layout="centered")
    set_background()

    menu = st.sidebar.selectbox("Menu", ["Login", "Daftar"])

    with st.container():
        st.markdown('<div class="custom-container">', unsafe_allow_html=True)

        if menu == "Login":
            st.markdown("<h2 style='text-align:center'><span class='selamat'>Selamat</span> <span class='datang'>Datang</span> <span class='kembali'>Kembali!</span></h2>", unsafe_allow_html=True)
            email = st.text_input("Email")
            password = st.text_input("Password", type="password")
            st.markdown('<div class="small-text">Lupa Password?</div>', unsafe_allow_html=True)
            if st.button("Masuk"):
                user = login_user(email, password)
                if user:
                    st.success(f"Login berhasil, selamat datang {user[2]}!")
                else:
                    st.error("Email atau password salah.")
            st.markdown('<div class="signup">Belum punya akun? <a href="#">Daftar</a></div>', unsafe_allow_html=True)

        elif menu == "Daftar":
            st.markdown("<h2 style='text-align:center'><span class='datang'>Yuk</span> <span class='kembali'>Mulai</span> <span class='selamat'>Kelola</span> Designmu!</h2>", unsafe_allow_html=True)
            email = st.text_input("Email")
            full_name = st.text_input("Nama Lengkap")
            password = st.text_input("Password", type="password")
            if st.button("Daftar"):
                if register_user(email, full_name, password):
                    st.success("Berhasil daftar! Silakan login.")
            st.markdown('<div class="signup">Sudah punya akun? <a href="#">Login</a></div>', unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
