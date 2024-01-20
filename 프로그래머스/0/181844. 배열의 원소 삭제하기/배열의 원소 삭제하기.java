import java.util.*;

class Solution {
    public int[] solution(int[] arr, int[] delete_list) {
        ArrayList<Integer> answer = new ArrayList<>();
        for (int num : arr) {
            if (containsValue(delete_list, num) == false) {
                answer.add(num);
            }
        }
        return answer.stream().mapToInt(Integer::intValue).toArray();
    }
    private static boolean containsValue(int[] arr, int target) {
        for (int element : arr) {
            if (element == target) {
                return true;
            }
        }
        return false;
    }

}