N = int(input())
words,word = [],[]
for i in range(N):
    words.append(input())

words = list(set(words))
words.sort(key=lambda x: (len(x),x))
print(*words, sep = '\n')