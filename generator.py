def generator_function():
    for i in range(10):
        yield i

for item in generator_function():
    print(item)

# generator version
def fibon(n):
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a + b

for x in fibon(90):
    print(x)

def fibonac(n):
    a = b = 1
    result = []
    for i in range(n):
        result.append(a)
        a, b = b, a + b
    return result

print(fibonac(100))

gen = fibon(4)
print(next(gen))


my_string = "Rosales"
my_iter = iter(my_string)
print(next(my_iter))
# Output: 'Y'

