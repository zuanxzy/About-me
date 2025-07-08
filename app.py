import streamlit as st
from PIL import Image
from pathlib import Path
import requests
from streamlit_lottie import st_lottie

# ---------- SETTINGS ----------
st.set_page_config(page_title="About Me", page_icon="👋", layout="wide")

# ---------- LOAD CSS ----------
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

# ---------- LOAD ASSETS ----------
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

# ---------- HEADER ----------
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

# ---------- ABOUT COLLEGE ----------
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

# ---------- GALLERY ----------
with st.container():
    st.write("---")
    st.header("📸 My Gallery")
    img_col1, img_col2, img_col3 = st.columns(3)
    with img_col1:
        st.image(img1, caption="Kucing 1", use_container_width=True)
    with img_col2:
        st.image(img2, caption="Kucing 2", use_container_width=True)
    with img_col3:
        st.image(img3, caption="Kucing 3", use_container_width=True)

# ---------- JOKE VIDEO ----------
with st.container():
    st.write("---")
    st.header("🎥 Monyet Joget (Lawak)")
    if st.button("TENGOK MONYET AFRIKA 😎"):
        st.markdown("""
        <video width="100%" autoplay controls loop>
            <source src="https://i.imgflip.com/49iy5a.mp4" type="video/mp4">
        </video>
        """, unsafe_allow_html=True)

# ---------- CONTACT FORM ----------
with st.container():
    st.write("---")
    st.header("📬 Contact Me")

    with st.form("contact_form"):
        name = st.text_input("Nama")
        email = st.text_input("Email")
        message = st.text_area("Mesej")
        submitted = st.form_submit_button("Hantar")

    if submitted:
        if name and email and message:
            try:
                sender_email = os.getenv("EMAIL_USER")
                receiver_email = os.getenv("EMAIL_TO")
                password = os.getenv("EMAIL_PASS")

                subject = "New Message from Streamlit Contact Form"
                body = f"Name: {name}\nEmail: {email}\nMessage: {message}"

                msg = MIMEMultipart()
                msg['From'] = sender_email
                msg['To'] = receiver_email
                msg['Subject'] = subject
                msg.attach(MIMEText(body, 'plain'))

                with smtplib.SMTP("smtp.gmail.com", 587) as server:
                    server.starttls()
                    server.login(sender_email, password)
                    server.sendmail(sender_email, receiver_email, msg.as_string())

                st.success("✅ Mesej berjaya dihantar!")
            except Exception as e:
                st.error(f"❌ Gagal hantar emel: {e}")
        else:
            st.error("❗ Sila isi semua bahagian dahulu.")
