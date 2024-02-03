import java.util.Scanner;
public class Main {
    public static void main (String[] args) {
        int A;
        Scanner sc = new Scanner(System.in);
        A = sc.nextInt();
        for (int i = 0; i < A/4; i++) {
            System.out.println("long");
        }
        System.out.println("int");
    }
}