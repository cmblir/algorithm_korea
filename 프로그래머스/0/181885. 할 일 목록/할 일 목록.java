import java.util.List;
import java.util.ArrayList;

class Solution {
    public String[] solution(String[] todo_list, boolean[] finished) {
        List<String> answer = new ArrayList<>(); 
        for (int i = 0; i < todo_list.length; i++) {
            if (finished[i] == false) {
                answer.add(todo_list[i]);
            }
        }
        return answer.stream()
            .map(Object::toString)
            .toArray(String[]::new);
    }
}