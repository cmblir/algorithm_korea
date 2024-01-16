import java.util.*;

class Solution {
    public int[] solution(int n) {
        ArrayList<Integer> answerList = new ArrayList<>();
        
        answerList.add(n);
        
        while (true) {
            if (n == 1) {
                break;
            }
            else if (n % 2 == 0) {
                n = n / 2;
            } else {
                n = 3 * n + 1;
            }
            answerList.add(n);
        }
        int[] answer = answerList.stream().mapToInt(Integer::intValue).toArray();
        
        return answer;
    }
}