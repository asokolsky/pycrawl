# Crawling in Python

Crawl the site, e.g. [asokolsky.github.io](https://asokolsky.github.io/),
in order to identify imperfections, such as broken links.

## Working with Virtual Environment

From [primer](https://realpython.com/python-virtual-environments-a-primer/):

* create it `python3 -m venv venv`
* activate it `source venv/bin/activate`
* install requirements `python3 -m pip install -r requirements.txt`
* install new packages...
* freeze it `python3 -m pip freeze > requirements.txt`

## Scrapy

"fast high-level web crawling and web scraping framework"

* [docs](https://docs.scrapy.org/en/latest/index.html)
* [repo](https://github.com/scrapy/scrapy)
* [intro](https://www.scrapingbee.com/blog/web-scraping-with-scrapy/)
* [example](https://www.scrapingbee.com/blog/crawling-python/#web-crawling-with-scrapy)
* [another example](https://github.com/SherMarri/scrapy-examples)

```
(venv) alex@latitude7490:~/Projects/pycrawl/ > scrapy -h
Scrapy 2.6.3 - no active project

Usage:
  scrapy <command> [options] [args]

Available commands:
  bench         Run quick benchmark test
  commands
  fetch         Fetch a URL using the Scrapy downloader
  genspider     Generate new spider using pre-defined templates
  runspider     Run a self-contained spider (without creating a project)
  settings      Get settings values
  shell         Interactive scraping console
  startproject  Create new project
  version       Print Scrapy version
  view          Open URL in browser, as seen by Scrapy

  [ more ]      More commands available when run from project directory

Use "scrapy <command> -h" to see more info about a command

(venv) alex@latitude7490:~/Projects/pycrawl/ > scrapy startproject -h
Usage
=====
  scrapy startproject <project_name> [project_dir]

Create new project

Options
=======
  -h, --help            show this help message and exit

Global Options
--------------
  --logfile FILE        log file. if omitted stderr will be used
  -L LEVEL, --loglevel LEVEL
                        log level (default: DEBUG)
  --nolog               disable logging completely
  --profile FILE        write python cProfile stats to FILE
  --pidfile FILE        write process ID to FILE
  -s NAME=VALUE, --set NAME=VALUE
                        set/override setting (may be repeated)
  --pdb                 enable pdb on failure
(venv) alex@latitude7490:~/Projects/pycrawl/ >
```

Start crawl
```
(venv) alex@latitude7490:~/Projects/pycrawl/ > scrapy startproject crawl
New Scrapy project 'crawl', using template directory '/home/alex/Projects/pycrawl/venv/lib/python3.10/site-packages/scrapy/templates/project', created in:
    /home/alex/Projects/pycrawl/crawl

You can start your first spider with:
    cd crawl
    scrapy genspider example example.com
```
