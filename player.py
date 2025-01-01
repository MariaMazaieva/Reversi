class MyPlayer:
    """PLayer makes a move dapending on its weight"""

    def __init__(self, my_color, opponent_color):
        self.my_color = my_color
        self.opponent_color = opponent_color
        self.board = [
        [30,  3,  20,  15,  15,  20,   3,  30],  
        [ 3,   1,   6,   6,   6,   6,   1,   3],  
        [20,   6,  12,   9,   9,  12,   6,  20],  
        [15,   6,   9,   11,   11,   9, 6, 15],  
        [15,   6,   9,   11,   11,   9, 6, 15],  
        [20,   6,  12,   9,   9,  12,   6,  20],  
        [ 3,   1,   6,   6,   6,   6,   1,   3],  
        [30,   3,  20,  15,  15,  20,   3,  30]   
        ]

    def select_move(self, board):
        return self.valid_move(board)

    def valid_in_dir(self, r, c, data, dr, dc):
        """Returns number of skipped stones, 0 otherwise"""
        count = 0
        r += dr
        c += dc

        while self.not_in_danger(r, c) and data[r][c] == self.opponent_color: #skipped enemy stone
            count += 1
            r += dr
            c += dc

        if self.not_in_danger(r, c): #ending with my_color stone
            if data[r][c] == self.my_color:
                return count
        return 0
    
    def check_opponent_rocks(self, r, c, data, dr, dc):
        """Returns number of opponents skipped stones, 0 otherwise"""
        count = 0
        r += dr
        c += dc

        while self.not_in_danger(r, c) and data[r][c] == self.my_color: 
            count += 1
            r += dr
            c += dc

        if self.not_in_danger(r, c):
            if data[r][c] == self.opponent_color: 
                return count

        return 0

    def valid_move(self, data):
        """Finds the best move, considering the opponent's possible gain"""
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (-1, -1), (-1, 1), (1, -1)]
        best_move = None
        max_flips = 0 #used for best_move
        max_flips_2 = 0 #used for second best_move
        min_opponent_gain = float('inf')
        second_best_move = None

        for r in range(8):
            for c in range(8):
                if data[r][c] == -1:  # Check for empty cells
                    total_flips = 0
                    for dr, dc in directions:
                        total_flips += self.valid_in_dir(r, c, data, dr, dc)

                    if total_flips > 0:  # Valid move
                        if (r,c) == (0, 0) or (r, c) == (0, 7) or (r, c) ==(7, 0) or (r, c) ==(7, 7):
                                return (r, c)
                        
                        if total_flips * self.board[r][c] > max_flips:
                            max_flips = total_flips * self.board[r][c]
                            second_best_move, max_flips_2 = best_move, max_flips
                            best_move = (r,c) 

                        #avoids those moves if possible
                        # if (r, c) in [(0, 1), (1, 0), (1, 1), (0, 6), (1, 6), (1, 7),
                        #     (6, 0), (6, 1), (7, 1), (6, 6), (7, 6), (6, 7)] and second_best_move !=None: 
                        #     continue


                        best_move = self.find_best_move(best_move, second_best_move, data, max_flips, max_flips_2)
        return best_move
    
    def find_best_move(self, best_move, second_best_move, data, max_flips, max_flips_2):
        """Finds the better move between the best and second best options"""
        opponent_gain = float('inf')  
        opponent_gain_2 = float('inf')  

        if best_move is not None:
            best_r, best_c = best_move
            simulated_board = self.simulate_move(data, best_r, best_c)
            opponent_gain = self.opponent_gain(simulated_board)

        if second_best_move is not None:
            second_r, second_c = second_best_move
            simulated_board = self.simulate_move(data, second_r, second_c)
            opponent_gain_2 = self.opponent_gain(simulated_board)

        if best_move is not None and second_best_move is not None:
            if opponent_gain < opponent_gain_2:
                return best_move
            elif opponent_gain > opponent_gain_2:
                return second_best_move
            else:  #If tie: judge by max_flips
                return best_move if max_flips >= max_flips_2 else second_best_move
        else:
            return best_move or second_best_move


    
    def simulate_move(self, board, r, c):
        """Makes a move and returns new copy-board"""
        if not (0 <= r < 8 and 0 <= c < 8 and board[r][c] == -1):
            return board
        new_board = [row[:] for row in board]  # copy of the board
        new_board[r][c] = self.my_color
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (-1, -1), (-1, 1), (1, -1)]
        
        for dr, dc in directions:
            self.flip_stones(new_board, r, c, dr, dc)
        return new_board

    def flip_stones(self, board, r, c, dr, dc):
        """Flips stones in the given direction for func simulate_move"""
        stones_to_flip = []
        r += dr
        c += dc

        while 0 <= r < 8 and 0 <= c < 8 and board[r][c] == self.opponent_color:
            stones_to_flip.append((r, c))
            r += dr
            c += dc

        if 0 <= r < 8 and 0 <= c < 8 and board[r][c] == self.my_color:
            for rx, cx in stones_to_flip:
                board[rx][cx] = self.my_color

    def opponent_gain(self, board):
        """Counts number of opponent stones"""
        max_opponent_gain = 0

        for r in range(8):
            for c in range(8):
                if board[r][c] == -1:  # Check empty cells
                    total_flips = 0
                    directions = [(0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (-1, -1), (-1, 1), (1, -1)]
                    for dx in directions:
                        total_flips += self.check_opponent_rocks(r, c, board,dx[0], dx[1])
                        if total_flips > 0 and total_flips * self.board[r][c]> max_opponent_gain: 
                                max_opponent_gain = total_flips * self.board[r][c]
                                total_flips = 0
        return max_opponent_gain
    
    def not_in_danger(self, r, c):
        """Checks if r or c is out of board size"""
        if r >= 0 and r < 8 and c >= 0 and c < 8:
            return True
        return False


if __name__ == "__main__":
    board = [
        [-1, -1, -1, 1, 1, -1, -1, -1],
        [-1, -1, -1, -1, -1, 1, -1, -1],
        [-1, -1, -1, 1, -1, -1, -1, -1],
        [-1, -1, 0,  0,  0,  -1, 1, -1],
        [-1, -1, -1, 1, -1,  -1, -1, -1],
        [-1, -1,-1,  1, -1,  -1, -1, -1],
        [-1, -1,-1, -1, -1, -1, -1, -1],
        [-1, -1, -1,-1, -1, -1, -1, -1]
    ]

    Matrix_1 = MyPlayer(0, 1)
    # print(f"Player selected: {Matrix_1.select_move(board)}")


