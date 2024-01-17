class Solution {
    public String solution(String my_string, int[][] queries) {
        char[] charArray = my_string.toCharArray();
        
        for (int i = 0; i < queries.length; i++) {
            
            int before = queries[i][0];
            int after = queries[i][1];
            
            for (int j = before, k = after; j <= k; j++, k--) {
                char temp = charArray[j];
                charArray[j] = charArray[k];
                charArray[k] = temp;
            }
            
        }
        
        String answer = new String(charArray);
        return answer;
    }
}