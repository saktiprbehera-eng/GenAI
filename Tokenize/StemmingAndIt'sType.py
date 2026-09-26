## PorterStemmer
from nltk.stem import PorterStemmer, snowball

words=["writing","writes","programming","programs","history","finally","final","finalize","eating","eat","eaten"]
## Porter stemming
porter_stemming=PorterStemmer()
for word in words:
    print(word+"-----"+porter_stemming.stem(word))

## Regexstemmer
from nltk.stem import RegexpStemmer
reg_stemmer=RegexpStemmer('ing$|s$|e$|able$', min=4)
print(reg_stemmer.stem('ing'))
print(reg_stemmer.stem('eating'))
print(reg_stemmer.stem('programming'))


## snowballstemmer
from nltk.stem import SnowballStemmer
snowball_stemmer=SnowballStemmer('english')
print(snowball_stemmer.stem('english'))
print(snowball_stemmer.stem('Eating'))
print(snowball_stemmer.stem('programming'))
print(snowball_stemmer.stem('programs'))

for word in words:
    print(word+"-----"+snowball_stemmer.stem(word))


## PorterStemmer
print(porter_stemming.stem("fairly"))
print(porter_stemming.stem("sportingly"))

## SnowballStemmer
print(snowball_stemmer.stem("fairly"))
print(snowball_stemmer.stem("sportingly"))

