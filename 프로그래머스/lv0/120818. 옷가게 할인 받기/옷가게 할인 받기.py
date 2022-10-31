import math
solution = lambda x: math.floor(x * 0.80) if x >= 500000 else (math.floor(x * 0.90) if x >= 300000 else (math.floor(x * 0.95) if x >= 100000 else(x if x < 100000 else())))
