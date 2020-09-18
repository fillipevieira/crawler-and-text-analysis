import nltk


class Tokenization(object):

    def __init__(self):
        """
        punkt is a tokenization model for nlkt
        """
        nltk.download('punkt')

    @staticmethod
    def __get_content():
        """
        Return content of noise free text
        """
        with open("noise-free-text.txt", "r") as f:
            text = f.read()
        return text

    @staticmethod
    def __tokenize(content):
        """
        Return list of words (tokenized content)
        """
        result = nltk.word_tokenize(content)
        return result

    @staticmethod
    def __save_file(wordlist):
        """
        Save tokenized content.
        """
        with open('tokenized-text.txt', 'w') as file:
            file.writelines("{}\n".format(word) for word in wordlist)

    def start(self):
        try:
            content = self.__get_content()
            words = self.__tokenize(content=content)
            self.__save_file(wordlist=words)

        except Exception as exc:
            print('Tokenization error: {}'.format(str(exc)))
            raise
