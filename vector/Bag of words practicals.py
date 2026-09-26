import pandas as pd

messages = pd.read_csv(r'D:\Workspace\Python\Smsspamcollection.txt', header=None,
                      sep='\t', names=["label", "message"])
message1 = pd.read_csv('../Smsspamcollection.txt', header=None,
                      sep='\t', names=["label", "message"])
print(messages)
print(message1)

import re
import nltk
# nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
ps=PorterStemmer()

corpus=[]
for i in range(0,len(messages)):
    review=re.sub('[^a-zA-Z]',' ',messages['message'][i])
    review=review.lower()
    review=review.split()
    review=[ps.stem(word) for word in review if not word in stopwords.words('english')]
    review=' '.join(review)
    corpus.append(review)

print(corpus)

## Create the Bag of Words model
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(binary=True,max_features=2500)
x=cv.fit_transform(corpus).toarray()
print(x)
print(x.shape)

## for Binary BOW enable max_feature
cv=CountVectorizer(max_features=200,binary=True,ngram_range=(1,1))
x=cv.fit_transform(corpus).toarray()
print(x)