from text_analysis.settings import HTML_TO_PREPROCESS, CREATE_TOKENIZATION_AND_NORMALIZATION
from text_analysis.preprocessing.noise_removal.main import NoiseRemoval
from text_analysis.preprocessing.tokenization.main import Tokenization
from text_analysis.preprocessing.normalization.main import Normalization

if __name__ == "__main__":
    try:
        NoiseRemoval().start(filename=HTML_TO_PREPROCESS)
        print("Noise Removal done!")
        if CREATE_TOKENIZATION_AND_NORMALIZATION:
            Tokenization().start()
            print("Tokenization done!")
            Normalization().start()
            print("Normalization done!")

    except:
        pass
