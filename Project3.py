class Hexagon_graph:
    def __init__(self):

        #create empty graph map for the game and set a temporey position for both Human and Ai player
        self.ai=1
        self.human=2
        self.target_depth=2
        self.graph=[[0,0,0,0,0,0],
                    [0,0,0,0,0,0],
                    [0,0,0,0,0,0],
                    [0,0,0,0,0,0],
                    [0,0,0,0,0,0],
                    [0,0,0,0,0,0]]
    

#function loop through the player moveset found and detect if any of these moveset are connect to each other
    def cycle_check(self, index_x, map, player):
        
        for x in map:
            indi=map[-1]
            map.pop

            if (self.graph[x-1][indi-1]==player and self.graph[indi-1][x-1]==player):
                return True
        return False
        
   

#Function verify if the current player has created a triangle cycle
    def check_win(self):

        indi= []

        #checks for ai player
        for x in range(len(self.graph)):
            for y in range(len(self.graph[x])):
                if self.graph[x][y] == self.ai:
                    indi.append(y+1)
            if self.cycle_check(x, indi,self.ai):
                return -10
            else: indi.clear()
        
        indi.clear()

        #checks for human player
        for x in range(len(self.graph)):
            for y in range(len(self.graph[x])):
                if self.graph[x][y] == self.human:
                    indi.append(y+1)
            if self.cycle_check(x, indi,self.human):
                return 10
            else: indi.clear()

        return None


    #minimax function that will recurisve through until a certain depth level
    def minimax(self, board, depth,flag):

        #check wether the states of the board is a win condition for either the ai or human player
        total = self.check_win()
        if total:
            return total

        final_score =0 
        if flag == True:
            final_score=-500
            
            # loop through all possible moved anand test it scoring values through minimax
            for x in range(len(board)):
                for y in range(len(board[x])):

                    #ignores moves set by itself
                    if x == y:
                        continue
                    
                    #when possible mov is found check it value by doing minimax recursion for Ai player
                    if board[x][y]==0:
                        #temporary change index for Ai player move and change it back when minimax has found the value
                        board[x][y]=self.ai
                        board[y][x]=self.ai


                        score=self.minimax( board, depth+1,False)


                        board[x][y]=0
                        board[y][x]=0

                        final_score= max(score, final_score)
            return final_score
        
        else:

            final_score=500
            
            # loop through all possible moved anand test it scoring values through minimax
            for x in range(len(board)):
                for y in range(len(board[x])):

                    #ignores moves set by itself
                    if x == y:
                        continue

                    #when possible mov is found check it value by doing minimax recursion for human player
                    if board[x][y]==0:

                        #temporary change index for human player move and change it back when minimax has found the value
                        board[x][y]=self.human
                        board[y][x]=self.human


                        score=self.minimax( board, depth+1,True)

                        board[x][y]=0
                        board[y][x]=0
                        final_score=min(score, final_score)
            return final_score

    #function work in deciding a move set to choose from for the ai player
    def next_moved(self):
        
        final_score= -500
        score = 0
        # loop through all possible moved anand test it scoring values through minimax
        for x in range(len(self.graph)):
            for y in range(len(self.graph[x])):

                #check wether the vertex has already being taken 
                if x == y:
                    continue
                
                #when possible mov is found check it value by doing minimax recursion for Ai player
                if self.graph[x][y]==0:
                        
                    
                    self.graph[x][y]=self.ai
                    self.graph[y][x]=self.ai

                    score = self.minimax(self.graph, 0, False)
                    print("****Ai is thinking of a move****")

                    self.graph[x][y]=0
                    self.graph[y][x]=0

                    if(score > final_score):
                        final_score= score
                        container =[x, y ]

        self.graph[container[0]][container[1]]=self.ai
        self.graph[container[1]][container[0]]=self.ai
        
        return
    
    #Function assing player position for ai and human
    def player_dec(self, player):
        if int(player) == 1:
            self.ai=1
            self.human=2
            return
        else:
            self.ai=2
            self.human=1

    #function adds the desired move from the human player to the adjencecy matrix
    def human_moved(self, v1, v2):

        if (int(v1)>6 or int(v1) < 0) or (int(v2)>6 or int(v2) < 0):
            print("Vertex are outside of the board")
            return True
        elif self.graph[int(v1)-1][int(v2)-1]==0 and self.graph[int(v2)-1][int(v1)-1]==0:
            self.graph[int(v1)-1][int(v2)-1]= self.human
            self.graph[int(v2)-1][int(v1)-1]=self.human
            return False
        else:
            print("Asingment is already take")
            return True

    #Function prints the current board map
    def print_graph(self):
        for x in range(len(self.graph)):
            print(self.graph[x])
        return        

    def play_session(self):

        print("Welcome to my Hexagon game:")
        print("Which player would you be the ai? Player 1 or Player 2 ")
        ans=input()
        self.player_dec(ans)

        print("Games session start: ")

        track=True
        while track:
            if self.ai == 1:
                
                print("AI turn")
                self.next_moved()

                win_status=self.check_win()
                if win_status!=None and win_status>0:
                    print("Player Ai won")
                    self.print_graph()
                    track=False
                    break

                print("Your turn now:")
                print("Map: ")
                self.print_graph()
                print("Pick two vertex to connect: ")
                a, b=input().split()
                self.human_moved(a, b)

                while self.human_moved(a,b):
                    print("Enter valide vertex")
                    a,b=input().split()

                win_status=self.check_win()
                if win_status!=None and win_status<0:
                    print("You won the game")
                    self.print_graph()
                    track=False
                    break
                
                return
            else:

                print("Your turn now:")
                print("Map: ")
                self.print_graph()
                print("Pick two vertex to connect: ")
                a, b=input().split()

                while self.human_moved(a,b):
                    print("Enter valide vertex")
                    a,b=input().split()

                win_status=self.check_win()
                if  win_status!=None and win_status<0:
                    print("You won the game")
                    self.print_graph()
                    track=False
                    break


                print("AI turn")
                self.next_moved()

                win_status=self.check_win()
                if win_status!=None and win_status<0:
                    print("Player Ai won")
                    self.print_graph()
                    track=False
                    break
            
        return

def main():

    hex=Hexagon_graph()
    hex.play_session()    

    return

main()