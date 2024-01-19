class Solution {
    public String[] solution(String[] names) {
        if (names.length < 6) {
            String[] answer = {names[0]};
            return answer;
        }
        double lng = Math.ceil((double)names.length / 5);
        String[] answer = new String[(int)lng];
        for (int i = 0, j = 0; i < answer.length; i++, j += 5) {
            answer[i] = names[j];
        }
        return answer;
    }
}