class Solution {
    public String[] solution(String[] names) {
        int range = names.length % 5 == 0 ? names.length / 5 : names.length / 5 + 1;
        String[] answer = new String[range];
        for (int i = 0, j = 0; j < names.length; i++, j += 5) {
            answer[i] = names[j];
        }
        return answer;
    }
}