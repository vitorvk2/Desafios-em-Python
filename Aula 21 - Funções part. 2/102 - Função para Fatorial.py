def fact(n, show=False):
    for i in range(1,n):
        n *= i
        if show == True:
            print(i,end=' ')

    return n
    



print(fact(5))