# 📄 Resume Genius AI

🚀 An intelligent Streamlit app that analyzes, optimizes, and enhances resumes using Generative AI and job descriptions. It provides ATS match scoring, skill gap analysis, AI suggestions, cover letter generation, and a personalized career chatbot.

![Resume Genius AI Banner](bg.jpg)

---

## 🔍 Features

- 📄 **Resume Upload** – Supports PDF and DOCX formats  
- 🧠 **AI Resume Optimization** – Customizes content based on job descriptions and persona  
- 📈 **ATS Score Calculation** – Compares resume against multiple job descriptions  
- 📊 **Job Readiness Score** – Visual scoring gauge  
- 🧰 **Skill Gap Recommendations** – Identifies missing skills from JD  
- 🧾 **Cover Letter Generation** – Auto-generates tailored cover letters  
- 🧠 **Career Chatbot (CareerGPT)** – Ask resume/career-related queries  
- 🌥️ **Dark Mode** – Toggle theme for better readability  
- 🎨 **Visual Word Cloud** – Displays missing keywords visually  
- 📋 **Resume Section Audit** – Evaluates sections for completeness and readability  

---

## 🛠️ Tech Stack

- **Frontend:** [Streamlit](https://streamlit.io/)  
- **Backend / LLMs:** [Cohere](https://cohere.com/) *(can be swapped with OpenAI, Claude, or HuggingFace)*  
- **Visuals:** Plotly, WordCloud  
- **NLP Tools:** PDFPlumber, docx2txt, TextStat, Scikit-learn  
- **Language:** Python  

---

## ⚙️ Setup Instructions

### 🔧 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/resume-genius-ai.git
cd resume-genius-ai
```

### 📦 2. Create Virtual Environment (Optional)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 📋 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 🔑 4. Set API Key

Create a `.streamlit/secrets.toml` file and add your Cohere (or LLM provider) API key:

```toml
[general]
COHERE_API_KEY = "your-api-key"
```

> 🛑 **Never commit `.env` or secrets to GitHub!**

---

## 🚀 Running the App Locally

```bash
streamlit run app.py
```

---

## 🌐 Deployment on Streamlit Cloud

1. Push code to GitHub  
2. Go to [Streamlit Cloud](https://share.streamlit.io)  
3. Connect your repo and deploy  
4. Add your `COHERE_API_KEY` under **Secrets** in App Settings  

---

## 🧠 How It Works

1. Upload your resume (PDF/DOCX)  
2. Paste up to 3 job descriptions (separated by `###`)  
3. Select your persona and experience level  
4. Hit **Run Optimization**  
5. View ATS match score, optimized resume, missing skills, and receive AI suggestions  

---

## 📌 Sample Use Case

> Upload your resume + 3 job postings you're applying for. Let the app tell you how to tailor your resume perfectly for each one, boost your job-readiness score, and even write a personalized cover letter.

---

## 🧑‍💻 Author

Made with ❤️ by **Hari Krishna Kamana**


## 🛡️ License

This project is licensed under the MIT License.
