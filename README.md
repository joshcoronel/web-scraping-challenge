Web Scraping
============

Background
----------

In this web scraping project, we will have a compile the latests news and data
on Mars from the following sources: [NASA Mars News
Site](https://mars.nasa.gov/news), [Jet Propulsion
Laboratory](https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars), [Space
Facts](https://space-facts.com/mars/), and [USGS
Astrogeology](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars).

 

Requirements
------------

Step 1 - Scraping

Complete initial scraping using Jupyter Notebook, BeautifulSoup, Pandas,
Requests/Splinter

-   [ ] Create a Jupyter Notebook file called mission_to_mars.ipynb

-   [ ] Scrape from [NASA Mars News Site](https://mars.nasa.gov/news/)

    -   [ ] Scrape the lastest News Title and Paragraph Text

    -   [ ] Assign the text to variables for reference later

-   [ ] Scrape from [Jet Propulsion
    Laboratory](https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars)

    -   [ ] Use splinter to find the image url for the current Featured Mars
        Image

        -   [ ] Assign to variable called featured_image_url

        -   [ ] Find the image url to the full size .jpg image

        -   [ ] Save a complete url string for this image

-   [ ] Scrape from [Space Facts](https://space-facts.com/mars/)

    -   [ ] Use pandas to scrape the table containing facts about planets
        (diameter, mass, etc)

    -   [ ] Use pandas to convert the data to a HTML table string

-   [ ] Scrape from [USGS
    Astrogeology](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars)

    -   [ ] Click the weblink to each hemisphere to find the image url to the
        full resolution image

    -   [ ] Save the image url string and the hemisphere title

        -   [ ] Use a python dictionary to store the data using the keys img_url
            and title

        -   [ ] Append the dictionary to a list. This list will contain one
            dictionary for each hemisphere

Step 2 - MongoDB and Flask Application

Use MongoDB with Flask templating to create a new HTML page that displays all
the information that was scraped from the URLs above

-   [ ] Convert Jupyter Notebook into a Python scraped called scrape_mars.py
    with a function called scrape

    -   [ ] Contains all scraping code

    -   [ ] Return one Python dictionary containing all the scraped data

-   [ ] Create a route called /scrape that

    -   [ ] Import the scrape_mars.py script and calls the scrape fucntion

    -   [ ] Store the return value in Mongo as a Python dictionary

-   [ ] Create a root route /

    -   [ ] Query the Mongo database

    -   [ ] Pass the mars data into an HTML template to display the data

-   [ ] Create a template HTML file called index.html

    -   [ ] Assign the mars data dictionary to the appropriate HTML element

 
