import java.util.Scanner;
public class Num2292 {
  public static void main(String[] args){
    Scanner sc= new Scanner(System.in);
    int n= sc.nextInt();
    int count= 1; //거리
    int range=2; //범위

    if(n==1){
      System.out.print(1);
    }
    else{
      while(range<=n){
        range= range+(6*count);
        count++;
      }
      System.out.print(count);
    }
  }
}
