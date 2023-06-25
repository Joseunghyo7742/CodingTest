import java.io.*;
import java.util.StringTokenizer;
public class Num2566{
  public static void main(String[] args)throws IOException{
    BufferedReader br= new BufferedReader(new InputStreamReader(System.in));
    int max= -1;
    int max_c=0; //최댓값의 column
    int max_r= 0;//최댓값의 row
    for(int i=0; i<9; i++){
      StringTokenizer st= new StringTokenizer(br.readLine());
      for (int j=0; j<9; j++){
        int input= Integer.parseInt(st.nextToken());
        if(input>max){
          max=input;
          max_c= i+1;
          max_r= j+1;
        }
      }
    }
    System.out.println(max);
    System.out.print(max_c+" "+max_r);
  }
}