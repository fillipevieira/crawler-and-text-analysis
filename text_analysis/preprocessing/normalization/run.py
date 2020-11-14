from settings import WORD_TOKENIZE, HTML_TO_PREPROCESS
import re
import nltk
import unicodedata
from nltk.corpus import stopwords


class Normalization(object):

    def __init__(self, audit):
        nltk.download('stopwords')
        self.__audit = audit

    @staticmethod
    def __get_content():
        """
        Return content of tokenized text into list
        """
        with open('preprocessed_files/' + HTML_TO_PREPROCESS + '/tokenized-text.txt', 'r') as f:
            content = [line.rstrip('\n') for line in f]
        return content

    @staticmethod
    def __remove_non_ascii(contents):
        """
        Return a words list without non-ASCII characters
        """
        contents_without_non_ascii = []
        for content in contents:
            new_word = unicodedata.normalize('NFKD', content).encode('ascii', 'ignore').decode('utf-8', 'ignore').strip()
            contents_without_non_ascii.append(new_word)
        return contents_without_non_ascii

    @staticmethod
    def __to_lowercase(contents):
        """
        Return characters to lowercase from tokenized words list
        """
        contents_to_lowercase = [content.lower() for content in contents]
        return contents_to_lowercase

    @staticmethod
    def __remove_special_character(contents):
        """
        Return list of tokenized words with no special character
        """
        contents_without_punctuation = []
        for content in contents:
            new_word = re.sub(r'[^\w\s]', '', content)
            if new_word != '':
                contents_without_punctuation.append(new_word)
        return contents_without_punctuation

    @staticmethod
    def __remove_stopwords(contents):
        """
        Return tokenized words list without stop words
        """
        if WORD_TOKENIZE:
            contents_without_stopwords = []
            for content in contents:
                if content not in stopwords.words('english'):
                    contents_without_stopwords.append(content)
            return contents_without_stopwords
        else:
            for key, value in enumerate(contents):
                tokenized_sentence_list = value.split(' ')
                aux = ''
                for word in tokenized_sentence_list:
                    if word not in stopwords.words('english'):
                        aux = aux + word + ' '
                contents[key] = aux.rstrip()

            return contents

    @staticmethod
    def __save_file(contents):
        """
        Save normalized content.
        """
        with open('preprocessed_files/' + HTML_TO_PREPROCESS + '/normalized-text.txt', 'w') as file:
            file.writelines("{}\n".format(content) for content in contents)

    def start(self):
        try:
            contents = self.__get_content()
            contents = self.__remove_non_ascii(contents=contents)
            contents = self.__to_lowercase(contents=contents)
            contents = self.__remove_special_character(contents=contents)
            contents = self.__remove_stopwords(contents=contents)
            self.__save_file(contents=contents)

        except Exception as exc:
            self.__audit.error('Normalization error: {}'.format(str(exc)))
            raise
