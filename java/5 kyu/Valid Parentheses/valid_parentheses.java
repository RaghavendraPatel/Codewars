import java.util.*; 
public class Solution{
  
  public static boolean validParentheses(String parens)
  {
    char[] c = parens.toCharArray();
    Stack<String>s = new Stack<String>();
    for(char i : c){
      try{   
        if(i=='(')
          s.push("(");
        else if(i==')')
          s.pop();
      }
      catch(Exception e){
        return false;
      }
    }
    if(s.empty())
      return true;
    return false;
  }
}
