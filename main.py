from crawler.main import Crawler
from text_analysis.preprocessing.main import Preprocessing
from settings import DEBUG
import logging
import sys
import os

def help():
    print("\n")
    print("Argumentos válidos:")
    print("- crawler: executa web crawler")
    print("- list: realiza a listagem de todos os htmls salvos pelo web crawler")
    print("- preprocessing <filename_to_preprocess>: executa a rotina de pré-processamento para o arquivo html citado")
    print("- help: exibe argumentos válidos da aplicação")
    print("\n")


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG) if DEBUG else logging.basicConfig(level=logging.INFO)

    if len(sys.argv) < 2:
        logging.error("Missing arguments.")
    elif sys.argv[1] == "help":
        help()
    elif sys.argv[1] == "list":
        print("\n")
        logging.info("############ CAPTURED PAGES ############")
        for file in os.listdir('htmls'):
            print(file)
        print("\n")
    elif sys.argv[1] == "crawler":
        logging.info("------------- Starting crawler stage -------------")
        crawler = Crawler(audit=logging)
        crawler.start()
        logging.info("------------- Crawler stage is finished -------------")
    elif sys.argv[1] == "preprocessing":
        if len(sys.argv) < 3:
            logging.error("Missing filename to preprocess.")
        else:
            logging.info("------------- Starting preprocessing stage -------------")
            logging.info("File to preprocess: " + sys.argv[2])
            preprocessing = Preprocessing(audit=logging, file=sys.argv[2].replace(".html", ''))
            preprocessing.start()
            logging.info("Preprocessed files have been saved in preprocessed_files/" + sys.argv[2].replace(".html", '') + "/")
            logging.info("------------- Preprocessing stage is finished -------------")
    else:
        logging.error("Argument is not valid.")
