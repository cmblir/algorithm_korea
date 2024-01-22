import java.util.*;

class Solution {
    public int[] solution(int[] arr) {
        List<Integer> stk = new ArrayList<>();
        int[] answer = {-1};
        int i = 0;
        while (i < arr.length) {
            if (stk.size() == 0) {
                stk.add(arr[i]);
                i++;
            } else if (stk.size() != 0 && stk.get(stk.size() - 1) == arr[i]) {
                stk.remove(stk.size() - 1);
                i++;
            } else if (stk.size() != 0 && stk.get(stk.size() - 1) != arr[i]) {
                stk.add(arr[i]);
                i++;
            }
        }
        return stk.size() > 0 ? stk.stream().mapToInt(x -> x).toArray() : answer;
    }
}