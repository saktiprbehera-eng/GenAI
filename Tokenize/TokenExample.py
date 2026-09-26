import nltk
nltk.download('punkt_tab')
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.tokenize import wordpunct_tokenize
from nltk.tokenize import TreebankWordTokenizer

corpus="""Hello Welcome to Sakti's NLP Tutorials. 
Please do watch entire course! to become expert in NLP.
"""

## Sent tokenize
documents=sent_tokenize(corpus)

print(documents)
print(type(documents))
for sentence in documents:
    print(sentence)

#word tokenize
words=word_tokenize(corpus)
print(words)

for sentence in documents:
    print(word_tokenize(sentence))

print(wordpunct_tokenize(corpus))

tokenizer=TreebankWordTokenizer().tokenize(corpus)
print(tokenizer)
