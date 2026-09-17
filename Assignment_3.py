def match_resistors(R,n): # leetcode 2sum problem
    def helper(left, right):
        if left >= right:
            return ()
            
        if R[left] + R [right] == n:
            return ((R[left],R[right]),) + helper(left+1, right-1)
        
        elif R[left] + R[right] > n:
            return helper(left, right-1)
            
        elif R[left] + R[right] < n:
            return helper(left+1, right)

    if len(R) < 2:
        return ()
        
    return helper(0, len(R)-1)
    

def match_resistors(R,n): #iterative because python no TCO
    left = 0
    right = len(R) - 1
    pairs = ()
    
    while left < right:
        if R[left] + R [right] == n:
            pairs = pairs + ((R[left], R[right]), )
            left += 1
            right -= 1
            
        elif R[left] + R[right] > n:
            right -= 1
            
        elif R[left] + R[right] < n:
            left += 1
    return pairs
    

def order_meal(n): # Postorder traveral -> left(H) -> right(HF) -> root(base case)
    if n == 0:
        return ('',)
        
    if n == 1:
        return ('H', 'F')
        
    def left(n): 
        if not n:
            return ()
        return (n[0] + 'H',) + left(n[1:])
    def right(n): 
        if not n:
            return ()
        return (n[0] + 'HF',) + right(n[1:])
        
    return left(order_meal(n-1)) + right(order_meal(n-2))

def check(puzzle, mapping):
    def str_2_int(string): # helper function to convert
        num_str = ""
        for char in string:
            for i in range(len(mapping)):
                if mapping[i] == char:
                    num_str += str(i)
        return int(num_str)

    total = 0

    for i in range(len(puzzle)): # iterate though puzzle
        word = puzzle[i]
        if word[0] == mapping[0]: # 0 check
            return False

        if i < len(puzzle) - 1: # tallying total
            total += str_2_int(word)

    if total == str_2_int(puzzle[-1]): # condition check
        return mapping
    else:
        return False

  def unique_letters(puzzle): # smash tgt string then iterate through. could sort then check but its max 10 unique anw.
    unique = ()
    for word in puzzle:
        for char in word:
            exists = False
            for u in unique:
                if u == char:
                    exists = True
                    break
            if not exists:
                unique += (char,)
                
    return unique

def assign(letters, numbers_left, mapping, puzzle):
    if len(letters) == 0: # base case
        return check(puzzle, mapping)
    
    for i in range(len(numbers_left)): # iterate through numbers left
        digit = numbers_left[i] # easier to read
        
        new_numbers_left = numbers_left[:i] + numbers_left[i+1:] # chop out the number being used
        new_mapping = mapping[:digit] + letters[0] + mapping[digit+1:] # update the new mapping

        result = assign(letters[1:], new_numbers_left, new_mapping, puzzle) # go next letters
    
        if result != False: # if it pass the check all g
            return result
            
    return False # not g

def solve(puzzle):
    letters = unique_letters(puzzle)
    numbers_left = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
    mapping = '..........'
    return assign(letters, numbers_left, mapping, puzzle)
    

