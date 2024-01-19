import java.util.Arrays;

class Solution {
    public int[] solution(int[] arr) {
        int start = -1;
        int end = -1;

        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == 2) {
                if (start == -1) {
                    start = i;
                }
                end = i;
            }
        }

        if (start == -1) {
            // 2가 없는 경우
            return new int[]{-1};
        } else {
            // 2가 있는 경우
            return Arrays.copyOfRange(arr, start, end + 1);
        }
    }
}