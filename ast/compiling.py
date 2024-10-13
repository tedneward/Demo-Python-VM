#! /usr/bin/env python3

# {{## BEGIN compile ##}}
code = """
print("Hello, Python!")
class Message:
    def __init__(self, body):
        self.body = body
    def print(self):
        print(f"This is a message from {self.body}")
msg = Message("dynamic code")
msg.print()
"""

comp_result = compile(code, "<string>", "exec")
# {{## END compile ##}}

# {{## BEGIN run-compile ##}}
print(comp_result)
#comp_result()  # TypeError: 'code' object is not callable
exec(comp_result)
# {{## END run-compile ##}}

# {{## BEGIN exec ##}}

# {{## END exec ##}}
