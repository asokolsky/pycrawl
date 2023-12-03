# Crawling in Python

Crawl the site, e.g. [asokolsky.github.io](https://asokolsky.github.io/),
in order to identify imperfections, such as broken links.

## Working with Virtual Environment

From [primer](https://realpython.com/python-virtual-environments-a-primer/):

* create it, if it is not there yet: `python3 -m venv .venv`
or just `make venv`
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

TLDR:

```sh
make run SITE=asokolsky.github.io
```

OR:

* create the venv: `make venv`
* activate the venv: `source .venv/bin/activate`
* use it:
```sh
python3 main.py -h
```
or:
```sh
python3 main.py -vv asokolsky.github.io
```
