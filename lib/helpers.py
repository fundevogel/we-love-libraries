#!/usr/bin/env python
# -*- coding: utf-8 -*-

from urllib.request import urlopen
from bs4 import BeautifulSoup as bs


# Takes per-state URL
# Returns per-state library URLs
def fetch(base_url):
    html = urlopen(base_url)
    soup = bs(html, 'lxml')
    dbv_url = 'https://www.bibliotheksverband.de'

    # Fetch table rows, cut first one (header)
    rows = soup.findAll('tr')[1:]
    library_urls = []

    for row in rows:
        library_url = row.find('a', href=True)['href']
        library_urls.append(dbv_url + library_url)

    return library_urls


# Takes per-library URL
# Returns per-library dictionary
def parse(base_url):
    html = urlopen(base_url)
    soup = bs(html, 'lxml')

    # Fetch table
    # (1) Find first header
    # (2) Select next table
    table = soup.find('h2').find_next_sibling('table')

    # Extract library dataset
    library = extract(table)

    return library


# Takes HTML containing per-library data
# Returns per-library dataset as dictionary
def extract(html):
    data = {}

    try:
        data['title'] = html.find('td', text="Bibliothek:").find_next().text
    except:
        pass

    try:
        data['institution'] = html.find('td', text="Institution:").find_next().text
    except:
        pass

    try:
        data['manager'] = html.find('td', text="Direktion/Leitung:").find_next().text
    except:
        pass

    try:
        data['street'] = html.find('td', text="Strasse:").find_next().text
    except:
        pass

    try:
        data['postal'] = html.find('td', text="PLZ Strasse:").find_next().text
    except:
        pass

    try:
        data['city'] = html.find('td', text="Ort:").find_next().text
    except:
        pass

    try:
        data['mail'] = html.find('td', text="Mail:").find_next().text
    except:
        pass

    try:
        data['web'] = html.find('td', text="Internet:").find_next().text
    except:
        pass

    try:
        data['phone'] = html.find('td', text="Telefon:").find_next().text
    except:
        pass

    try:
        data['fax'] = html.find('td', text="Fax:").find_next().text
    except:
        pass

    return data
