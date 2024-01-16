import java.util.*;

class Solution {
    public int[] solution(int[] num_list, int n) {
        ArrayList<Integer> numList = new ArrayList<>();
        
        for (int i = n - 1; i < num_list.length; i++) {
            numList.add(num_list[i]);
        }
        int[] answer = numList.stream().mapToInt(Integer::intValue).toArray();
        
        return answer;
    }
}