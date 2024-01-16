class Solution {
    public String solution(String myString) {
        String answer = "";
        for (int i = 0; i < myString.length(); i ++) {
            char checkChar = myString.charAt(i);
            if (Character.toString(checkChar).matches("[a-z]")) {
                answer += Character.toUpperCase(checkChar);
            } else {
                answer += checkChar;
            }
        }
        return answer;
    }
}