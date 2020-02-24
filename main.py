#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import json
import argparse

from lib.helpers import fetch, parse, extract


parser = argparse.ArgumentParser(
    description="Fetches information about libraries from the German Library Association",
    usage='Use "%(prog)s --help" for more information',
)

parser.add_argument(
    '-s', '--states', nargs='+',
    help="Fetches information for given federal states",
    choices={
        'baden-wuerttemberg',
        'bayern',
        'berlin',
        'brandenburg',
        'bremen',
        'hamburg',
        'hessen',
        'mecklenburg-vorpommern',
        'niedersachsen',
        'nordrhein-westfalen',
        'rheinland-pfalz',
        'saarland',
        'sachsen-anhalt',
        'sachsen',
        'schleswig-holstein',
        'thueringen'
    },
)


if __name__ == "__main__":
    # Parsing arguments (if any)
    args = parser.parse_args()

    # Loading URLs from JSON
    base_urls = []

    with open('states.json', 'r') as file:
        data = json.load(file)
        for state, url in data.items():
            base_urls.append([state, url])

    # Fetching data, storing as JSON
    for state, base_url in base_urls:
        # (1) Check if states are provided
        # (2)
        if len(args.states) is not False and state not in args.states:
            continue

        file = 'libraries/' + state + '.json'

        if os.path.isfile(file) is False:
            with open(file, 'w') as file:
                library_urls = fetch(base_url)
                libraries = []

                for library_url in library_urls:
                    library = parse(library_url)
                    libraries.append(library)

                json.dump(libraries, file, ensure_ascii=False, indent=4)
