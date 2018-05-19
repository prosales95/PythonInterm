# 1. they are data consumers
def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

    for i in fib():
        print(i)


# 2. first was data generator, now a coroutine
def grep(pattern):
    print("Searching for", pattern)
    while True:
        line = (yield)
        if pattern in line:
            print(line)


# 3. we supply them valsa using send meth
search = grep('coroutine')
next(search)
# Output: Searching for coroutine
search.send("I love you")
search.send("Don't you love me?")
search.send("I love coroutines instead!")

# Output: I love coroutines instead!

# 4. how to close them
search = grep('coroutine')
# ...
search.close()
