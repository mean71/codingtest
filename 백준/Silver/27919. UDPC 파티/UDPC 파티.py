uc, dp = 0, 0
for c in input():
    if c in "UC":
        uc += 1
    else:
        dp += 1

u = uc > sum(divmod(dp, 2))
print("U"*u + "D"*bool(dp) + "P"*bool(dp))