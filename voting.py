import streamlit as st
from database import conn, cursor
from datetime import datetime
import os

def voting_page():

    parties = [
        "BJP",
        "TMC",
        "Congress",
        "AAP",
        "CPM"
    ]

    # LOGIN CHECK
    if "user" not in st.session_state:

        st.error("❌ Please Login First")

        return

    voter_id = st.session_state["user"]

    # CHECK VOTING STATUS
    cursor.execute(
        "SELECT has_voted FROM users WHERE voter_id=?",
        (voter_id,)
    )

    voted = cursor.fetchone()[0]

    # ==========================================
    # ALREADY VOTED
    # ==========================================

    if voted == 1:

        st.warning("⚠️ You are already voted")

        # GET USER DETAILS
        cursor.execute("""

        SELECT users.name,
               users.phone,
               users.voter_id,
               votes.candidate

        FROM users

        JOIN votes
        ON users.voter_id = votes.voter_id

        WHERE users.voter_id=?

        """, (voter_id,))

        data = cursor.fetchone()

        if data:

            name, phone, voter_id, candidate = data

            vote_date = datetime.now().strftime(
                "%d-%m-%Y | %I:%M %p"
            )

            st.markdown("""

            ---
            # 🇮🇳 SmartVote India Receipt
            ### ✅ Vote Successfully Submitted

            """)

            # USER IMAGE
            image_path = f"users/{voter_id}.jpg"

            if os.path.exists(image_path):

                st.image(image_path, width=180)

            st.markdown(f"""

            **👤 Name:** {name}

            **🆔 Voter ID:** {voter_id}

            **📱 Phone:** {phone}

            **🗳️ Voted Party:** {candidate}

            **📅 Date:** {vote_date}

            ### 🔒 This receipt is private and visible only to you.

            ---

            """)

        return

    # ==========================================
    # VOTE SECTION
    # ==========================================

    candidate = st.radio(
        "Choose Your Party",
        parties
    )

    if st.button("Submit Vote"):

        # SAVE VOTE
        cursor.execute("""

        INSERT INTO votes
        (voter_id, candidate)

        VALUES (?, ?)

        """, (voter_id, candidate))

        # UPDATE STATUS
        cursor.execute("""

        UPDATE users
        SET has_voted=1
        WHERE voter_id=?

        """, (voter_id,))

        conn.commit()

        st.success("✅ Vote Submitted Successfully")

        st.balloons()

        st.rerun()