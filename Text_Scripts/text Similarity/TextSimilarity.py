from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from scipy.spatial import distance


def finding_text_similarity_using_cosine_distance(s1, s2):

    # sentences to list
    allsentences = [s1, s2]
    # Using Count Vectorizer
    count_vectorizer = CountVectorizer()
    all_sentences_to_vector = count_vectorizer.fit_transform(allsentences)
    text_to_vector_v1 = all_sentences_to_vector.toarray()[0].tolist()
    text_to_vector_v2 = all_sentences_to_vector.toarray()[1].tolist()

    # distance of similarity
    cosine = distance.cosine(text_to_vector_v1, text_to_vector_v2)
    print('Using Count Vectorizer :Similarity of two sentences are equal to ',
          round((1 - cosine) * 100, 2), '%')

    # Using TFIDF Vectorizer
    tfidf_vectorizer = TfidfVectorizer()
    all_sentences_to_vector = tfidf_vectorizer.fit_transform(allsentences)
    text_to_vector_v1 = all_sentences_to_vector.toarray()[0].tolist()
    text_to_vector_v2 = all_sentences_to_vector.toarray()[1].tolist()

    # distance of similarity
    cosine = distance.cosine(text_to_vector_v1, text_to_vector_v2)
    print('Using TFIDF Vectorizer :Similarity of two sentences are equal to ',
          round((1 - cosine) * 100, 2), '%')


# To clean the sentences
def clean_article(article):
    import re
    art = re.sub("[^A-Za-z0-9' ]", '', str(article))
    art2 = re.sub("[( ' )(' )( ')]", ' ', str(art))
    art3 = re.sub("%s[A-Za-z]%s", ' ', str(art2))
    return art3.lower()


print("Enter the first sentence :")
s1 = input()
print("Enter the second sentence :")
s2 = input()
s1 = clean_article(s1)
s2 = clean_article(s2)
finding_text_similarity_using_cosine_distance(s1, s2)
