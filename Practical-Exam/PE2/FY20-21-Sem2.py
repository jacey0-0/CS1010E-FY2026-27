#DID UNDER TIMECRUNCH, CODE IS UGLY. Q1 Easy, Q2 Explaination is nonsense. is_cousin only checks for FIRST cousin, nth cousin is nth cousin, cousin-removed doesnt exist. Q3 is DFS traversal (impossible to do in 2hr istg)
def derivative_I(poly):
    d_poly = []
    i = len(poly) - 1

    while i >= 0:
        d_poly += [i * poly[i]]
        i -= 1
    d_poly = d_poly[:-1]
    d_poly = d_poly[::-1]
  
    return d_poly

def derivative_R(poly):
    if len(poly) == 1:
        return []
    if len(poly) == 0:
        return []
    i = len(poly) - 1
    
    return  derivative_R(poly[:-1]) + [i * poly[i]]

def newton(poly, x0):
    def eval_poly(poly, x):
        ttl = 0
        for i in range(len(poly)):
            ttl += poly[i]*x**i
        return ttl
        
    d_poly = derivative_I(poly)
    while True:
        Px0 = eval_poly(poly, x0)
        
        if abs(Px0) < 0.00001:
            return x0
        
        x0 -= Px0 /eval_poly(d_poly, x0)

  def is_cousin(name1, name2, tree): #can be done easier i just did nth cousin first so cpy pasted the sol
    if name1 == name2:
        return False
        
    tree1 = [name1]
    tree2 = [name2]
    current = name1
    
    while current in tree:
        parent = tree.get(current)
        tree1.append(parent)
        current = parent
    
    current = name2
    
    while current in tree:
        parent = tree.get(current)
        tree2.append(parent)
        current = parent
    
    if len(tree1) < 3 or len(tree2) < 3:
        return False
    
    if tree1[1] == tree2[1]:
        return False
    i = 2
    
    while i < len(tree1) and i < len(tree2):
        if tree1[i] == tree2[i] and i < 3:
                return True
                
        i += 1
        
    return False

def nth_cousin(name1, name2, tree):
    if name1 == name2:
        return - 1
        
    tree1 = [name1]
    tree2 = [name2]
    current = name1
    
    while current in tree:
        parent = tree.get(current)
        tree1.append(parent)
        current = parent
    
    current = name2
    
    while current in tree:
        parent = tree.get(current)
        tree2.append(parent)
        current = parent
    
    if len(tree1) < 3 or len(tree2) < 3:
        return -1
    
    if tree1[1] == tree2[1]:
        return -1
    
    i = 2
    
    while i < len(tree1) and i < len(tree2):
        if tree1[i] == tree2[i]:
                return i - 1
                
        i += 1
        
    return -1
