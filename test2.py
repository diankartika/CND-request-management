import streamlit as st
import streamlit.components.v1 as components
import base64
import os
import mysql.connector
import hashlib

# Fungsi embed gambar ke HTML
def embed_assets_in_html(html_path, asset_folder="assets"):
    with open(html_path, "r", encoding="utf-8") as f:
        html = f.read()

    for filename in os.listdir(asset_folder):
        if filename.endswith((".png", ".jpg", ".jpeg", ".gif")):
            filepath = os.path.join(asset_folder, filename)
            with open(filepath, "rb") as img_file:
                b64_data = base64.b64encode(img_file.read()).decode()
                data_uri = f"data:image/png;base64,{b64_data}"
                html = html.replace(f"assets/{filename}", data_uri)

    return html

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
    hashed_pw = hash_password(password)
    query = "SELECT * FROM users WHERE email = %s AND password = %s"
    cursor.execute(query, (email, hashed_pw))
    result = cursor.fetchone()
    conn.close()
    return result

def main():
    st.set_page_config(page_title="Login Page", layout="wide")

    # 1. Tampilkan HTML
    html_content = embed_assets_in_html("login.html")
    components.html(html_content, height=1000, scrolling=False)

    # 2. Ambil parameter dari URL (via JavaScript)
    params = st.experimental_get_query_params()
    email = params.get("email", [None])[0]
    password = params.get("password", [None])[0]

    # 3. Jika ada input dari login form, proses login
    if email and password:
        user = login_user(email, password)
        if user:
            st.success(f"Login berhasil, selamat datang {user[2]}!")
        else:
            st.error("Email atau password salah.")

if __name__ == "__main__":
    main()
