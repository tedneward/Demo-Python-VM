#!/usr/bin/env python3

# Python meta-object protocol examples

import datetime

# {{## BEGIN dynamic ##}}
string = "This is a string"
print(dir(string))
number = 5
print(dir(number))
# do it on a builtin function, even!
print(dir(dir))

class FakeNumber:
    def __add__(self, other):
        return 0

fake = FakeNumber()
print(fake + 5)     # prints '5'
#print(fake - 5)    # error!
# {{## END dynamic ##}}

# {{## BEGIN functional ##}}
# The dictionary: A poor man's class ...
person = { 'first': 'Ted', 'last' : 'Neward' }
# ... as long as it can take functions as values
person["speak"] = lambda: print(person['first'] + " " + person['last'])

# ... but it works!
person["speak"]()
# {{## END functional ##}}

# {{## BEGIN type ##}}
print(type(3)) # <class 'int'>
print(type(['a', 'b', 'c'])) # <class 'list'>
print(type((1, 2, 3, 4))) # <class 'tuple'>

class Foo:
    pass
obj = Foo()

print(obj.__class__) # <class '__main__.Foo'>
print(type(obj)) # <class '__main__.Foo'>
print(obj.__class__ is type(obj)) # True
# {{## END type ##}}

# {{## BEGIN runtime-type ##}}
RFoo = type('RFoo', (), {})
obj = RFoo()
print(obj)  # <__main__.RFoo object at ...?>

RBar = type('RBar', (RFoo,), dict(scotches=100))
obj = RBar()
print(obj.scotches)  # 100
print(dir(obj))
print(obj.__class__)
print(obj.__class__.__bases__)

Person = type('Person', (), {
  'first' : 'Ted', 'last' : 'Neward', 'speak' : lambda self: self.first + " " + self.last
})
ted = Person()
print(ted.speak())
# {{## END runtime-type ##}}

# {{## BEGIN override-new ##}}
class Foo:
    pass

def new(cls):
    x = object.__new__(cls)
    x.randomAttribute = 100
    return x

Foo.__new__ = new

f = Foo()
print(f.randomAttribute) # 100
# {{## END override-new ##}}

# {{## BEGIN custom-meta ##}}
class Meta(type):
    def __new__(cls, name, bases, dct):
        x = super().__new__(cls, name, bases, dct)
        x.randomAttribute = 100
        return x

class Foo(metaclass=Meta):
    pass

print(Foo.randomAttribute) # 100
# {{## END custom-meta ##}}