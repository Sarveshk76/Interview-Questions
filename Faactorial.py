#Using for loop

def fact(n):
    if n==0 or n==1:
        return 1
    elif n<0:
        return -1
    temp=1
    for i in range(2,n+1):
        temp *= i
    return (temp)
print(fact(-11))

#Using recursion

def fact1(n):
    if n==0 or n==1:
        return 1
    elif n<0:
        return -1
    return n * fact1(n-1)

print(fact1(5))
