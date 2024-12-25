solution=lambda n,a,b:next(i for i in range(1,21) if a//2**i + bool(a%2**i) == b//2**i + bool(b%2**i))
    