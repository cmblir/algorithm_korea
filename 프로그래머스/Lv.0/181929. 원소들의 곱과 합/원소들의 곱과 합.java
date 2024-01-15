class Solution {
    public int solution(int[] num_list) {
        int multipl = num_list[0];
        int squared = num_list[0];
        for (int i = 1; i < num_list.length; i++) {
            multipl *= num_list[i];
            squared += num_list[i];
        }
        squared *= squared;
        return (multipl < squared) ? 1 : 0;
    }
}