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

    # Creating list for holding states & respective URLs
    state_urls = []

    with open('states.json', 'r') as file:
        # Load URLs from JSON
        data = json.load(file)

        # Store them along with state names
        for state, url in data.items():
            state_urls.append([state, url])

    # Fetching data, storing as JSON
    for state, library_url in state_urls:
        # (1) Check if any states are provided via CLI
        # (2) Check if current state isn't among them
        # (3) Move on to next state if both are true
        if len(args.states) is not False and state not in args.states:
            continue

        # Build output path
        file = 'data/' + state + '.json'

        # Only (over)write files for states whose data ..
        # (1) .. doesn't exist or
        # (2) .. was aborted during execution
        if os.path.isfile(file) is False or os.path.getsize(file) == 0:
            with open(file, 'w') as file:
                # Fetch library URLs for all states
                library_urls = fetch(library_url)

                # Holds information of all libraries
                libraries = []

                # Parse each library URL, extract its data & save it
                for library_url in library_urls:
                    library = parse(library_url)
                    libraries.append(library)

                # Store data as (UTF-8 encoded) JSON file
                json.dump(libraries, file, ensure_ascii=False, indent=4)
