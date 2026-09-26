import pandas as pd

messages = pd.read_csv(r'D:\Workspace\Python\Smsspamcollection.txt', header=None,
                      sep='\t', names=["label", "message"])
message1 = pd.read_csv('../Smsspamcollection.txt', header=None,
                      sep='\t', names=["label", "message"])

import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
wordlemmatize=WordNetLemmatizer()


corpus=[]
for i in range(0,len(messages)):
    review=re.sub('[^a-zA-Z]',' ',messages['message'][i])
    review=review.lower()
    review=review.split()
    review=[wordlemmatize.lemmatize(word) for word in review if not word in stopwords.words('english')]
    review=' '.join(review)
    corpus.append(review)

print(corpus)

from sklearn.feature_extraction.text import TfidfVectorizer
tfidf = TfidfVectorizer(max_features=100)
x=tfidf.fit_transform(corpus).toarray()

import numpy as np
np.set_printoptions(edgeitems=30, linewidth=100000, formatter=dict(float=lambda x: "%.3g" % x))
print(x)


# N-Grams
tfidf = TfidfVectorizer(max_features=100,ngram_range=(2,2))
x=tfidf.fit_transform(corpus).toarray()
print(tfidf.vocabulary_)
