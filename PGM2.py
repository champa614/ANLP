from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

docs = input("Enter sentences separated by |: ").split("|")
q = input("Enter your question: ")

v = TfidfVectorizer()
X = v.fit_transform(docs + [q])
i = cosine_similarity(X[-1], X[:-1]).argmax()

print("Answer:", docs[i])
