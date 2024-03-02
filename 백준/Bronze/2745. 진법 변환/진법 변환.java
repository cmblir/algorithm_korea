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

        String N = arr[0];
        int B = Integer.parseInt(arr[1]);
        br.close();

        int result = 0;
        int sum = 0;
        int idx = 0;
        for (int i = N.length()-1; i >= 0; i--) {
            char c = N.charAt(i);
            if (c>='0' && c<='9')
                sum = c - '0';//0~9 사이는 그대로 출력
            else
                sum = c - 55;//A~Z는 숫자로 변경
            result += sum * Math.pow(B, idx++);
        }

        bw.write(String.valueOf(result));
        bw.flush();
        bw.close();
    }
}