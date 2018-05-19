#1. Basic using of for loop

fruits = ['apple', 'banana', 'mango']
for fruit in fruits:
    print(fruit.capitalize())

# Output: Apple
#         Banana
#         Mango

#2.For with a flag
m = int(input('Give n '))
def operation(n):
    for n in range(2, m):
        for x in range(2, n):
            if n % x == 0:
                print(n, 'equals', x, '*', n/x)
                break

print(operation(m))

#3. To look for prime numbers
m = int(input('Give m '))
def prime(n):

    for n in range(2, m):
        for x in range(2, n):
            if n % x == 0:
                print(n, 'equals', x, '*', n/x)
                break
        else:
            # loop fell through without finding a factor
            print(n, 'is a prime number')
print(prime(m))
