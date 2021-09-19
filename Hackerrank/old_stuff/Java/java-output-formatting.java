import java.util.Scanner;

public class Solution {

    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        System.out.println("================================");
        for(int i=0;i<3;i++){
            String s1=sc.next();
            int x=sc.nextInt();
            // my ("Kirche um's Dorf") solution:
            String x1 = Integer.toString(x);
            String space = new String(new char[15-s1.length()]).replace("\0", " "); // thx [Andi](https://stackoverflow.com/a/16812721)
            String zeros = new String(new char[3-x1.length()]).replace("\0", "0");
            String result = s1 + space + zeros + x1;
//            System.out.println(result);

            // awesome solution!: thx [Alamir](https://www.hackerrank.com/challenges/java-output-formatting/forum/comments/78622)
            System.out.printf("%-15s%03d%n", s1, x);
        }
        System.out.println("================================");

    }
}



