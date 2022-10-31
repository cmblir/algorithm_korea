reject = ["a", "e", "i", "o", "u"]
solution = lambda x: "".join([i for i in x if i not in reject])