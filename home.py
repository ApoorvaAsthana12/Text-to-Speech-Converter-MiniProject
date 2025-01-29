import streamlit as st

# Custom CSS for background, fonts, and styling
st.markdown("""
    <style>
        body {
            background-color: #f4f4f4;
        }
        .main {
            background-color: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
        }
        h1, h2 {
            color: #333;
            text-align: center;
        }
        .feature-box {
            background-color: #eef;
            padding: 10px;
            border-radius: 8px;
            margin: 10px 0;
        }
    </style>
""", unsafe_allow_html=True)

st.title("🎤 Text-to-Speech & PDF-to-Audio Converter")

st.markdown("### 🔹 Convert text or PDF documents into high-quality speech easily.")

st.sidebar.header("📌 Navigation")

st.markdown("---")

# 📝 Overview
st.markdown("## 📖 Overview")
st.write("""
This project helps you convert text or PDF files into **natural-sounding speech**.  
It’s useful for **students, professionals, and visually impaired users** to listen to documents instead of reading.
""")

# 🚀 How It Works
st.markdown("## 🚀 How It Works")
col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🗣️ Text-to-Speech")
    st.write("""
    1️⃣ Enter your **text** in the provided box.  
    2️⃣ Select your **preferred voice & speed**.  
    3️⃣ Click the **Convert to Speech** button.  
    4️⃣ Listen or **download** the generated audio file. 🎧
    """)

with col2:
    st.markdown("### 📂 PDF-to-Speech")
    st.write("""
    1️⃣ Upload a **PDF file**.  
    2️⃣ The system extracts text automatically.  
    3️⃣ Choose voice & speed.  
    4️⃣ Generate and **download** the MP3 file. 🎵
    """)

# ⭐ Features Section
st.markdown("## ⭐ Features")
st.markdown("""
✅ **Supports multiple voices** for customization  
✅ **Adjustable speech rate** for better understanding  
✅ **PDF text extraction** for listening convenience  
✅ **Downloadable MP3 files** for offline access  
""")

# 🎯 Use Cases Section
st.markdown("## 🎯 Who Can Use This?")
st.write("""
🔸 **Students** - Convert notes into audio for learning on the go.  
🔸 **Professionals** - Listen to reports & documents while multitasking.  
🔸 **Visually Impaired Users** - Access content via speech output.  
🔸 **Language Learners** - Improve pronunciation & listening skills.  
""")

st.markdown("---")
st.markdown("### 🎉 Start using the tool now by selecting an option from the sidebar! 🚀")
