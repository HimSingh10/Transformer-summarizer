import streamlit as st
from transformers import pipeline
import PyPDF2

# Page config
st.set_page_config(page_title="AI PDF Summarizer", page_icon="📄")

st.title("AI PDF Text Summarizer")
st.write("Summarize PDFs using Transformer models (T5 / BART)")

# -----------------------------
# MODEL SELECTION
# -----------------------------
model_choice = st.selectbox(
    "Choose Model",
    ["T5 (Fast)", "BART (Better Quality)"]
)

@st.cache_resource
def load_model(choice):
    if choice == "T5 (Fast)":
        return pipeline("summarization", model="t5-small")
    else:
        return pipeline("summarization", model="facebook/bart-large-cnn")

summarizer = load_model(model_choice)

# -----------------------------
# PDF TEXT EXTRACTION
# -----------------------------
def extract_text_from_pdf(pdf_file):
    reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text

# -----------------------------
# CHUNKING FUNCTION
# -----------------------------
def chunk_text(text, chunk_size=400):
    words = text.split()
    chunks = []

    for i in range(0, len(words), chunk_size):
        chunk = " ".join(words[i:i + chunk_size])
        chunks.append(chunk)

    return chunks

# -----------------------------
# SUMMARIZE LONG TEXT
# -----------------------------
def summarize_long_text(text, summarizer, max_len, min_len):
    chunks = chunk_text(text)
    summaries = []

    for i, chunk in enumerate(chunks):
        st.write(f"Processing chunk {i+1}/{len(chunks)}...")

        summary = summarizer(
            chunk,
            max_length=max_len,
            min_length=min_len,
            do_sample=False
        )

        summaries.append(summary[0]['summary_text'])

    final_summary = " ".join(summaries)
    return final_summary

# -----------------------------
# INPUT
# -----------------------------
uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])
text_input = st.text_area("Or paste text")

max_len = st.slider("Max Summary Length", 20, 150, 80)
min_len = st.slider("Min Summary Length", 10, 60, 25)

# -----------------------------
# BUTTON
# -----------------------------
if st.button("Summarize"):
    text = ""

    if uploaded_file is not None:
        text = extract_text_from_pdf(uploaded_file)
    elif text_input.strip() != "":
        text = text_input

    if text.strip() != "":
        with st.spinner("Generating summary... ⏳"):

            st.subheader("Preview:")
            st.write(text[:500] + "...")

            final_summary = summarize_long_text(
                text,
                summarizer,
                max_len,
                min_len
            )

        st.subheader("Final Summary:")
        st.write(final_summary)

    else:
        st.warning("Please upload PDF or enter text!")