import java.math.BigInteger;
class Solution {
    public String solution(String a, String b) {
        BigInteger sumA = new BigInteger(a);
        BigInteger sumB = new BigInteger(b);
        BigInteger sumAB = sumA.add(sumB);
        return sumAB.toString();
    }
}