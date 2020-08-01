from crawler.settings import SITES
import time


class Capture(object):

    def __init__(self, log, driver):
        self.__log = log
        self.__driver = driver
        self._sleep = 5

    def start(self):
        try:
            for url in SITES:
                self.__log.info("Crawling site: {}".format(url))
                self.__driver.get(url=url)

                self.__log.info('Waiting {} secs'.format(str(self._sleep)))
                time.sleep(self._sleep)
                html = self.__driver.page_source

                self.__save_file(url=url, html=html)
                self.__log.info('Getting next site...')

            self.__driver.quit()
            self.__log.info('End')

        except Exception as exc:
            self.__log.error("An error ocurred while crawling: {}".format(str(exc)))
            raise

    def __save_file(self, url, html):
        try:
            self.__log.info("Saving file...")
            filename = self.get_file_name(url)

            with open('htmls/{}.html'.format(filename), 'w') as file:
                file.write(html)

            self.__log.info("File saved!")

        except Exception as exc:
            self.__log.error("An error ocurred while saving file: {}".format(str(exc)))
            raise

    @staticmethod
    def get_file_name(url):
        filename = url.split("//")[1]
        return filename
