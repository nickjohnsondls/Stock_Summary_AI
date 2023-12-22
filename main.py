from flask import Flask, render_template
from app import extraction, container
from sumry import summarize_text_list

# do the app 
app = Flask(__name__)

#Biotech extraction
titlesBio = extraction('https://www.biospace.com/news/money/')
#summaryBiotech = summarize_text_list(titlesBio)

#Energy Extraction
titlesEnergy = extraction('https://seekingalpha.com/market-news/energy')

#yfinance extraction 
titlesOverall = extraction('https://finance.yahoo.com/tech/')

@app.route('/')
def index():
    return render_template('template.html', summary =titlesBio, energysum=titlesEnergy, Techsummary=titlesOverall )  # Your HTML file

if __name__ == '__main__':
    app.run(debug=True)