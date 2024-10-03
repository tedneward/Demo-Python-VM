#!/usr/bin/env python3

from pprint import pprint

# {{## BEGIN example_1 ##}}
class Base:
    """A base class."""
    base_count = 0

    def __init__(self, color):
        Base.base_count += 1
        self.color = color

    def doSomething(self):
        print(f"I'm a Base and I am {self.color}")

    @classmethod
    def printCount(cls):
        print(Base.base_count)
# {{## END example_1 ##}}

# {{## BEGIN example_2 ##}}
class Derived(Base):
    """A derived class."""
    derived_count = 0

    def __init__(self, color, sound):
        super().__init__(color)
        Derived.derived_count += 1
        self.sound = sound

    def doSomething(self):
        Base.doSomething(self)
        print(f"I'm a Derived and I say {self.sound}")

    @classmethod
    def printCount(cls):
        print(Derived.base_count)
# {{## END example_2 ##}}

b = Base("White")
d = Derived("Brown", "Bark bark")

print(f"b documentation: {b.__doc__}")

print("b.__dict__:")
pprint(b.__dict__)
print("Base.__dict__")
pprint(Base.__dict__)
