class Solution {
    public int solution(int[][] lines) {
        int answer = 0;
        
        for (int i = -100; i < 100; i++) {
            // 전체 길이 - 100 ~ 100
            
            int line = 0;
            
            if (lines[0][0]<=i && lines[0][1]>i) line++;
            // 1번라인
            
            if (lines[1][0]<=i && lines[1][1]>i) line++;
            // 2번라인
            
            if (lines[2][0]<=i && lines[2][1]>i) line++;
            // 3번라인
            
            if(line > 1) answer++;
            // 현재 라인에 점이 있다면
        }

        return answer;
    }
}