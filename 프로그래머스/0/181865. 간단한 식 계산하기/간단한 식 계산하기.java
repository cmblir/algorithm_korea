import java.util.*;

class Solution {
    public int solution(String binomial) {
        String[] strArr = binomial.split(" ");
        int a = Integer.parseInt(strArr[0]);
        String op = strArr[1];
        int b = Integer.parseInt(strArr[2]);
        if (op.equals("+")) {
            return a + b;
        } else if (op.equals("*")) {
            return a * b;
        } else {
            return a - b;
        }
    }
}