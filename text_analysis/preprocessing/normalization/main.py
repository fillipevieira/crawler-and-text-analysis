import re
import nltk
import unicodedata
from nltk.corpus import stopwords


class Normalization(object):

    def __init__(self):
        nltk.download('stopwords')

    @staticmethod
    def __get_content():
        """
        Return content of tokenized text into list
        """
        with open("tokenized-text.txt", "r") as f:
            content = [line.rstrip('\n') for line in f]
        return content

    @staticmethod
    def __remove_non_ascii(words):
        """
        Return a words list without non-ASCII characters
        """
        words_without_non_ascii = []
        for word in words:
            new_word = unicodedata.normalize('NFKD', word).encode('ascii', 'ignore').decode('utf-8', 'ignore')
            words_without_non_ascii.append(new_word)
        return words_without_non_ascii

    @staticmethod
    def __to_lowercase(words):
        """
        Return characters to lowercase from tokenized words list
        """
        words_to_lowercase = [word.lower() for word in words]
        return words_to_lowercase

    @staticmethod
    def __remove_punctuation(words):
        """
        Return list of tokenized words with no punctuation
        """
        words_without_punctuation = []
        for word in words:
            new_word = re.sub(r'[^\w\s]', '', word)
            if new_word != '':
                words_without_punctuation.append(new_word)
        return words_without_punctuation

    @staticmethod
    def __remove_stopwords(words):
        """
        Return tokenized words list without stop words
        """
        words_without_stopwords = []
        for word in words:
            if word not in stopwords.words('english'):
                words_without_stopwords.append(word)
        return words_without_stopwords

    @staticmethod
    def __save_file(words):
        """
        Save normalized content.
        """
        with open('normalized-text.txt', 'w') as file:
            file.writelines("{}\n".format(word) for word in words)

    def start(self):
        try:
            wordlist = self.__get_content()
            words = self.__remove_non_ascii(words=wordlist)
            words = self.__to_lowercase(words=words)
            words = self.__remove_punctuation(words=words)
            words = self.__remove_stopwords(words=words)
            self.__save_file(words=words)

        except Exception as exc:
            print('Normalization error: {}'.format(str(exc)))
            raise
