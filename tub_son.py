def tub(son):
    if son>1:
        a=int(son/2)
        for i in range(2,a+1):
            if son%i==0:
                return("tub son emas")
                break
        return ("tub son")
print(tub(int(input(">>> "))))
