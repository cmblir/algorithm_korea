import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] strs = br.readLine().split(" ");
        int N = Integer.parseInt(strs[0]);
        int M = Integer.parseInt(strs[1]);
        int[] answer = new int[N];
        for (int cnt = 0; cnt < M; cnt ++) {
            String[] num = br.readLine().split(" ");
            int i = Integer.parseInt(num[0]);
            int j = Integer.parseInt(num[1]);
            int k = Integer.parseInt(num[2]);
            for (int m = i - 1; m < j; m++) {
                answer[m] = k;
            }
        }
        for (int l = 0; l < answer.length; l++) {
            System.out.print(answer[l] + " ");
        }
    }
    
    public static void main(String[] args) throws Exception {
        new Main().solution();
    }
}