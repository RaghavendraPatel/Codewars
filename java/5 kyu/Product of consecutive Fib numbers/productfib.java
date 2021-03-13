public class ProdFib { // must be public for codewars 
  
  public static long[] productFib(long prod) {
    long curr = 0,next = 1;
    while(curr*next<prod){
      next = next + curr;
      curr = next - curr;
    }
    return new long[] {curr, next, curr*next == prod ? 1:0};
   }
}
