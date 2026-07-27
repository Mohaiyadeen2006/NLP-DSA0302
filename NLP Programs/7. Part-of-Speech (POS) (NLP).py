import nltk

sentence = "The cat is sleeping on the mat"

words = nltk.word_tokenize(sentence)

tags = nltk.pos_tag(words)

print(tags)
