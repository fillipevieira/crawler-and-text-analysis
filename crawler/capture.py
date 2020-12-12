from settings import SITES
import time
import os


class Capture(object):

    def __init__(self, audit, driver):
        self.__audit = audit
        self.__driver = driver
        self._sites = SITES
        self._sleep = 3
        self.create_html_folder_if_not_exists()

    def start(self):
        """
        Process to capture HTML pages from links list

        """
        try:
            for filename, url in self._sites.items():
                html = None

                self.__audit.info("Crawling site: {}".format(url))
                try:
                    self.__driver.get(url=url)
                except:
                    self.__audit.error("An error ocurred while visiting website: {}. Skipping to next...".format(url))
                    continue

                self.__audit.info('Waiting {} secs'.format(str(self._sleep)))
                time.sleep(self._sleep)
                html = self.__driver.page_source

                self.__save_file(filename=filename, html=html)
                self.__audit.info('Getting next site...')

            self.__driver.quit()
            self.__audit.info('End')

        except Exception as exc:
            self.__audit.error("An error ocurred while crawling: {}".format(str(exc)))
            raise

    def __save_file(self, filename, html):
        """
        Save a file with HTML content

        :param url: Site link used to capture
        :param html: HTML code of page

        """
        try:
            self.__audit.info("Saving file...")

            with open('htmls/{}.html'.format(filename), 'w') as file:
                file.write(html)

            self.__audit.info("File saved!")

        except Exception as exc:
            self.__audit.error("An error ocurred while saving file: {}".format(str(exc)))
            raise

    @staticmethod
    def create_html_folder_if_not_exists():
        if not os.path.exists('htmls/'):
            os.makedirs('htmls/')


if __name__ == '__main__':
    help(Capture.start)
