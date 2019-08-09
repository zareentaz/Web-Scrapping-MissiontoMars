# import necessary libraries
from flask import Flask, render_template

# Dependencies
from splinter import Browser
from bs4 import BeautifulSoup
import requests
import pymongo
import re
import pandas as pd

# Import our pymongo library, which lets us connect our Flask app to our Mongo database.
import pymongo

# Create an instance of our Flask app.
app = Flask(__name__)

# Create connection variable
conn = 'mongodb://localhost:27017'

# Pass connection to the pymongo instance.
client = pymongo.MongoClient(conn)


# Initialize browser
def init_browser(): 

    executable_path = {'executable_path': 'chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)

mars_info = {}

# NASA MARS NEWS
def scrape_mars_news():
    
      mission_url = 'https://mars.nasa.gov/news/'
      browser.visit(mission_url)
      html=browser.html
      soup = BeautifulSoup(html, 'html.parser')
      #Extract the latest News Title
      content = soup.find('li', class_='slide')
      #print(content)

      #scrape the title from h3 tag & print the news_title
      news_title = content.find('h3').text
      # print(f"news_title = {news_title}")

      #Extract the latest paragraph text from the class
      news_p=soup.find('div',class_='article_teaser_body').text.strip()
      # print(f"news_p = {news_p}")

      # Dictionary entry from MARS NEWS
      mars_info['news_title'] = news_title
      mars_info['news_p'] = news_p

      return mars_info






