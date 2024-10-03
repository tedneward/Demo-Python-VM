import gc
import sys
from swampy.Lumpy import Lumpy

def dump_garbage(dumpeach=True):
    """
    show us what's the garbage about
    """
    # force collection
    print("\nGARBAGE:")
    gc.collect()

    if dumpeach:
        print("\nGARBAGE OBJECTS:")
        for x in gc.garbage:
            s = str(x)
            if len(s) > 80: s = s[:80]
            print(type(x),"\n  ", s)

gc.enable()
gc.set_debug(gc.DEBUG_LEAK)

class Person:
    def __init__(self, firstName : str, lastName : str, age : int):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        self.parents = None
        self.spouse = None
        self.children = []

    def __repr__(self):
        rstr = f"{self.firstName} {self.lastName} (Age {self.age})"
        if self.parents != None:
            rstr += f" born to {self.parents[0]} and {self.parents[1]}"
        if len(self.children) > 0:
            rstr += f" parent to "
            for child in self.children:
                rstr += f"{child.firstName} "

    #def __del__(self):
    #    print(f"Farewell, {self.firstName}!")

def create_family():
    #lumpy = Lumpy()
    #lumpy.make_reference()

    # When this man met this lady
    ted = Person("Ted", "Neward", 53)
    char = Person("Charlotte", "Neward", 39)
    
    # They got married
    ted.spouse = char
    char.spouse = ted

    # And had some kids
    mike = Person("Michael", "Neward", 30)
    mike.parents = [ted, char]
    ted.children.append(mike)
    char.children.append(mike)

    matt = Person("Matthew", "Neward", 25)
    matt.parents = [ted, char]
    ted.children.append(matt)
    char.children.append(matt)

    #lumpy.object_diagram()

    return (ted, char, mike, matt)

print("==================> Created family")
family = create_family()
dump_garbage()

print("==================> family = None")
family = None
dump_garbage()
