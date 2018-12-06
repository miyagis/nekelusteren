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


s = TextBlob("Stevige toespraak van @SecPompeo over multilateralisme en de rol van de States in de wereld. Duidelijke steun voor de NAVO.")
#s = TextBlob("'Ik ben het kotsbeu dat er jaar na jaar een armoederapport wordt opgesteld, waar vervolgens niets mee gebeurt. Onze oppositie zal sociaal én hard zijn' @peter_mertens bij de voorstelling van de nieuwe fractie @pvda_antwerpen #gemra")

s_en = s.translate(from_lang="nl", to="en")

myTags = s_en.tags

for t in myTags:
    # Nouns
    if t[1]in ("NN", "NNS", "NNP", "NNPS"):
        if len(t[0]) > 2:
            print(t[0])
print(s_en)
print(s_en.sentiment)