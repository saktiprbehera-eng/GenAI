
## Q&A, chatbots, text summerization
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()
words=["writing","writes","programming","programs","history","finally","final","finalize","eating","eat","eaten"]

for word in words:
    print(word+"---->"+lemmatizer.lemmatize(word,pos="v"))


print(lemmatizer.lemmatize("goes"))

print(lemmatizer.lemmatize("fairly",pos="v"))
print(lemmatizer.lemmatize("sportingly",pos="v"))