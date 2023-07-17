import math, Trigonometry as tg

#math.pi = 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679
again = True
while again:
    system_rad = True           # deg or rad
    if(not input("Radian or Degree?\n\t1)Radian\n\t2)Degree\nChoose one of the option by typing the assigned number. (default-deg)\n") == "1"):
        system_rad = False

    def sin(t):
        x = get_two_pi_range(t, system_rad)
        result = 0
        for n in range(0,23):
            result += ((-1)**n)*(x**(2*n+1))/(fac(2*n+1))
        return result
    def cos(t):
        x = get_two_pi_range(t, system_rad)
        result = 0
        for n in range(0,23):
            result += ((-1)**n)*(x**(2*n))/(fac(2*n))
        return result
    def tan(t): #sin/cos
        if float(f"{sin(t):.15f}") == 0:return 0
        if float(f"{cos(t):.15f}") == 0:
            print("---------undefined--------")
            return 0
        return sin(t)/cos(t)
    def cot(t): #1/tan = cos/sin
        if float(f"{cos(t):.15f}") == 0:return 0
        if float(f"{sin(t):.15f}") == 0:
            print("---------undefined--------")
            return 0
        return cos(t)/sin(t)
    def sec(t): #1/cos
        cost = float(f"{cos(t):.1f}")
        if not cost == 0: return 1/cost
        print("--------undefined--------")
        return 0
    def csc(t): #1/sin
        sint = float(f"{sin(t):.15f}")
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
    def get_float(s):
        try:
            result = float(input(s))
            return result
        except:
            print("Error: only number shoud be an input.")
            return get_float(s)
    def get_int(s):
        try:
            result = int(input(s))
            return result
        except:
            print("Error: only integer shoud be an input.")
            return get_float(s)
    dict_1 = {1:tg.sin,2:tg.cos,3:tg.tan,4:tg.csc,5:tg.sec,6:tg.cot} #function options
    while True: # choose function
        func = get_int("Choose a function: \n\t1)sin\t4)csc\n\t2)cos\t5)sec\n\t3)tan\t6)cot\n")
        if func >0 and func < 7: break
        print("1-6 only")

    theta = get_float("Enter angel:\n") # get angel, theta 

    print(f"Result : {dict_1.get(func)(theta, system_rad):.10f}")

    if(input("Use again?(Y/N): ") in ["Y","y","True","1"," "]): again = True #calculate again?
    else: again =  False
    
    
