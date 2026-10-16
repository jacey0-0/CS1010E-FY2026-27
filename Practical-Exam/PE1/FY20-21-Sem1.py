#CODE DONE UNDER TIME CRUNCH, DO NOT EXPECT TO BE PERFECT

def encode_I(word):
    letters = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    lookup = {}
    count = 0
    encode = ""
    for letter in letters:
        lookup[letter] = f"{count:02d}"
        count += 1
        
    while len(word) > 0:
        encode = encode + lookup.get(word[0], "99")
        word = word[1:]
        
    return encode
    
def encode_R(word):
    if len(word) < 1:
        return ""
        
    letters = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    count = 0
    lookup = {}
    for letter in letters:
        lookup[letter] = f"{count:02d}"
        count += 1
    return lookup.get(word[0], "99") + encode_R(word[1:])

def decode(msg, offset):
    letters = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ") 
    lookup = {}
    count = 0
    decode = ""
    for letter in letters:
        lookup[letter] = f"{count:02d}"
        count += 1
        
    decoder = {value: key for key, value in lookup.items()}
        
    while len(msg) > 0:
        if msg[0]+msg[1] == "99":
            decode += " "
        else:
            encoded_letter = msg[0]+msg[1]
            val = int(encoded_letter) 
            val = (val - offset) % 26
            decode += decoder.get(f"{val:02d}", "")
        msg = msg[2:]
        
    return decode

def decode_with_love(msg):
    lst = []
    ori_msg = msg
    while len(msg) > 2:
        encoded_letter = msg[0]+msg[1]
        msg = msg[2:]
        encoded_letter2 = msg[0]+msg[1]
        
        val = int(encoded_letter)
        val2 = int(encoded_letter2) 
       
        lst.append((val - val2) % 26)
        
    for i in range(len(lst) - 2):
        if lst[i:i+3] == [23, 19, 17]:
            offset = (int(ori_msg[2 * i: 2 * i + 2]) - 11) % 26
            return decode(ori_msg, offset)

def calculate_areas(w_list, h_list):
    total = [0,0,0]
    for i in range(len(w_list)):
        for j in range(len(h_list)):
            color = (i+j) % 3
            area = (w_list[i] * h_list[j])
            if color == 0: #white
                total[0] += area 
            elif color == 1: # yellow
                total[1] += area 
            elif color == 2: #red
                total[2] += area 
    return tuple(total)

#You do a map then u do (i * j) mod 3 -> EXPLAINATION BELOW
def calculate_areas(w_list, h_list):
    w_white = w_list[0::3] #0
    w_yellow = w_list[1::3] #1
    w_red = w_list[2::3] #2
    h_white = h_list[0::3] #0
    h_yellow = h_list[1::3] #1
    h_red = h_list[2::3] #2
    
    white = sum(w_white) * sum(h_white) + sum(w_yellow) * sum(h_red) + sum(w_red) * sum(h_yellow)
    # (0+0 mod 3 = 0) + (1+2 mod 3 = 0) + (2+1 mod 3 = 0)
    yellow = sum(w_white) * sum(h_yellow) + sum(w_red) * sum(h_red) + sum(h_white) * sum(w_yellow)
    
    red = sum(w_yellow) * sum(h_yellow) + sum(w_white) * sum(h_red) + sum(h_white) * sum(w_red)
    
    return (white,yellow,red)
