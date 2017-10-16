from pipenv.patched.piptools import logging
from selenium import webdriver
import logging


class ActionWithOurElements:
    super(webdriver)

    def enter_text(self, element, text):
        try:
            element.clear()
            element.send_keys(text)
            logging.info(text + " was inputted")
        except Exception:
            logging.error("Can not work with element" + element)

    def click_on_element(self, element):
        try:
            element.click()
            logging.info("Element was clicked")
        except Exception:
            logging.error("Can not work with element" + element)

    def is_element_present(self, locatorWithText):
        try:
            .find_element_by_xpath
        except Exception:
            logging.error("Can not work with element" + locatorWithText)
