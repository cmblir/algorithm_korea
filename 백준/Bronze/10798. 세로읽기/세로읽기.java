
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String[] arr = new String[5];

        for (int i = 0; i < 5; i++) {
            String temp = br.readLine();
            if (temp.length() < 15) {
                StringBuilder sb = new StringBuilder(temp);
                for (int j = temp.length(); j < 15; j++) {
                    sb.append("-");
                }
                String paddedString = sb.toString();
                arr[i] = paddedString;
            } else {
                arr[i] = temp;
            }
        }

        for (int i = 0; i < 15; i ++) {
            for (int j = 0; j < 5; j++) {
                if (arr[j].charAt(i) != '-') {
                    bw.write(arr[j].charAt(i));
                }
            }
        }

        bw.flush();
        bw.close();

    }
}