class Solution {
    public int[] solution(int start, int end_num) {
        int count = start - end_num;
        int[] answer = new int[count + 1];
        for (int i = 0; i <= count; start--, i++){
            answer[i] = start;
        }
        return answer;
    }
}