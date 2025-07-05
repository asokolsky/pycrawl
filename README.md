# Crawling in Python

Crawl the site, e.g. [asokolsky.github.io](https://asokolsky.github.io/), in order to identify imperfections, such as broken links.

## Scrapy

"fast high-level web crawling and web scraping framework"

* [docs](https://docs.scrapy.org/en/latest/index.html)
* [repo](https://github.com/scrapy/scrapy)
* [intro](https://www.scrapingbee.com/blog/web-scraping-with-scrapy/)
* [simple use example](https://doc.scrapy.org/en/latest/topics/practices.html)
* [example1](https://github.com/SherMarri/scrapy-examples)
* [example2](https://www.scrapingbee.com/blog/crawling-python/#web-crawling-with-scrapy)

## Usage

TLDR:

```sh
make run SITE=asokolsky.github.io
```

OR:

```sh
uv run main.py -h
```
or:
```sh
uv run main.py -vv asokolsky.github.io
```

## Typing Verification
```console
make mypy
```

## Docker-izing the app

Added [Dockerfile](Dockerfile) - see:

* the [Dockerfile reference](https://docs.docker.com/engine/reference/builder/)
* [Python image](https://hub.docker.com/_/python)
* [sample uv Dockerfile](https://github.com/astral-sh/uv-docker-example/blob/main/Dockerfile)

### Build a pycrawl docker image

```sh
make build
```

Then publish it:
```sh
make release
```

### Using it

```sh
docker run asokolsky/pycrawl -v "asokolsky.github.io"
```
