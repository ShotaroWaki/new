from gensim.models import KeyedVectors

model = KeyedVectors.load_word2vec_format('model.vec', binary=False)
model.save("model.kv")
word = input()
ans = model.most_similar(word)
print(ans)