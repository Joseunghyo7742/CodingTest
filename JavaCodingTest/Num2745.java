import java.io.*;
public class Num2745 {
  public static void main(String[] args) throws IOException{

    BufferedReader br= new BufferedReader(new InputStreamReader(System.in));
    String n= br.readLine();
    int b= Integer.parseInt(br.readLine()); //b진법 수 
    long result=0;
    int count=1;
    for(int i=n.length()-1; i>=0; i--){
      int c= n.charAt(i);
      if(48<= c && c<=57){
        c= c-'0';
      } 
      if(65<=c && c<=90){
        c= c-55;
      }

      result+=count*c;
      count=count*b;
    }
    System.out.print(result);
    
}
}
