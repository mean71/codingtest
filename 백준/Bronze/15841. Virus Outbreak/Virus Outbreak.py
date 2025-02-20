while -1 != (h:=int(input())):
    a, b = 1, 1
    for _ in range(1, h):
        a,b = b, a+b
    print(f"Hour {h}: {a} cow(s) affected")