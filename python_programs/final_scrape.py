# final project for python 1
# created by Ashton Pankey
# last revised 12/2/2024

# imports tools needed for web scraping
from bs4 import BeautifulSoup
import os
from selenium import webdriver
import requests
import re

# creates a selenium driver that opens microsoft edge
driver = webdriver.ChromiumEdge()

# sets up the headless portion of the web scrape
# taken from https://stackoverflow.com/questions/65171183/how-to-run-headless-microsoft-edge-with-selenium-in-python
settings = webdriver.EdgeOptions()
settings.add_argument("--headless=new")
driver = webdriver.Edge(options=settings)


# creates a Webscraper class that handles site scraping
class Webscraper:
    # creates a scrape_site method that takes one variable
    def scrape_site(self, location):
        """
        this method takes 1 variable called location which is a website link and returns the BeautifulSoup object as page
        """
        # checks if the location has a website present
        site_confirm = requests.get(location)
        # if the website is actually present it continues along the code
        if site_confirm.status_code == 200:
            # tells the webscraper to scrape the site
            driver.get(location)
            # creates a file path for the file
            os.path.dirname(__file__)
            source = driver.page_source
            # creates a BeautifulSoup object called wiki_page
            page = BeautifulSoup(source, "html.parser")
            # returns the page the scrape found
            return page
        # otherwise the site is returned as None
        else:
            return None

    # creates a method to get paragraphs in a site, taking only one variable
    def get_paragraphs(self, location):
        """
        this method also takes 1 variable called location and uses the scrape_site method to get the BeautifulSoup object.
        the method then splits the paragraphs of the object into a list of words and returns that list
        """
        # uses try and except in case there are no paragraphs
        try:
            # creates an empty string called article
            article = ''
            # scrapes the website
            page = self.scrape_site(location)
            # runs through all of the paragraphs in the article
            for paragraph in page.select('p'):
                # gets the text from each paragraph
                article += paragraph.get_text()
                # replaces all of the unhelpful items with stuff that can be removed
                article = article.replace('-', ' ')
                article = article.replace('!', '')
                article = article.replace('\\', '')
                # splits the paragraphs by the unhelpful stuff
                listed = re.split('[/,":;(). ]+', article)
                # returns the list of words
            return listed
        # if there are no paragraphs, the method returns an empty list
        except Exception as ex:
            ex = ex
            return []

    def get_tables(self, location):
        """
        this method also takes 1 variable called location and uses the scrape_site method to get the BeautifulSoup object.
        the method then splits the tables of the object into a list of words and returns that list
        """
        # creates an empty string called article
        article = ''
        # assigns the webscrape to the name page
        page = self.scrape_site(location)
        # tries searching for the words in tables
        try:
            # searches through each table
            for table in page.select('tr'):
                # adds the text of each table to the string article
                article += table.get_text()
                # uses a for loop to remove all bracketed items from the string
                for i in range(100):
                    article = article.replace(f'[{i}]', '')
                # replaces the items from the string that cause issues
                article = article.replace('\n', '/')
                article = article.replace('-', '/')
                article = article.replace('(', '')
                article = article.replace(')', '')
                # splits the string into a list of words, eliminating all problematic characters in the process
                listed = re.split('[/,":;() ]+', article)
            # returns the list of words
            return listed
        # if the word find fails, the method returns an empty list
        except Exception as ex:
            ex = ex
            return []
    # creates a method to get the instances of specific words within an article

    def get_word(self, location, word):
        """
        This method takes 2 variables, article and word.
        It uses them to get lists of words from tables and paragraphs in a website.
        It then looks for any words that match the variable 'word' adding 1 to the integer instances with every found instance.
        """
        # sets instances to 0
        instances = 0

        try:
            # gets all paragraphs within an article
            page1 = self.get_paragraphs(location)
            # gets all tables within an article
            page2 = self.get_tables(location)

            # runs through each word in the paragraphs list
            for i in page1:
                # if the word is found, the instances increase by 1 with each find
                if str(i) == word:
                    instances += 1
            # runs through each word in the tables list
            for i in page2:
                # if the word is found, the instances increase by 1 with each find
                if str(i) == word:
                    instances += 1
            # returns how many instances were found for that word
            return instances
        except Exception as ex:
            ex = ex
            return None


# if this program is the main program, the print functions are run
if __name__ == "__main__":
    scraper = Webscraper()
    print(scraper.get_paragraphs("https://www.geeksforgeeks.org/write-regular-expressions/"))
    print(scraper.get_tables("https://www.geeksforgeeks.org/write-regular-expressions/"))
