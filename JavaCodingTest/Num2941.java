import java.util.*;
public class Num2941 {
  public static void main(String[] args){
    Scanner sc= new Scanner(System.in);
    String str= sc.next();
    String[] croatian = {"c=", "c-","dz=", "d-", "lj", "nj", "s=","z="};
    for(String s : croatian){
      str= str.replace(s,"@"); // 	replace​(char oldChar, char newChar): Returns a string resulting from replacing all occurrences of oldChar in this string with newChar
      
    }
    int str_len= str.length(); 
    System.out.println(str_len);
  }
}
