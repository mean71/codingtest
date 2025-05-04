alpha = {chr(k):v for v, k in enumerate(range(97,123), 1)}
input()
print(sum(alpha[c]*(31**i) for i, c in enumerate(input()))%1234567891)