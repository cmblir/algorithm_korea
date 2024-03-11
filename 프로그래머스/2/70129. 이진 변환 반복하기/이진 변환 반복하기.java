class Solution {
    public int[] solution(String s) {
        int deleteCount = 0;
        int binaryCount = 0;
        while (s.length() != 1) {
            
            boolean temp = false;
            
            for (int i = 0; i < s.length(); i++) { // 0 제거 필요여부와 개수파악
                if (s.charAt(i) == '0') {
                    deleteCount ++;
                    temp = true;
                }
            }
            
            if (temp == true) { // 0 제거구문
                s = s.replaceAll("0", "");
            }
            
            s = Integer.toString(s.length(), 2); // 문자열 길이를 2진법으로 변환
                        
            binaryCount ++; // 변환횟수 증가
            
        }
        int[] answer = {binaryCount, deleteCount};
        return answer;
    }
}