import java.io.*;
import java.util.*;
public class quicksort {
    public static void main(String[] args) {
        File file = new File("numbers.txt");
        try {
            Scanner in = new Scanner(file);
            boolean yeet = true;
            List<Integer> a = new ArrayList<Integer>();
            for (int i = 0; i < 1000000000; i++) {
                a.add(in.nextInt());
            }

            for (int i = 0; i < 100; i++) {
                Collections.shuffle(a);
                int[] b = new int[a.size()];
                for (int j = 0; j < a.size(); j++) {
                    b[j] = a.get(j);
                }
                sort(b);
                if (!isSorted(b)) {
                    System.out.println("rip");
                    yeet = false;
                }
            }

            if (yeet)
                System.out.println("yeet");

        }
        catch (Exception e) {
            System.out.println("ur bad");
        }
    }

    public static boolean isSorted(int[] a) {
        for (int i = 0; i < a.length - 1; i++)
            if (a[i] > a[i+1])
                return false;
        return true;
    }

    public static void sort(int[] a) {
        sort(a, 0, a.length - 1);
    }

    public static void sort(int[] a, int min, int max) {
        if (max <= min)
            return;
        int j = partition(a, min, max);
        sort(a, min, j - 1);
        sort(a, j + 1, max);
    }

    public static int partition(int[] a, int min, int max) {
        int i = min;
        int j = max + 1;
        int v = a[min];

        while (true) {
            while (a[++i] < v)
                if (i == max)
                    break;
            while (v < a[--j])
                if (j == min)
                    break;
            if (i >= j)
                break;

            exch(a, i, j);
        }

        exch(a, min, j);
        
        return j;
    }

    public static void exch(int[] a, int i, int j) {
        int temp = a[i];
        a[i] = a[j];
        a[j] = temp;
    }
}
