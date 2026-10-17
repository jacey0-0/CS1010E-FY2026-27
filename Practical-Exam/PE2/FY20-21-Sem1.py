#DONE UNDER TIME CRUNCH, CODE IS VERY UGLY. Q3 EXPLAINATION: https://leetcode.com/problems/game-of-life/solutions/7161780/beats-100-in-place-constant-space-java-c-vtbn/
#FORCED TO USE SPACE COMPLEXITY O(M⋅N)

def extract_parentheses_I(stmt):
    str_p = ""
    for i in stmt:
        if i == "(" :
            str_p += "("
        if i == ")":
            str_p += ")"
        
    return str_p

def extract_parentheses_R(stmt):
    if len(stmt) == 0:
        return ""
    elif stmt[0] == "(" :
        return "(" + extract_parentheses_R(stmt[1:])
    elif stmt[0] == ")" :
        return ")" + extract_parentheses_R(stmt[1:])
    else:
        return extract_parentheses_R(stmt[1:])
    

def check_balanced(stmt):
    str_p = ""
    count1 = 0
    for i in stmt:
        if i == "(" :
            count1 += 1
        if i == ")":
            count1 -= 1
        if count1 < 0:
            return False
            
    if count1 == 0:
        return True
    else:
        return False

def most_expensive_burger(money, price_dict):
    c_price_dict = price_dict.copy()
    if money < min(price_dict.values()):
        return ('', money)
        
    burger = "B"
    #Just declare a var ingredient so u dont call the same expression so many times
    while c_price_dict and money >= min(c_price_dict.values()): # if money is more or equals to the lowest)
        while money < max(c_price_dict.values()): #if max is more than the money
            c_price_dict.pop(max(c_price_dict, key=c_price_dict.get)) # remove most expensive
            
        
        burger += max(c_price_dict, key=c_price_dict.get)
        money -= max(c_price_dict.values())
        c_price_dict.pop(max(c_price_dict, key=c_price_dict.get))
        
    return (burger + "B", money)

def add_cells(board, cell_list): 
    for cell in cell_list:
        i = cell[0]
        j = cell[1]
        if 0 <= i < len(board) and 0 <= j < len(board[0]):
            board[i][j] = 1

    
    
def step(board):
    next_board = [row.copy() for row in board]
    m = len(board)
    n = len(board[0])

    neighbours = [
        (-1, 1), (0, 1), (1, 1),
        (-1, 0),         (1, 0),
        (-1,-1), (0,-1), (1,-1)
    ]

    for i in range(m):
        for j in range(n):
            live = 0

            for dr, dc in neighbours:
                r = i + dr
                c = j + dc

                if 0 <= r < m and 0 <= c < n:
                    if board[r][c] == 1:
                        live += 1

            if live == 3 and board[i][j] == 0:
                next_board[i][j] = 1

            if live < 2 and board[i][j] == 1:
                next_board[i][j] = 0

            if live > 3 and board[i][j] == 1:
                next_board[i][j] = 0

    return next_board
