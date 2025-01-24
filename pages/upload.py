import streamlit as st

st.title("📂 Upload a Text File")

uploaded_file = st.file_uploader("Choose a text file", type=['txt'])

if uploaded_file is not None:
    content = uploaded_file.read().decode("utf-8")
    st.text_area("File Content:", content, height=250)

    if st.button("Process Text"):
        st.success("Text file processed successfully!")
        st.write("Preview of the file content:")
        st.write(content)
