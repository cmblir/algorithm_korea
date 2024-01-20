class Solution {
    public int[] solution(String myString) {
        String[] count = myString.split("x", myString.length());
        int[] answer = new int[count.length];
        for (int i = 0; i < count.length; i ++) {
            answer[i] = count[i].length();
        }
        return answer;
    }
}