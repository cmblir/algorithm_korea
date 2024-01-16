class Solution {
    public int[] solution(int[] arr, int[][] queries) {
        
        for (int i = 0; i < queries.length; i++) {
            for (int j = 1; j < queries[i].length; j++) {   
                int beforeNumber = queries[i][j - 1];
                int afterNumber = queries[i][j];
                int tempNumber = arr[beforeNumber];
                arr[beforeNumber] = arr[afterNumber];
                arr[afterNumber] = tempNumber;
            }        
        
        }
        return arr;
    }

}