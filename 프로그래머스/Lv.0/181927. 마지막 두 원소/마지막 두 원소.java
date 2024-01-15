import java.util.Arrays;

class Solution {
    public int[] solution(int[] num_list) {
        int beforeValue = num_list[num_list.length - 2];
        int afterValue = num_list[num_list.length - 1];
        
        int[] newList = new int[num_list.length];
        
        newList = Arrays.copyOf(num_list, num_list.length + 1);
        
        
        if (afterValue > beforeValue) {
            int newValue = afterValue - beforeValue;
            newList[newList.length - 1] = newValue;
            
        } else if (afterValue <= beforeValue) {
            int newValue = afterValue * 2;
            newList[newList.length - 1] = newValue;
        }
        
        
        return newList;
    }
}