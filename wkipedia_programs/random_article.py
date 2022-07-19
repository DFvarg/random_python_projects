import requests
from bs4 import BeautifulSoup as BS

def random_request():
    # gets a random wikipedia article
    request = requests.get("https://en.wikipedia.org/wiki/Special:Random")
    soup = BS(request.content, 'html.parser')
    return soup

def specific_request(title):
    # gets a random wikipedia article
    URL = "https://en.wikipedia.org/wiki/" + str(title)
    request = requests.get(URL)
    soup = BS(request.content, 'html.parser')
    return soup

request = "random"

print(" \n\n#####  INSTRUCTIONS  ##### \n" +
        "This will return random Wikipedia articles. \n" +
        "To read them, type 'y' \n" +
        "To get a new article, type 'n' \n" +
        "To get a specific article, type 's'. NOTE: Write _ instead of spaces and capatalize first letter in each word. \n" +
        "       If you get a message 'Other reasons this message may be displayed:' You may have misspelled something \n" +
        "To close the program, type 'c'. \n\n\n")

while True:
    if request == "random":
        soup = random_request()
    else:
        soup = specific_request(request)

    # finds the title
    s = soup.find('h1', id='firstHeading')
    print("would you like to read about:", s.text)

    cont = input("y/n/s/c: ")
    if cont == 'y':
        # if yes, print article
        lines = soup.findAll('p')
        for line in lines:
            print(line.text)
    elif cont == 'n':
        # else go back and make a new request
        request = "random"
    elif cont == 's':
        request = input("What would you like to read about? ")
    else:
        break
