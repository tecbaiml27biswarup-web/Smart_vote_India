import streamlit as st
from database import cursor

def admin_panel():

    st.title("📊 Admin Dashboard")

    password = st.text_input(
        "Enter Admin Password",
        type="password"
    )

    if st.button("Open Admin Panel"):

        if password == "admin123":

            st.success("✅ Admin Login Successful")

            st.subheader("🗳️ Voting Results")

            cursor.execute("""

            SELECT candidate, COUNT(*)
            FROM votes
            GROUP BY candidate

            """)

            results = cursor.fetchall()

            if results:

                for candidate, count in results:

                    st.info(
                        f"{candidate} : {count} votes"
                    )

            else:

                st.warning("No votes yet")

        else:

            st.error("❌ Wrong Admin Password")