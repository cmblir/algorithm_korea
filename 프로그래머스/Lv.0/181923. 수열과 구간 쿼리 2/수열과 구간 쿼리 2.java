class Solution {
    public int[] solution(int[] arr, int[][] queries) {

        int[] result = new int[queries.length];
        
        for (int i = 0; i < queries.length; i++) {
            
            int startRange = queries[i][0];
            int endRange = queries[i][1];
            int compareNumber = queries[i][2];
            
            int resultNumber = -1;
            
            for (int j = startRange; j <= endRange; j ++) {
                
                if (arr[j] > compareNumber) {
                    
                    if (resultNumber == -1 || arr[j] < resultNumber) {
                        
                        resultNumber = arr[j];
                    }
                }
            
            }
            
            result[i] = resultNumber;
        }
        return result;
    }
}