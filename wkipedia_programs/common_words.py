import requests
from bs4 import BeautifulSoup as BS
import matplotlib.pyplot as plt

def random_request():
    # gets a random wikipedia article
    request = requests.get("https://en.wikipedia.org/wiki/Special:Random")
    soup = BS(request.content, 'html.parser')
    return soup

word_appearances = dict()

iteration = 0
total_iterations = 5 # Increase this number to gather information from more articles!
while iteration < total_iterations:
    soup = random_request()
    # finds the title
    s = soup.find('h1', id='firstHeading')
    print("Article:", s.text)

    # Seperates the words from <p> tags into a dictionary
    lines = soup.findAll('p')
    for line in lines:
        words = str(line.text).split(' ')
        for i in words:
            i = i.lower()
            word_appearances[i] = word_appearances.get(i, 0) + 1

    if iteration < total_iterations-1:
        print("Finished. Collecting next article...\n")
    else:
        print("Finished. Gathering final data...\n")
    
    iteration += 1


top_words = []
top_values = []

# Sorts the words by value and stores them in a list (By default Order does not matter in dictionaries, it does in lists)
wordlist=sorted((value, key) for (key,value) in word_appearances.items())
i = 1
while i < 6:
    print(wordlist[-i])
    top_words.append(wordlist[-i][1])
    top_values.append(wordlist[-i][0])
    i += 1


# Plots the bar graph
fig = plt.figure(figsize = (10, 5))
plt.bar(top_words, top_values, width=.4, color="maroon")
plt.ylabel('Occurences')
plt.xlabel('Words')
plt.title('Number of word occurences in random wikipedia entries')
plt.show()


