import java.util.*;
class Solution {
    public String[] solution(String myString) {
        String[] answer = myString.split("x");
        Arrays.sort(answer);
        List<String> result = new ArrayList<>();
        for (String str : answer) {
            if (!str.isEmpty()) {
                result.add(str);
            }
        }
        return result.toArray(new String[0]);
    }
}