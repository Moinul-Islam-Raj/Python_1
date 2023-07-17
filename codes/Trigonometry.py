import math
def sin(t, isRad=True):
    x = get_two_pi_range(t, isRad)
    result = 0
    for n in range(0,23):
        result += ((-1)**n)*(x**(2*n+1))/(fac(2*n+1))
    return result
def cos(t, isRad=True): 
    x = get_two_pi_range(t, isRad)
    result = 0
    for n in range(0,23):
        result += ((-1)**n)*(x**(2*n))/(fac(2*n)) #cos(x) = sum_n=0_infinity d^n/dx^n(cosx) * x^(2n)/(2n)! = sum_n=0_infinity (-1)^n * x^(2n)/(2n)!
    return result

def tan(t, isRad=True): #sin/cos
    sint = float(f"{sin(t, isRad):.15f}")
    cost = float(f"{cos(t, isRad):.15f}")
    if sint == 0:return 0
    if cost == 0:
        print("---------undefined--------")
        return 0
    return sint/cost
def cot(t, isRad=True): #1/tan = cos/sin
    sint = float(f"{sin(t, isRad):.15f}")
    cost = float(f"{cos(t, isRad):.15f}")
    if cost == 0:return 0
    if sint == 0:
        print("---------undefined--------")
        return 0
    return cost/sint
def sec(t, isRad=True): #1/cos
    cost = float(f"{cos(t, isRad):.15f}")
    if not cost == 0: return 1/cost
    print("--------undefined--------")
    return 0
def csc(t, isRad=True): #1/sin
    sint = float(f"{sin(t, isRad):.15f}")
    if not sint == 0: return 1/sint
    print("-------undefined--------")
    return 0
def fac(n):  # n! = n(n-1)!
    if n <= 1: return 1
    return n*fac(n-1)
def get_two_pi_range(t, isTRad): # sin(4pi) = sin(0) and sin(370 deg) = sin(10 deg) for all trig functions. It is useful for taylor series.
    if not isTRad: # is it deg or rad
        if t>360 or t<-360:
            return (t/360 - t//360)*2*math.pi
        return t*math.pi/180 # 1 rad = 1 deg * pi rad/180 deg
    
    if t > 2*math.pi or t < -2*math.pi:
        return (t/(2*math.pi) - t//(2*math.pi))*2*math.pi
    return t
# print("cos",cos(67.3, False))
# print()
# print("sin",sin(179.99, False))
# print()
# print("tan",tan(90.01, False))
# print()
# print("1/sin=csc",csc(34, False))
# print()
# print("1/cos=sec",sec(89.99999, False))
# print()
# print("1/tan=cot",cot(89.9999, False))