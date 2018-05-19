print('Lambda has blueprint lambda argument: manipulate(argument) ')

add = lambda x, y: x + y

print(add(3, 5))
# Output: 8

print('Useful when sorting e.g for spec value in a list')
a = [(1, 2), (4, 1), (9, 10), (13, -3)]
a.sort(key=lambda x: x[1])

print(a)
# Output: [(13, -3), (4, 1), (1, 2), (9, 10)]

n = int(input('Give me n ='))

list1 = [x for x in range(n) if x % 2 == 0]
list2 = [y for y in range(1, n+1) if n % y == 0]
print(list1)
print(list2)

data = list(zip(list1, list2))

data.sort()
list1, list2 = map(lambda t: list(t), zip(*data))
print(list1)
print(list2)
