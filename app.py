import streamlit as st
from PIL import Image
import requests
from streamlit_lottie import st_lottie
import folium
from streamlit_folium import st_folium
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# ===== SETTINGS =====
st.set_page_config(page_title="About Me", page_icon="👋", layout="wide")

import time

# === TUTORIAL BUBBLE / GUIDE ===
if "show_sidebar_hint" not in st.session_state:
    st.session_state.show_sidebar_hint = True

if st.session_state.show_sidebar_hint:
    st.markdown("""
        <div style="
            position: fixed;
            top: 20px;
            left: 40px;
            background-color: #fffae6;
            padding: 12px 18px;
            border-radius: 8px;
            box-shadow: 0 2px 6px rgba(0,0,0,0.15);
            z-index: 9999;
            font-size: 15px;
            font-weight: 500;
            color: #333;
        ">
            👉 Tip: Click the arrow at the top-left to open the sidebar menu.
        </div>
    """, unsafe_allow_html=True)

    time.sleep(5)
    st.session_state.show_sidebar_hint = False



# ===== CSS =====
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

# ===== ASSETS =====
def load_lottieurl(url):
    try:
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    except:
        return None

lottie_hello = load_lottieurl("https://lottie.host/afb5e48c-63ad-4589-a51a-069a8faa7cc0/2UOBuEjjFP.json")
lottie_coding = load_lottieurl("https://lottie.host/7aa80ad3-97bb-4b64-aa94-5800263195c5/aoW6sdJFhW.json")
img1 = Image.open("images/kucing1.jpg")
img2 = Image.open("images/kucing2.jpg")
img3 = Image.open("images/kucing3.jpg")

# ===== SIDEBAR NAVIGATION =====
st.sidebar.title("📌 Navigation")
page = st.sidebar.radio("Pergi ke:", ["Home", "Gallery", "Contact", "Location"])

# ===== PAGE: HOME =====
if page == "Home":
    with st.container():
        left_col, right_col = st.columns(2)
        with left_col:
            st.subheader("Hi, I'm Muhammad Ridzuan 👋")
            st.title("Diploma Student in Corporate Investigation")
            st.markdown("""
            <div class='justified-text'>
            Hello! My name is Muhammad Ridzuan Bin Darwin, and I am a 20-year-old student at SMART College, Kuala Lumpur. I’m excited to find internship opportunities in fraud investigation, compliance, or internal audit. I am a fast learner, adaptable, and motivated to contribute positively to a company.
            </div>
            """, unsafe_allow_html=True)
            st.write("[🌐 My Linktree](https://linktr.ee/zunohuzz)")
        with right_col:
            st_lottie(lottie_hello, height=250, key="hello")

    with st.container():
        st.write("---")
        left_col, right_col = st.columns(2)
        with left_col:
            st.header("📚 What I Learn at SMART College")
            st.markdown("""
            <div class='justified-text'>
            I gained knowledge in corporate law, fraud investigation, digital forensics, and ethical practices. I also improved soft skills like communication and teamwork, preparing me for real-world investigation work.
            </div>
            """, unsafe_allow_html=True)
            st.write("[📄 My Resume](https://drive.google.com/file/d/1ee1u7Z7JFByLf4gfSn2biWBL7FmdSsaU/view?usp=drive_link)")
        with right_col:
            st_lottie(lottie_coding, height=300, key="coding")

    # ===== SKILLSET SECTION =====
    st.write("---")
    st.header("🧠 My Skillset")

    skills = {
        "Digital Forensics": 80,
        "Fraud Investigation": 85,
        "Python (Basic)": 60,
        "Report Writing": 75,
        "Teamwork & Communication": 90
    }

    for skill, level in skills.items():
        st.write(f"{skill}")
        st.progress(level)

# ===== PAGE: GALLERY =====
elif page == "Gallery":
    with st.container():
        st.header("📸 My Saya Gallery")
        img_col1, img_col2, img_col3 = st.columns(3)
        with img_col1:
            st.image(img1, caption="Me Sleep", use_container_width=True)
        with img_col2:
            st.image(img2, caption="Me Wekap", use_container_width=True)
        with img_col3:
            st.image(img3, caption="Me Study", use_container_width=True)

    with st.container():
        st.write("---")
        st.header("🎥 Monyet Joget")
        if st.button("SYBAU 😎"):
            st.markdown("""
            <video width="100%" autoplay controls loop>
                <source src="https://i.imgflip.com/49iy5a.mp4" type="video/mp4">
            </video>
            """, unsafe_allow_html=True)

# ===== PAGE: CONTACT =====
elif page == "Contact":
    st.header("📬 Contact Form")

    with st.form("contact_form"):
        name = st.text_input("Nama")
        email = st.text_input("Email")
        message = st.text_area("Mesej")
        submitted = st.form_submit_button("SEND")

    if submitted:
        if name and email and message:
            try:
                sender = st.secrets["EMAIL_USER"]
                pwd = st.secrets["EMAIL_PASS"]
                receiver = st.secrets["EMAIL_TO"]

                msg = MIMEMultipart()
                msg["From"] = sender
                msg["To"] = receiver
                msg["Subject"] = "Contact Form Test"
                msg.attach(MIMEText(f"Name: {name}\nEmail: {email}\nMessage: {message}", "plain"))

                with smtplib.SMTP("smtp.gmail.com", 587) as server:
                    server.starttls()
                    server.login(sender, pwd)
                    server.sendmail(sender, receiver, msg.as_string())

                st.success("✅ Emel berjaya dihantar!")
            except Exception as e:
                st.error(f"❌ Gagal hantar emel: {e}")
        else:
            st.error("❗ Sila lengkapkan semua bahagian.")

# ===== PAGE: LOCATION =====
elif page == "Location":
    st.header("📍 Lokasi SMART College")
    smart_location = [3.1442368716195292, 101.72928812695515]
    m = folium.Map(location=smart_location, zoom_start=17)
    folium.Marker(smart_location, tooltip="SMART College", popup="SMART College, Kuala Lumpur").add_to(m)
    st_folium(m, width=700, height=500)

#---------ambient---------
st.markdown("""
    <audio autoplay loop>
        <source src="https://www.bensound.com/bensound-music/bensound-dreams.mp3" type="audio/mpeg">
        Your browser does not support the audio element.
    </audio>
""", unsafe_allow_html=True)

# ===== FOOTER =====
st.markdown("""
    <hr style="margin-top: 50px; margin-bottom: 10px; border: 0.5px solid #e0e0e0;" />
    <div style='text-align: center; font-size: 14px; color: #777; padding-bottom: 20px;'>
        Built with ❤️ by <strong>Muhammad Ridzuan</strong> | 
        <a href='mailto:ridzuan245z@gmail.com' style='color:#555; text-decoration: none;'>Email</a> • 
        <a href='https://linktr.ee/zunohuzz' target='_blank' style='color:#555; text-decoration: none;'>Linktree</a><br>
        © 2025 Muhammad Ridzuan. All rights reserved.
    </div>
""", unsafe_allow_html=True)



