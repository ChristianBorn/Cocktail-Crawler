#!/usr/bin/python
# -*- coding: utf-8 -*-

import universal_functions
from bs4 import BeautifulSoup
from bs4 import SoupStrainer
from urllib.parse import urlparse
import json

def main():
    with open('errors.txt', 'w') as errorlog:
        errorlog.write('')
    website = universal_functions.open_website("https://www.allrecipes.com/recipes/133/drinks/cocktails/?page=1")







if __name__ == '__main__':
    main()