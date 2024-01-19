import java.util.*;

class Solution {
    public int[] solution(int n, int[] slicer, int[] num_list) {
        int a = slicer[0];
        int b = slicer[1];
        int c = slicer[2];
        List<Integer> arrList = new ArrayList<>();
        switch (n) {
            case 1:
                for(int i = 0; i <= b; i ++) {
                    arrList.add(num_list[i]);
                }
                break;
            case 2:
                int endIndex = num_list.length-1;
                for(int i = a; i <= endIndex; i++) {
                    arrList.add(num_list[i]);
                }
                break;
            case 3:
                for (int i = a; i <= b; i++) {
                    arrList.add(num_list[i]);
                }
                break;
            case 4:
                for (int i = a; i <= b; i+= c) {
                    arrList.add(num_list[i]);
                }
                break;
        }
        int[] answer = arrList.stream().mapToInt(Integer::intValue).toArray();
        return answer;
    }
}