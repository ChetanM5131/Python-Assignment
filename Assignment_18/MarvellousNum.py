def ChkPrime(no1):
    l1=[]
    if no1<=1:
        return False

    for  val in range(2,no1):
        if (no1 % val ==0):
           return False
    return True