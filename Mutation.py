#what happens here is not a bug it is just a mutable variable foo in action

foo = ['hi']
print(foo)
# Output: ['hi']

bar = foo
bar += ['bye']
print(foo)
print(bar)
# Output: ['hi', 'bye']

#cause target is mutable it changes with every call of the function
def add_to(num, target=[]):
    target.append(num)
    return target

add_to(1)
# Output: [1]

add_to(2)
# Output: [1, 2]

add_to(3)
# Output: [1, 2, 3]

def add_to(element, target=None):
    if target is None:
        target = []
    target.append(element)
    return target

print(add_to(4, ["cool", 5]))
print(add_to("yupi", ["stuff", 7]))

