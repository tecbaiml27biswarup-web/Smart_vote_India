import streamlit as st
from auth import register_user, login_user
from voting import voting_page
from PIL import Image
import os

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="SmartVote India",
    page_icon="🗳️",
    layout="wide"
)

# ==========================================
# LOAD IMAGES SAFELY
# ==========================================

logo = None
flag = None
banner = None
ink = None

if os.path.exists("assets/logo.png"):
    logo = Image.open("assets/logo.png")

if os.path.exists("assets/india_flag.png"):
    flag = Image.open("assets/india_flag.png")

if os.path.exists("assets/voting_banner.jpg"):
    banner = Image.open("assets/voting_banner.jpg")

if os.path.exists("assets/ink_mark.png"):
    ink = Image.open("assets/ink_mark.png")

# ==========================================
# CUSTOM CSS
# ==========================================

st.markdown("""

<style>

/* MAIN APP BACKGROUND */
.stApp {

background:
linear-gradient(
135deg,
#ff9933,
#ffffff,
#138808
);

background-attachment: fixed;
}

/* MAIN CONTAINER */
.block-container {

background: rgba(255,255,255,0.25);

padding: 2rem;

border-radius: 25px;

backdrop-filter: blur(10px);
}

/* SIDEBAR */
section[data-testid="stSidebar"] {

background:
linear-gradient(
180deg,
#0c1b33,
#1f4068,
#3b6978
);
}

/* SIDEBAR TEXT */
section[data-testid="stSidebar"] * {

color: white !important;
}

/* BUTTON */
.stButton > button {

width: 100%;

height: 55px;

border-radius: 15px;

border: none;

background:
linear-gradient(
90deg,
#ff9933,
#138808
);

color: white;

font-size: 18px;

font-weight: bold;
}

/* INPUT BOX */
.stTextInput > div > div > input {

border-radius: 15px;

padding: 12px;

background: rgba(255,255,255,0.8);
}

/* NUMBER INPUT */
.stNumberInput input {

border-radius: 15px !important;

background: rgba(255,255,255,0.8);
}

/* TITLES */
h1, h2, h3 {

color: #0c1b33;
text-align: center;
}

/* IMAGE */
img {

border-radius: 20px;
}

</style>

""", unsafe_allow_html=True)

# ==========================================
# HEADER
# ==========================================

col1, col2 = st.columns([1,4])

with col1:

    if logo:
        st.image(logo, width=130)

with col2:

    st.markdown("""

    <h1>🗳️ SmartVote India</h1>

    <h3>
    Secure • Transparent • Digital Voting System
    </h3>

    """, unsafe_allow_html=True)

# ==========================================
# FLAG
# ==========================================

if flag:
    st.image(flag, use_container_width=True)

# ==========================================
# BANNER
# ==========================================

if banner:
    st.image(banner, use_container_width=True)

# ==========================================
# SIDEBAR
# ==========================================

if logo:
    st.sidebar.image(logo, width=120)

menu = [

    "🏠 Home",
    "🔐 Login",
    "📝 Register",
    "🗳️ Vote",
    "📊 Admin Panel"
]

choice = st.sidebar.radio(
    "Navigation Menu",
    menu
)

# ==========================================
# HOME PAGE
# ==========================================

if choice == "🏠 Home":

    st.markdown("""

    ## 🇮🇳 Welcome to SmartVote India

    ### Features

    ✅ One Person One Vote  
    ✅ Aadhaar Based Registration  
    ✅ Secure Login System  
    ✅ Digital Election Platform  
    ✅ Senior Citizen Friendly  
    ✅ AI Face Verification  

    ### Important Rule

    🔞 Only users above 18 years can register and vote.

    """, unsafe_allow_html=True)

    st.success("Empowering Democracy Through Technology")

# ==========================================
# LOGIN PAGE
# ==========================================

elif choice == "🔐 Login":

    st.subheader("🔐 Login to Your Account")

    voter_id = st.text_input("🆔 Enter Voter ID")

    password = st.text_input(
        "🔒 Password",
        type="password"
    )

    if st.button("Login"):

        login_user(voter_id, password)

# ==========================================
# REGISTER PAGE
# ==========================================

elif choice == "📝 Register":

    st.subheader("📝 Create Your Account")

    col1, col2 = st.columns(2)

    with col1:

        name = st.text_input("👤 Full Name")

        age = st.number_input(
            "🎂 Enter Your Age",
            min_value=1,
            max_value=120,
            step=1
        )

        voter_id = st.text_input(
            "🆔 Enter Voter ID"
        )

    with col2:

        phone = st.text_input("📱 Phone Number")

        aadhaar = st.text_input("🆔 Aadhaar Number")

        password = st.text_input(
            "🔒 Create Password",
            type="password"
        )

    uploaded_image = st.file_uploader(
        "📸 Upload Face Image",
        type=["jpg", "png", "jpeg"]
    )

    if st.button("Register"):

        register_user(
            name,
            age,
            voter_id,
            phone,
            aadhaar,
            password
        )

        # SAVE USER IMAGE
        if uploaded_image:

            with open(f"users/{voter_id}.jpg", "wb") as f:

                f.write(uploaded_image.getbuffer())

            st.success(
                "✅ Face Image Uploaded Successfully"
            )

    st.subheader("📝 Create Your Account")

    col1, col2 = st.columns(2)

    with col1:

        name = st.text_input("👤 Full Name")

        age = st.number_input(
            "🎂 Enter Your Age",
            min_value=1,
            max_value=120,
            step=1
        )

        phone = st.text_input("📱 Phone Number")

    with col2:

        aadhaar = st.text_input("🆔 Aadhaar Number")

        password = st.text_input(
            "🔒 Create Password",
            type="password"
        )

    uploaded_image = st.file_uploader(
        "📸 Upload Face Image",
        type=["jpg", "png", "jpeg"]
    )

    if st.button("Register"):

        register_user(
            name,
            age,
            phone,
            aadhaar,
            password
        )

        # SAVE USER IMAGE
        if uploaded_image:

            with open(f"users/{phone}.jpg", "wb") as f:

                f.write(uploaded_image.getbuffer())

            st.success("✅ Face Image Uploaded Successfully")

# ==========================================
# VOTING PAGE
# ==========================================

elif choice == "🗳️ Vote":

    st.subheader("🗳️ Cast Your Vote")

    if ink:
        st.image(ink, width=120)

    if "user" not in st.session_state:

        st.warning("⚠️ Please Login First")

    else:

        voting_page()

# ==========================================
# ADMIN PANEL
# ==========================================

elif choice == "📊 Admin Panel":

    st.title("📊 Election Admin Panel")

    admin_password = st.text_input(
        "Enter Admin Password",
        type="password"
    )

    if st.button("Login Admin"):

        if admin_password == "admin123":

            st.success("✅ Admin Login Successful")

            from database import cursor

            cursor.execute("""

            SELECT candidate, COUNT(*)
            FROM votes
            GROUP BY candidate

            """)

            results = cursor.fetchall()

            st.subheader("🗳️ Election Statistics")

            if results:

                total_votes = 0

                for candidate, count in results:

                    total_votes += count

                st.success(
                    f"🗳️ Total Votes Casted : {total_votes}"
                )

            else:

                st.warning("No votes found")

        else:

            st.error("❌ Wrong Admin Password")

# ==========================================
# FOOTER
# ==========================================

st.markdown("""

<hr>

<div style='text-align:center;'>

<h3>🇮🇳 SmartVote India</h3>

<p>
One Nation • One Vote • One Digital Future
</p>

<p style='color:gray;'>
Made by Biswarup using Streamlit
</p>

</div>

""", unsafe_allow_html=True)