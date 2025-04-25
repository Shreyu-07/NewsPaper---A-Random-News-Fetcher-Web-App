# 📰 NewsPaper - A Random News Fetcher Web App

A simple and elegant Flask web application that fetches a **random top headline** from the [NewsAPI](https://newsapi.org/) and displays it in a beautifully designed Bootstrap interface.


# See the live web site : 
[Click ME](https://newspaper-4h43.onrender.com/)
## 🚀 Features

- Fetches **random news** from a list of top headlines.
- Displays **news title**, **author**, **description**, **content**, and **image**.
- Mobile responsive and clean UI using **Bootstrap 5**.
- Navigation links to developer's **portfolio**, **GitHub**, and **LinkedIn**.

## 📸 Screenshot
![op6](https://github.com/user-attachments/assets/911c7ce5-1db2-43b4-9f04-a5e9a01de91f)
![op7](https://github.com/user-attachments/assets/61adc2d5-1d60-4e5f-bcb6-a64956c876bf)
![op8](https://github.com/user-attachments/assets/9a159f06-9721-437e-89ec-8fa0a81c21fe)



## 🔧 Technologies Used

- [Python 3](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/)
- [NewsAPI](https://newsapi.org/)
- [Bootstrap 5](https://getbootstrap.com/)
- HTML5 + CSS3

## 📁 Project Structure

```
NewsPaper/
│
├── static/
│   └── style.css           # Custom styles
│
├── templates/
│   └── index.html          # Main HTML template
│
├── app.py                  # Flask backend logic
├── README.md               # Project description
└── requirements.txt        # Dependencies
```

## 🛠️ Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/NewsPaper.git
   cd NewsPaper
   ```

2. **Create a Virtual Environment (Optional but Recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Add Your NewsAPI Key**

   Replace the existing API key in `app.py` with your own:
   ```python
   'apiKey': 'your_own_api_key_here'
   ```

   You can get one from [https://newsapi.org/](https://newsapi.org/).

5. **Run the App**
   ```bash
   python app.py
   ```

6. **Visit in Browser**
   ```
   http://127.0.0.1:5000/
   ```

## 📦 Requirements

Create a `requirements.txt` file:
```txt
Flask
requests
```

To generate it automatically:
```bash
pip freeze > requirements.txt
```

## 🙋‍♂️ Author

**Shreyas Shridhar Kulkarni**  
🔗 [Portfolio](https://shreyasshridharkulkarni.netlify.app/)  
💼 [LinkedIn](https://linkedin.com/in/shreyas-shridhar-kulkarni-946a0225a)  
💻 [GitHub](https://github.com/Shreyu-07)
