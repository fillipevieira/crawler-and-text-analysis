from bs4 import BeautifulSoup
import contractions

# This module creates a noise-free text from HTML page

def denoise_content(html):
    """
    :param html: all content of the page.
    :return text: noise-free text

    """
    text = get_html(html=html)
    text = remove_newline(text=text)
    text = remove_contractions(text=text)
    return text

def get_html(html):
    """
    :param text: all content of the page.
    :return text with no HTML markups

    """
    soup = BeautifulSoup(html, "html.parser")
    return soup.get_text()

def remove_newline(text):
    """
    :param text: text with no HTML markups
    :return text: without newllines

    """
    text = text.replace("\n", '')
    return text

def remove_contractions(text):
    """
    :param text: text with contractions
    :return text: without contractions. Ex: can't -> can not

    """
    return contractions.fix(text)


if __name__ == '__main__':
    try:
        file_to_handle = ""  # Ex: pronounced-dead-michigan.html

        content = None
        with open('../../../htmls/'+file_to_handle, 'r') as file:
            if file.mode == 'r':
                content = file.read()

        if content:
            denoised_content = denoise_content(content)

            with open('../noise-free-text.txt', 'w') as file:
                content = file.write(denoised_content)


    except Exception as exc:
        print('Error: {}'.format(str(exc)))
