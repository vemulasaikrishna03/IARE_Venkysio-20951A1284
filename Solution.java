import java.util.*;
public class Solution {
    public static String solve(String A) {
        String s[] = A.split(" ");
        String ans = "";
        for (int i = s.length - 1; i >= 0; i--) {
            ans += s[i] + " ";
        }
        return ans.substring(0, ans.length() - 1);
    }
    public static void main(String args[]){
        Scanner sc =new Scanner(System.in);
        String s = sc.nextLine();
        System.out.println(solve(s));

    }
}
