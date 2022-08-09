def solution(numbers, hand):
    answer = ''
    
    # 키패드 좌표
    dic = {1: [0, 0], 2: [0, 1], 3: [0, 2],
           4: [1, 0], 5: [1, 1], 6: [1, 2],
           7: [2, 0], 8: [2, 1], 9: [2, 2],
           '*':[3, 0], 0: [3, 1], '#': [3, 2]}
    
    # 시작 위치
    left = dic['*']
    right = dic['#']
    
    for i in numbers:
        now = dic[i]
        if i in [1, 4, 7]: # 왼손손 시작지점
            answer += 'L'
            left = now
            
        elif i in [3, 6, 9]: # 오른손 시작지점
            answer += 'R'
            right = now
            
        else: # 중간에 위치한 경우
            left_mid = 0 
            right_mid = 0
            
            for a, b, c in zip(left, right, now):
                left_mid += abs(a-c)
                right_mid += abs(b-c)
            
            # 왼손이 더 가까운 경우
            if left_mid < right_mid:
                answer += 'L'
                left = now
                
            # 오른손이 더 가까운 경우
            elif left_mid > right_mid:
                answer += 'R'
                right = now
            
            # 두 거리가 같은 경우
            else:
                # 왼손잡이 경우
                if hand == 'left':
                    answer += 'L'
                    left = now
                    
                # 오른손잡이 경우
                else:
                    answer += 'R'
                    right = now
    return answer