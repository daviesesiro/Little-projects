import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner ask = new Scanner(System.in);
        while(true){
            System.out.print("Enter number: "); String digit = ask.next();
            String sqrt = String.valueOf(Math.sqrt(Integer.parseInt(digit)));
            try {
                String tSqrt = sqrt.substring(sqrt.indexOf(".")+1,sqrt.indexOf(".")+4);
                String sq = String.valueOf((int)Math.pow(Integer.parseInt(digit), 2));
                if(tSqrt.contains(sq)) System.out.println("True");
                else System.out.println("false");
            }catch(Exception err) {
                System.out.println("False");
            }
        }

    }
}
