import gc
import sys
from swampy.Lumpy import Lumpy

def dump_garbage(dumpeach=True):
    """
    show us what's the garbage about
    """
    # force collection
    unreachable = gc.collect()
    print("\nGARBAGE:",unreachable)

    if dumpeach:
        print("\nGARBAGE OBJECTS:")
        for x in gc.garbage:
            s = str(x)
            if len(s) > 80: s = s[:80]
            print(type(x),": '", s, "'")

    print("This concludes the garbage dump")

gc.enable()
gc.set_debug(gc.DEBUG_UNCOLLECTABLE)

# make a leak
print("==================> Created leak")
l = []
l.append(l)
print(sys.getrefcount(l))
dump_garbage()
del l

# show the dirt ;-)
dump_garbage()
