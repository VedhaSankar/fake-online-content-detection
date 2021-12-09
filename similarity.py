import spacy

# Run:
# python -m spacy download en_core_web_sm
# the first time you run this file


def check_similarity(cnt_1, cnt_2):

    cnt_1 = cnt_1.lower()
    cnt_2 = cnt_2.lower()

    nlp = spacy.load('en_core_web_sm')

    search_doc = nlp(cnt_1)

    main_doc = nlp(cnt_2)

    print(main_doc.similarity(search_doc))

def test():

    cnt_1 = '''
    Amazon Elastic Compute Cloud (Amazon EC2) is a web service that provides secure, resizable compute capacity in the cloud.
    '''

    cnt_2 = '''
    Amazon Elastic Compute Cloud (Amazon EC2) provides scalable computing capacity in the Amazon Web Services (AWS) Cloud. Using Amazon EC2 eliminates your need to invest in hardware up front, so you can develop and deploy applications faster.
    '''
    
    check_similarity(cnt_1, cnt_2)
    
if __name__ == '__main__':

    test()