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

# {{## BEGIN exec-source ##}}
morecode = """
print(1 + 1)
1 + 1
"""
result = exec(morecode)
print(result)               # "None"
# {{## END exec-source ##}}

# {{## BEGIN eval-source ##}}
morecode = """
1 + 1
"""
result = eval(morecode)
print(result)               # "2"
# {{## END eval-source ##}}
