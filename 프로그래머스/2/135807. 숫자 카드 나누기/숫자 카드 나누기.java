import java.util.*;
import java.lang.Math;

class Solution {
    public int solution(int[] arrayA, int[] arrayB) {
        int answer = 0;
        Arrays.sort(arrayA);
        Arrays.sort(arrayB);
        
        int[] aCandidate = getCandidate(arrayA);
        int[] bCandidate = getCandidate(arrayB);
        
        int result1 = checkCondition(arrayA, arrayB, aCandidate);
        int result2 = checkCondition(arrayB, arrayA, bCandidate);
        
        answer = Math.max(result1, result2);
        
        return answer;
    }
    
    public int[] getCandidate(int[] array){
        int minValue = array[0];
        int lastIdx = (int) Math.pow(minValue, 0.5) + 1;
        TreeSet<Integer> candidateSet = new TreeSet<>(Collections.reverseOrder());
        for(int i = 1; i <= lastIdx; i++){
            if (minValue % i == 0){
                candidateSet.add(i);
                candidateSet.add(minValue / i);
            }
        }
        return candidateSet.stream()
            .mapToInt(Integer::intValue)
            .toArray();
    }
    
    public int checkCondition(int[] array, int[] otherArray, int[] candidate){
        int result = 0;
        ArrayList<Integer> passedCondition = new ArrayList<>();
        for(int i = 0; i < candidate.length; i++){
            int now = candidate[i];
            if(passAllCardsDividedByCardCondition(array, now)){
                passedCondition.add(now);
            }
        }
        
        for(int j = 0; j < passedCondition.size(); j++){
            int now = passedCondition.get(j);
            if(passNoneCardsDividedByCardCondition(otherArray, now)){
                result = now;
                return result;
            }
        }
        
        return result;
    }
    
    private boolean passAllCardsDividedByCardCondition(int[] cardArray, int card){
        for(int i = 0; i<cardArray.length; i++){
            if(cardArray[i] % card != 0){
                return false;
            }
        }
        return true;
    }
    
    private boolean passNoneCardsDividedByCardCondition(int[] cardArray, int card){
        for(int i = 0; i<cardArray.length; i++){
            if(cardArray[i] % card == 0){
                return false;
            }
        }
        return true;
    }
}