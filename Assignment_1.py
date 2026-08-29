#Q1
def rootsCharacter(a,b,c):
    discriminant = b**2 - 4 * a * c
#    if discriminant < 0:       discriminant always > 0 
#        return None
    discriminant = 0.0 if abs(discriminant) < 1e-12 else discriminant  # floating pt error
    x1 = (-b + discriminant**0.5) / (2 * a)
    x2 = (-b - discriminant**0.5) / (2 * a)
    return 1 if (x1 > 0 and x2 > 0) else (-1 if (x1 < 0 and x2 < 0) else 0)
#Q2
from math import *
def areaPoly(n,d):
    apothem = d / (2 * tan(pi / n))
    perimeter = n * d
    return (perimeter * apothem) / 2

def polySide(n,area):
    return sqrt((4 * area * tan(pi / n)) / n)

#Q3
from math import pi
def find_circumcircle_area(sq_side):
    return (pi * sq_side * sq_side) / 2
    
# r = (dsqrt(2))/2
# area = pi * r * r
# area = (pi*sq_side*sq_side)/2

#Q4
def power_sum(p,a,b):
    return (a**p) if a == b else (a**p) + power_sum(p, a + 1, b)

def power_big_sum(p,a,b):
    return a**p if a == b else power_big_sum(p, a, (a + b) // 2) + power_big_sum(p, ((a + b) // 2) + 1, b)  # base case: a**p, divide and conquer with mid point= a+b//'2' O(logN) space complexity 
                                                                                            
                
    

                                                                                            
                
    

