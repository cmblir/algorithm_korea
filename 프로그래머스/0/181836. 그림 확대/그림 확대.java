import java.util.*;
class Solution {
    public String[] solution(String[] picture, int k) {
        List<String> answer = new ArrayList<>();
        for (String str : picture) {
            String addStr = "";
            for (int i = 0; i < str.length(); i++) {
                for (int j = 0; j < k; j++) {
                    addStr += str.charAt(i);    
                }
            }
            for (int i = 0; i < k; i++) {
                answer.add(addStr);
            }
        
        }
        return answer.toArray(new String[0]);
    }
}