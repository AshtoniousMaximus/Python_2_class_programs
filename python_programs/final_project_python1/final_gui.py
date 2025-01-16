# gui window for final project
# created by Ashton Pankey
# revised on 11/21/2024


import tkinter as tk
from tkinter import Label, PhotoImage
from utilities import path
from final_scrape import Webscraper

# creates an object from the class Webscraper
scraper = Webscraper()
# creates a tkinter window
window = tk.Tk()

# this section and the update function are from a stackoverflow question and were modified to work properly.
# all they do is make the gif animation work
#  https://stackoverflow.com/questions/43770847/play-an-animated-gif-in-python-with-tkinter
frames = [
    # takes the file path of the gif and gives an index within the PhotoImage
    PhotoImage(file=path("thing.gif"), format="gif -index %i" % (i))
    # runs through the 60 frames of the image, making the animation work
    for i in range(60)
]


# taken and modified from stackoverflow
# creates a function called update
def update(ind):
    """
    This function uses an if statement that runs in an odd recursive loop to continuously update the framerate.
    It does this by increasing the frame value and the if statement resets the value if it is over 59, causing it to start over again.
    """

    # sets the frame to be at the frame at ind
    frame = frames[ind]
    # adds 1 to the value ind
    ind += 1
    # With this condition it will play gif infinitely
    # if the framerate is greater than 59, the frame is set back to 0
    if ind > 59:
        ind = 0
        # configures the image for the current frame
    label.configure(image=frame)
    # after the duration of update speed, the frame changes
    window.after(40, update, ind)


# starts the animation
window.after(0, update, 0)


# creates a function to write the search history to a text file
def add_record(site, word, instances):

    """
    This function creates a text file that is the user history of searches
      it prints what and where the user searched whenever the user searches for a word into a text file
    """
    # opens/creates the history.txt file and references it as hist
    with open("history.txt", 'a') as hist:
        # writes the search history into the file with every word search
        if instances is not None:
            hist.write(f"user searched {site} site for '{word}', finding {str(instances)} instances of the word\n")
        else:
            hist.write("failed search attempt, user searched invalid website address\n")


# creates a function that checks if the website exists
def find_website():
    """
    This function takes both the user entered website and verifies that the website is there.
    It does this by checking if the code recieved is a 200 or not.
    It then tells the user if the website has been found or not based on the code it recieved.
    """
    # aliases the website link as a string under location
    location = str(site_entry.get())
    # runs the scrape_site method from the scraper object
    validation = scraper.scrape_site(location)
    # if the method says the site was found, a page found message is created and configured to the gui
    if validation is not None:
        status_text = "Success! page found"
        status_label.configure(text=status_text)
    # if the method says the site was not found, a page not found message is created and configured to the gui
    else:
        status_text = "page not found"
        status_label.configure(text=status_text)


# creates a word instances function that interfaces with the scraper object
def word_instances():
    """
    This function takes the user entered websites and scrapes the website using the scraper.get_word method,
      finding all instances of the word entered within the paragraphs and tables of the article.
      Finally, the function creates a history of the user search
    """

    # creates a string of the word entered by the user
    word = str(word_entry.get())
    # tries searching for the word
    try:
        # sets instances to the word count within an article
        instances = scraper.get_word(site_entry.get(), word)
        # creates an f string that takes the instances of a word and the word itself and prints the quantity for the user
        status_text = f"the page contains {instances} instances of the word '{word}'"
        # configures the label and prints it to the gui
        status_label.configure(text=status_text)
        # adds a record of the word search to the history.txt
        add_record(site_entry.get(), word_entry.get(), instances)
    # if the search fails, an error message is created
    except Exception as ex:
        ex = ex
        # creates the error message
        status_text = "invalid search entry, enter a valid website"
        # prints the error message to the gui
        status_label.configure(text=status_text)
        # adds a history of the user search
        add_record(site_entry.get(), word_entry.get(), None)


# aliases the word label with the Label function in tkinter
label = Label(window)
# packs the label function
label.pack()
# sets the title of the window
window.title("Wikipedia word instance finder")

# creates a text entry box for the user to enter websites
site_entry = tk.Entry(window, text=' enter site link', width=20)
# packs the entry box to the gui
site_entry.pack()

# creates a button to check if the entered website exists
entry_button = tk.Button(window, text='Enter a website link', command=find_website)
# packs the entry button to the gui
entry_button.pack()

# creates a text entry box for the user to enter a search word
word_entry = tk.Entry(window, text='enter search word', width=20)
# packs the entry box to the gui
word_entry.pack()

# creates a button to search the scraped website for the word
entry_button = tk.Button(window, text='Enter a word to search', command=word_instances)
# packs the entry button to the gui
entry_button.pack()


# creates a label for an status message
status_label = tk.Label(window)
# packs the message
status_label.pack()

# runs the gui window in a loop
window.mainloop()
