import streamlit as st
import pyttsx3

st.set_page_config(page_title="Text-to-Speech", layout="centered")

# Custom CSS
st.markdown("""
    <style>
        .stTextArea, .stSlider, .stButton, .stSelectbox {
            background-color: #ffffff;
            padding: 10px;
            border-radius: 8px;
        }
        .stButton button {
            background-color: #ff7f50;
            color: white;
            font-size: 16px;
            border-radius: 5px;
        }
    </style>
""", unsafe_allow_html=True)

st.title("🗣️ Text-to-Speech Converter")

# Text input area
text = st.text_area("Enter text:", height=200, placeholder="Type something here...")

if text:
    voice_rate = st.slider("Select Speech Rate:", 50, 200, 150)
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    selected_voice = st.selectbox("Choose Voice:", [voice.name for voice in voices])

    if st.button("Convert to Speech 🎧"):
        engine.setProperty('voice', voices[[v.name for v in voices].index(selected_voice)].id)
        engine.setProperty('rate', voice_rate)
        engine.say(text)
        engine.runAndWait()
        st.success("Speech generated successfully!")
