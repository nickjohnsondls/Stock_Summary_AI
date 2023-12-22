from flask import Flask, render_template
from app import extraction, container

# do the app 
app = Flask(__name__)

titles = extraction('https://www.biospace.com/news/money/')

@app.route('/')
def index():
    return render_template('template.html', jobs =titles)  # Your HTML file

if __name__ == '__main__':
    app.run(debug=True)