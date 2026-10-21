import spacy
nlp = spacy.load("en_core_web_sm")

text = input("Enter a paragraph: ")
doc = nlp(text)

print("\nWord\tPOS Tag")
for t in doc:
    print(t.text, "\t", t.pos_)

print("\nNamed Entities:")
for e in doc.ents:
    print(e.text, "-", e.label_)
