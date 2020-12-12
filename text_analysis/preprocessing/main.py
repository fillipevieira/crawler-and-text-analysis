from settings import CREATE_TOKENIZATION_AND_NORMALIZATION
from text_analysis.preprocessing.noise_removal.run import NoiseRemoval
from text_analysis.preprocessing.tokenization.run import Tokenization
from text_analysis.preprocessing.normalization.run import Normalization
import os


class Preprocessing(object):

    def __init__(self, audit, file):
        self.audit = audit
        self.file = file
        self.create_preprocessed_folder_if_not_exists()

    def create_preprocessed_folder_if_not_exists(self):
        if not os.path.exists('preprocessed_files/' + self.file):
            os.makedirs('preprocessed_files/' + self.file)

    def start(self):
        try:
            NoiseRemoval(audit=self.audit, input_file=self.file).start()
            self.audit.info("Noise Removal done!")
            if CREATE_TOKENIZATION_AND_NORMALIZATION:
                Tokenization(audit=self.audit, input_file=self.file).start()
                self.audit.info("Tokenization done!")
                Normalization(audit=self.audit, input_file=self.file).start()
                self.audit.info("Normalization done!")

        except:
            pass
