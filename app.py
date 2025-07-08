import streamlit as st
from PIL import Image
import requests
from streamlit_lottie import st_lottie
import folium
from streamlit_folium import st_folium
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time

# ===== SETTINGS =====
st.set_page_config(page_title="About Me", page_icon="👋", layout="wide")

# ===== LOAD CSS =====
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

# ===== POP-UP SIDEBAR HINT (5s) =====
if "show_sidebar_hint" not in st.session_state:
    st.session_state.show_sidebar_hint = True

if st.session_state.show_sidebar_hint:
    st.markdown("""
    <div style="
        position: fixed;
        top: 10px;
        left: 80px;
        z-index: 9999;
        background: linear-gradient(135deg, #ffecd2, #fcb69f);
        padding: 12px 18px;
        border-radius: 12px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.15);
        font-weight: 600;
        font-size: 14px;
    ">
        👈 <span style="font-size:17px;">Click arrow to open the sidebar menu!</span>
    </div>
    """, unsafe_allow_html=True)
    time.sleep(5)
    st.session_state.show_sidebar_hint = False

# ===== LOAD ASSETS =====
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

# ===== SIDEBAR =====
st.sidebar.title("📌 Navigation")
page = st.sidebar.radio("Go to", ["Home", "Gallery", "Contact", "Location"])

# ===== PAGE: HOME =====
if page == "Home":
    with st.container():
        left_col, right_col = st.columns(2)
        with left_col:
            st.subheader("Hi, I'm Muhammad Ridzuan 👋")
            st.title("Diploma Student in Corporate Investigation")
            st.markdown("""
            <div class='justified-text'>
            I'm a student at SMART College, KL. Currently seeking internship in fraud investigation, compliance or forensic audit. I’m a fast learner, analytical and highly motivated to grow.
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
            My studies cover corporate law, fraud detection, digital forensics, and investigation reporting. I’ve also built strong teamwork and communication skills.
            </div>
            """, unsafe_allow_html=True)
            st.write("[📄 My Resume](https://drive.google.com/file/d/1ee1u7Z7JFByLf4gfSn2biWBL7FmdSsaU/view?usp=drive_link)")
        with right_col:
            st_lottie(lottie_coding, height=300, key="coding")

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
        st.header("📸 My Gallery")
        col1, col2, col3 = st.columns(3)
        col1.image(img1, caption="Me Sleep", use_container_width=True)
        col2.image(img2, caption="Me Wekap", use_container_width=True)
        col3.image(img3, caption="Me Study", use_container_width=True)

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
    st.header("📬 Contact Me")
    with st.form("contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Email")
        message = st.text_area("Message")
        sent = st.form_submit_button("SEND")
    if sent:
        if name and email and message:
            try:
                sender = st.secrets["EMAIL_USER"]
                pwd = st.secrets["EMAIL_PASS"]
                receiver = st.secrets["EMAIL_TO"]

                msg = MIMEMultipart()
                msg["From"] = sender
                msg["To"] = receiver
                msg["Subject"] = "Contact Form"
                msg.attach(MIMEText(f"Name: {name}\nEmail: {email}\nMessage: {message}", "plain"))

                with smtplib.SMTP("smtp.gmail.com", 587) as server:
                    server.starttls()
                    server.login(sender, pwd)
                    server.sendmail(sender, receiver, msg.as_string())
                st.success("✅ Email sent successfully!")
            except Exception as e:
                st.error(f"❌ Error sending email: {e}")
        else:
            st.error("❗ Please fill all fields.")

# ===== PAGE: LOCATION =====
elif page == "Location":
    st.header("📍 Location of SMART College")
    smart_location = [3.1442368716195292, 101.72928812695515]
    map = folium.Map(location=smart_location, zoom_start=17)
    folium.Marker(smart_location, tooltip="SMART College", popup="SMART College, KL").add_to(map)
    st_folium(map, width=700, height=500)

# ===== BACKGROUND MUSIC =====
st.markdown("""
    <audio autoplay loop>
        <source src="https://www.bensound.com/bensound-music/bensound-dreams.mp3" type="audio/mpeg">
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
