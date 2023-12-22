from flask import Flask, render_template
from app import extraction, container
from sum import summarize_text_list

# do the app 
app = Flask(__name__)

titles = extraction('https://www.biospace.com/news/money/')
summary = summarize_text_list(titles)


@app.route('/')
def index():
    return render_template('template.html', summary =summary)  # Your HTML file

if __name__ == '__main__':
    app.run(debug=True)