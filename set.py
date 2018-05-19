#without set
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = []
for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)

#second if is cause our duplicates list is empty at the beginning and we cant have twice the same duplicate


print(duplicates)
# Output: ['b', 'n']

some_list = ['b', 'b', 'c', 'c', 'd', 'm', 'n', 'n', 'h', 'h']
duplicates = set([x for x in some_list if some_list.count(x) > 1])
print(duplicates)

valid = set(['yellow', 'red', 'blue', 'green', 'black'])
input_set = set(['red', 'brown'])
print(input_set.difference(valid))
# Output: set(['brown'])

a_set = {'red', 'blue', 'green'}
print(type(a_set))
# Output: <type 'set'>