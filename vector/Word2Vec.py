import gensim
from gensim.models import Word2Vec, keyedvectors
import gensim.downloader as api
wv=api.load('word2vec-google-news-300')
vec_king=wv['king']
print(vec_king)
print(vec_king.shape)
print(wv['cricket'])
print(wv.most_similar('cricket'))
print(wv.most_similar('happy'))
print(wv.most_similar())