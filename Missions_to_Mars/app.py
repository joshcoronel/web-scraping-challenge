from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")

@app.route("/")
def home():

    # Find one record of data from the mongo database
    mars = mongo.db.mars.find_one()

    # Return template and data
    return render_template("index.html",mars=mars)

# Route to execute scrape function
@app.route("/scrape")
def get_scrape():
    mars = mongo.db.mars

    # Run the scrape function
    mars_data = scrape_mars.scrape()

    # Update the mongo database
    mars.update({},mars_data,upsert=True)

    # Redirect back to the root directory
    return redirect("/")



if __name__ == "__main__":
    app.run(debug=True)