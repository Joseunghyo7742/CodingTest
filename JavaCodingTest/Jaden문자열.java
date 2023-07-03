import java.util.*;

class Solution {
    public String solution(String s) {
        s=s.toLowerCase();
        StringTokenizer st= new StringTokenizer(s, " ", true); 
        // true => flag값으로 구분자도 나눠줌.
        String result= "";
        while(st.hasMoreTokens()){
            String word= st.nextToken();
            if(word.equals(" ")) result+=word;
            else result+=word.substring(0,1).toUpperCase()+word.substring(1);
        }
        return result;
    }
}