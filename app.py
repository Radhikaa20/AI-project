# app.py
import streamlit as st
import os
from backend.parser import extract_text_from_pdf, extract_text_from_txt
from backend.summarizer import summarize_text

# Set UI title
st.title("Smart Assistant for Research Summarization")

# Upload section
uploaded_file = st.file_uploader("Upload a PDF or TXT file", type=["pdf", "txt"])

if uploaded_file:
    # Save file to /data/
    os.makedirs("data", exist_ok=True)
    file_path = os.path.join("data", uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Extract text
    if uploaded_file.name.endswith(".pdf"):
        text = extract_text_from_pdf(file_path)
    else:
        text = extract_text_from_txt(file_path)

    # Show success and summary
    st.success("✅ File uploaded and text extracted successfully!")
    with st.spinner("Summarizing..."):
        summary = summarize_text(text)

    st.subheader(" Document Summary (≤ 150 words):")
    st.write(summary)