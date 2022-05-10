import sys
input = sys.stdin.readline
N, K = map(int, input().split())
def top_down(n, k):
    if k > n:
        return 0
    DP = [[-1 for _ in range(n + 1)] for _ in range(n + 1)]

    def select(times, got):
        if times == n:
            return got == k
        if DP[times][got] != -1:
            return DP[times][got]
        DP[times][got] = select(times+1, got) + select(times+1, got+1)
        return DP[times][got]

    return select(0, 0)

print(top_down(N, K))