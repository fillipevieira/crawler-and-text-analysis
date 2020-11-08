from bs4 import BeautifulSoup
import contractions


class NoiseRemoval(object):

    def __init__(self):
        self.__content = None
        self.__denoised_content = None

    def __denoise_content(self, html):
        """
        Return noise-free text
        """
        text = self.__get_html(html=html)
        text = self.__remove_newline(text=text)
        text = self.__remove_contractions(text=text)
        return text

    @staticmethod
    def __get_html(html):
        """
        Return text with no HTML markups
        """
        soup = BeautifulSoup(html, "html.parser")
        return soup.get_text()

    @staticmethod
    def __remove_newline(text):
        """
        Return text without newllines
        """
        text = text.replace("\n", '').strip()
        return text

    @staticmethod
    def __remove_contractions(text):
        """
        Return text without contractions. Ex: can't -> can not
        """
        return contractions.fix(text)

    def start(self, filename):
        try:
            with open('../../htmls/' + filename, 'r') as file:
                if file.mode == 'r':
                    self.__content = file.read()

            if self.__content:
                self.__denoised_content = self.__denoise_content(html=self.__content)

                with open('noise-free-text.txt', 'w') as file:
                    file.write(self.__denoised_content)

        except Exception as exc:
            print('Noise Removal error: {}'.format(str(exc)))
            raise
