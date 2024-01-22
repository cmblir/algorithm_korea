import java.util.Arrays;

class Solution {
    public int solution(int[] rank, boolean[] attendance) {
        int answer = 0;
        int[][] newRank = new int[rank.length][2];
        
        // 배열 초기화 및 유효한 값 설정
        for (int i = 0; i < rank.length; i++) {
            if (attendance[i]) {
                newRank[i][0] = rank[i];
                newRank[i][1] = i;
            } else {
                newRank[i][0] = 101; // 임의의 큰 값, 충분히 큰 값으로 설정
                newRank[i][1] = 101; // 임의의 큰 값, 충분히 큰 값으로 설정
            }
        }
        
        // 배열 정렬
        Arrays.sort(newRank, (a, b) -> Integer.compare(a[0], b[0]));

        // 결과 계산
        answer = newRank[0][1] * 10000 + newRank[1][1] * 100 + newRank[2][1];
        
        return answer;
    }
}
