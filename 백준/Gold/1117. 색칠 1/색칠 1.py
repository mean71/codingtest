W, H, f, c, x1, y1, x2, y2 = map(int, input().split())
print(W*H - (c + 1)*(y2 - y1)*(x2-x1 + max(0, min(f, W-f, x2) - x1)))