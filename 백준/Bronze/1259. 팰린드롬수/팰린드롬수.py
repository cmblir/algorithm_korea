def solution():
    while True:
        h = [i for i in str(input())]
        if h[0] == "0":
            break
        elif h[0:] == h[-1::-1]:
            print("yes")
        else:
            print("no")

solution()