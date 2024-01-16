class Solution {
    public int[] solution(int n, int k) {
        int temp = n / k;
        int[] answer = new int[temp];
        
        for(int i = 0, j = 1; i < temp; i++, j++) {
            answer[i] = k * j;
        }
        return answer;
    }
}