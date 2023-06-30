  import java.io.*;

  public class Num1978 {
    public static void main(String [] args)throws IOException{
      BufferedReader br= new BufferedReader(new InputStreamReader(System.in));
      int n= Integer.parseInt(br.readLine());
      String[] firstLine = br.readLine().split(" ");
      int count=0; //소수 아닌 수 세기
      for(int i=0; i<n; i++){
        int num= Integer.parseInt(firstLine[i]);
        if( num==1){
          count++;
        }
        else{
          for(int j=2; j<=num; j++){
          if(num%j!=0 || num==j){
            continue;
          }
          else{
            count++;
            break;
          }
          }
          
        }
      }
      System.out.print(n-count);
    }
  }
