AI PDF Text Summarizer (Transformer Based)
Project Overview

This project is a Transformer-based AI application that summarizes long text and PDF documents using advanced NLP models like:

T5 (t5-small)
BART (facebook/bart-large-cnn)

The application is built using:

Python
Streamlit
Hugging Face Transformers
PyPDF2

It supports:

✅ PDF Upload ✅ Long Text Summarization ✅ Chunking for Large Documents ✅ Multiple Transformer Models ✅ Interactive Web UI

 How the Project Works
PDF/Text Input
      ↓
Text Extraction
      ↓
Chunking
      ↓
Transformer Model (T5/BART)
      ↓
Generated Summaries
      ↓
Final Combined Summary
📂 Project Structure
transformer-summarizer/
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
⚙️ Installation
1. Clone Repository
git clone https://github.com/YOUR_USERNAME/transformer-summarizer.git
cd transformer-summarizer
2. Create Virtual Environment
Windows
py -3.11 -m venv venv
venv\Scripts\activate
3. Install Dependencies
pip install -r requirements.txt
▶️ Run Application
streamlit run app.py
📦 requirements.txt
streamlit
transformers==4.41.2
torch
PyPDF2
sentencepiece
Features
 PDF Summarization

Upload PDF files and generate concise summaries.

Chunking System

Large documents are split into smaller chunks before summarization.

Transformer Models

Choose between:

T5 (Fast)
BART (Better Quality)
  Adjustable Summary Length

Control output size using sliders.

Technologies Used
Technology	Purpose
Streamlit	Web UI
Hugging Face	NLP Models
Transformers	Transformer Pipeline
PyTorch	Deep Learning Backend
PyPDF2	PDF Text Extraction
Interview Explanation

“I developed an end-to-end NLP application using Transformer models for document summarization. The system supports PDF uploads, chunking for large documents, and multiple summarization models including T5 and BART.”

GitHub Upload Steps
1. Initialize Git
git init
2. Add Files
git add .
3. Commit Project
git commit -m "Initial commit - AI PDF Summarizer"
4. Create GitHub Repository

Go to:

https://github.com/

Create a new repository:

transformer-summarizer
5. Connect Local Repo to GitHub
git remote add origin https://github.com/YOUR_USERNAME/transformer-summarizer.git
6. Push Code
git branch -M main
git push -u origin main
Streamlit Deployment
1. Push project to GitHub
2. Open Streamlit Cloud

https://streamlit.io/cloud

3. Connect GitHub repository
4. Select:
Repository
Branch: main
File: app.py
5. Click Deploy 🚀
  Future Improvements
Recursive summarization
OCR for scanned PDFs
Translation support
AI-powered keyword extraction
Summary download as PDF
User authentication
   Resume Project Description
AI PDF Text Summarizer Using Transformers

Developed a Transformer-based NLP web application capable of summarizing long text and PDF documents using T5 and BART models. Implemented chunking techniques for processing large documents efficiently and deployed the application using Streamlit.

  Author

Himanshu Singh

