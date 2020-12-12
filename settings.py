####################### SELENIUM #######################
GECKODRIVER = "/home/fillipe/TCC/geckodriver-v0.27.0-linux64/geckodriver"


####################### CRAWLING #######################
SITES = {
    'pronounced': 'https://www.mlive.com/news/2020/08/pronounced-dead-michigan-woman-found-alive-at-funeral-home.html',
    'police': 'https://www.mlive.com/news/saginaw-bay-city/2020/08/police-identify-northern-michigan-woman-whose-burned-body-was-found-in-bay-county.html',
    'pirates': 'https://www.mlive.com/tigers/2020/08/pirates-claim-former-tigers-pitcher-off-waivers.html',
    'tigers':  'https://www.mlive.com/tigers/2020/08/tigers-cubs-lineup-schoop-returns-candelario-remains-in-the-clean-up-spot.html',
    'liveboot': 'https://www.technewsworld.com/story/86918.html',
    'ibm': 'https://www.technewsworld.com/story/86911.html'
}


####################### PREPROCESSING #######################
CREATE_TOKENIZATION_AND_NORMALIZATION = True
WORD_TOKENIZE = True


####################### TESTS #######################
DEBUG = False