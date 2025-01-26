import math
from collections import Counter
solution=lambda clothes: math.prod([v+1 for v in Counter(map(lambda x:x[1], clothes)).values()]) - 1