from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
import cssutils

def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)


def scrape_info():
    browser = init_browser()

    # Visit visitcostarica.herokuapp.com
#    url = "https://visitcostarica.herokuapp.com/"
    url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url)

    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    carousel = soup.find('div', class_= 'carousel_items')
    div_style = carousel.find('article')['style']
    style = cssutils.parseStyle(div_style)
    partial_url = style['background-image']

#    print(partial_url)

    partial_url = partial_url.replace('url(', '').replace(')', '')
    featured_image_url = "https://jpl.nasa.gov" + partial_url


    print("###############")
    print(featured_image_url)
    print("###############")

#    mars_image = soup.find('div',id='page')
    mars_image = featured_image_url

    # Get the average temps
#    avg_temps = soup.find('div', id='weather')

    # Get the min avg temp
#    min_temp = avg_temps.find_all('strong')[0].text

    # Get the max avg temp
#    max_temp = avg_temps.find_all('strong')[1].text

    # BONUS: Find the src for the sloth image
#    relative_image_path = soup.find_all('img')[2]["src"]
#    mars_img = url + relative_image_path

    min_temp = 66
    max_temp = 99

    # Store data in a dictionary
    mars_data = {
        "mars_img": mars_image,
        "min_temp": min_temp,
        "max_temp": max_temp
    }

    # Close the browser after scraping
    browser.quit()

    # Return results
    return mars_data
