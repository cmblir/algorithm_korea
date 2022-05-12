import sys
N, M = map(int, sys.stdin.readline().split())
# 나무의 수 N, 나무의 길이 M
tree = list(map(int, sys.stdin.readline().split()))
'''
# 절단기보다 큰 나무는 H 위 부분이 잘린다.
# 절단기보다 작은 나무는 잘리지 않는다.
# ==> 잘린 나무의 남은 부분 + 자르지 못한 나무 = 상근이가 가져갈 나무
# 핵심 : M 크기 이상의 나무중 상근이가 가져갈 나무를 최소화하기
'''
def solution(tree, H_lf, H_rf): # 이진탐색으로 문제 해결
    # 점차 좌우로 절단기 크기를 크게하고 줄이게 하면서
    # 최적의 절단기 값을 찾은 경우 반환
    res = 0
    while H_lf <= H_rf: # 만약 좌값과 우값이 같거나 우값이 큰 경우
        H_mid = (H_lf + H_rf) // 2 # 중간값
        total = 0 # 전체 개수
        for i in tree:   
            if i > H_mid: # 절단기보다 나무가 크다면
                total += i - H_mid # 전체 값은 나무 - 절단기
        if total < M: # 만약 가져가고자 하는 값보다 전체 개수가 적다면
            H_rf = H_mid - 1 # 우값이 절단기 크기를 줄인 값이다.
        else:
            res = H_mid # 찾고자하는 절단기 값을 저장
            H_lf = H_mid + 1 # 좌값이 절단기 크기를 늘린 값이다.
    return res

print(solution(tree, 0, max(tree)))