<h1 align="center">📰 NewsPaper</h1>

<p align="center">A beautiful Flask app that fetches a <strong>random top news headline</strong> from around the world and displays it in an elegant, responsive UI built with Bootstrap 5.</p>

<p align="center">
  <a href="https://newspaper-4h43.onrender.com/" target="_blank"><strong>🌍 Live Demo</strong></a> • 
  <a href="#-features">Features</a> • 
  <a href="#-tech-stack">Tech Stack</a> • 
  <a href="#-getting-started">Getting Started</a> • 
  <a href="#-author">About Me</a>
</p>

---

## 🚀 Features

- 📰 Displays **random headlines** from NewsAPI
- 📸 Shows **image**, **title**, **description**, **author**, and **content**
- 📱 **Fully responsive UI** built with Bootstrap 5
- 🌐 Navigation to **Portfolio**, **GitHub**, and **LinkedIn**
- 💡 Lightweight, fast, and beginner-friendly Flask codebase

---

## 📸 Preview

<p float="left">
  <img src="https://github.com/user-attachments/assets/911c7ce5-1db2-43b4-9f04-a5e9a01de91f" width="30%" />
  <img src="https://github.com/user-attachments/assets/61adc2d5-1d60-4e5f-bcb6-a64956c876bf" width="30%" />
  <img src="https://github.com/user-attachments/assets/9a159f06-9721-437e-89ec-8fa0a81c21fe" width="30%" />
</p>

---

## 🛠️ Tech Stack

| Layer       | Tech Used                            |
|-------------|--------------------------------------|
| Backend     | Python 3, Flask                      |
| API         | [NewsAPI](https://newsapi.org/)      |
| Frontend    | HTML5, CSS3, Bootstrap 5             |
| Hosting     | [Render](https://render.com/)        |
| Extra       | Responsive Design, Clean UI/UX       |

---

## 📂 Project Structure

```bash
NewsPaper/
│
├── static/
│   └── style.css           # Custom styling
│
├── templates/
│   └── index.html          # Main frontend layout
│
├── app.py                  # Flask backend logic
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

---

## ⚙️ Getting Started

Get the project up and running in minutes:

### 🔁 Clone the Repo
```bash
git clone https://github.com/your-username/NewsPaper.git
cd NewsPaper
```

### 🧪 Set Up Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

### 📦 Install Requirements
```bash
pip install -r requirements.txt
```

### 🔐 Add Your NewsAPI Key
Sign up on [NewsAPI.org](https://newsapi.org/) and get your free API key.  
Replace the placeholder in `app.py`:
```python
'apiKey': 'your_api_key_here'
```

### ▶️ Run the App
```bash
python app.py
```

Open in your browser: [http://localhost:5000](http://localhost:5000)

---

## 📋 Requirements

Here’s what you’ll need to install:

```txt
Flask
requests
```

Generate it with:
```bash
pip freeze > requirements.txt
```

---

## ✨ Author

Made with 💙 by [**Shreyas Shridhar Kulkarni**](https://shreyasshridharkulkarni.netlify.app/)

- 💼 [LinkedIn](https://linkedin.com/in/shreyas-shridhar-kulkarni-946a0225a)  
- 💻 [GitHub](https://github.com/Shreyu-07)  
- 📬 [Portfolio](https://shreyasshridharkulkarni.netlify.app/)

---

## 🤝 Contributing

Pull requests are welcome! If you spot a bug or have a cool idea, feel free to fork the repo and open a PR.

```bash
git checkout -b feature/your-feature-name
git commit -m "Added some epic feature 🚀"
git push origin feature/your-feature-name
```

---

## 🙌 Support

If you like this project, drop a ⭐ on the repo and share it with your developer friends! Let’s spread code that informs ✨
