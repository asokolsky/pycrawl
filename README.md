# Crawling in Python

Crawl the site, e.g. [asokolsky.github.io](https://asokolsky.github.io/),
in order to identify imperfections, such as broken links.

## Working with Virtual Environment

From [primer](https://realpython.com/python-virtual-environments-a-primer/):

* create it, if it is not there yet: `python3 -m venv venv`
* activate it `source venv/bin/activate`
* install requirements `python3 -m pip install -r requirements.txt`
* install new packages if needed...
* freeze it `python3 -m pip freeze > requirements.txt`

## Scrapy

"fast high-level web crawling and web scraping framework"

* [docs](https://docs.scrapy.org/en/latest/index.html)
* [repo](https://github.com/scrapy/scrapy)
* [intro](https://www.scrapingbee.com/blog/web-scraping-with-scrapy/)
* [simple use example](https://doc.scrapy.org/en/latest/topics/practices.html)
* [example1](https://github.com/SherMarri/scrapy-examples)
* [example2](https://www.scrapingbee.com/blog/crawling-python/#web-crawling-with-scrapy)

## Typing Verification
```console
(venv) alex@L07A97UF:/mnt/c/Users/asoko/Projects/pycrawl$ mypy .
```

## Usage

```console
alex@latitude7490:~/Projects/pycrawl/ > source venv/bin/activate
(venv) alex@latitude7490:~/Projects/pycrawl/ >

(venv) alex@latitude7490:~/Projects/pycrawl/ > python3 main.py -h
usage: main.py [-h] [-v] site

Crawl the site and identify broken links saving these into `site.json`.

positional arguments:
  site           DNS or IP address of the site to crawl

options:
  -h, --help     show this help message and exit
  -v, --verbose  make helpful noises, combine for extra verbosity, e.g. -vvv

(venv) alex@latitude7490:~/Projects/pycrawl/ > python3 main.py asokolsky.github.io
INFO: Scrapy 2.6.3 started (bot: scrapybot)
INFO: Versions: lxml 4.9.1.0, libxml2 2.9.14, cssselect 1.1.0, parsel 1.6.0, w3lib 2.0.1, Twisted 22.8.0, Python 3.10.6 (main, Aug 10 2022, 11:40:04) [GCC 11.3.0], pyOpenSSL 22.1.0 (OpenSSL 3.0.5 5 Jul 2022), cryptography 38.0.1, Platform Linux-5.15.0-50-generic-x86_64-with-glibc2.35
(venv) alex@latitude7490:~/Projects/pycrawl/ >
```
