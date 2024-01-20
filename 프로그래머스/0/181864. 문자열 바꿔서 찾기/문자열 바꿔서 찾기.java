class Solution {
    public int solution(String myString, String pat) {
        String reverseString = "";
        for (int i = 0; i < myString.length(); i++) {
            if (myString.charAt(i) == 'A') {
                reverseString += 'B';
            } else if (myString.charAt(i) == 'B') {
                reverseString += 'A';
            }
        }
        return reverseString.contains(pat) ? 1 : 0;
    }
}