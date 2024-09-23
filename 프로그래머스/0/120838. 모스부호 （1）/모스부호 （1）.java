class Solution {
    public String solution(String letter) {
        String result = "";
        String[] mosArr = {".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."};
       String[] letterArr = letter.split(" ");
        
        for(int i = 0;i<letterArr.length;i++){
            for(int j = 0;j<mosArr.length;j++){
                if(letterArr[i].equals(mosArr[j])){
                    result += (char)(j+'a');
                    break;
                }
            }
        }
        return result;
    }
}