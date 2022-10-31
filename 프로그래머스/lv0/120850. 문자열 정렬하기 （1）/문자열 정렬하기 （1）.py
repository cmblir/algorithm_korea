import re
solution = lambda x: sorted([int(i) for i in list(re.sub(r"[^0-9]", '', x))])