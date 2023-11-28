import streamlit as st

def display_bot_information():

    logo_image = "scarlett-fleet-logo.png"
    st.image(logo_image)

    st.markdown("<h1 style='text-align: center;'>Scarlett - Bot Fleet</h1>", unsafe_allow_html=True)

    st.header("Bot Fleet Overview")
    st.write("Scarlett - Bot Fleet is a dynamic collection of Discord bots developed using Python and the Discord API.")
    
    st.header("Features")
    st.write("- Efficient image retrieval and delivery")
    st.write("- ~100% uptime for reliable performance")
    st.write("- Active in diverse servers with an engaged user base")
    st.write("- Regular updates, content enhancements and new bot releases")

    st.header("Availability")
    st.write("For personalized demonstrations, server invites, or further inquiries, Scarlett is available upon request.")

    st.markdown(
        "<p style='text-align: center; color: #888; bottom: 0; left: 0; width: 100%; padding: 10px; '>rushilshekhar1@gmail.com | linkedin.com/in/rushil-s13/ <br> © 2023 Scarlett - Bot Fleet. All rights reserved.</p>",
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    display_bot_information()
