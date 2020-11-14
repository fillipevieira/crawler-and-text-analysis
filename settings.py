####################### SELENIUM #######################
GECKODRIVER = ""


####################### CRAWLING #######################
SITES = {'pronounced-dead-michigan': 'https://www.mlive.com/news/2020/08/pronounced-dead-michigan-woman-found-alive-at-funeral-home.html',
         'police-identify-northern': 'https://www.mlive.com/news/saginaw-bay-city/2020/08/police-identify-northern-michigan-woman-whose-burned-body-was-found-in-bay-county.html',
         'pirates-claim-former': 'https://www.mlive.com/tigers/2020/08/pirates-claim-former-tigers-pitcher-off-waivers.html',
         'tigers-cubs-lineup':  'https://www.mlive.com/tigers/2020/08/tigers-cubs-lineup-schoop-returns-candelario-remains-in-the-clean-up-spot.html'}


####################### PREPROCESSING #######################
HTML_TO_PREPROCESS = "pronounced-dead-michigan"
CREATE_TOKENIZATION_AND_NORMALIZATION = True
WORD_TOKENIZE = True


####################### TESTS #######################
DEBUG = False