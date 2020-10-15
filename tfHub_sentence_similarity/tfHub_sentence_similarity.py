import re
import string
import tensorflow_hub as hub
from scipy.spatial.distance import cdist

module_url = "https://tfhub.dev/google/universal-sentence-encoder/4"


class SimilarityModel():
    def __init__(self):
        print("Loading model from tf hub...")
        self.model = hub.load(module_url)
        print("module %s loaded" % module_url)

    def process_text(self, text):
        '''Clean text by removing unnecessary characters and altering the format of words.'''
        re_print = re.compile('[^%s]' % re.escape(string.printable))
        text = text.lower()

        text = re.sub(r"i'm", "i am", text)
        text = re.sub(r"he's", "he is", text)
        text = re.sub(r"she's", "she is", text)
        text = re.sub(r"it's", "it is", text)
        text = re.sub(r"that's", "that is", text)
        text = re.sub(r"what's", "that is", text)
        text = re.sub(r"where's", "where is", text)
        text = re.sub(r"how's", "how is", text)
        text = re.sub(r"\'ll", " will", text)
        text = re.sub(r"\'ve", " have", text)
        text = re.sub(r"\'re", " are", text)
        text = re.sub(r"\'d", " would", text)
        text = re.sub(r"\'re", " are", text)
        text = re.sub(r"won't", "will not", text)
        text = re.sub(r"can't", "cannot", text)
        text = re.sub(r"n't", " not", text)
        text = re.sub(r"n'", "ng", text)
        text = re.sub(r"'bout", "about", text)
        text = re.sub(r"'til", "until", text)
        text = re.sub(r"[$-()\"#/@;:<>{}`+=~|.!?,'*-^]", "", text)

        text = text.split()
        text = [re_print.sub('', w) for w in text]
        return ' '.join(text)

    def similarity(self, sentence1, sentence2):
        processed_sent1 = self.process_text(sentence1)
        processed_sent2 = self.process_text(sentence2)
        sent_vector1 = self.model([processed_sent1])
        sent_vector2 = self.model([processed_sent2])
        similarities = cdist(sent_vector1, sent_vector2, metric='cosine')
        return similarities


if __name__ == "__main__":
    sim_model = SimilarityModel()
    sentence1 = "Hi there"
    sentence2 = "I want money"
    distance = sim_model.similarity(sentence1, sentence2)
    print("Similarity score is: ", 1 - distance[0][0])
