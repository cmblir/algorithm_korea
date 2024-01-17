class Solution {
    public int solution(String my_string, String is_suffix) {
        String[] suffix = new String[my_string.length()];
        for (int i = 0; i < my_string.length(); i++) {
            suffix[i] = my_string.substring(i);
        }
        for (String str : suffix) {
            if (is_suffix.equals(str)) {
                return 1;
            }
        }
        return 0;
    }
}