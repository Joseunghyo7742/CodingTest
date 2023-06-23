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