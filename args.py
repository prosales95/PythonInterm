

def test_lot_args(f_arg, *argv):
    print("first normal arg:", f_arg)
    for arg in argv:
        print("another arg through *argv:", arg)

test_lot_args('yasoob', 'python', 'eggs', 'test')

def greet_me(**kvars):
    for key, value in kvars.items():
        print("{0} is awesome in {1}".format(key, value))

greet_me(face= "pablo")

def test_var_vars(var1, var2, var3):
    print("arg1:", var1)
    print("arg2:", var2)
    print("arg3:", var3)

vars = ("cool",6,7)
kvars = {"var2": 4, "var3": "nice", "var1":2}

test_var_vars(*vars)
test_var_vars(**kvars)

