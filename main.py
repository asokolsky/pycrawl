import argparse
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.http import Request
from scrapy.http.response.text import TextResponse
from typing import List, Optional, Generator
from datetime import datetime
import logging
import os
import socket
from sys import stderr

#msg_format = "%(asctime)s.%(msecs)03d %(levelname)s %(threadName)s %(filename)s:%(lineno)s %(message)s"
#msg_format = "%(asctime)s.%(msecs)03d %(levelname)s %(message)s"
msg_format = "%(levelname)s: %(message)s"
date_format = '%m%d.%H%M%S'

#log_level = logging.DEBUG
#log_level = logging.INFO
log_level = logging.ERROR

#log_file_path = '/tmp/foobar.log'
log_file_path = None

def create_logger( log_file_path: Optional[str], log_level:int ) -> logging.Logger:
    '''
    Get the logger object to use for logging.
    '''
    logging.basicConfig(
        level=log_level,
        filename=log_file_path,
        format=msg_format, datefmt=date_format )
    log = logging.getLogger()

    return log

log = create_logger( log_file_path, log_level )

#def get_logger() -> logging.Logger:
#    return log

class LinksCheckerSpider(scrapy.Spider):

    name = 'links_checker'

    def __init__(self, allowed_domains: Optional[List[str]]=None,
            start_urls: Optional[List[str]]=None) -> None:
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

        self.logger.setLevel(log_level)
        return

    def parse(self, response: TextResponse) -> Generator:
        '''
        '''
        if response.status != 200:
            self.logger.error('Broken: %s', response.url)
            return

        #self.logger.info("Total ad divs: %s", len(ad_divs))
        self.logger.debug('parse: %s', response.url) #response.body
        # extract all links from page
        all_links = response.xpath('*//a/@href').extract()

        # iterate over links
        for link in all_links:
            self.logger.debug('[+] link: %s', link)
            full_link = response.urljoin(link)
            yield Request(url=full_link, callback=self.on_request)
        return

    def on_request(self, response: TextResponse) -> Generator:
        if response.status != 200:
            self.logger.error('on_request %d: %s', response.status, response.url)
            yield {'url': response.url, 'status': response.status}
        else:
            self.logger.debug('on_request: %s', response.url)
            #title = response.xpath('//title/text()').get() # get() will replace extract() in the future
        return

def main() -> None:
    parser = argparse.ArgumentParser(
        usage="%(prog)s [OPTIONS] site",
        description="Crawl the site and identify broken links saving these into `site.json`.")
    parser.add_argument('-v', '--verbose', action='count', default=0,
        help='make helpful noises, combine for extra verbosity, -vv')
    parser.add_argument('site', type=str,
        help='DNS or IP address of the site to crawl')

    args = parser.parse_args()
    print('args', args)
    site = args.site
    verbose = args.verbose

    global log_level
    if verbose == 0:
        log_level = logging.ERROR
    elif verbose <= 1:
        log_level = logging.INFO
    else:
        log_level = logging.DEBUG
    global log
    log = create_logger( log_file_path, log_level )

    log.debug("Verifying DNS name '%s'", site)
    try:
        socket.gethostbyname(site)
    except Exception:
        log.error("Faied to resolve '%s'", site)
        return

    settings = {
        'USER_AGENT': 'Mozilla/5.0',
        'FEED_FORMAT': 'json',     # csv, json, xml
        'FEED_URI': f'{site}.json',
        'HTTPERROR_ALLOWED_CODES': [404],
        'LOG_LEVEL': 'ERROR'
    }
    logs = ["scrapy", "scrapy.crawler", "scrapy.utils", "scrapy.utils.log"]
    for n in logs:
        logging.getLogger(n).setLevel(log_level)

    c = CrawlerProcess(settings, install_root_handler=False)

    #for n in logs:
    #    logging.getLogger(n).setLevel(log_level)

    c.crawl(LinksCheckerSpider, allowed_domains=[site],
        start_urls=[ f'http://{site}/'])
    c.start()
    c.join()
    log.debug("See '%s.json' for results", site)
    return

if __name__ == "__main__":
    main()
