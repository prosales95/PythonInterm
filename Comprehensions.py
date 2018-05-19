print('List comprehension Examples with multiples of 3 until 30')
multiples = [i for i in range(30) if i % 3 == 0]
print(multiples)

print('Awesome the same applies for divisors if we just remember that range is')
print('only considering from 1 until n-1, then we have to adjust limits')

n = int(input('Divisors of n = '))


def divisors(n):
    divisors = [j for j in range(1, n + 1) if n % j == 0]
    print(divisors)


print('divisors of n are')
print(divisors(n))
# Output: [0, 3, 6, 9, 12, 15, 18, 21, 24, 27]

# normal option with 3 lines
squared = []
for x in range(10):
    squared.append(x ** 2)

# better opt with compreh
squared = [x ** 2 for x in range(10)]
print(squared)

# 2. dict compr
mcase = {'a': 10, 'b': 34, 'A': 7, 'Z': 3, 'd': 32, 'D': 3}

mcase_frequency = {
    k.lower(): mcase.get(k.lower(), 0) + mcase.get(k.upper(), 0)
    for k in mcase.keys()
}

print(mcase_frequency)
# mcase_frequency == {'a': 17, 'z': 3, 'b': 34}

# 3. set compr
squared = {x ** 2 for x in range(n + 1)}
print('the square numbers until then are :')
print(sorted(squared))
# Output: {1, 4}

# great! even better if we use sorted cause if not they are all over the place
