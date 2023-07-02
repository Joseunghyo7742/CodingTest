import java.util.*;

class Solution {
    public String solution(String s) {
        String answer = "";
        String [] words= s.split("\\s");
        for(String word : words){
            char first_c= word.charAt(0);
            String temp= word.substring(1,word.length()).toLowerCase();
            
            if((int)'0'<=(int)first_c && (int)first_c<=(int)'9'){
                answer+=Character.toString(first_c);
            }
            else{
                answer+=Character.toString(first_c).toUpperCase();
            }
            answer+=temp;
            answer+=" ";
        }
        answer=answer.trim();
        return answer;
    }
}