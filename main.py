from flask import Flask, render_template
from app import extraction, container
from sumry import summarize_text_list
from apscheduler.schedulers.background import BackgroundScheduler

# INitialize Flask App  
app = Flask(__name__)

# Initialize Scheduler
scheduler = BackgroundScheduler()

# Global variable to store the results
biotech = ''
energy = ''
overall = ''


def scrape_and_summarize():

    #Biotech extraction
    titlesBio = extraction('https://www.biospace.com/news/money/')
    biotech = titlesBio
   

    #Energy Extraction
    titlesEnergy = extraction('https://seekingalpha.com/market-news/energy')
    energy = titlesEnergy

    #yfinance extraction 
    titlesOverall = extraction('https://finance.yahoo.com/tech/')
    overall = titlesOverall


# Add a scheduled job
scheduler.add_job(func=scrape_and_summarize, trigger='interval', hours=1)  # Adjust the interval as needed
scheduler.start()


@app.route('/')
def index():
    return render_template('template.html', summary =biotech, energysum=energy, Techsummary=overall )  # Your HTML file

if __name__ == '__main__':
    try:
        app.run(debug=True)
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()