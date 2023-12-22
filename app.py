#import libraries
from bs4 import BeautifulSoup
import requests
import pandas as pd
import matplotlib.pyplot as plt


# function returning which id, section heading, and class based on website
def container (url_path, html_type):
   #biotech
    if url_path == 'https://www.biospace.com/news/money/' :
        if html_type == 'id':
            return 'main'
        elif html_type == 'section':
            return 'h3'
        elif html_type == 'class':
            return 'lister__header'
    if url_path == 'https://seekingalpha.com/market-news/energy':
        if html_type == 'id':
            return 'content'
        elif html_type == 'section':
            return 'a'
        elif html_type == 'class':
            return 'text-share-text visited:text-share-text hover:text-share-text focus:text-share-text'
    if url_path == 'https://finance.yahoo.com/tech/':
        if html_type == 'id': 
            return 'Main'
        elif html_type == 'section':
            return 'h3'
        elif html_type == 'class':
            return 'Mb(5px)'


def extraction(url_path):
    #URl + extraction 
    url = url_path
    html = requests.get(url)
    soup = BeautifulSoup(html.content, 'html.parser')

    # finding all of the job titles using the 
    results = soup.find(id = container (url_path, 'id'))
    job_title = results.find_all(container (url_path, 'section'), class_= container (url_path, 'class'))

    # Example Extracting 
    data = [] 
    for job in job_title:
        if len(data) < 3:
            data.append(job.text)

    return data

















