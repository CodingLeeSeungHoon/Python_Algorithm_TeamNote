import java.util.*;

class Solution {
    static boolean[][] visited;
    static char[][] maze;
    static int[] dx = {1, -1, 0, 0};
    static int[] dy = {0, 0, 1, -1};
    
    public int solution(String[] maps) {
        int answer = 0;
        int xsize = maps.length;
        int ysize = maps[0].length();
        PointLog startPoint = fillStaticVariables(maps, xsize, ysize);
        PointLog leverBfs = bfs(startPoint.getX(), startPoint.getY(), 'L', xsize, ysize);
        if(leverBfs.getMovedCount() == -1){
            return -1;
        }
        
        initVisited(xsize, ysize);
        PointLog exitBfs = bfs(leverBfs.getX(), leverBfs.getY(), 'E', xsize, ysize);
        if(exitBfs.getMovedCount() == -1){
            return -1;
        }
        
        return leverBfs.getMovedCount() + exitBfs.getMovedCount();
    }
    
    public PointLog bfs(int x, int y, char endPoint, int xsize, int ysize){
        Queue<PointLog> queue = new LinkedList<>();
        queue.add(new PointLog(x, y, 0));
        visited[x][y] = true;
        while (!queue.isEmpty()){
            PointLog now = queue.poll();
            int nowX = now.getX();
            int nowY = now.getY();
            int nowMovedCount = now.getMovedCount();
            
            if(maze[nowX][nowY] == endPoint){
                return new PointLog(nowX, nowY, nowMovedCount);
            }
            
            for(int i = 0; i<4; i++){
                int nextX = nowX + dx[i];
                int nextY = nowY + dy[i];
                
                if(!OOB(nextX, nextY, xsize, ysize)){
                    if(!visited[nextX][nextY] && maze[nextX][nextY] != 'X'){
                        queue.add(new PointLog(nextX, nextY, nowMovedCount + 1));
                        visited[nextX][nextY] = true;
                    }
                }
            }
        }
        return new PointLog(-1, -1, -1);
    }
    
    public boolean OOB(int x, int y, int xsize, int ysize){
        if(0 > x || x >= xsize || 0 > y || y >= ysize){
            return true;
        }
        return false;
    }
    
    public void initVisited(int xsize, int ysize){
        for(int i = 0; i<xsize; i++){
            for(int j = 0; j<ysize; j++){
                visited[i][j] = false;
            }
        }
    }
    
    public PointLog fillStaticVariables(String[] maps, int xsize, int ysize){
        visited = new boolean[xsize][ysize];
        maze = new char[xsize][ysize];
        int x = -1;
        int y = -1;
        
        for(int i = 0; i<xsize; i++){
            String line = maps[i];
            for(int j = 0; j<line.length(); j++){
                visited[i][j] = false;
                maze[i][j] = line.charAt(j);
                if(line.charAt(j) == 'S'){
                    x = i;
                    y = j;
                }
            }
        }
        
        return new PointLog(x, y, 0);
    }
}

class PointLog {
    private int x;
    private int y;
    private int movedCount;
    
    public PointLog(int x, int y, int movedCount){
        this.x = x;
        this.y = y;
        this.movedCount = movedCount;
    }
    
    public int getX(){
        return this.x;
    }
    
    public int getY(){
        return this.y;
    }
    
    public int getMovedCount(){
        return this.movedCount;
    }
}