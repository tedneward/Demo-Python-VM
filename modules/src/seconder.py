# This is our "other" bit of Python code
def say_something():
    print("I said, SOMETHING!")
    print(f"Our module is {say_something.__module__}")

print("This is always executed, regardless of how we are loaded")

if __name__ == "__main__":
    print("We are being executed as an application")
else:
    print("Do library-relevant initialization")
