import java.util.*;

class Solution {
    public int solution(int a, int b, int c, int d) {
        int answer = 0;
        int[] numbers = {a, b, c, d};
        
        Arrays.sort(numbers);
        HashMap<Integer, Integer> countMap = new HashMap<>();
        
        for (int num : numbers) {
            countMap.put(num, countMap.getOrDefault(num, 0) + 1);
        }
        
        switch (countMap.size()) {
                
            // 모두 같음
            case 1:
                answer = numbers[0] * 1111;
                break;
                
            // 2개씩 같음
            case 2:
                int count = 0;
                int threeKey = 0;
                int oneKey = 0;
                
                for (int key : countMap.keySet()) {
                    // 2개만 같은 경우
                    if (countMap.get(key) == 2) {
                        count = 2;
                        break;
                        
                    // 3개가 같고, 1개가 다름
                    } else if (countMap.get(key) == 3) {
                        count = 3;
                        threeKey = key;
                    } else {
                        oneKey = key;
                    }
                }
                
                if (count == 2) {
                    answer = (numbers[0] + numbers[3]) * (numbers[3] - numbers[0]);
                    // 2개 2개
                    break;
                } else {
                    int[] result = countMap.keySet().stream().mapToInt(Integer::intValue).toArray();    
                    answer = (int) Math.pow((10 * threeKey + oneKey), 2);
                    // 3개 1개
                    break;
                }
                
            // 3개의 값이 나온 경우, 2개가 같고 나머지 2개가 다름
            case 3:
                for (int key : countMap.keySet()) {
                    if (countMap.get(key) == 1 && answer == 0) {
                        answer = key;
                    } else if (countMap.get(key) == 1) {
                        answer *= key;
                    }
                }
                break;
                
            // 모두 다름
            case 4:
                answer = numbers[0];
                break;
            }
    return answer;
    }
}