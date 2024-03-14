class Solution {
    public int solution(int storey) {
        int answer = 0;
        while (storey > 0) {
            int number = storey % 10;
            storey = storey / 10;
            
            if (number > 5){
                answer += (10 - number);
                storey += 1;
            } else if (number < 5){
                answer += number;
            } else if (storey % 10 >= 5){
                answer += 5;
                storey++;
            } else {
                answer += 5;
            }
        }
        
        return answer;
    }
}