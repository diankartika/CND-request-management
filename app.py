import streamlit as st
import mysql.connector
from mysql.connector import Error
import hashlib

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

# Cek login
def login_user(email, password):
    conn = create_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE email = %s AND password = %s"
    hashed_pw = hash_password(password)
    cursor.execute(query, (email, hashed_pw))
    result = cursor.fetchone()
    conn.close()
    return result

# Simpan user baru
def register_user(email, full_name, password):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        query = "INSERT INTO users (email, full_name, password) VALUES (%s, %s, %s)"
        hashed_pw = hash_password(password)
        cursor.execute(query, (email, full_name, hashed_pw))
        conn.commit()
        return True
    except Error as e:
        st.error(f"Gagal daftar: {e}")
        return False
    finally:
        conn.close()

# UI utama
def main():
    st.set_page_config(page_title="Login App", layout="centered")

    menu = st.sidebar.selectbox("Menu", ["Login", "Daftar"])

    if menu == "Login":
        st.markdown("<h2 style='text-align: center; color: #00BFFF;'>Selamat <span style='color:purple'>Datang</span> <span style='color:green'>Kembali!</span></h2>", unsafe_allow_html=True)
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        if st.button("Masuk"):
            user = login_user(email, password)
            if user:
                st.success(f"Login berhasil, selamat datang {user[2]}!")
            else:
                st.error("Email atau password salah.")
        st.info("Belum punya akun? Daftar")

    elif menu == "Daftar":
        st.markdown("<h2 style='text-align: center; color: #FF69B4;'>Yuk <span style='color:limegreen'>Mulai</span> <span style='color:blue'>Kelola</span> Designmu!</h2>", unsafe_allow_html=True)
        email = st.text_input("Email")
        full_name = st.text_input("Nama Lengkap")
        password = st.text_input("Password", type="password")
        if st.button("Daftar"):
            if register_user(email, full_name, password):
                st.success("Berhasil daftar! Silakan login.")
        st.info("Sudah punya akun? Login")

if __name__ == "__main__":
    main()
