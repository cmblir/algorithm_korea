class Solution {
    public int[] solution(int[] arr) {
        int arrLength = 0;
        for (int i = 0; i < 1000; i++) {
            arrLength = (int) Math.pow(2, i);
            if (arrLength >= arr.length) {
                break;
            }
        }
        int[] answer = new int[arrLength];
        System.arraycopy(arr, 0, answer, 0, arr.length);
        return answer;
    }
}