from settings import GECKODRIVER, DEBUG
from crawler.capture import Capture
from selenium import webdriver


class Crawler(object):

    def __init__(self, audit):
        self.audit = audit

    def __get_webdriver(self):
        """
        :return: Firefox driver for capture
        """
        try:
            self.audit.debug("Setting webdriver")
            driver = webdriver.Firefox(executable_path=GECKODRIVER)
            return driver

        except Exception as exc:
            self.audit.error("An error ocurred while webdriver handling: {}".format(str(exc)))
            raise

    def start(self):
        try:
            driver = self.__get_webdriver()
            crawler = Capture(audit=self.audit, driver=driver)
            crawler.start()

        except Exception as exc:
            self.audit.error("Error: {}".format(str(exc)))

