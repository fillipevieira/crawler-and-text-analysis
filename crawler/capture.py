from crawler.settings import SITES
import time


class Capture(object):

    def __init__(self, log, driver):
        self.__log = log
        self.__driver = driver
        self._sites = SITES
        self._sleep = 7

    def start(self):
        """
        Process to capture HTML pages from links list

        """
        try:
            for filename, url in self._sites.items():
                html = None

                self.__log.info("Crawling site: {}".format(url))
                try:
                    self.__driver.get(url=url)
                except:
                    self.__log.error("An error ocurred while visiting website: {}. Skipping to next..."
                                     .format(url))
                    continue

                self.__log.info('Waiting {} secs'.format(str(self._sleep)))
                time.sleep(self._sleep)
                html = self.__driver.page_source

                self.__save_file(filename=filename, html=html)
                self.__log.info('Getting next site...')

            self.__driver.quit()
            self.__log.info('End')

        except Exception as exc:
            self.__log.error("An error ocurred while crawling: {}".format(str(exc)))
            raise

    def __save_file(self, filename, html):
        """
        Save a file with HTML content

        :param url: Site link used to capture
        :param html: HTML code of page

        """
        try:
            self.__log.info("Saving file...")

            with open('htmls/{}.html'.format(filename), 'w') as file:
                file.write(html)

            self.__log.info("File saved!")

        except Exception as exc:
            self.__log.error("An error ocurred while saving file: {}".format(str(exc)))
            raise


if __name__ == '__main__':
    help(Capture.start)