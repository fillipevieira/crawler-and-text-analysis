from bs4 import BeautifulSoup

# This module creates a noise-free text from HTML page

def denoise_content(text):
    """
    :param
        text: all content of the page.

    :return:
        noise-free text
    """
    text = get_html(text)
    text = remove_trailing_newline(text)
    return text

def get_html(text):
    """
    :param
        text: all content of the page.

    :return:
        text with no HTML markups
    """
    soup = BeautifulSoup(text, "html.parser")
    return soup.get_text()

def remove_trailing_newline(text):
    """
    :param
        text: text with no HTML markups

    :return:
        text without newllines
    """
    text = text.replace("\n", '')
    return text


if __name__ == '__main__':
    try:
        file_to_handle = "../../htmls/www.r7.com.html"

        content = None
        with open(file_to_handle, 'r') as file:
            if file.mode == 'r':
                content = file.read()

        if content:
            denoised_content = denoise_content(content)

            with open('preprocessed.txt', 'w') as file:
                content = file.write(denoised_content)


    except Exception as exc:
        print('Error: {}'.format(str(exc)))
