from nltk.stem import PorterStemmer

ps = PorterStemmer()

words = ["playing", "running", "happily", "studies"]

for word in words:
    print(word, "->", ps.stem(word))
