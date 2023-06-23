//정수 N개로 이루어진 수열 A와 정수 X가 주어진다. 이때, A에서 X보다 작은 수를 모두 출력하는 프로그램을 작성하시오.
//첫째 줄에 N과 X가 주어진다. (1 ≤ N, X ≤ 10,000)

//둘째 줄에 수열 A를 이루는 정수 N개가 주어진다. 주어지는 정수는 모두 1보다 크거나 같고, 10,000보다 작거나 같은 정수이다.

//X보다 작은 수를 입력받은 순서대로 공백으로 구분해 출력한다. X보다 작은 수는 적어도 하나 존재한다.


import java.io.*; 

public class num10871{
    public static void main( String[] args)throws IOException{
        BufferedReader br= new BufferedReader( new InputStreamReader(System.in)); 
        String[] firstLine = br.readLine().split(" ");
        int n = Integer.parseInt(firstLine[0]); // 배열의 크기
        int m = Integer.parseInt(firstLine[1]); // 찾을 숫자의 개수

        String[] secondLine= br.readLine().split(" ");
        int[] array= new int [n];
        for ( int i =0; i< n; i++){
          array[i]=Integer.parseInt(secondLine[i]);
        }

        for(int j=0; j<n; j++){
          if(array[j]<m){
            System.out.printf("%d ",array[j]);
          }
        }
    }
}