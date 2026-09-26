sentence="The Eiffel Tower was built from 1887 to 1889 by French engineer Gustave Eiffel, whose company specialized in building metal frameworks and structures."
"""
Person Eg: Krish C Naik
Place Or Location Eg: India
Date Eg: September,24-09-1989
Time  Eg: 4:30pm
Money Eg: 1 million dollar
Organization Eg: iNeuron Private Limited
Percent Eg: 20%, twenty percent
"""

import nltk
words=nltk.word_tokenize(sentence)
print(words)

tag_elements=nltk.pos_tag(words)
print(tag_elements)

nltk.download('maxent_ne_chunker')
nltk.download('maxent_ne_chunker_tab')  # ← this was missing
nltk.download('words')                  # often needed too
result=nltk.ne_chunk(tag_elements).draw()
print(result)