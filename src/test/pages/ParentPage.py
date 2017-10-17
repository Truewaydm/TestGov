from selenium import webdriver
import logging


class ParentPage:
    def __init__(self, wd):
        self.webdriver = wd

    def open_url(self, url):
        try:
            logging.info("Page was opened" + url)
        except Exception:
            logging.error("Page can not opened" + url)