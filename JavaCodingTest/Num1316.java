import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
public class Num1316 {
  public static void main(String[] args) throws IOException{
    int result=0; //그룹숫자 카운트
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); //선언
    int n = Integer.parseInt(br.readLine()); //Int
    for(int i=0; i<n; i++){

      String str= br.readLine(); 
      
      for(int j=0; i<str.length(); j++){
        String sub= str.substring(j+2);
        if(sub.indexOf(str.charAt(j))!=-1 && str.charAt(j+1)!= str.charAt(j) ){
          break;
        }
      }
      result++;
      }
      System.out.println(result);
    }
  }

