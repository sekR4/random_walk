import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;
// Wahnsinn, was ich hier alles importieren muss für ein so banales Problem...
public class Solution {

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        // https://www.hackerrank.com/challenges/java-if-else/problem
        int N = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");
        if (N % 2 == 0) {
            if (N > 1 && N < 5) {
                System.out.println("Not Weird");
            }
            if (N > 5 && N < 21) {
                System.out.println("Weird");
            }
            if (N > 20) {
                System.out.println("Not Weird");
            }
        }
        else System.out.println("Weird");

        scanner.close();
    }
}
