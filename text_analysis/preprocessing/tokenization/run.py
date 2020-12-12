from settings import WORD_TOKENIZE
import nltk


class Tokenization(object):

    def __init__(self, audit, input_file):
        """
        punkt is a tokenization model for nlkt
        """
        nltk.download('punkt')
        self.__audit = audit
        self.input_file = input_file

    def __get_content(self):
        """
        Return content of noise free text
        """
        with open('preprocessed_files/' + self.input_file + '/noise-free-text.txt', 'r') as f:
            text = f.read()
        return text

    @staticmethod
    def __tokenize(content):
        """
        Return list of words or sentence (tokenized content)
        """
        result = nltk.word_tokenize(content) if WORD_TOKENIZE else nltk.sent_tokenize(content)
        return result

    def __save_file(self, wordlist):
        """
        Save tokenized content.
        """
        with open('preprocessed_files/' + self.input_file + '/tokenized-text.txt', 'w') as file:
            file.writelines("{}\n".format(word) for word in wordlist)

    def start(self):
        try:
            content = self.__get_content()
            tokenized_content = self.__tokenize(content=content)
            self.__save_file(wordlist=tokenized_content)

        except Exception as exc:
            self.__audit.error('Tokenization error: {}'.format(str(exc)))
            raise
