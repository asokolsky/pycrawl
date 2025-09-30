import argparse

# from datetime import datetime
import logging
import socket

# from sys import stderr
from collections.abc import Generator
from urllib.parse import urlparse

from scrapy.crawler import CrawlerProcess
from scrapy.http import Request
from scrapy.http.response.text import TextResponse
from scrapy.spiders import Spider

# msg_format = "%(asctime)s.%(msecs)03d %(levelname)s %(threadName)s %(filename)s:%(lineno)s %(message)s"
# msg_format = "%(asctime)s.%(msecs)03d %(levelname)s %(message)s"
msg_format = '%(levelname)s: %(message)s'
date_format = '%m%d.%H%M%S'

# log_level = logging.DEBUG
# log_level = logging.INFO
log_level = logging.ERROR

# log_file_path = '/tmp/foobar.log'
log_file_path: str | None = None


def create_logger(log_file_path: str | None, log_level: int) -> logging.Logger:
    """
    Get the (root) logger object to use for logging.
    """
    logging.basicConfig(
        level=log_level, filename=log_file_path, format=msg_format, datefmt=date_format
    )
    return logging.getLogger()


log = create_logger(log_file_path, log_level)


class LinksCheckerSpider(Spider):
    """
    Custom spider invoked on every site page
    """

    name = 'links_checker'

    def __init__(
        self,
        allowed_domains: list[str] | None = None,
        start_urls: list[str] | None = None,
    ) -> None:
        super().__init__()

        # self.name = name
        if allowed_domains is None:
            self.allowed_domains = []
        else:
            self.allowed_domains = allowed_domains

        if start_urls is None:
            self.start_urls = []
        else:
            self.start_urls = start_urls

        self.parsed_urls: dict[str, bool] = {}
        self.logger.setLevel(log_level)
        return

    def parse(self, response: TextResponse) -> Generator[Request]:
        """
        Parse the response.
        """
        if response.status != 200:
            self.logger.error('parse (%d): %s', response.status, response.url)
            return

        if self.parsed_urls.get(response.url, False):
            self.logger.debug('Already parsed: %s', response.url)
            return

        self.parsed_urls[response.url] = True
        # self.logger.info("Total ad divs: %s", len(ad_divs))
        self.logger.debug('parse: %s', response.url)  # response.body
        # extract all links from page
        all_links = response.xpath('*//a/@href').extract()

        # iterate over links
        for link in all_links:
            self.logger.debug('[+] link: %s', link)
            full_link = response.urljoin(link)
            # yield Request(url=full_link, callback=self.on_request)
            try:
                yield response.follow(full_link, self.parse)
            except ValueError:
                continue
        return

    def on_request(self, response: TextResponse) -> Generator[Request]:
        """
        Request handler.
        """
        if response.status != 200:
            self.logger.error('on_request %d: %s', response.status, response.url)
            yield {'url': response.url, 'status': response.status}
        else:
            self.logger.debug('on_request: %s', response.url)
            # title = response.xpath('//title/text()').get() # get() will replace extract() in the future
            if not self.parsed_urls.get(response.url, False):
                return self.parse(response)
            else:
                yield {'url': response.url, 'status': response.status}
        return


def main() -> None:
    """
    Main entry point
    """

    def adjust_scrapy_logging() -> None:
        logs = ['scrapy', 'scrapy.crawler', 'scrapy.utils', 'scrapy.utils.log']
        for n in logs:
            logging.getLogger(n).setLevel(log_level)
        return

    def parse_args() -> tuple[int, str, str]:
        """
        Parse arguments, return (verbose, site)
        """
        parser = argparse.ArgumentParser(
            description='Crawl the site and identify broken links saving these into `site.json`.'
        )
        parser.add_argument(
            '-v',
            '--verbose',
            action='count',
            default=0,
            help='make helpful noises, combine for extra verbosity, e.g. -vvv',
        )
        parser.add_argument(
            'site', type=str, help='DNS or IP address of the site to crawl or a URL'
        )
        args = parser.parse_args()

        site = ''
        start = ''
        pr = urlparse(args.site)
        if pr.scheme:
            start = args.site
            site = pr.netloc
        else:
            site = pr.path
            start = f'http://{site}/'

        print('args', args, site, start, pr)
        return args.verbose, site, start

    verbose, site, start = parse_args()
    global log_level
    if verbose == 0:
        log_level = logging.ERROR
    elif verbose <= 1:
        log_level = logging.INFO
    else:
        log_level = logging.DEBUG

    log.setLevel(log_level)
    log.debug("Verifying DNS name '%s'", site)
    try:
        socket.gethostbyname(site)
    except Exception: # noqa: BLE001
        log.error("Failed to resolve '%s'", site) # noqa: TRY400
        return

    adjust_scrapy_logging()

    settings = {
        'USER_AGENT': 'Mozilla/5.0',
        'FEED_FORMAT': 'json',  # csv, json, xml
        'FEED_URI': f'{site}.json',
        'HTTPERROR_ALLOWED_CODES': [404],
        'LOG_LEVEL': 'ERROR',
    }
    c = CrawlerProcess(settings=settings, install_root_handler=False)

    adjust_scrapy_logging()

    c.crawl(LinksCheckerSpider, allowed_domains=[site], start_urls=[start])
    c.start()
    c.join()
    log.debug("See '%s.json' for results", site)
    return


if __name__ == '__main__':
    main()
