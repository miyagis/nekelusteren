# https://textblob.readthedocs.io/en/dev/quickstart.html#sentiment-analysis

# if tag in ("NN", "NNS", "NNP", "NNPS"):
#     return _wordnet.NOUN
# if tag in ("JJ", "JJR", "JJS"):
#     return _wordnet.ADJ
# if tag in ("VB", "VBD", "VBG", "VBN", "VBP", "VBZ"):
#     return _wordnet.VERB
# if tag in ("RB", "RBR", "RBS"):
#     return _wordnet.ADV

# Translate to EN to apply TextBlob methods
# get sentiment and polarity
# get nouns to find the topic

from textblob import TextBlob
import csv
import re


def analyse_file(file_name):
    with open("DATA/"+file_name, 'r') as f:
        f = csv.reader(f, delimiter=';')

        for row in f:
            s = row[3]
            s = clean_text(s)
            s = TextBlob(s)
            s_en = s.translate(from_lang="nl", to="en")

            # myTags = s_en.tags

            # for t in myTags:
            #     # Nouns
            #     if t[1]in ("NN", "NNS", "NNP", "NNPS"):
            #         if len(t[0]) > 2:
            #             print(t[0])
            print(s_en)
            print(s_en.sentiment)
            print('=========================================')


def clean_text(s):
    cleaned_text = s
    cleaned_text = cleaned_text.replace('\\n', " ")
    cleaned_text = cleaned_text.replace('\\xbb', "")
    cleaned_text = cleaned_text.replace("b'", "")
    cleaned_text = cleaned_text.replace('\\xf0', "")
    cleaned_text = cleaned_text.replace('\\x9f', "")
    cleaned_text = cleaned_text.replace('\\x8c', "")
    cleaned_text = cleaned_text.replace('\\xf0', "")
    cleaned_text = cleaned_text.replace('\\x9f', "")
    cleaned_text = cleaned_text.replace('\\x8f', "")
    cleaned_text = cleaned_text.replace('\\x8a', "")
    cleaned_text = cleaned_text.replace('\\x91', "")
    cleaned_text = cleaned_text.replace('\\x92', "")
    cleaned_text = cleaned_text.replace('\\x8b', "")
    cleaned_text = cleaned_text.replace('\\x80', "")
    cleaned_text = cleaned_text.replace('\\x', "")
    cleaned_text = cleaned_text.replace('#', "")
    cleaned_text = cleaned_text.replace('@', "")
    cleaned_text = re.sub(r"http\S+", "", str(cleaned_text))  # remove links
    return cleaned_text


analyse_file('DataGatherer_20181206_11.csv')

