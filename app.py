#import libraries
from bs4 import BeautifulSoup
import requests
import pandas as pd
import matplotlib.pyplot as plt
from flask import Flask, render_template

#URl + extraction 
url = 'https://realpython.github.io/fake-jobs/'
html = requests.get(url)
soup = BeautifulSoup(html.content, 'html.parser')

results = soup.find(id='ResultsContainer')
job_title = results.find_all('h2', class_= 'title is-5')




# Example Extracting 
data = [] 
for job in job_title:
    data.append(job.text)



#Convert data to a DataFrame
df = pd.DataFrame(data, columns=['jobs'])

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('template.html', jobs =data)  # Your HTML file

if __name__ == '__main__':
    app.run(debug=True)










