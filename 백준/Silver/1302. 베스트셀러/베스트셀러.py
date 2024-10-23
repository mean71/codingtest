import sys
input = sys.stdin.readline
book_n = {}
bestseller = [0,'']
if (N:=int(input()))==1:
    print(input().strip())
else:
    for _ in range(N):
        book = input().strip()
        
        book_n[book] = book_n.get(book, 0) + 1
            
        if bestseller[0] < book_n[book]:
            bestseller = [book_n[book], book]
        elif bestseller[0] == book_n[book] and bestseller[1] > book:
            bestseller = [book_n[book], book]
print(bestseller[1])