from flask import Flask, render_template, redirect
import pymongo
import scrape_mars

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
#app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_db"
#mongo = pymongo(app)

# Or set inline
# mongo = PyMongo(app, uri="mongodb://localhost:27017/craigslist_app")

# setup mongo connection
conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)
db=client.mars1_db
collection=db.mars_info
#mars1_db.mars_data.insert_many(mars_info)
#db.collection.insert_many(mars_data)


@app.route("/")
def home():
    mars_data= db.mars_info.find_one()
    #mars_data=list(db.collection.find())
    return render_template("index.html", mars_data=mars_data)



@app.route("/scrape")
def scrape():
    mars_data = db.mars_info
    mars_fact= scrape_mars.scrape_mars_news()
    mars_fact = scrape_mars.scrape_mars_image()
    mars_fact = scrape_mars.scrape_mars_weather()
    mars_fact = scrape_mars.scrape_mars_facts()
    mars_fact = scrape_mars.scrape_mars_hemispheres()
    mars_data.update({}, mars_fact, upsert=True)
    # redirecting the route we are the code
    return redirect("/", code=302)


if  __name__ == "__main__":
    app.run(port=5002,debug=True)