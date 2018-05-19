import inspect

my_list = [1, 2, 3]
print('list methods')
print(dir(my_list))


print('dict methods')
my_dict = dict({'Name': 'Pablo', 'Age':22, 'Dick Size': 16, 'Destiny': 'success'})
print(dir(my_dict))
# Output: ['__add__', '__class__', '__contains__', '__delattr__', '__delitem__',
# '__delslice__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
# '__getitem__', '__getslice__', '__gt__', '__hash__', '__iadd__', '__imul__',
# '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__',
# '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__',
# '__setattr__', '__setitem__', '__setslice__', '__sizeof__', '__str__',
# '__subclasshook__', 'append', 'count', 'extend', 'index', 'insert', 'pop',
# 'remove', 'reverse', 'sort']

#we can also print the types of our obj really easy. it shows us a class
print(type(''))
# Output: <type 'str'>

print(type([]))
# Output: <type 'list'>

print(type({}))
# Output: <type 'dict'>

print(type(dict))
# Output: <type 'type'>

print(type(3))
# Output: <type 'int'>

#3. inspect module
print('members of str shown by inspect func module')
print(inspect.getmembers(str))
# Output: [('__add__', <slot wrapper '__add__' of ... ...