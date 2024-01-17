import java.util.*;
class Solution {
    public int[] solution(String[] intStrs, int k, int s, int l) {
        ArrayList<Integer> answerList = new ArrayList<>();
        
        for (String str : intStrs) {
            int checkNumber = Integer.valueOf(str.substring(s, s+l));
            if (k < checkNumber) {
                answerList.add(checkNumber);
            }
        }
        int[] answer = answerList.stream().mapToInt(Integer::intValue).toArray();
        return answer;
    }
}