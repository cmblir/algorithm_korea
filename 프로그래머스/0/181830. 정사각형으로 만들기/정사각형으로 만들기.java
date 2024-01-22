import java.util.*;

class Solution {
    public int[][] solution(int[][] arr) {
        List<List<Integer>> newArr = new ArrayList<>();
        for (int[] row : arr) {
            List<Integer> rowList = new ArrayList<>();
            for (int num : row) {
                rowList.add(num);
            }
            newArr.add(rowList);
        }
        
        int col = newArr.get(0).size();
        int row = newArr.size();
        
        if (row < col) {
            while (row < col) {
                List<Integer> appendList = new ArrayList<>();
                for (int i = 0; i < col; i++) {
                    appendList.add(0);
                }
                newArr.add(appendList);
                row = newArr.size();
            }
        } else {
            for (List<Integer> rowList : newArr) {
                while (rowList.size() < row) {
                    rowList.add(0);
                }
            }
        }
        int[][] answer = new int[newArr.size()][];
        for (int i = 0; i < newArr.size(); i++) {
            List<Integer> rowList = newArr.get(i);
            answer[i] = new int[rowList.size()];
            for (int j = 0; j < rowList.size(); j ++) {
                answer[i][j] = rowList.get(j);
            }
        }
        return answer;
    }
}