def add(value1, value2):
    return value1 + value2

result = add(3, 5)
print(result)
# Output: 8

# first without the global variable
def add(value1, value2):
    result = value1 + value2

add(2, 4)
print(result)

# Oh crap, we encountered an exception. Why is it so?
# the python interpreter is telling us that we do not
# have any variable with the name of result. It is so
# because the result variable is only accessible inside
# the function in which it is created if it is not global.

# Now lets run the same code but after making the result
# variable global
def add(value1, value2):
    global result
    result = value1 + value2

add(2, 4)
print(result)





n = int(input('Give n ='))


def code_fkt(n):
    f = 1
    count = 0
    for j in range(1, 2 ** n):

        if f > 2**n:

            break
        f = f*2

        for k in range(1, n+1):
            count = count + 1
        print(count)
    return count


print('No of times ' + str(code_fkt(n)))


#2. Multiple return values, but better not with global keyword

def profile():
    global name
    global age
    name = "Danny"
    age = 30

profile()
print(name)
# Output: Danny

print(age)
# Output: 30

#giving funcs with indexes works nice
def profile():
    name = "Danny"
    age = 30
    return (name, age)

profile_data = profile()
print(profile_data[0])
# Output: Danny

print(profile_data[1])
# Output: 30

#finally we can also use the conventional method

def profile():
    name = "Danny"
    age = 30
    return name, age

profile_name, profile_age = profile()
print(profile_name)
# Output: Danny
print(profile_age)
# Output: 30