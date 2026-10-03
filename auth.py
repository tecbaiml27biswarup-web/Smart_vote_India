import streamlit as st
from database import conn, cursor

# ==========================================
# REGISTER USER
# ==========================================

def register_user(
    name,
    age,
    voter_id,
    phone,
    aadhaar,
    password
):

    try:

        # AGE CHECK
        if age < 18:

            st.error(
                "❌ Only users above 18 years can register and vote"
            )

            return

        # CHECK EXISTING USER
        cursor.execute("""

        SELECT * FROM users

        WHERE phone=?
        OR aadhaar=?
        OR voter_id=?

        """, (phone, aadhaar, voter_id))

        existing = cursor.fetchone()

        if existing:

            st.error("❌ User already registered")

        else:

            # INSERT USER
            cursor.execute("""

            INSERT INTO users
            (name, age, voter_id, phone, aadhaar, password)

            VALUES (?, ?, ?, ?, ?, ?)

            """, (
                name,
                age,
                voter_id,
                phone,
                aadhaar,
                password
            ))

            conn.commit()

            st.success("✅ Registration Successful")

    except Exception as e:

        st.error("❌ Registration Error")


# ==========================================
# LOGIN USER
# ==========================================

def login_user(voter_id, password):

    cursor.execute("""

    SELECT * FROM users
    WHERE voter_id=? AND password=?

    """, (voter_id, password))

    user = cursor.fetchone()

    if user:

        st.session_state["user"] = voter_id

        st.success("✅ Login Successful")

    else:

        st.error("❌ Invalid Voter ID or Password")