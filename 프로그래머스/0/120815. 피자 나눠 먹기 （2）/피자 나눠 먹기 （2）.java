class Solution {
    public int solution(int n) {
       int pizza_num = 6;
       int pizza_pan = 1;
       while(pizza_num % n != 0){
           pizza_pan +=1;
           pizza_num = 6 * pizza_pan;
       }
        return pizza_pan;
    }
}