import java.util.Arrays;
import java.io.*;
import java.util.Scanner;

public class sort {
    public static void main(String[]args) {
        File file = new File("numbers.txt");
        try {
            Scanner in = new Scanner(file);
            boolean yeet = true;
            for (int i = 0; i < 1; i++) {
                int[] a = new int[10000];
                for (int j = 0; j < 10000; j++) {
                    a[j] = in.nextInt();
                }
                Arrays.sort(a);
            }
        }
        catch (Exception e) {
            System.out.println("ur bad");
        }
    }
}
