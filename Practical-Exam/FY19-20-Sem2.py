#DID IT UNDER TIMECRUNCH, DO NOT EXPECT PERFECT CODE
def rotate(bouquet, step):
    step = step % len(bouquet)
    return  bouquet[step:] + bouquet[:step]

def flower_I(bouquet, k):
    flower = ""
    while len(bouquet) > 0:
        bouquet = rotate(bouquet, k - 1)
        flower = flower + str(bouquet[0])
        bouquet = bouquet[1:]
    return flower

def flower_R(bouquet, k):
    if len(bouquet) == 0:
        return ""
    if len(bouquet) > 0:
        bouquet = rotate(bouquet, k - 1)
    return str(bouquet[0]) + flower_R(bouquet[1:], k)

def pink_rose(bouquet):
    if 'P' not in bouquet:
        return -1

    cnt = 1
    while cnt < 100:
        if 'P' == flower_I(bouquet, cnt)[-1]:
            return cnt
        else:
            cnt += 1
        
        
def make_bouquet(shop, number):
    pink_check = False
    pink = []
    for i in range(len(shop)):
        if shop[i][0] == 'P' and shop[i][1] <= number:
            pink_check = True
            pink.append(shop[i][1])
    
    if pink_check == False:
        return False
        
    check = []
    
    for i in pink:
        check.append(number - i)
        
    for n in check:
        for bundle in shop:
            if n - bundle[1] == 0:
                return True
            elif n - bundle[1] > 0:
                for bundle2 in shop:
                    if n - bundle2[1] - bundle[1] == 0:
                        return True
                    
    return False

        
def minimum_cost(shop, number):
    pink_check = False
    pink = []
    bundle_perm = []
    for i in range(len(shop)):
        if shop[i][0] == 'P' and shop[i][1] <= number:
            pink_check = True
            pink.append(shop[i])
    
    if pink_check == False:
        return -1
        
    check = []
    
    for i in pink:
        check.append(number - i[1])
        
    counter = 0
    
    for n in check:
        for bundle in shop:
            if n - bundle[1] == 0:
                bundle_perm.append(pink[counter][2] + bundle[2])
            elif n - bundle[1] > 0:
                for bundle2 in shop:
                    if n - bundle2[1] - bundle[1] == 0:
                        bundle_perm.append(pink[counter][2] + bundle[2] + bundle2[2])
        counter += 1
        
    return min(bundle_perm) if len(bundle_perm) > 0 else -1
    
    

from random import *

def paint_area(S, C, D):
    def inside_pink_area(x,y):
        top_y = (S/2-D) + D/2
        top_x = 0
        
        bottom_y = -1 * top_y
        bottom_x = 0
        
        left_y = 0
        left_x = -1 * top_y
        
        right_y = 0
        right_x = top_y
        
        petal_centres = ((top_x, top_y), (bottom_x, bottom_y), (left_x, left_y), (right_x, right_y))
        
        for a, b in petal_centres:
            inside_petal = (x-a)**2 + (y-b)**2 <= (D/2)**2
            outside_centre = (x)**2 + (y)**2 > (C/2)**2
            if inside_petal and outside_centre:
              return True
        
    n = 10000
    m = 0
    
    for i in range(n):
        x = uniform(-S/2, S/2)
        y = uniform(-S/2, S/2)
    
        if inside_pink_area(x, y):
            m += 1
            
    pink_area = (m / n) * S**2
    
    return pink_area
