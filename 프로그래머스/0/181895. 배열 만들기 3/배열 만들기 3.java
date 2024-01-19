import java.util.*;
class Solution {
    public int[] solution(int[] arr, int[][] intervals) {
        List<Integer> answer = new ArrayList<>();
        int[] arr1 = Arrays.copyOfRange(arr, intervals[0][0], intervals[0][1] + 1);
        int[] arr2 = Arrays.copyOfRange(arr, intervals[1][0], intervals[1][1] + 1);
        for (int num : arr1) {
            answer.add(num);
        }
        for (int num : arr2) {
            answer.add(num);
        }
        return answer.stream().mapToInt(x -> x).toArray();
    }
}