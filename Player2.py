import random
from time import sleep

LEFT = (-1,0)
RIGHT = (1,0)
UP = (0,-1)
DOWN = (0,1)
STAY = (0,0)
EMPTY = 0

class player:
    def __init__(self):
        self.step=0
        self.right=0
        self.left=0
        self.up=0
        self.down=0
        self.phase1=0
        self.reach_x=0 
        self.phase2=0   
        self.phase2_y=0

    def move(self,B,N,cur_x,cur_y):
        self.step+=1
        if(self.step==1):
            return (0,0)
        if(self.step==2):
            self.phase1=1
            

        if self.phase1:
            if(cur_x!=10 and self.phase1):
                return self.RUN(cur_x, 10, N)
            else:
                self.phase1=0
                self.phase2_y=(cur_y+6)%N
                
                
        if self.phase2==0:
            if(cur_y!= self.phase2_y):
                return self.make_rect(B, N, 6)
            else:
                self.right=0
                self.left=0
                self.down=0
                self.phase2=1

        if B[cur_x][(cur_y+1)%N]==0:
            return (0,1)

        if B[cur_x][(cur_y+N-1)%N]==0:
            return (0,-1)
        
        if B[(cur_x+1)%N][cur_y]==0:
            return (1,0)

        if B[(cur_x+N-1)%N][cur_y]==0:
            return (-1,0)

        return self.closest_empty(B,N,cur_x,cur_y)


    def RUN(self, cur_x, reach_x, N):
        if reach_x > cur_x:
            if reach_x-cur_x < N/2:
                return RIGHT
            else:
                return LEFT

        if reach_x < cur_x:
            if cur_x-reach_x < N/2:
                return LEFT
            else:
                return RIGHT
    
    def make_rect(self, B, N, size):
        if(self.right != size-1):
            self.right+=1
            return RIGHT
        elif(self.down < size-1):
            self.down+=1
            return DOWN
        elif(self.left != size-1):
            self.left+=1
            return LEFT
        elif(self.up < 2*size-1):
            self.up+=1
            return UP
        self.right=0
        self.left=0
        self.down=0
        self.up=0
        return STAY

    def closest_empty(self,B,N,cur_x,cur_y):
        dis=2*N+1
        best = {"x":cur_x,"y":cur_y}
        for i in range(N):
            for j in range(N):
                if B[i][j] == EMPTY:
                    dx = min ( abs(cur_x - i) , N - abs(cur_x - i) )
                    dy = min ( abs(cur_y - j) , N - abs(cur_y - j) )
                    cur_dis = dx+dy
                    if cur_dis < dis:
                        dis = cur_dis
                        best["x"] = i 
                        best["y"] = j 

        # Pick the direction to go in
        if best["y"] > cur_y:
            if best["y"]-cur_y < N/2:
                return (0,1)
            else:
                return (0,-1)
        if best["y"] < cur_y:
            if cur_y-best["y"] < N/2:
                return (0,-1)
            else:
                return (0,1)
        if best["x"] > cur_x:
            if best["x"]-cur_x < N/2:
                return (1,0)
            else:
                return (-1,0)
        if best["x"] < cur_x:
            if cur_x-best["x"] < N/2:
                return (-1,0)
            else:
                return (1,0)
        return (0,0)
