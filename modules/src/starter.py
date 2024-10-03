import sys

# This is a single-file Python script
def main():
    print("Hello world")
    print(f"Our module is {main.__module__}")
    print(f"Our module name is {__name__}")

    #print(f"sys.modules = {sys.modules}")
    if "seconder" in sys.modules.keys(): print("seconder already loaded!")
    else: print("Nope, no seconder")

    from seconder import say_something
    say_something()

    #print(f"sys.modules = {sys.modules}")
    if "seconder" in sys.modules.keys(): print("seconder already loaded!")
    else: print("Nope, no seconder")

    import seconder
    say_something()


if __name__ == "__main__":
    main()

