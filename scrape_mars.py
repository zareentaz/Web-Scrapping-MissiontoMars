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
#app = Flask(__name__)

# Create connection variable
#conn = 'mongodb://localhost:27017'

# Pass connection to the pymongo instance.
#client = pymongo.MongoClient(conn)


# Initialize browser
def init_browser(): 

    executable_path = {'executable_path': 'chromedriver'}
    return Browser('chrome', **executable_path, headless=False)

mars_data = {}

# NASA MARS NEWS
def scrape_mars_news():
    try:

      browser=init_browser()
    
      mission_url = 'https://mars.nasa.gov/news/'
      browser.visit(mission_url)
      html=browser.html
      soup = BeautifulSoup(html, 'html.parser')
      #Extract the latest News Title
      #content = soup.find('li', class_='slide')
      #print(content)

      #scrape the title from h3 tag & print the news_title
      news_title = soup.find('div', class_='content_title').find('a').text
      # print(f"news_title = {news_title}")

      #Extract the latest paragraph text from the class
      news_p=soup.find('div',class_='article_teaser_body').text.strip()
      # print(f"news_p = {news_p}")

      # Dictionary entry from MARS NEWS
      mars_data['news_title'] = news_title
      mars_data['news_p'] = news_p

      return mars_data
    finally:

      browser.quit()

# FEATURED IMAGE
def scrape_mars_image():

      try: 
  
          # Initialize browser 
          browser = init_browser()

          #JPL Mars Space Images - Featured Image
          JPL_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
          browser.visit(JPL_url)
          html=browser.html
          soup = BeautifulSoup(html, 'html.parser')

          #Getting the soucre image name  .jpg
          first_image=soup.find('article')['style'].replace('background-image: url(','').replace(');', '')[1:-1]
          
          # Website Url 
          main_url = 'https://www.jpl.nasa.gov'

          #concatinating the url and the image url
          featured_image_url = main_url+first_image
          #print(f"featured_image_url = {featured_image_url}")

          mars_data['featured_image_url']=featured_image_url

          return mars_data
      finally:
          browser.quit()

# Mars Weather 
def scrape_mars_weather():

      try: 
  
          # Initialize browser 
          browser = init_browser()
          twitter_url="https://twitter.com/marswxreport?lang=en"
          browser.visit(twitter_url)
          html=browser.html
          soup = BeautifulSoup(html, 'html.parser')
          #soup.prettify()
          mars_weather_data=soup.find('div',class_='js-tweet-text-container')
          mars_weather=mars_weather_data.find('p').text.strip()
          #print(f"mars_weather = {mars_weather}")
           # Dictionary entry from WEATHER TWEET
          mars_data['mars_weather'] = mars_weather
        
          return mars_data
      finally:

        browser.quit()

# Mars Facts
def scrape_mars_facts():

      #Mars Facts url
    mars_facts_url='http://space-facts.com/mars/'
    mars_facts = pd.read_html(mars_facts_url)

    # Find the mars facts DataFrame in the list of DataFrames 
    mars_df = mars_facts[1]


    # Assign the columns `['Description', 'Value']`
    mars_df.columns = ['Description','Value']

    # Set the index to the `Description` column without row indexing
    mars_df.set_index('Description', inplace=True)

    # Save html code to folder Assets
    data=mars_df.to_html()

    #data = mars_df.to_dict(orient='records')  # Here's our added param..

    # Display mars_df
    mars_data['data'] = data

    return mars_data

# MARS HEMISPHERES


def scrape_mars_hemispheres():

      try: 
  
          # Initialize browser 
          browser = init_browser()
  
          # Visit hemispheres website through splinter module 
          executable_path = {'executable_path': 'chromedriver'}
          browser = Browser('chrome', **executable_path, headless=False)

          mars_hemi_url="https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
          browser.visit(mars_hemi_url)
          html=browser.html
          soup = BeautifulSoup(html, 'html.parser')
          # Retreive all items that contain mars hemispheres information
          items = soup.find_all('div', class_='item')


          # Create empty list for hemisphere urls 
          hemi_url = []

           # Store the main_ul 
          hemispheres_main_url = 'https://astrogeology.usgs.gov' 

           # Loop through the items previously stored
          for i in items: 
           # Store title
            title = i.find('h3').text
    
           # Store link that leads to full image website
            partial_img_url = i.find('a', class_='itemLink product-item')['href']

    
    # Visit the link that contains the full image website 
            browser.visit(hemispheres_main_url + partial_img_url)
    
    # HTML Object of individual hemisphere information website 
            partial_img_html = browser.html
    
    # Parse HTML with Beautiful Soup for every individual hemisphere information website 
            soup = BeautifulSoup( partial_img_html, 'html.parser')
    
    # Retrieve full image source 
            img_url = hemispheres_main_url + soup.find('img', class_='wide-image')['src']
    
    # Append the retreived information into a list of dictionaries 
            hemi_url.append({"title" : title, "img_url" : img_url})

# Display hemisphere_image_urls
          mars_data['hemi_url'] = hemi_url

          return mars_data
      finally:

          browser.quit()