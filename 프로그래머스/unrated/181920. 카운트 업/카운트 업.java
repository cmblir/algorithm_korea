class Solution {
    public int[] solution(int start_num, int end_num) {
        int[] answer = new int[end_num + 1 - start_num];
        for (int i = 0; start_num <= end_num; start_num++, i++) {
            answer[i] = start_num;
        }
        return answer;
    }
}