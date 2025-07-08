from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie
from pathlib import Path

st.set_page_config(page_title="ABOUT ME", page_icon=":tada:", layout= "wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
#use local css
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

#load assets
lottie_coding = load_lottieurl("...json")
if lottie_coding:
    st_lottie(lottie_coding, height=300, key="coding")
else:
    st.error("Lottie animation failed to load.")
lottie_coding = load_lottieurl("https://lottie.host/7aa80ad3-97bb-4b64-aa94-5800263195c5/aoW6sdJFhW.json")
lottie_hai = load_lottieurl("https://lottie.host/afb5e48c-63ad-4589-a51a-069a8faa7cc0/2UOBuEjjFP.json")
image_contact_form = Image.open(Path("images/kucing1.jpg"))
image_lottie_animation = Image.open("images/kucing2.jpg")
image_contact_form1 = Image.open("images/kucing3.jpg")

#header section
with st.container():
    left_column, right_column = st.columns(2)
    with left_column:
        st.subheader("HI, I am Muhammad Ridzuan :smile:")
        st.title("INTRODUCTION")
        import streamlit as st

        # Justify text using HTML and CSS
        st.markdown("""
        <style>
        .justified-text {
            text-align: justify;
        }
        </style>

        <div class="justified-text">
        Hello! My name is Muhammad Ridzuan Bin Darwin, and I am a 20-year-old student currently pursuing my studies at SMART College in Kuala Lumpur. I am eager to apply for an internship opportunity as I am deeply enthusiastic about learning and gaining hands-on experience in a professional environment. I believe that an internship will not only allow me to apply the knowledge I’ve gained in my studies but also help me develop new skills, grow as an individual, and contribute meaningfully to an organization. I am highly motivated, adaptable, and ready to take on new challenges to build a strong foundation for my future career. I look forward to the opportunity to learn, grow, and make a positive impact!        </div>
        """, unsafe_allow_html=True)
        st.write("[My Linktree >](https://linktr.ee/zunohuzz)")
    with right_column:
        st_lottie(lottie_hai,height=250, key="hai")

#what I do
with st.container():
    st.write("---")
    Left_column, right_column = st.columns(2)
    with Left_column:
        st.header("What I learn at SMART college")
        st.markdown("""
        <style>
        .justified-text {
            text-align: justify;
        }
        </style>

        <div class="justified-text">
        During my time at college, I have developed a strong foundation in various areas, including investigative techniques, corporate law, and understanding criminal behavior. Additionally, I have honed essential soft skills such as time management and effective collaboration in group settings. These experiences have equipped me with a well-rounded skill set, enabling me to approach challenges with analytical thinking, legal awareness, and teamwork. I am eager to apply these skills in a professional environment and continue growing through hands-on experience.               """, unsafe_allow_html=True)
        st.write("[My resume >](https://drive.google.com/file/d/1ee1u7Z7JFByLf4gfSn2biWBL7FmdSsaU/view?usp=drive_link)")
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")
#DAD JOKE
st.title("Click button tu kalau nak tengok monyet joget 🎥")

if st.button("MONYET AFRIKA UTARA 😎"):
       st.markdown(
        """
        <video width="100%" autoplay controls loop>
            <source src="https://i.imgflip.com/49iy5a.mp4" type="video/mp4">
            Your browser does not support the video tag.
        </video>
        """,
        unsafe_allow_html=True
    )

#projects
with st.container():
    st.write("___")
    st.header("My Projects")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(image_lottie_animation)
    with text_column:
        st.subheader("how I wake up")
        st.write("""I open my eyes""")

with st.container():
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(image_contact_form)
    with text_column:
        st.subheader("how to save enegi")
        st.write("""I save my enegi by sleep""")

#contact
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Title of the app
st.title("Contact Form, not working animor hiks") 

# Create a form
with st.form("contact_form"):
    st.write("Please fill out the form below:")

    # Input fields
    name = st.text_input("Name")
    email = st.text_input("Email")
    message = st.text_area("Message")

    # Submit button
    submitted = st.form_submit_button("Submit")

    # If the form is submitted
    if submitted:
        # Validate inputs
        if name and email and message:
            try:
                # Email configuration
                sender_email = "zuanxzy@gmail.com"  # Replace with your email
                receiver_email = "zuanxzy@gmail.com"  # Replace with your email
                password = "evjl hpch xydw qzfu"  # Replace with your app password (see notes below)

                # Create the email
                subject = "New Contact Form Submission"
                body = f"""
                Name: {name}
                Email: {email}
                Message: {message}
                """

                msg = MIMEMultipart()
                msg['From'] = sender_email
                msg['To'] = receiver_email
                msg['Subject'] = subject
                msg.attach(MIMEText(body, 'plain'))

                # Send the email
                with smtplib.SMTP('smtp.gmail.com', 587) as server:
                    server.starttls()  # Secure the connection
                    server.login(sender_email, password)
                    server.sendmail(sender_email, receiver_email, msg.as_string())

                st.success("Thank you for your submission! We will get back to you soon.")
            except Exception as e:
                st.error(f"An error occurred while sending the email: {e}")
        else:
            st.error("Please fill out all fields.")


#--------------roulette
with st.container():
    st.write("___")
    st.header("ROULETTE")

import random
import matplotlib.pyplot as plt

st.title("🎰 take me to internship yes/no") #

# Define Yes/No sections
options = ["Yes", "No"]
colors = ["green", "red"]
probabilities = [0.7, 0.3]  # 70% Yes, 30% No

def draw_roulette(selected_option=None):
    fig, ax = plt.subplots(figsize=(5, 5))
    wedges, texts, autotexts = ax.pie(probabilities, labels=options, colors=colors, startangle=90, counterclock=False, autopct='%1.0f%%')
    # (rest as before)

    # Highlight the selected option
   selected = random.choices(options, weights=probabilities)[0]
draw_roulette(selected)
st.write(f"Result: {selected}")



