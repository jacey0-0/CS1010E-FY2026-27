#DONE UNDER TIMECRUNCH, CODE IS UGLY. VERY DIFFICULT IMO. Q2 NOT DONE CAUSE OOP EW. Q3 IS TREE TRAVERSAL-ESQUE QUESTION
def super_fib_R(term2, n):
    if n == 3:
        return [1, term2, term2 + 1]
    if n == 2:
        return [1, term2]
    if n == 1:
        return [1]
        
    previous = super_fib_R(term2, n-1)
    return previous + [previous[-1]*2]

def super_fib_I(term2, upper):
    current = 1
    fib_list = []
    while current <= upper:
      #WTHELLY IS THIS
        if len(fib_list) == 0:
            fib_list = [1]
        if len(fib_list) == 1:
            fib_list = [1, term2]
        if len(fib_list) == 2:
            fib_list = [1, term2, term2 + 1]
        else:
            fib_list += [fib_list[-1] * 2]
        
        current = fib_list[-1]
    #I think there is a btr way but im lazy
    return [x for x in fib_list if x <= upper]
        
def smallest_second(n):
    if n == 1:
        return 1

    while n % 2 == 0 and n > 2:
        n //= 2

    return n - 1

def equal_to(lhs, rhs, ops):
    def generate(f, index):
        if index == len(lhs):
            return [f]

        result = []

        for op in ops + " ":
            if op == " ":
                result += generate(f + lhs[index], index + 1)
            else:
                result += generate(f + op + lhs[index], index + 1)

        return result
    
    return set(x + "="+str(rhs) for x in generate(lhs[0], 1) if eval(x) == rhs)
