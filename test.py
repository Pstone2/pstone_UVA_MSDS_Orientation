print("hello worlld")
a = 0
b = 0

### Problem 1 ###
for i in range(10):
    if i % 3 == 0:
        a += i
    elif i % 5 == 0:
        b += i
print(a + b)




### Problem 2 ###
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

fibnum = 0
fib_total = 0
x = 0
while fibnum < 4000000:
    fibnum = fibonacci(x)
    if fibnum % 2 == 0:
        fib_total += fibnum
    x += 1
print(fib_total)

### Problem 3 ###
i = 2
y= []
prime = 600851475143
while i * i <= prime:
    if prime % i:
        i += 1
    else:
        prime //= i
        y.append(i)
if prime > 1:
    y.append(prime)
print(max(y))