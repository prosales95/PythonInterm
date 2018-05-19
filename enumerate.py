
#as we can see the counter adds 1 by default and value is the elem in list being iterated
my_list = ['apple', 'banana', 'grapes', 'pear']
for counter, value in enumerate(my_list, 1):
    print(counter, value)


# Output:
# 1 apple
# 2 banana
# 3 grapes
# 4 pear

my_list = ['china', 'us', 'russia', 'europe', 'japan']
counter_list = list(enumerate(my_list, 1))
print(counter_list)
# Output: [(1, 'apple'), (2, 'banana'), (3, 'grapes'), (4, 'pear')]