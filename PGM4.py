from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation

n = int(input("Enter number of documents: "))
docs = [input(f"Document {i+1}: ") for i in range(n)]

v = CountVectorizer(stop_words="english")
X = v.fit_transform(docs)
lda = LatentDirichletAllocation(n_components=2, random_state=0)
lda.fit(X)
words = v.get_feature_names_out()

for i, topic in enumerate(lda.components_):
    print("Topic", i+1, ":",
          [words[j] for j in topic.argsort()[-5:][::-1]])
