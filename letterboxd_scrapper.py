import urllib.request
import pandas as pd
import sys
import time
from bs4 import BeautifulSoup


def fetch_html(url):

    headers = {"User-Agent": "Mozilla/5.0"}
    request = urllib.request.Request(url, headers=headers)

    with urllib.request.urlopen(request) as response:
        html = response.read().decode("utf-8")
    return html

def find_titles(user: str):# 1. Find ONE element with any data-item-name value
    
    blankPage = False
    iteration = 0
    elements_titles = []

    while not blankPage:
        elements = []
        if iteration == 0:
            url = 'https://letterboxd.com/'+user+'/watchlist/'
        else:
            url = 'https://letterboxd.com/'+user+'/watchlist/page/'+str(iteration+1)+'/'
        html = fetch_html(url)
        soup = BeautifulSoup(html, "html.parser")
        elements = soup.find_all(attrs={"data-item-name": True})

        for element in elements:
            elements_titles.append(element["data-item-name"])
        iteration += 1
        if len(elements) == 0:
            blankPage = True
        else:
            print('Reviewed page number ', iteration)

    return elements_titles

def separate_in_title_year(titlesAndYears: str):

    titles = []
    years = []

    for titleAndYear in titlesAndYears:
        titles.append(titleAndYear.split('(')[0])
        years.append(titleAndYear.split('(')[1].split(')')[0])

    return titles, years

def print_title_list(titles: list):
    print('\nWatchlist:\n')
    for title in titles:
        print(title)
    print('\n')

if __name__ == "__main__":
    if "-h" in sys.argv[1:] or "--help" in sys.argv[1:]:
        print("Usage: python letterboxd_scrapper.py <username> <username2> <username3> ...")
    else:
        date = time.strftime("%Y-%m-%d-%H-%M-%S", time.gmtime())
        if len(sys.argv) > 1:
            argv = sys.argv[1:]
            for arg in argv:
                user = arg
                try:
                    titlesAndYears = find_titles(user)
                    if len(titlesAndYears) == 0:
                        print("\nNo titles found for user", user)
                    else:
                        print("\nTitles found for user", user)
                        print_title_list(titlesAndYears)

                        titles, years = separate_in_title_year(titlesAndYears)
                        df = pd.DataFrame(titles, columns=['Name'])
                        df['Year'] = years

                        # On utc
                        nameToStore = f"watchlist-{user}-{date}-utc.csv"

                        df.to_csv(nameToStore, index=False)

                        print(f'Stored on {nameToStore}')
                except :
                    print(f'User {user} does not exist')
        else:
            print("Please provide a username or a list of username separated by a space")
