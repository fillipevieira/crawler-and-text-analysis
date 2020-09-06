import nltk

def download_model(pack):
    """
    :param pack: nltk package name to download
    """
    nltk.download(pack)

def get_content():
    """
    :return text: content of noise free text
    """
    with open("../noise-free-text.txt", "r") as f:
        text = f.read()
    return text

def tokenize(content):
    """
    :param content: text to tokenize
    :return result: list of words (tokenized content)
    """
    result = nltk.word_tokenize(content)
    return result

def save_file(wordlist):
    """
    :param wordlist: list of words (tokenized content)

    Save tokenized content.
    """
    with open('../tokenized-text.txt', 'w') as file:
        file.writelines("{}\n".format(word) for word in wordlist)


if __name__ == '__main__':
    try:
        download_model(pack='punkt')  # punkt is a tokenization model for nlkt
        content = get_content()
        words = tokenize(content=content)
        save_file(wordlist=words)

    except Exception as exc:
        print('Error: {}'.format(str(exc)))
