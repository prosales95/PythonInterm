#we define the construct of our func without slots with init

class MyClass(object):
    def __init__(self, name, identifier):
        self.name = name
        self.identifier = identifier
        self.set_up()
    # ...


#using slots func we give it the attributes of our class. This overrides attr of our obj
#this gives us a reduct 50% of our RAM
class MyClass(object):
    __slots__ = ['name', 'identifier']
    def __init__(self, name, identifier):
        self.name = name
        self.identifier = identifier
        self.set_up()
    # ...

#the ide pypy makes all these optioizations automat