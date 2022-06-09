#Using for loop

def fib(n):
    a = 0
    b = 1
    if n == 1:
        print(a)
    else:
        print(a)
        print(b)
        for i in range(2,n):
            c = a + b
            a = b
            b = c
            print(c)

#Using recursion

def fib1(n):
    if (n == 0):
        return 0
    elif (n == 1):
        return 1
    else:
        return (fib1(n - 2) + fib1(n - 1))

for i in range(10):
    print(fib1(i))

