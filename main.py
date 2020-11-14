from crawler.main import Crawler
from text_analysis.preprocessing.main import Preprocessing
from settings import DEBUG, HTML_TO_PREPROCESS
import logging
import time

if __name__ == "__main__":

    if DEBUG:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)

    logging.info("------------- Starting crawler stage -------------")
    crawler = Crawler(audit=logging)
    crawler.start()
    logging.info("------------- Crawler stage is finished -------------\n")

    time.sleep(5)

    logging.info("------------- Starting preprocessing stage -------------")
    logging.info("File to preprocess: " + HTML_TO_PREPROCESS + ".html")
    preprocessing = Preprocessing(audit=logging)
    preprocessing.start()
    logging.info("Preprocessed files have been saved in preprocessed_files/" + HTML_TO_PREPROCESS + "/")
    logging.info("------------- Preprocessing stage is finished -------------\n")
