import streamlit as st
import streamlit.components.v1 as components
import base64
import os
import mysql.connector
import hashlib

# Fungsi embed gambar ke dalam HTML
def embed_assets_in_html(html_path, asset_folder="assets"):
    with open(html_path, "r", encoding="utf-8") as f:
        html = f.read()

    for filename in os.listdir(asset_folder):
        if filename.lower().endswith((".png", ".jpg", ".jpeg", ".gif")):
            filepath = os.path.join(asset_folder, filename)
            with open(filepath, "rb") as img_file:
                b64_data = base64.b64encode(img_file.read()).decode()
                data_uri = f"data:image/png;base64,{b64_data}"
                html = html.replace(f"assets/{filename}", data_uri)

    return html

# Koneksi ke database MySQL
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

# Proses login user
def login_user(email, password):
    conn = create_connection()
    cursor = conn.cursor()
    hashed_pw = hash_password(password)
    query = "SELECT * FROM users WHERE email = %s AND password = %s"
    cursor.execute(query, (email, hashed_pw))
    result = cursor.fetchone()
    conn.close()
    return result

# Halaman Landing Page
def show_landing_page():
    html_content = embed_assets_in_html("landing_page.html")
    components.html(html_content, height=1000, scrolling=False)
    
# Halaman Login Page
def show_login_page():
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    if not st.session_state.logged_in:
        # Get credentials from query params
        params = st.experimental_get_query_params()
        email = params.get("email", [None])[0]
        password = params.get("password", [None])[0]

        if email and password:
            user = login_user(email, password)
            if user:
                st.session_state.logged_in = True
                st.session_state.user_name = user[2]  # assuming column 3 is name
                st.experimental_set_query_params(page="dashboard")  # redirect
                st.rerun()
            else:
                st.error("Email atau password salah.")

        # Render the login HTML
        html_content = embed_assets_in_html("login.html")
        components.html(html_content, height=1000, scrolling=False)
    else:
        st.success(f"Login berhasil, selamat datang {st.session_state.user_name}!")



# Main Routing
def main():
    st.set_page_config(page_title="Internship OmahTI", layout="wide")  # ✅ benar: di-indent

    params = st.experimental_get_query_params()
    page = params.get("page", ["landing"])[0]

    if page == "login":
        show_login_page()
    elif page == "dashboard":
        st.write(f"Selamat datang di Dashboard, {st.session_state.get('user_name', 'User')}!")
        if st.button("Logout"):
            st.session_state.logged_in = False
            st.session_state.user_name = ""
            st.experimental_set_query_params(page="landing")
            st.rerun()
    else:
        show_landing_page()


if __name__ == "__main__":
    main()
