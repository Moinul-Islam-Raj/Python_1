def primes(minn,maxx):
    primes = [2]
    t_n = 1

    for number in range(max(2,minn),max(1,maxx)+1):
        if number == 2:continue
        isD = False
        for n in range(2,number):
            if  number-((number//n)*n) == 0:
                isD = True
        if isD == False:
            primes += [number]
            t_n+=1
    return primes,t_n



for i in range(5):
    print(primes(1,1000*i)[1])
