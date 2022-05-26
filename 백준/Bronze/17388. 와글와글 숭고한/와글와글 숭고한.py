S, K, H = map(int, input().split())
if S + K + H >= 100:
    print("OK")
elif S + K + H < 100 and S < K and S < H:
    print("Soongsil")
elif S + K + H < 100 and K < S and K < H:
    print("Korea")
elif S + K + H < 100 and H < S and H < K:
    print("Hanyang")