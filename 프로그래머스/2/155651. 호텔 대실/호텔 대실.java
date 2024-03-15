import java.util.*;
import java.lang.Math;

class Solution {
    public int solution(String[][] book_time) {
        int answer = 0;
        int timeTableSize = 24 * 60 + 10;
        int[] timeTable = new int[timeTableSize];
        
        int inputSize = book_time.length;
        
        for(int i = 0; i<inputSize; i++){
            int startIdx = convertToSecond(book_time[i][0]);
            int endIdx = convertToSecond(book_time[i][1]) + 10;
            for (int j = startIdx; j<endIdx; j++){
                timeTable[j]++;
            }
        }
        
        Arrays.sort(timeTable);
        return timeTable[timeTableSize-1];
    }
    
    private int convertToSecond(String time){
        String[] splitedTime = time.split(":");
        return Integer.parseInt(splitedTime[0]) * 60 + Integer.parseInt(splitedTime[1]);
    }
}