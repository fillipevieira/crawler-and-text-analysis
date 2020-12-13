from crawler.main import Crawler
from text_analysis.preprocessing.main import Preprocessing
from text_analysis.algorithms.brute_force.run import BruteForce
from text_analysis.algorithms.rabin_karp.run import RabinKarp
from settings import DEBUG
import logging
import sys
import os

def help():
    print("\n")
    print("----------------------------------------------------------------------------------------------")
    print("Argumentos para execução do WEB CRAWLER:")
    print("- crawler: executa web crawler")
    print("- list-htmls: realiza a listagem de todos os htmls salvos pelo web crawler")
    print("\n")
    print("Argumentos para execução do PREPROCESSING:")
    print("- preprocessing <filename_to_preprocess>: executa a rotina de pré-processamento para o arquivo html citado")
    print("- list-preprocessed-htmls: realiza a listagem de todos os htmls preprocessados")
    print("\n")
    print("Argumentos para execução do ANALYZE:")
    print("- brute-force-analyze <preprocessed_html_1> <preprocessed_html_2>: executa o algoritmo Brute Force entre os htmls citados")
    print("- rabin-karp-analyze <preprocessed_html_1> <preprocessed_html_2>: executa o algoritmo Rabin-Karp entre os htmls citados")
    print("\n")
    print("Other commands:")
    print("- help: exibe argumentos válidos da aplicação")
    print("----------------------------------------------------------------------------------------------")
    print("\n")


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG) if DEBUG else logging.basicConfig(level=logging.INFO)

    if len(sys.argv) < 2:
        logging.error("Missing arguments.")
    elif sys.argv[1] == "help":
        help()
    elif sys.argv[1] == "list-htmls":
        print("\n")
        print("############ CAPTURED PAGES ############")
        for file in os.listdir('htmls'):
            print(file)
        print("\n")
    elif sys.argv[1] == "list-preprocessed-htmls":
        print("\n")
        print("############ PREPROCESSED HTMLS ############")
        for file in os.listdir('preprocessed_files'):
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
    elif sys.argv[1] == "brute-force-analyze":
        if len(sys.argv) < 3:
            logging.error("Missing preprocessed html to analyze.")
        else:
            logging.info("------------- Starting Brute Force analysis stage -------------")
            html_1 = sys.argv[2]
            html_2 = sys.argv[3]
            logging.info("Files to analyse: {} | {}".format(html_1, html_2))
            BruteForce().start(html_1=html_1, html_2=html_2)
            logging.info("------------- Brute Force analysis stage is finished -------------")
    elif sys.argv[1] == "rabin-karp-analyze":
        if len(sys.argv) < 3:
            logging.error("Missing preprocessed html to analyze.")
        else:
            logging.info("------------- Starting Rabin-Karp analysis stage -------------")
            html_1 = sys.argv[2]
            html_2 = sys.argv[3]
            logging.info("Files to analyse: {} | {}".format(html_1, html_2))
            RabinKarp().start(html_1=html_1, html_2=html_2)
            logging.info("------------- Rabin-Karp analysis stage is finished -------------")
    else:
        logging.error("Argument is not valid.")
