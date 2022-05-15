H = int(input())
for _ in range(H):
    n = int(input())
    print(f"Pairs for {n}:", end=' ') # Pairs for 먼저 출략
    for i in range(1, n//2+1): # 두 쌍이므로 n // 2까지의 범위
        if i != n-i:
            if i != 1: # 만약 1이 아니라면
                print(',', end=' ')
            print(i, n-i, end='') # 쌍을 출력한다
    print() # 한 줄이 끝난 뒤 한칸 띄기