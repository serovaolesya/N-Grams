import spacy
from ngrams import bigram, trigram


def main():
    # load English model
    nlp = spacy.load('en_core_web_sm')
    nlp = spacy.load('ru_core_news_sm')

    # create a document
    doc = nlp("Я устала и все время хочу спать.")

    result = bigram(doc)
    result_2 = trigram(doc)

    print('Bigrams:')
    for element in result:
        for token in element:
            print(token, end=' ')
        print()  # new line

    print()  # new line

    print('Trigrams:')
    for element in result_2:
        for token in element:
            print(token, end=' ')
        print()  # new line


main()
