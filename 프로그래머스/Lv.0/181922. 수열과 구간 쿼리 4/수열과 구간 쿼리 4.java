class Solution {
    public int[] solution(int[] arr, int[][] queries) {
        for (int j = 0; j < queries.length; j ++) {
            int startIdx = queries[j][0];
            int endIdx = queries[j][1];
            int compareValue = queries[j][2];
            
            for (int i = startIdx; i <= endIdx; i ++) {
                if (i == 0 || i % compareValue == 0) {
                    arr[i] = arr[i] + 1;
                }
            }
        }
        return arr;
    }
}