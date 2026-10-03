import streamlit as st
import os
from PIL import Image
import numpy as np

# ==========================================
# AI FACE VERIFICATION FUNCTION
# ==========================================

def verify_face(uploaded_image, saved_image_path):

    try:

        # CHECK FILE EXISTS
        if not os.path.exists(saved_image_path):

            st.error("❌ Saved user image not found")
            return False

        # OPEN IMAGES
        img1 = Image.open(uploaded_image)
        img2 = Image.open(saved_image_path)

        # RESIZE BOTH
        img1 = img1.resize((200, 200))
        img2 = img2.resize((200, 200))

        # CONVERT TO ARRAY
        arr1 = np.array(img1)
        arr2 = np.array(img2)

        # SIMPLE COMPARISON
        difference = np.mean(np.abs(arr1 - arr2))

        # THRESHOLD CHECK
        if difference < 50:

            st.success("✅ Face Verification Successful")

            return True

        else:

            st.error("❌ Face Verification Failed")

            return False

    except Exception as e:

        st.error(f"Error: {e}")

        return False


# ==========================================
# DEMO FACE CHECK PAGE
# ==========================================

def face_verification_page():

    st.subheader("🤖 AI Face Verification")

    phone = st.text_input("📱 Enter Phone Number")

    uploaded_image = st.file_uploader(
        "📸 Upload Your Face Image",
        type=["jpg", "png", "jpeg"]
    )

    if st.button("Verify Face"):

        if uploaded_image:

            saved_path = f"users/{phone}.jpg"

            result = verify_face(
                uploaded_image,
                saved_path
            )

            if result:

                st.balloons()

        else:

            st.warning("⚠️ Please upload an image")