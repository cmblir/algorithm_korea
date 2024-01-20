class Solution {
    public String solution(String myString) {
        String answer = "";
        for (int i = 0; i < myString.length(); i ++) {
            if ((int)myString.charAt(i) == 97 || (int)myString.charAt(i) == 65) {
                answer += "A";
            } else {
                answer += Character.toLowerCase(myString.charAt(i));
            }
        }
        return answer;
    }
}