def derivative(f):
    def dx(x):
        return (f(x+1e-5)-f(x))/1e-5 
    return dx

def alphabet_to_digit(c):
    return ord(c) % 32 #look ascii and derive

def convert_prefix(prefix):
    prefix = ('@' + prefix)[-2:] # pad with any multiple of 32 then grab last 2
    return tuple(map(alphabet_to_digit, prefix)) 

def convert_num_series(num_series):
    num_series = '000' + num_series
    num_series = num_series[-4:] 
    
    return tuple(map(int, num_series))
  
def multiply_and_add_ho(multiplier):
    def int_series(series):
        return reduce(lambda acc, val: acc + val, map(lambda m, s: m * s, multiplier, series))
    return int_series 

def remainder_to_checksum_letter(remainder):
    checksum = ('A', 'Z', 'Y', 'X', 'U', 'T', 'S', 'R', 'P', 'M', 'L', 'K', 'J', 'H', 'G', 'E', 'D', 'C', 'B') 
    return checksum[remainder]

def checksum_calculator_ho(multiplier):
    calc_sum = multiply_and_add_ho(multiplier)
    
    def calc(str_series):
        prefix = reduce(lambda acc, val:acc + val, filter(lambda c: not('0' <= c <= '9'), str_series), '')
        num_series = reduce(lambda acc, val:acc + val, filter(lambda c: '0' <= c <= '9', str_series), '')
        
        prefix_tuple = convert_prefix(prefix)
        num_series_tuple = convert_num_series(num_series)
        series = prefix_tuple + num_series_tuple
        remainder = calc_sum(series) % 19
        return remainder_to_checksum_letter(remainder)
    return calc

def sum1(seq):
    reduce(lambda total, value:(total+value, print(f"{value},{total+value}@"))[0], seq ,0) #just use the 1st element of tuple to print while using reduce to iterate through the seq
    return

def sum2(seq):
    acc_seq = tuple(map(lambda i: sum(seq[0:i+1]), range(len(seq)))) # map accumalated sum 
    tuple(map(lambda value, total:print(f"{value},{total}@"), seq, acc_seq)) # print accumalated and current
    print(f"{max(acc_seq, default=0)}@") # use max to find max accumalated sum
    return

def sum3(seq):
    acc_seq = reduce(lambda total, value:
                    (total+(max(total[-1],0)+value,), # store the new total at the end of the tuple
                    print(f"{value},{max(total[-1],0)+value}@"))[0], # value + 0 or prev max value, use the 2nd element of the tuple to execute print
                    seq, (0,))
    print(f"{max(acc_seq[1:], default=0)}@")
    return

def sum4(lst):
    acc_seq = reduce(lambda total, value:
                    (total+(max(total[-1],0)+value,), # store the new total at the end of the tuple
                    print(f"{value},{max(total[-1],0)+value}@"))[0], # value + 0 or prev max value, use the 2nd element of the tuple to execute print
                    lst, (0,))
    acc_seq = acc_seq[1:] # remove first element
    
    max_sum = max(acc_seq)
    for i in range(len(acc_seq)-1,-1,-1): #cant use break so need to iterate through the whole thing backwards.
        if acc_seq[i] == max_sum:
            end = i

    start = end
    while start > 0 and acc_seq[start-1] > 0: #working backwords
        start-=1
    print(f"{max_sum}({start+1},{end+1})@")
    

