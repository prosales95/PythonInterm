fat = True
fitness = ("skinny", "fat")[fat]
print("Ali is ", fitness)
# Output: Ali is fat

condition = True
print(2 if condition else 1/0)
#Output is 2

print((1/0, 2)[condition])
#ZeroDivisionError is raised