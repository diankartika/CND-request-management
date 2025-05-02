# 🎨 Content & Design Request Management Website

A simple internal web-based platform to help the **Content & Design Division of OmahTI** manage design requests efficiently. This system enables structured form submissions, real-time status tracking, automated reminders, and calendar views for improved workflow and collaboration.

---

## 📌 Features

- 📝 **Structured Design Request Form**
- 📊 **Request Dashboard with Status Tracking** (Pending, On Progress, Done)
- 📅 **Calendar View** (Monthly)
- 🔔 **Automatic H-1 Reminders** before deadlines
- 🧑‍💻 **Admin Assignment** of requests to designers
- 🔐 **Basic Login Authentication**

---

## 🧱 Tech Stack

- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Streamlit
- **Database:** MySQL
- **Deployment:** Streamlit Community Cloud (Free hosting)

---

## 📁 Folder Structure

```bash
.
├── frontend/             # Static files (HTML/CSS/JS)
├── backend/              # Streamlit app & logic
├── database/             # SQL schema and scripts
├── assets/               # Images or mockups
└── README.md
🚀 Getting Started (Local Development)

1. Clone the Repository
git clone https://github.com/your-org/request-management.git
cd request-management
2. Setup Virtual Environment
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate for Windows
3. Install Dependencies
pip install -r requirements.txt
4. Run the App
streamlit run backend/app.py
🗂️ Project Documents

🎨 UI Design (Figma) : https://www.figma.com/design/tKHBBDzb2sGNlSKuBaqu5q/UI-Design-OmahTIpes?node-id=75-1661&t=jJDv8edAFGqhAHZi-1
📄 Project Requirement Document (PRD) : https://docs.google.com/document/d/1tUwVXxiGxhRV3zGL7xieCE_my7ZCj3yV/edit?usp=sharing&ouid=111051125610553820387&rtpof=true&sd=true
📆 Development Timeline

Stage	Date
Initial Planning	16 Mar – 20 Apr
UX Research	20 – 25 Apr
UI Design	25 – 28 Apr
Development	28 Apr – 1 May
Testing & Bugfixing	1 May
Deployment	1 – 2 May
🧑‍🤝‍🧑 Project Team

PM: Dian Kartika Putri
PO: Maulana Faris
UI/UX: Rafael
Frontend: Deira, Faris
Backend: Deira, Nugi
📄 License

This project is open source and free to use for internal educational and organizational purposes. No commercial use without permission.
