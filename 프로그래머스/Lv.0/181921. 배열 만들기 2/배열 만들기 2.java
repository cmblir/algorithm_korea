import java.util.*;

class Solution {
    public int[] solution(int l, int r) {
        ArrayList<Integer> answerList = new ArrayList<>();
        for (int i = l; i <= r; i++) {
            
            String target = Integer.toString(i);
            if (target.matches("[05]+")) {
                answerList.add(Integer.valueOf(target));
            }
        }
        
        int[] answer = answerList.stream().mapToInt(i->i).toArray();
        
        return answer.length != 0 ? answer : new int[]{-1};
    }
}