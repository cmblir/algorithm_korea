import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        boolean[] Student = new boolean[30];

        for (int i = 0; i < 28; i++) {
            int n = Integer.parseInt(br.readLine());
            Student[n - 1] = true;
        }

        for (int i = 0; i < Student.length; i++) {
            if (!Student[i]) {
                bw.write((i+1) + "\n");
            }
        }
        br.close();
        bw.flush();
        bw.close();
    }
}