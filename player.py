import random
opponent_color = 1
my_color = 0
board_size = 8
class MyPlayer:
    '''Hrac hraje prvni tah'''

    def __init__(self, my_color,opponent_color):
        self.my_color = my_color
        self.opponent_color = opponent_color
        # self.number_of_iterations = number_of_iterations
        # self.history =  []
        # self.cur_iteration = 0
        # self.my_points = 0 
        # self.opponent_points = 0 
        # self.avarage_value()       

    def select_move (self, board):
        self.valid_move(board)
        # print(f"from select_move {r=} and {c=}")
        print(self.valid_move)
        return (r, c)


    def valid_in_dir(self,r,c,data,dr,dc):
        count = 0
        color = data[r][c]
        c  += dc 
        r  += dr 
        while(self.not_in_danger(r,c) and color == opponent_color): # color = opponent_color
            c  += dc 
            r  += dr 
            count +=1
        
        if self.not_in_danger(r,c):
            if data[r][c] == my_color:
                return True
        return False

        #pridat podminku,kdyz je konec check if in danger or color = -1  
        
    def valid_move(self,data):
        for r in range (8):
            for c in range (8):
                if data[r][c] == -1:
                    directions = [(0,1),(1,0),(-1,0),(0,-1),(1,1),(-1,-1),(-1,1),(1,-1)]
                    for dx in directions:
                        if self.valid_in_dir(r,c,data, dx[0],dx[1]):
                            print(f"{r=},{c=}")
                            break
                    return r,c # returns the first found -1

    def not_in_danger(self,r,c):
        if( r >= 0 and r < board_size and c > 0 and c < board_size):
            return True
        return False                        




    # def region_size (r,c,data):                                                                                                                                                                                       
    #     directions = [(0,1),(1,0),(-1,0),(0,-1),(1,1),(-1,-1),(-1,1),(1,-1)]
    #     count = 1
    #     for dx in directions:
    #         count += line_size_in_dir(r,c,data, dx[0],dx[1])

    #     return count
        

    # def line_column_size(r,c,data):
    #     count = 1
    #     count += line_size_in_dir(r,c,data,0,1)
    #     count += line_size_in_dir(r,c,data,1,0)
    #     count += line_size_in_dir(r,c,data,0,-1)
    #     count += line_size_in_dir(r,c,data,-1,0)

    #     return count 


    





if __name__ == "__main__" :
    r=2
    c=6
    board = [ 
    [1, 0, 0, 0, 1, 1, 0, 0 ] , 
    [1, 1, -1, 0, 0, 1, -1, 1 ] , 
    [0, 1, 0, 0, 1, 1, 1, 1 ] , 
    [0, -1, 0, 1, 0, 1, 1, 1 ] , 
    [0, 1, 1, 0, 0, 0, -1, 1 ] , 
    [1, 0, 0, 0, -1, 1, 0, 0 ] , 
    [0, 0, -1, 0, 1, 1, 1, 0 ] , 
    [0, 0, 1, 0, 1, 0, 1, 0 ]] 
        
    Matrix_1 = MyPlayer(0,1)
    Matrix_1.select_move(board)


    
#__init__	my_color (moje barva), opponent_color (barva soupeře)	
   #select_move	board (n x n matice hrací plochy)	
   # vystup: r, c (row, column souřadnice Vašeho tahu v tuple(n-tici) se dvěma inty)
   

   

#for generator
    # row = 4 
    # col = 5
    # data = generate_data(row,col)

    # line_size_in_dir(r,c,data,0,-1)

    # reg_size = region_size(r,c,data)
    # print(reg_size) 

    # print(line_size_in_dir(r,c,data, 1, -1)) 



#join soujuje v seznamu prvky
#"ahoj".join(["1"," ","2"])
# #def format_data(matrix):
#     result = ""
#     for row in matrix:
#         for elem in row:
#            result.append(str(elem))
#            result.append(" ")
#         # print()
#         result.append("\n")
#     return "".join(result)