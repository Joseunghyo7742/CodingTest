import java.io.*;
public class Num2720 {
  public static void main(String[] args) throws IOException{
    BufferedReader br= new BufferedReader(new InputStreamReader (System.in));
    int n= Integer.parseInt(br.readLine()); //실행횟수
    int[] changes= new int[n];
    for(int i=0; i<n; i++){
      int m= Integer.parseInt(br.readLine());
      changes[i]=m;
    }
    int [] coins= {25, 10, 5, 1};
    for(int change: changes){
      for(int coin: coins){
        System.out.print(change/coin+" ");
        change=change%coin; 
      }
      System.out.println();
    }

  }
}
