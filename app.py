# pip install gunicorn
# pip freeze > requirements.txt

from flask import Flask, render_template
import requests
import random

app = Flask(__name__)

@app.route('/')
def home():
    url = 'https://newsapi.org/v2/top-headlines'
    params = {
        'country': 'us',  # You can change this to 'us', 'gb', etc.
        'apiKey': 'ADD YOUR OWN API KEY'
    }

    response = requests.get(url=url, params=params)
    data = response.json()

    articles = data.get('articles', [])
    if not articles:
        return render_template('index.html',
                               title="No News Available",
                               auther="N/A",
                               description="No Description",
                               url="#",
                               image="https://via.placeholder.com/600x400?text=No+Image",
                               content="No content could be fetched.")

    # Pick a random article
    article = random.choice(articles)

    auther = article.get('author', 'N/A')
    title = article.get('title', 'No Title')
    description = article.get('description', 'No Description')
    url = article.get('url', '#')
    image = article.get('urlToImage', 'https://via.placeholder.com/600x400?text=No+Image')
    content = article.get('content', 'No content could be fetched.')

    return render_template('index.html',
                           auther=auther,
                           title=title,
                           description=description,
                           url=url,
                           image=image,
                           content=content)

if __name__ == "__main__":
    app.run(debug=True)

