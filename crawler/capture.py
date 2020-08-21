from crawler.settings import SITES
import time


class Capture(object):

    def __init__(self, log, driver):
        self.__log = log
        self.__driver = driver
        self._sleep = 7

    def start(self):
        """
        Process to capture HTML pages from links list

        """
        try:
            for url in SITES:
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

                self.__save_file(url=url, html=html)
                self.__log.info('Getting next site...')

            self.__driver.quit()
            self.__log.info('End')

        except Exception as exc:
            self.__log.error("An error ocurred while crawling: {}".format(str(exc)))
            raise

    def __save_file(self, url, html):
        """
        Save a file with HTML content

        :param url: Site link used to capture
        :param html: HTML code of page

        """
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
        """
        :param url: Site link used to capture
        :return: A file name based on link

        """
        filename = url.split("//")[1]
        return filename


if __name__ == '__main__':
    help(Capture.start)