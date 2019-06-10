package Collatz_Conjecture;
import java.util.*;
public class Main {

    public static void main(String[] args) {
        Scanner as = new Scanner(System.in);
        System.out.print("Enter number: "); int no = as.nextInt();
        int count = 0;
        boolean end = false;
        while(!end && count <= 50){
            if (no%2==0){
                System.out.println(no+" / 2 = "+(no/2));
                no /= 2;
            }else{
                System.out.println("("+no+" * 3) + 1 = "+((no*3)+1));
                no = (no*3)+1;
            }
            if(no == 1){
                end = true;
            }
            count++;
        }
        System.out.println(count+" iterations");
    }
}
