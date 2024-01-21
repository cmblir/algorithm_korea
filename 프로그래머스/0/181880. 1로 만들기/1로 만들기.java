class Solution {
    public int solution(int[] num_list) {
        int answer = 0;
        int sum = 0;
        while (sum != num_list.length) {
            sum = 0;
            for (int num : num_list) {
                sum += num;
            }
            for (int i = 0; i < num_list.length; i ++) {
                if (num_list[i] == 1) {
                    continue;
                }
                if (num_list[i] % 2 == 0) {
                    num_list[i] = num_list[i] / 2;
                } else {
                    num_list[i] = (num_list[i] - 1) / 2;
                }
                answer ++;
            }
        }
        return answer;
    }
}