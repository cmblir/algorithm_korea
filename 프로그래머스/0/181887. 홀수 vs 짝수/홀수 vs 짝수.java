class Solution {
    public int solution(int[] num_list) {
        int sumOdd = 0;
        int sumEven = 0;
        for (int num = 0; num < num_list.length; num++) {
            if (num % 2 == 0) {
                sumEven += num_list[num];
            } else {
                sumOdd += num_list[num];
            }
        }
        return sumOdd > sumEven ? sumOdd : sumEven;
    }
}