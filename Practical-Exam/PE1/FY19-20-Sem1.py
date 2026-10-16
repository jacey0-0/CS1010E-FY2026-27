#DID UNDER TIME CRUNCH DO NOT EXPECT PERFECT CODE
def sum_digit_square_I(n):
    total = 0
    while n > 0:
        total += (n % 10)**2
        n = n // 10
    return total
    
def sum_digit_square_R(n):
    if n == 0:
        return 0
    return (n % 10)**2 + sum_digit_square_R(n // 10)

def is_happy_number(n):
    def sum_digit_square_I(n):
        total = 0
        while n > 0:
            total += (n % 10)**2
            n = n // 10
        return total
    
    visited = []
    while True:
        n = sum_digit_square_I(n)
        if n == 1:
            return True
        elif n in visited:
            return False
        visited.append(n)
        
def all_happy_number(n,m):
    def is_happy_number(n):
        def sum_digit_square_I(n):
            total = 0
            while n > 0:
                total += (n % 10)**2
                n = n // 10
            return total
        check = n
        visited = []
        while True:
            check = sum_digit_square_I(check)
            if check == 1:
                return n
            elif check in visited:
                return None
            visited.append(check)
    if n > m:
        temp = n
        n = m
        m = temp
    
    lst = [result for result in map(is_happy_number, range(n, m + 1)) if result is not None]
 
    return lst

def is_unique(seq):
    cnt = 0
    for i in seq:
        if i in seq[cnt+1:]:
            return False
        cnt += 1
    return True

    
