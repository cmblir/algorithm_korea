class Solution {
    public String solution(String myString, String pat) {
        String answer = "";
        String temp = "";
        for (int i = 0; i < myString.length(); i ++) {
            temp += myString.charAt(i);
            if (temp.contains(pat)) {
                answer += temp;
                temp = "";
            }
        }
        return answer;
    }
}