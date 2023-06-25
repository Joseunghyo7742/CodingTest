
import java.io.*;

public class Num10798 {
  public static void main(String[] args)throws IOException{
    BufferedReader br= new BufferedReader(new InputStreamReader(System.in));
    char [][] charArray= new char[5][15];
    for(int i=0; i<5; i++){
      char[] firstLine= br.readLine().toCharArray();
      for(int j=0; j<firstLine.length; j++){
        charArray[i][j]= firstLine[j];
      }
    }
    for(int i=0; i<charArray[0].length; i++){
      for(int j=0; j<5; j++){
        if(charArray[j][i]==0) //char '0' 인거랑 0은 다르니까
          continue;
        else{
          System.out.print(charArray[j][i]);
        }
      }    
    }
  }

    // char[] firstLine= br.readLine().toCharArray(); //첫 줄 입력받음
    // char[][] charArrays= new char[firstLine.length][5];
    // for(int i=0; i<firstLine.length; i++){
    //   charArrays[i][0]=firstLine[i];
    // }
    // for(int i=1; i<5; i++){
    //   char [] readLine= br.readLine().toCharArray();
    //   for(int j=0; j<firstLine.length; j++){
    //     if(j>=readLine.length){
    //       charArrays[j][i]='#';
    //       continue;
    //     }
    //     charArrays[j][i]= readLine[j];
    //   }
    //   }
    
    //   for(int i=0; i<firstLine.length; i++){
    //     for(int j=0; j<5; j++){
    //       if(charArrays[i][j]=='#')
    //         continue;
    //       else{
    //         System.out.print(charArrays[i][j]);
    //       }
    //     }
    //   }
    // }
  }
