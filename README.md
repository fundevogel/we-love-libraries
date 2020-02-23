# We love libraries!
This library provides an easy way to generate lists of *german libraries* by scraping the website of the [German Library Association](https://www.bibliotheksverband.de/metamenue/english.html).

## Getting started
Depending on your setup you might prefer a ..

### Local installation via `virtualenv`
Running `setup.sh` will install all dependencies inside a virtual environment, ready for action.

### Global installation via `requirements.txt`
It's as easy as `pip install -r requirements.txt`, but you might want to make sure that Python v3 is installed on your system.

## Usage
Generating datasets is really straightforward:

```bash
$ python main.py
```

This will generate `json` files for all [german states](https://en.wikipedia.org/wiki/States_of_Germany) under `libraries/`.

**Happy coding!**


:copyright: Fundevogel Kinder- und Jugendbuchhandlung
