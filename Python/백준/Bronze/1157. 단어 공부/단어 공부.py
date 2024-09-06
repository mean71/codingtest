w = input().upper()
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
count = [0,'']

for j in alpha:
    if j in w:
        if count[0] < w.count(j):
            count[0] = w.count(j)
            count[1] = j 
        elif count[0] == w.count(j):
            count[1] = '?'
print(count[1])