import java.util.Arrays;
class Solution {
    public int solution(int[] arr1, int[] arr2) {
        int arr1Sum = Arrays.stream(arr1).sum();
        int arr2Sum = Arrays.stream(arr2).sum();
        if (arr1.length == arr2.length && arr1Sum < arr2Sum || arr1.length < arr2.length) {
            return -1;
        } else if (arr1.length == arr2.length && arr1Sum > arr2Sum || arr1.length > arr2.length) {
            return 1;
        } else {
            return 0;
        }
    }
}