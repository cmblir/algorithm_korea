class Solution {
    public int[][] solution(int n) {
        int[][] answer = new int[n][n];
        int number = 1;
        int x = 0, y = -1;
        int direction = 1; 
        /**
        x, y 는 현재 위치변수로 y가 -1인 이유는 첫 행이 0이므로
        direction은 이동방향을 의미한다.
        오른쪽으로 (1), 왼쪽으로 (-1)
        */
        
        while (n > 0) {
            for (int i = 0; i < n; i++) {
                y += direction;
                answer[x][y] = number++;
            }
            n--;
            
            for (int i = 0; i < n; i++) {
                x += direction;
                answer[x][y] = number++;
            }
            direction *= -1;
            // 반대 방향 전환
        }
        return answer;
    }
}