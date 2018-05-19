from collections import *
import json
from enum import *

# 1. defaultdict in action

colours = (
    ('Yasoob', 'Yellow'),
    ('Ali', 'Blue'),
    ('Arham', 'Green'),
    ('Ali', 'Black'),
    ('Yasoob', 'Red'),
    ('Ahmed', 'Silver'),
)

favourite_colours = defaultdict(list)

for name, colour in colours:
    favourite_colours[name].append(colour)

print(favourite_colours)

# output
# defaultdict(<type 'list'>,
#    {'Arham': ['Green'],
#     'Yasoob': ['Yellow', 'Red'],
#     'Ahmed': ['Silver'],
#     'Ali': ['Blue', 'Black']
# })

#some_dict = {}
#some_dict['colours']['favourite'] = "yellow"
# Raises KeyError: 'colours'

#instead use
import collections
tree = lambda: collections.defaultdict(tree)
some_dict = tree()
some_dict['colours']['favourite'] = "yellow"
# Works fine

print(json.dumps(some_dict))
# Output: {"colours": {"favourite": "yellow"}}

# 2. OrdererdDict in action

colours =  {"Red" : 198, "Green" : 170, "Blue" : 160}
for key, value in colours.items():
    print(key, value)
# Output:
#   Green 170
#   Blue 160
#   Red 198
# Entries are retrieved in an unpredictable order


#now with orderedDict much more organized

colours = OrderedDict([("Red", 198), ("Green", 170), ("Blue", 160)])
for key, value in colours.items():
    print(key, value)
# Output:
#   Red 198
#   Green 170
#   Blue 160
# Insertion order is preserved

#3 .Counter in action


colours = (
    ('Yasoob', 'Yellow'),
    ('Ali', 'Blue'),
    ('Arham', 'Green'),
    ('Ali', 'Black'),
    ('Yasoob', 'Red'),
    ('Ahmed', 'Silver'),
)

favs = Counter(name for name, colour in colours)
print(favs)
# Output: Counter({
#    'Yasoob': 2,
#    'Ali': 2,
#    'Arham': 1,
#    'Ahmed': 1
# })

#with file opener we can count too. It works it counted my lines
with open('C:/Users/Anwender/PycharmProjects/PythonInterm/Test', 'rb') as f:
    line_count = Counter(f)
print(line_count)

#The deque double queue to access either side


d = deque()
d.append('1')
d.append('2')
d.append('3')

print(len(d))
# Output: 3

print(d[0])
# Output: '1'

print(d[-1])
# Output: '3'

#see how popping from both sides is possible therefore removing the elem from each side
print("Lets get it on with deque")

e = deque(range(5))
print(len(e))
# Output: 5

print(e.popleft())
# Output: 0

print(e.pop())
# Output: 4

print(e)
# Output: deque([1, 2, 3])

#new deque with max length 30

f = deque(maxlen=30)

f = deque([1,2,3,4,5])
f.extendleft([0])
f.extend([6,7,8])
print(f)
# Output: deque([0, 1, 2, 3, 4, 5, 6, 7, 8])


#5. NamedTuples are like lists but cant be reassigned with an item.
man = ('Ali', 30)
print(man[0])
# Output: Ali

#with namedtuples we access data with their keys defined before

Animal = namedtuple('Animal', 'name age type')
perry = Animal(name="perry", age=31, type="cat")

print(perry)
# Output: Animal(name='perry', age=31, type='cat')

print(perry.name)
# Output: 'perry'

#we can convert namedTuple into dictionary with
Animal = namedtuple('Animal', 'name age type')
perry = Animal(name="Perry", age=31, type="cat")
print(perry._asdict())
# Output: OrderedDict([('name', 'Perry'), ('age', 31), ...

#6. enum to avoid user syntax mistakes with strings

class Species(Enum):
    feline = 1
    canine = 2
    horse = 3
    aardvark = 4
    butterfly = 5
    owl = 6
    platypus = 7
    dragon = 8
    unicorn = 9
    # The list goes on and on...

    # But we don't really care about age, so we can use an alias.
    kitten = 1
    cat =1
    puppy = 2
    dog= 2
#works great cause look cat =kitten=1 and dog = puppy=2. therefore its an alias

Animal = namedtuple('Animal', 'name age type')
perry = Animal(name="Perry", age=31, type=Species.cat)
drogon = Animal(name="Drogon", age=4, type=Species.dragon)
tom = Animal(name="Tom", age=75, type=Species.cat)
charlie = Animal(name="Charlie", age=2, type=Species.kitten)

# And now, some tests.
print(charlie.type == tom.type)

print(charlie.type)


print("test different ways to fetch data from enum class")
print(Species(1))
print(Species['cat'])
print(Species.cat)