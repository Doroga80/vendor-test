num ={1: 0, 2: 1}

def fib(n):
    if n not in num:
        num[n] = fib(n - 1) + fib(n - 2)
    return num[n]

print(fib(95))