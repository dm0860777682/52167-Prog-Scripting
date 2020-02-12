def fib(N):
    L=[]
    a=0
    b=1
    while len(L) < N:
        a = b
        b = a + b
        L.append(a)
        print(L)
    
    
    fib(10)