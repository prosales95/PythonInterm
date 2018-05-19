# 1. Everything in Python is object

def hi(name="yasoob"):
    return "hi " + name


print(hi())
# output: 'hi yasoob'

# We can even assign a function to a variable like
greet = hi
# We are not using parentheses here because we are not calling the function hi
# instead we are just putting it into the greet variable. Let's try to run this

print(greet())
# output: 'hi yasoob'
# greet with () cause it implies we are calling a function

# Let's see what happens if we delete the old hi function!

print(hi())
# outputs: NameError

print(greet())
# outputs: 'hi yasoob'

print("--------------------")


# 2. Defining functions within functions
def hi(name="yasoob"):
    print("now you are inside the hi() function")

    def greet():
        return "now you are in the greet() function"

    def welcome():
        return "now you are in the welcome() function"

    print(greet())
    print(welcome())
    print("now you are back in the hi() function")


hi()
# output:now you are inside the hi() function
#       now you are in the greet() function
#       now you are in the welcome() function
#       now you are back in the hi() function

# This shows that whenever you call hi(), greet() and welcome()
# are also called. However the greet() and welcome() functions
# are not available outside the hi() function e.g:

greet()
# outputs: NameError: name 'greet' is not defined

print("--------------------------")
print("#3. Return func form within functs")


def hi(name="yasoob"):
    def greet():
        return "now you are in the greet() function"

    def welcome():
        return "now you are in the welcome() function"

    if name == "yasoob":
        return greet
    else:
        return welcome


a = hi()
b = hi(name="pablo")
print(a)
# outputs: <function greet at 0x7f2143c01500>
print(b)
print(b())
# This clearly shows that `a` now points to the greet() function in hi()
# Now try this

print(a())
# outputs: now you are in the greet() function

print("_________________________")

print(" 4 . Giving func as arg from other func")


def hi():
    return "hi yasoob!"


def doSomethingBeforeHi(func):
    print("I am doing some boring work before executing hi()")
    print(func())


doSomethingBeforeHi(hi)
# outputs:I am doing some boring work before executing hi()
#        hi yasoob!

print("-------------------------")
print("5. First decorator")


def a_new_decorator(a_func):
    def wrapTheFunction():
        print("I am doing some boring work before executing a_func()")

        a_func()

        print("I am doing some boring work after executing a_func()")

    return wrapTheFunction


def a_function_requiring_decoration():
    print("I am the function which needs some decoration to remove my foul smell")


a_function_requiring_decoration()
# outputs: "I am the function which needs some decoration to remove my foul smell"

a_function_requiring_decoration = a_new_decorator(a_function_requiring_decoration)
# now a_function_requiring_decoration is wrapped by wrapTheFunction()

a_function_requiring_decoration()


# outputs:I am doing some boring work before executing a_func()
#        I am the function which needs some decoration to remove my foul smell
#        I am doing some boring work after executing a_func()

@a_new_decorator
def a_function_requiring_decoration():
    """Hey you! Decorate me!"""
    print("I am the function which needs some decoration to "
          "remove my foul smell")


a_function_requiring_decoration()
# outputs: I am doing some boring work before executing a_func()
#         I am the function which needs some decoration to remove my foul smell
#         I am doing some boring work after executing a_func()

# the @a_new_decorator is just a short way of saying:
a_function_requiring_decoration = a_new_decorator(a_function_requiring_decoration)

from functools import wraps


def a_new_decorator(a_func):
    @wraps(a_func)
    def wrapTheFunction():
        print("I am doing some boring work before executing a_func()")
        a_func()
        print("I am doing some boring work after executing a_func()")

    return wrapTheFunction


@a_new_decorator
def a_function_requiring_decoration():
    """Hey yo! Decorate me!"""
    print("I am the function which needs some decoration to "
          "remove my foul smell")


print(a_function_requiring_decoration.__name__)
# Output: a_function_requiring_decoration

def decorator_name(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not can_run:
            return "Function will not run"
        return f(*args, **kwargs)
    return decorated

@decorator_name
def func():
    return("Function is running")

can_run = True
print(func())
# Output: Function is running

can_run = False
print(func())
# Output: Function will not run

def logit(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        print(func.__name__ + " was called")
        return func(*args, **kwargs)
    return with_logging

@logit
def addition_func(x):
   """Do some math."""
   return x + x


result = addition_func(4)
# Output: addition_func was called

