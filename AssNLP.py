import nltk
a = "Google is the site where you can find the best tutorials for Software Testing Tutorial, SAP "
words = nltk.tokenize.word_tokenize(a)
fd = nltk.FreqDist(words)
fd.plot()
import nltk
text = "Google is a totally new kind of learning experience."
Tokens = nltk.word_tokenize(text)
output = list(nltk.bigrams(Tokens))
print(output)
from nltk.stem import PorterStemmer
e_words= ["wait", "waiting", "waited", "waits"]
ps =PorterStemmer()
for w in e_words:
 rootWord=ps.stem(w)
 print(rootWord)