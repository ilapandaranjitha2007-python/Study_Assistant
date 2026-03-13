# 📚 **AI Study Assistant (Sarvam AI Powered)**

A simple **AI Study Assistant API** built using **Flask** and **Sarvam AI APIs** that helps students with **language translation, speech-to-text, and text-to-speech features**.

This project acts as a **backend service for educational applications** where students can **translate text, convert speech into text, and generate audio from text**.

---

## 🚀 **Features**

🔄 **Text Translation** – Translate text between languages  
🔊 **Text to Speech** – Convert text into spoken audio  
🎤 **Speech to Text** – Convert audio into written text  
🌐 **REST API Support** – Easy integration with web or mobile apps  
⚡ **Fast Flask Backend** – Lightweight and simple API server  
🔐 **Secure API Key Handling** – Uses **.env** file for API key protection  

---

## 🛠 **Tech Stack**

- **Python**
- **Flask**
- **Sarvam AI API**
- **Requests Library**
- **python-dotenv**
- **REST API**

---

## ▶ **How to Run**

### 1️⃣ **Create Virtual Environment**

```bash
python -m venv venv
```

Activate it (Windows)

```bash
venv\Scripts\activate
```

---

### 2️⃣ **Install Dependencies**

```bash
pip install flask requests python-dotenv
```

OR

```bash
pip install -r requirements.txt
```

---

### 3️⃣ **Create `.env` File**

Add your **Sarvam AI API key**

```
SARVAM_API_KEY=your_api_key_here
```

---

### 4️⃣ **Run the Application**

```bash
python app.py
```

---

### 5️⃣ **Server Runs At**

```
http://127.0.0.1:5001/
```

---

## 🔗 **API Endpoints**

### 🏠 **Home**

```
GET /
```

Check if the API server is running.

---

### 🌐 **Translate Text**

```
POST /translate
```

Example JSON request

```json
{
"text": "Hello",
"source_language": "en-IN",
"target_language": "te-IN"
}
```

---

### 🔊 **Text to Speech**

```
POST /tts
```

Example JSON request

```json
{
"text": "Hello Students",
"language": "te-IN"
}
```

---

### 🎤 **Speech to Text**

```
POST /stt
```

Upload an **audio file** to convert speech into text.

---

## 📁 **Project Structure**

```
AI-Study-Assistant/
│
├── app.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

---

## 🌍 **Push Project to GitHub**

### 1️⃣ Initialize Git

```bash
git init
```

### 2️⃣ Add Files

```bash
git add .
```

### 3️⃣ Commit

```bash
git commit -m "Initial commit"
```

### 4️⃣ Create Repository on GitHub

Go to  
https://github.com  

Click **New Repository** and copy the repository URL.

---

### 5️⃣ Connect Local Project to GitHub

```bash
git remote add origin https://github.com/yourusername/AI-Study-Assistant.git
```

---

### 6️⃣ Push to GitHub

```bash
git branch -M main
git push -u origin main
```

---

## 👩‍💻 **Author**

**Ranjitha Ilapanda**

---

## ⭐ **Future Improvements**

📱 **Add Frontend (HTML, CSS, JS)**  
📚 **Add AI Doubt Solver Chatbot**  
🧠 **Add AI Notes Generator**  
📊 **Add Study Analytics Dashboard**  
☁ **Deploy to Render / Railway / AWS**
