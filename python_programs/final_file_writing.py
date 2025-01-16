# file writing portion of my python 1 class final
# created by Ashton Pankey
# revised on 11/24/2024


def add_record(site,word,instances):
    with open("history.txt", 'a') as hist:
        hist.write(f"user searched {site} site for {word} word, finding {instances} instances of the word")
