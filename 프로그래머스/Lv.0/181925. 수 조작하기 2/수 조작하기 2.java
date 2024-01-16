class Solution {
    public String solution(int[] numLog) {
        int beforeNumber = numLog[0];
        String answer = "";
        for (int i = 1; i < numLog.length; i++) {
            int afterNumber = numLog[i];
            if (beforeNumber + 1 == afterNumber) {
                answer += "w";
            } else if (beforeNumber - 1 == afterNumber) {
                answer += "s";
            } else if (beforeNumber + 10 == afterNumber) {
                answer += "d";
            } else if (beforeNumber - 10 == afterNumber) {
                answer += "a";
            }
            beforeNumber = afterNumber;
        }
        return answer;
    }
}