#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Assignment 9, football stats"""

import urllib2
from bs4 import BeautifulSoup
import csv

url = 'https://www.cbssports.com/nfl/stats/playersort/nfl/year-2017-season-regular-category-touchdowns'
html = urllib2.urlopen(url)
soup = BeautifulSoup(html.read(), "lxml")

trs = soup.find_all('tr')

for tr in trs[:20]:
    for link in tr.find_all('a'):
        fulllink = link.get ('href')

    tds = tr.find_all("td")

    try:
        Player = str(tds[0].get_text())
        Team = str(tds[1].get_text())
        Position = str(tds[2].get_text())
        Touchdowns = str(tds[3].get_text())

    except:
        print "bad tr string"
        continue

    print(Player, Team, Position, Touchdowns)