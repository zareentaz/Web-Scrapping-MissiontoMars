# Web-Scrapping-MissiontoMars
Created a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page.

Web scraping using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter. Used MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped earlier finally, deployed Flask app to Heroku.

Step 1 - Scraping

Create a Jupyter Notebook fle called mission_to_mars.ipynb and use this to complete all of your scraping and analysis tasks. The following outlines what you need to scrape.

  1.NASA Mars News
    Scrape the NASA Mars News Site and collect the latest News Title and Paragraph Text. Assign the text to variables that you can 
    reference later.

 2.JPL Mars Space Images - Featured Image
   Use splinter to navigate the site and find the image url for the current Featured Mars Image and assign the url string to a variable        called featured_image_url.
 
 3.Mars Weather
   Visit the Mars Weather twitter account and scrape the latest Mars weather tweet from the page. Save the tweet text for the weather          report as a variable called mars_weather.
   
 4.Mars Facts
   Visit the Mars Facts webpage here and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.
   We use Pandas to convert the data to a HTML table string.

Step 2 - MongoDB and Flask Application

 1. Start by converting your Jupyter notebook into a Python script called scrape_mars.py with a function called scrape that will execute     all of your scraping code from above and return one Python dictionary containing all of the scraped data.

 2. Next, create a route called /scrape that will import your scrape_mars.py script and call your scrape function.

 3. Store the return value in Mongo as a Python dictionary.
    Create a root route / that will query your Mongo database and pass the mars data into an HTML template to display the data.

 4. Create a template HTML file called index.html that will take the mars data dictionary and display all of the data in the appropriate     HTML elements. Use the following as a guide for what the final product should look like, but feel free to create your own design.

