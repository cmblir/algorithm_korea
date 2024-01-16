import java.util.*;

class Solution {
    public int[] solution(int n, int k) {
        ArrayList<Integer> answerList = new ArrayList<>();
        
        int maxValue = k;
        int i = 1;
        while (true) {
            maxValue = k * i;
            if (maxValue > n) {
                break;
            }
            i++;
            answerList.add(maxValue);
        }
        
        int[] answer = answerList.stream().mapToInt(Integer::intValue).toArray();
        
        return answer;
    }
}