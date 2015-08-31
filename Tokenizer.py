'''
How can I use our dataset in this Tokenizer?
How can I use stemming?
I tried to do but I couldn't
'''


from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
#from nltk.corpus import gutenberg
from nltk.corpus import movie_reviews


#ps = PorterStemmer()
# sample text
#sample = gutenberg.raw("bible-kjv.txt")
#sample =  movie_reviews("neg//cv000_29416.txt")
sample = "plot : two teen couples go to a church party , drink and then drive . they get into an accident . one of the guys dies , but his girlfriend continues to see him in her life , and has nightmares . what is the deal ? watch the movie and sorta  find out."

stop_words = set(stopwords.words('english'))

tok = word_tokenize(sample)

#for w in tok:
#    print(ps.stem(w))

filtered_sentence = []

for w in tok:
    if w not in stop_words:
        filtered_sentence.append(w)


print(filtered_sentence)
