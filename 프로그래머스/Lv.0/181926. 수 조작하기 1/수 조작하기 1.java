class Solution {
    public int solution(int n, String control) {
        for (int i = 0; i < control.length(); i ++) {
            char conn = control.charAt(i);
            if (conn == 'w') {
                n += 1;
            } else if (conn == 's') {
                n -= 1;
            } else if (conn == 'd') {
                n += 10;
            } else if (conn == 'a') {
                n -= 10;
            }
        }
        return n;
    }
}