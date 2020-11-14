from settings import HTML_TO_PREPROCESS, CREATE_TOKENIZATION_AND_NORMALIZATION
from text_analysis.preprocessing.noise_removal.run import NoiseRemoval
from text_analysis.preprocessing.tokenization.run import Tokenization
from text_analysis.preprocessing.normalization.run import Normalization
import os


class Preprocessing(object):

    def __init__(self, audit):
        self.audit = audit
        self.create_preprocessed_folder_if_not_exists()

    @staticmethod
    def create_preprocessed_folder_if_not_exists():
        if not os.path.exists('preprocessed_files/' + HTML_TO_PREPROCESS):
            os.makedirs('preprocessed_files/' + HTML_TO_PREPROCESS)

    def start(self):
        try:
            NoiseRemoval(audit=self.audit).start(filename=HTML_TO_PREPROCESS)
            self.audit.info("Noise Removal done!")
            if CREATE_TOKENIZATION_AND_NORMALIZATION:
                Tokenization(audit=self.audit).start()
                self.audit.info("Tokenization done!")
                Normalization(audit=self.audit).start()
                self.audit.info("Normalization done!")

        except:
            pass
