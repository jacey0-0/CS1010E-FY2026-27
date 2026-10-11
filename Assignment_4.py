#Q1
def set_smooth(left, centre, right):
    valid = abs(left + centre + right - 1.0) <= 1e-12 #flt error correction
    def smoother(wave):
        if not valid: #check for invalid case
            return wave
        
        n = len(wave) 
        if n == 0: #check for list of none
            return wave
    
        ctr_val = 0 #ini as 0 for left_val base case
        
        for i in range(n):
            left_val = ctr_val
            right_val = wave[i+1] if i < n - 1 else 0 #take care of over right val
            ctr_val = wave[i]
            wave[i] = int(left * left_val + centre * ctr_val + right * right_val) # formula
        return wave
    return smoother


def smooth_transformer(parameter_list, repetition_list):
    def transformer(wave):
        if not parameter_list or not repetition_list or not wave: #check for invalids
            return wave
            
        for i in range(len(parameter_list)): #param list & repetition list is the same length so no data cleanup needed
            params = parameter_list[i] #data extraction
            rep = repetition_list[i]
            left, centre, right = params
          
            smoother = set_smooth(left, centre, right) #applying to func
            
            for _ in range(rep): #repeating for rep val
                    wave = smoother(wave)
        return wave
    return transformer

#Q2
def flatten_with_depth(lst):
    depth = 0
    result = []
    
    def traverse_nested(lst, depth): #simple recursive list traversal with depth counter
        for i in lst:
            if type(i) is list: #if its still a list then go deeper else append to result
                traverse_nested(i, depth + 1)
            else:
                result.append((depth, i))
                
    traverse_nested(lst, depth)
    return result

def nested_from_depth(ddata):
    if not ddata: #check for empty
        return []
        
    data = []
    
    for i in ddata: #iterate through ddata
        depth, value = i 
        
        if type(depth) is not int or depth < 0:
            raise ValueError("Depth must be a non-negative integer")

        if type(value) not in (int, float):
            raise ValueError("Value must be numerical")
            
        curr = data # Reference to the current nesting level
        
        for _ in range(depth): #go to the last value of nested list of depth then append
            if len(curr) == 0 or type(curr[-1]) is not list: #if there is nth there then make a list
                curr.append([])

            curr = curr[-1] #go to last
            
        curr.append(value) #plug in value then go to next val

    return data

#Q3
def is_ancestor(name1, name2, pdict): # check if name1 is an ancestor of name2
    if name1 == name2:
        return False
    curr = name2
    visited = {}
    
    while curr in pdict:
        if curr in visited:
            return False
            
        visited[curr] = True   
        curr = pdict[curr]
        if curr == name1:
            return True
        
    return False

def is_related(name1, name2, pdict):
    if name1 == name2:
        return name1 in pdict or name1 in pdict.values()
        
    curr = name2
    visited = {}

    while curr in pdict and curr not in visited:
        visited[curr] = True
        curr = pdict[curr]

    visited[curr] = True

    curr = name1
    checked = {}

    while curr in pdict and curr not in checked:
        if curr in visited:
            return True

        checked[curr] = True
        curr = pdict[curr]

    return curr in visited
