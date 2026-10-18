#Q1 and Q3, Q2 not bothered. Q3 solution requires hashmap because unsorted and stuff makes all time complexity long if not using hashmao
def encode_I(s1,s2,m): #s1 is the string, s2 is int tuple, m is int
    if len(s1) == 0:
        return ""
    encoded = ""
    while len(s1) > 0:
        encoded +=chr(((ord(s1[0]) - 97) + int(s2[0]) * m) % 26 + 97)
        s1 = s1[1:]
        s2 = s2[1:]
    return encoded

def encode_R(s1,s2,m):
    if len(s1) == 0:
        return ""
    return chr(((ord(s1[0]) - 97) + int(s2[0]) * m) % 26 + 97) + encode_R(s1[1:],s2[1:],m)

def encode_U(s1,s2,m): #weird
    return  "".join(chr(((ord(s1[i]) - 97) + int(s2[i]) * m) % 26 + 97) for i in range(len(s1)))

def min_no_of_turns(L):
    if len(L) == 0:
        return 0
        
    freq = {}
    
    for num in L:
        freq[num] = freq.get(num, 0) + 1
        
    count = 0
    
    for num in freq:
        curr = freq[num]
        prev = freq.get(num-1, 0)
        if curr > prev:
            count += curr - prev
            
    return count

