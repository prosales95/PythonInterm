# 1. simplest contman is the with statement
with open('some_file', 'w') as opened_file:
    opened_file.write('Hola!')

    # 2. equivalent 1 to 1 to
file = open('some_file', 'w')
try:
    file.write('Hola!')
finally:
    file.close()


# 3. now showing contman as a class

class File(object):
    def __init__(self, file_name, method):
        self.file_obj = open(file_name, method)

    def __enter__(self):
        return self.file_obj

    def __exit__(self, type, value, traceback):
        self.file_obj.close()


with File('demo.txt', 'w') as opened_file:
    opened_file.write('Hola!')


# 4. Handling except in exit meth


class File(object):
    def __init__(self, file_name, method):
        self.file_obj = open(file_name, method)

    def __enter__(self):
        return self.file_obj

    def __exit__(self, type, value, traceback):
        print("Exception has been handled")
        self.file_obj.close()
        return True


with File('demo.txt', 'w') as opened_file:
    opened_file.undefined_function()

# Output: Exception has been handled

# 5. Implement as a generator

from contextlib import contextmanager


@contextmanager
def open_file(name):
    f = open(name, 'w')
    yield f
    f.close()


with open_file('some_file') as f:
    f.write('hola!')
