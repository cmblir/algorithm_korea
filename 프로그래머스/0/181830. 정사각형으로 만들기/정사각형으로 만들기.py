def solution(arr):
    col = len(arr[0])
    row = len(arr)
    if row < col:
        appendlist = [0 for i in range(col)]
        while row < col:
            arr.append(appendlist)
            row = len(arr)
    else:
        for i in arr:
            while len(i) < row:
                i.append(0)
    return arr