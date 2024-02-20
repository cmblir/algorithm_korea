import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int N = Integer.parseInt(br.readLine());
        br.close();

        for (int i = 1; i <= N; i++) {
                bw.write(" ".repeat(N - i));
                bw.write("*".repeat(2 * i - 1));
                bw.write("\n");
            }

        for (int i = N - 1; i >= 1; i--) {
            bw.write(" ".repeat(N - i));
            bw.write("*".repeat(2 * i - 1));
                bw.write("\n");
       
        }
            bw.flush();
            bw.close();
    }
}