
//N*M크기의 두 행렬 A와 B가 주어졌을 때, 두 행렬을 더하는 프로그램을 작성하시오.
//첫째 줄에 행렬의 크기 N 과 M이 주어진다. 둘째 줄부터 N개의 줄에 행렬 A의 원소 M개가 차례대로 주어진다. 이어서 N개의 줄에 행렬 B의 원소 M개가 차례대로 주어진다. N과 M은 100보다 작거나 같고, 행렬의 원소는 절댓값이 100보다 작거나 같은 정수이다.
//첫째 줄부터 N개의 줄에 행렬 A와 B를 더한 행렬을 출력한다. 행렬의 각 원소는 공백으로 구분한다.
// 3 3
// 1 1 1
// 2 2 2
// 0 1 0
// 3 3 3
// 4 4 4
// 5 5 100

// //출력
// //4 4 4
// 6 6 6
// 5 6 100
import java.io.*;
import java.util.StringTokenizer;
public class Num2738 {
  public static void main(String[] args)throws IOException{
    BufferedReader br= new BufferedReader( new InputStreamReader(System.in));
    String s= br.readLine();
    StringTokenizer st= new StringTokenizer(s);

    int n= Integer.parseInt(st.nextToken());
    int m= Integer.parseInt(st.nextToken());
    int[][] arr= new int[n][m];

    for(int i=0; i<2; i++){
      for(int j=0; j<n; j++){
        StringTokenizer st_2= new StringTokenizer(br.readLine());
        for(int k=0; k<m; k++){
          arr[j][k]+=Integer.parseInt(st_2.nextToken());
        }
      }
    }

    for(int k=0; k<n; k++){
      for(int j=0; j<m; j++){
        System.out.print(arr[k][j]+" ");
      }
      System.out.println();
    }
  }
}
