#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib.request
from http.cookiejar import CookieJar

def open_website(link):
    website = urllib.request.Request(link, headers={'User-Agent' : "Magic Browser"})
    cj = CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    website = opener.open(website)
    return website