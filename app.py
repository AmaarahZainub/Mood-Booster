import streamlit as st
from groq import Groq

# Initialize Groq client (make sure you set your GROQ_API_KEY in Streamlit Cloud secrets)
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

st.title("🌸 Mood Booster AI Companion")

# Sidebar for personalization
username = st.sidebar.text_input("Enter your name (optional)", "")
mood = st.sidebar.selectbox("How are you feeling?", ["Happy", "Sad", "Stressed", "Tired", "Motivated"])

# Main input
user_input = st.text_area("Tell me about your mood or thoughts:")

if st.button("Boost My Mood"):
    # Build prompt dynamically
    name_or_friend = username if username.strip() else "friend"
    prompt = f"The user ({name_or_friend}) feels {mood}. Respond with a short, kind, and motivating message."

    response = client.chat.completions.create(
        model="llama3-8b-8192",  # Groq model
        messages=[{"role": "user", "content": prompt}]
    )

    st.success(response.choices[0].message.content)

# Daily boost button
if st.button("Daily Boost"):
    prompt = "Give me one sweet, uplifting motivational message."
    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[{"role": "user", "content": prompt}]
    )
    st.info(response.choices[0].message.content)
