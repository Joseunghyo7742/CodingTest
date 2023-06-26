import java.io.*;
import java.util.StringTokenizer;
public class Num2563 {
  public static void main(String[] args) throws IOException{
    BufferedReader br= new BufferedReader(new InputStreamReader(System.in));
    int n = Integer.parseInt(br.readLine()); //Int
    int[][] board= new int[100][100]; //도화지 크기
    for(int i=0; i<n; i++){
      StringTokenizer st= new StringTokenizer(br.readLine());
      int x= Integer.parseInt(st.nextToken());
      int y= Integer.parseInt(st.nextToken());
      for(int j=x; j<x+10; j++){
        for(int k=y; k<y+10; k++){
          board[j][k]=1;
        }
      }
    }
    int result=0;
    for( int i=0; i<100; i++){
      for(int j=0; j<100; j++){
        if(board[i][j]==1)
          result++;
      }
    }
    System.out.println(result);
  }
}
