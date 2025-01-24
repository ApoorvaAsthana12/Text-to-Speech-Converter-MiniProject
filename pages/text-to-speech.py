import streamlit as st
import pyttsx3
import os

# Ensure the assets directory exists
os.makedirs("assets", exist_ok=True)

st.title("🗣️ Text-to-Speech Converter")

text = st.text_area("Enter your text:", "")
voice_rate = st.slider("Select Speech Rate:", 50, 200, 150)
filename = st.text_input("Enter filename (without extension):", "output")

engine = pyttsx3.init()
voices = engine.getProperty('voices')
selected_voice = st.selectbox("Choose Voice:", [voice.name for voice in voices])

if st.button("Convert to Speech"):
    if text.strip() == "":
        st.warning("Please enter some text.")
    else:
        engine.setProperty('voice', voices[[v.name for v in voices].index(selected_voice)].id)
        engine.setProperty('rate', voice_rate)
        audio_file = f"assets/{filename}.mp3"
        engine.save_to_file(text, audio_file)
        engine.runAndWait()
        st.success("Conversion successful! You can now play and download the audio below.")
        st.audio(audio_file, format="audio/mp3")
        st.download_button("Download Audio", audio_file, file_name=f"{filename}.mp3")
