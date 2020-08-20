from crawler.settings import GECKODRIVER, DEBUG
from crawler.capture import Capture
from selenium import webdriver
import logging

def get_webdriver():
    try:
        logging.debug("Setting webdriver")
        driver = webdriver.Firefox(executable_path=GECKODRIVER)
        return driver

    except Exception as exc:
        logging.error("An error ocurred while webdriver handling: {}".format(str(exc)))
        raise


if __name__ == '__main__':
    try:
        print("Starting app")

        if DEBUG:
            logging.basicConfig(level=logging.DEBUG)
        else:
            logging.basicConfig(level=logging.INFO)

        driver = get_webdriver()

        crawler = Capture(log=logging, driver=driver)
        crawler.start()

    except Exception as exc:
        logging.error("Error: {}".format(str(exc)))

