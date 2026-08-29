#Q1
def rootsCharacter(a,b,c):
    scale = max(abs(a), abs(b), abs(c))  # scale to prevent overflow/underflow for a,b,c
    a, b, c = a/scale, b/scale, c/scale

    discriminant = b*b - 4*a*c 

    discriminant = 0.0 if abs(discriminant) < 1e-12 * max(abs(b*b), abs(4*a*c)) else discriminant  # snap positive near 0 flt point errors to 0 
    discriminant = max(0.0, discriminant) # snap negative near 0 flt point errors to 0 (assuming is always b^2-4ac > 0)

    # refactored quadratic formula to prevent cancellation of -b +/-sqrt(b^2-4ac), where b ≈ sqrt(b^2-4ac) when b^2 >> 4ac
    q =  b + (discriminant**0.5 if b >= 0 else -discriminant**0.5)  
    x1 = -q / (2 * a)
    x2 = (-2 * c / q) if q != 0 else 0.0

    return 1 if x1 > 0 and x2 > 0 else -1 if x1 < 0 and x2 < 0 else 0
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
                                                                                            
                
    

                                                                                            
                
    

