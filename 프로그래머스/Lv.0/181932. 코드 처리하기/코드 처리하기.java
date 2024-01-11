class Solution {
    public String solution(String code) {
        String answer = "";
        int mode = 0; // mode
        for (int i = 0; i < code.length(); i++) {
            char temp = code.charAt(i);
            if (temp == '1') { // 1일때
                if (mode == 0) { // mode 변경
                    mode = 1;
                } else { // mode 변경
                    mode = 0;
                }
                continue;
            }
            if (mode == 0 && i % 2 == 0) { // mode 0일때 짝수
                answer += temp;
            }
            if (mode == 1 && i % 2 != 0) { // mode 1일때 홀수
                answer += temp;
            }
        }
        if ("".equals(answer)) {
            return "EMPTY";
        } else {
            return answer;   
        }
    }
}