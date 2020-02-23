#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import json

from slugify import slugify, PRE_TRANSLATIONS

from lib.helpers import fetch, parse, extract


if __name__ == "__main__":
    # Loading URLs from JSON
    base_urls = []

    with open('states.json', 'r') as file:
        data = json.load(file)
        for state, url in data.items():
            base_urls.append([state, url])

    # Fetching data, storing as JSON
    for state, base_url in base_urls:
        file = 'libraries/' + slugify(state, replacements=PRE_TRANSLATIONS) + '.json'

        if os.path.isfile(file) is False:
            with open(file, 'w') as file:
                library_urls = fetch(base_url)
                libraries = []

                for library_url in library_urls:
                    library = parse(library_url)
                    libraries.append(library)

                json.dump(libraries, file, ensure_ascii=False, indent=4)
