import java.io.BufferedWriter;
import java.io.OutputStreamWriter;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String[] arr = br.readLine().split(" ");
        int N = Integer.parseInt(arr[0]);
        int K = Integer.parseInt(arr[1]);

        int[] answer = new int[N];
        int count = 0;

        for (int i = 1; i < N+1; i++) {
            if (N % i == 0) {
                answer[count] = i;
                count++;
            }
        }
        if (answer[0] == 0) {
            bw.write(String.valueOf(0));
        } else {
            bw.write(String.valueOf(answer[K - 1]));
        }
        bw.flush();
        bw.close();
    }
}