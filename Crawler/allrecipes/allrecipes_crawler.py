#!/usr/bin/python
# -*- coding: utf-8 -*-

from Crawler import universal_functions
from bs4 import BeautifulSoup
from bs4 import SoupStrainer
from urllib.parse import urlparse
from urllib.error import HTTPError
import json

def gather_links():
    link_list = []
    limit_pages = 1000

    with open('errors.txt', 'w') as errorlog:
        errorlog.write('')

    for pagenumber in range(1, limit_pages):
        try:
            print(f'[+] Getting Links from https://www.allrecipes.com/recipes/133/drinks/cocktails/?page={pagenumber}')
            website = universal_functions.open_website(f'https://www.allrecipes.com/recipes/133/drinks/'
                                                       f'cocktails/?page={pagenumber}')
            soup = BeautifulSoup(website, 'html.parser')
            recipe_cards = soup.find_all('article', class_='fixed-recipe-card')
            for recipe in recipe_cards:
                recipe_link = recipe.find('a')['href']
                link_list.append(recipe_link)
        except HTTPError:
            print('Reached last page: '+str(pagenumber))
            break
    number_links = len(link_list)
    print(f'[+] Number of Extracted links: {number_links}')
    with open('allrecipes_links.json', 'w') as file:
        json.dump(link_list, file, indent=2)

def main():
    gather_links()


if __name__ == '__main__':
    main()