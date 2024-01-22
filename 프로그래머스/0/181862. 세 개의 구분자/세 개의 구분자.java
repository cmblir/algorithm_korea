import java.util.*;
class Solution {
    public String[] solution(String myStr) {
        List<String> list = new ArrayList<>();
        String temp = "";
        // 중간 중간 받을 문자열
        
        for (int i = 0; i < myStr.length(); i++) {
            char value = myStr.charAt(i);
            
            // 현재 문자값
            
            if (value == 'a' || value == 'b' || value == 'c') {
                // 나눠야할 문자라면
                
                if (!temp.isEmpty()) {
                    // temp가 빈 문자열이 아니라면
                    
                    list.add(temp);
                    // 리스트에 현재 문자열을 넣어주고 문자열을 다시 비워준다.
                    
                    temp = "";
                }
            } else {
                // 나눌 문자가 아니라면 문자를 다시 쌓아준다.
                
                temp += value;
            }
        }
        if (!temp.isEmpty()) {
            // 반복문이 끝난 이후 (문자를 나눈 이후)에 남은 문자열을 넣어준다.
            
            list.add(temp);
        }
        
        if (list.size() == 0) {
            list.add("EMPTY");
        }
        
        return list.toArray(new String[0]);
    }
}