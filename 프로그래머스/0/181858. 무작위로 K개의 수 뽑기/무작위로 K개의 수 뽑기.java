import java.util.*;
class Solution {
    public int[] solution(int[] arr, int k) {
        List<Integer> answerList = new ArrayList<>();
        for (int num : arr) {
            if (!answerList.contains(num) && answerList.size() < k) {
                answerList.add(num);
            }
        }
        while (answerList.size() < k) {
            answerList.add(-1);
        }
        return answerList.stream().mapToInt(x -> x).toArray();
    }
}