import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
public class Num1316 {
  public static void main(String[] args) throws IOException{
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); //선언
    int n = Integer.parseInt(br.readLine()); //Int
    int result=n; //그룹숫자 카운트

    for(int i=0; i<n; i++){
      boolean[] check= new boolean[26]; // 알파벳이 26자니까 
      String str= br.readLine(); 
      check[(int)str.charAt(0)-97]=true;
      for(int j=1; j<str.length(); j++){
        
        char target= str.charAt(j);
        if(check[(int)target - 97]==false){//알파벳 'a'의 아스키코드는 97 , 만약 아직 나오지 않았던 알파벳이면
          check[(int)target-97]=true;
          continue;
        }
        else{
          if(str.charAt(j-1)!= target){
            result--;
            break;
          }
        }

      }
    }
  System.out.println(result);
  }
}

