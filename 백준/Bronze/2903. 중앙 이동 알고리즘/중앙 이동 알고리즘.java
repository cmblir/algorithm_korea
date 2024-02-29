import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int N = Integer.parseInt(br.readLine());
        int answer = (int)Math.pow(Math.pow(2, N) + 1, 2);

        br.close();
        bw.write(String.valueOf(answer));
        bw.flush();
        bw.close();
    }
}