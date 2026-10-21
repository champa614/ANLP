import nltk
from nltk.corpus import wordnet as wn

nltk.download('wordnet')
word = input("Enter a word: ")

for s in wn.synsets(word):
    print("\nMeaning:", s.definition())
    print("Synonyms:", [l.name() for l in s.lemmas()])
