import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int X, N;
        int total = 0;
        X = Integer.parseInt(br.readLine());
        N = Integer.parseInt(br.readLine());
        for (int i = 0; i < N; i ++) {
            String[] strs = br.readLine().split(" ");
            int a = Integer.parseInt(strs[0]);
            int b = Integer.parseInt(strs[1]);
            total += a * b;
        }
        String answer = total == X ? "Yes" : "No";
        System.out.println(answer);
    }
    
    public static void main(String[] args) throws Exception {
        new Main().solution();
    }
}