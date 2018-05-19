import inspect

print(' 1. Handling single exceptions with try-except is in this form')

try:
    file = open('C:/Users/Anwender/PycharmProjects/PythonInterm/Test', 'rb')
except IOError as e:
    print('An IOError occurred. {}'.format(e.args[-1]))


print('to handle multiple exceptions')
print('1. possibility with a tuple and multiple except inside')
try:
    file = open('C:/Users/Anwender/PycharmProjects/PythonInterm/Test', 'rb')
except (IOError, EOFError) as e:
    print("An error occurred. {}".format(e.args[-1]))

print('2. multiple except blocks')
try:
    file = open('C:/Users/Anwender/PycharmProjects/PythonInterm/Test', 'rb')
except EOFError as e:
    print("An EOF error occurred.")
    raise e
except IOError as e:
    print("An error occurred.")
    raise e

print('3. capture all general except when no idea of spec')
try:
    file = open('C:/Users/Anwender/PycharmProjects/PythonInterm/Test', 'rb')
except Exception:
    # Some logging if you want
    raise

print('The use of finally is for cleanup after except was or wasnt caught')

try:
    file = open('C:/Users/Anwender/PycharmProjects/PythonInterm/Test', 'rb')
except IOError as e:
    print('An IOError occurred. {}'.format(e.args[-1]))
finally:
    print("This would be printed whether or not an exception occurred!")

# Output: An IOError occurred. No such file or directory
# This would be printed whether or not an exception occurred!

print('try-else. Else includes if no exception occurs, here no Error is caught ')
try:
    print('I am sure no exception is going to occur!')
except Exception:
    print('exception')
else:
    # any code that should only run if no exception occurs in the try,
    # but for which exceptions should NOT be caught
    print('This would only run if no exception occurs. And an error here '
          'would NOT be caught.')
finally:
    print('This would be printed in every case.')

# Output: I am sure no exception is going to occur!
# This would only run if no exception occurs.
# This would be printed in every case.