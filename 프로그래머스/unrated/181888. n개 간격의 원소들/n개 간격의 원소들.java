class Solution {
    public int[] solution(int[] num_list, int n) {
        int cnt = 0;
        for (int i = 0; i < num_list.length; i += n) {
            cnt += 1;
        }
        int[] answer = new int[cnt];
        for (int i = 0, j = 0; i < cnt; i++, j += n) {
            answer[i] = num_list[j];
        }
        return answer;
    }
}