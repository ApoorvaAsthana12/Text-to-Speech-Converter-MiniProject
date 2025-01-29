import streamlit as st
import PyPDF2
import pyttsx3
import os

st.set_page_config(page_title="Upload PDF", layout="centered")

# Custom CSS for styling
st.markdown("""
    <style>
        .stFileUploader, .stTextArea, .stSlider, .stButton, .stSelectbox {
            background-color: #ffffff;
            padding: 10px;
            border-radius: 8px;
        }
        .stButton button {
            background-color: #008cba;
            color: white;
            font-size: 16px;
            border-radius: 5px;
        }
        .main {
            background: linear-gradient(to right, #00c6ff, #0072ff);
            padding: 20px;
            border-radius: 10px;
        }
    </style>
""", unsafe_allow_html=True)

st.title("📂 Upload PDF & Convert to Speech")

# File uploader
uploaded_file = st.file_uploader("Choose a PDF file", type=['pdf'])

if uploaded_file is not None:
    st.success("✅ PDF Uploaded Successfully!")

    # Extract text
    pdf_reader = PyPDF2.PdfReader(uploaded_file)
    text = "".join([page.extract_text() for page in pdf_reader.pages])

    if text.strip():
        st.text_area("Extracted Text:", text, height=250)

        filename = st.text_input("Enter filename (without extension):", "pdf_audio")
        voice_rate = st.slider("Select Speech Rate:", 50, 200, 150)
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        selected_voice = st.selectbox("Choose Voice:", [voice.name for voice in voices])

        if st.button("Convert to Speech 🎵"):
            audio_file = f"assets/{filename}.mp3"
            engine.setProperty('voice', voices[[v.name for v in voices].index(selected_voice)].id)
            engine.setProperty('rate', voice_rate)
            engine.save_to_file(text, audio_file)
            engine.runAndWait()

            st.success("🎉 Audio file generated successfully!")
            st.audio(audio_file, format="audio/mp3")
            st.download_button("Download MP3", audio_file, file_name=f"{filename}.mp3")
    else:
        st.warning("⚠️ No text found in the PDF file!")
