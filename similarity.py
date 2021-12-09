import spacy

# Run:
# python -m spacy download en_core_web_sm
# the first time you run this file


def check_similarity(cnt_1, cnt_2):

    nlp = spacy.load('en_core_web_sm')

    search_doc = nlp(cnt_1)

    main_doc = nlp(cnt_2)

    print(main_doc.similarity(search_doc))

def test():

    cnt_1 = "Cats are cute"

    cnt_2 = "I want water"

    check_similarity(cnt_1, cnt_2)
    
if __name__ == '__main__':

    test()