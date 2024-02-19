import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int T = Integer.parseInt(br.readLine());
        for (int i = 0; i < T; i ++) {
            String S = br.readLine();
            if (S.length() > 1) {
                bw.write(S.charAt(0));
                bw.write(S.charAt(S.length() - 1) + "\n");
            } else {
                bw.write(S.charAt(0));
                bw.write(S.charAt(0) + "\n");
            }
            bw.flush();
        }
        br.close();
        bw.close();
    }
}