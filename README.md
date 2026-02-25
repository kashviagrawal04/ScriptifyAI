# 🧠 Scriptify AI

A full-stack handwriting recognition web application built using FastAPI and a Transformer-based OCR model (TrOCR).

---

## 🚀 Features

- Upload handwritten text images  
- Transformer-based text recognition  
- REST API backend (FastAPI)  
- Responsive frontend interface  
- End-to-end ML inference pipeline  

---

## 🛠️ Tech Stack

### Backend
- FastAPI  
- PyTorch  
- HuggingFace Transformers  
- TrOCR (`trocr-large-handwritten`)  

### Frontend
- HTML  
- CSS  
- JavaScript  

---

## 📂 Project Structure

```
ScriptifyAI/
│
├── app/
│   ├── api.py          # FastAPI endpoints
│   ├── model.py        # Model loading
│   ├── utils.py        # Image preprocessing & prediction
│
├── index.html
├── requirements.txt
└── README.md
```

---

## ⚙️ Run Locally

```bash
git clone https://github.com/kashviagrawal04/ScriptifyAI.git
cd ScriptifyAI

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt
uvicorn app.api:app --reload
```

Open in browser:  
http://127.0.0.1:8000/docs

---

## 🎯 Overview

The application uses a Vision Transformer encoder and Transformer decoder architecture to convert handwritten text images into digital text through an end-to-end inference pipeline.

---

## 👩‍💻 Author

Kashvi Agrawal  
GitHub: https://github.com/kashviagrawal04
