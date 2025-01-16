# web scraper
# created by Ashton Pankey
# revised 11/16/2024

from bs4 import BeautifulSoup
import os
from selenium import webdriver

# creates the terms to search with the web scrape
terms = "America"

# sets the scraper to open microsoft edge
driver = webdriver.ChromiumEdge()
# sets the location site to wikipedia searching for the term
location  = f"https://en.wikipedia.org/wiki/{terms}"
# finds the location and opens the browser
site = driver.get(location)


# geeks for geeks stuff
# sets the source of the page to the variable source
source = driver.page_source
# searches population in the source
search_text = "population"

# creates a file path for the file
dir_path = os.path.dirname(__file__)

# creates a BeautifulSoup object called wiki_page
wiki_page = BeautifulSoup(source, "html.parser")

# finds all tables in the site and sets them equal to rows
rows = wiki_page.find_all("tr")

# creates a function that finds a specific item in one specific wiki page, not very versitile
def get_us_population(n):
    """
    this function takes the input tables from a website and finds the specific location of the population, but it only works for the united states wiki page
    
    """
# creates an empty list
    master_list = []
    # runs through the rows by turning it into a dictionary
    for index, n in enumerate(n):
        # if the word Population is found in one of the rows: the rows are gathered into the list
        if "Population" in n.text:
            # gets the next line in the row
            stuff = rows[index + 1].getText()#getting the population
            # splits the lines into a list based on the spaces
            items = stuff.split(" ")
            # appends the items to the master list
            master_list.append(items)
    # grabs the specific point where the population number is
    raw = master_list[0][2]
    # splits the number off by the left square bracker
    raw = raw.split("[")
    # prints the population of the united states
    return print(f"the population of the united states is: {raw[0]}")


if __name__ == "__main__":
    # activates the population function
    get_us_population(rows)
