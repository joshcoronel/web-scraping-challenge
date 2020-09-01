# Import dependecies
from bs4 import BeautifulSoup as bs
import pandas as pd
from splinter import Browser
import requests
import time

def scrape():
    mars_dict = {}

    # Set up Browser
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)

    # Scrape from [NASA Mars News Site](https://mars.nasa.gov/news/)
    url = 'https://mars.nasa.gov/news/'

    # Retrieve page with the requests module
    response = requests.get(url)

    time.sleep(1)

    # Create BeautifulSoup object; parse with 'html.parser'
    soup = bs(response.text, 'html.parser')

    article = soup.find("div",class_="slide")

    news_title = article.find('div',class_="content_title").a.text.strip()
    news_paragraph = article.a.text.strip() 
    mars_dict['news_title'] = news_title
    mars_dict['news_paragraph'] = news_paragraph

    # Scrape from [Jet Propulsion Laboratory](https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars)
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)

    time.sleep(1)
    
    # Output html of webpage
    html = browser.html
    soup = bs(html,'html.parser')

    # Store the url of the featured image
    featured_image_url = soup.find('a', class_="button fancybox")['data-fancybox-href']
    featured_image_url = "https://www.jpl.nasa.gov" + str(featured_image_url)
    mars_dict['featured_img_url'] = featured_image_url

    # Scrape from [Space Facts](https://space-facts.com/mars/)
    url = 'https://space-facts.com/mars/'
    tables = pd.read_html(url)

    time.sleep(1)

    # Define pandas datafame
    df = tables[0]
    df.columns = ['description','value']
    df.set_index('description',inplace=True)
    # Convert dataframe back to html
    mars_facts = df.to_html()

    mars_dict['mars_facts'] = mars_facts

    # Scrape from [USGS Astrogeology](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars)
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)

    time.sleep(1)

    # Output html of webpage
    html = browser.html
    soup = bs(html,'html.parser')

    images = soup.find_all('div',class_='item')
    base_url = "https://astrogeology.usgs.gov"
    hem_dict = []

    for image in images:
        # Find the hemisphere's url and title
        image_url = image.find('a',class_='itemLink product-item')['href']
        title = image.h3.text
        
        # Launch the hemisphere's url
        browser.visit(base_url + image_url)
        img = browser.html
        soup = bs(img,'html.parser')
        
        img_url = base_url + soup.find('img', class_='wide-image')['src']
        hem_dict.append({'title':title,'img_url':img_url})

    mars_dict['hem_dict'] = hem_dict

    return mars_dict