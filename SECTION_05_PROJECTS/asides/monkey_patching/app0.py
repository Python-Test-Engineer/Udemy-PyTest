""" Based on https://medium.com/@cini01/how-to-patch-the-monkey-right-243898b6715a

I have extracted code and imported it into my own module. for demonstration purposes
"""

import sys
import mymodule
from pyboxen import boxen
from rich.console import Console
from itertools import dropwhile

console = Console()
globals()["mymodule"]
print("\n")

print("===== locals() =====")
console.print(locals())
print("\n")

print('===== globals()["mymodule"] =====')
console.print(globals()["mymodule"])
print("\n")

print("===== globals() =====")
console.print(globals())
print("\n")

print("===== sys.modules =====")
console.print(sys.modules)
print("\n")

print(
    boxen(
        str(mymodule.__dict__["I"]),
        title='mymodule.__dict__["I"]',
        subtitle="mymodule.__dict__['I']",
        subtitle_alignment="left",
        color="red",
        padding=1,
    )
)
print(
    boxen(
        str(mymodule.__dict__["reduce"]),
        title='mymodule.__dict__["reduce"]',
        subtitle="=== reduce ===",
        subtitle_alignment="left",
        color="green",
        padding=1,
    )
)
print(
    boxen(
        str(mymodule.__dict__["Path"]),
        title="=== Path ===",
        subtitle="=== Path ===",
        subtitle_alignment="left",
        color="blue",
        padding=1,
    )
)
my_list = (1, 2, 3, 4, 5)

output = list(mymodule.I.dropwhile(lambda x: x < 3, my_list))
print(
    boxen(
        str(output),
        title="=== dropwhile ===",
        subtitle="=== dropwhile ===",
        subtitle_alignment="left",
        color="blue",
        padding=1,
    )
)

console.print(list(mymodule.I.dropwhile(lambda x: x < 3, my_list)))
# this
setattr(
    getattr(mymodule, "I"),
    "dropwhile",
    lambda my_filter, my_list: "dropwhile replaced with patched",
)  # dropwhile needs two arguments hence f,c

# or this:
print("Patching dropwhile")
mymodule.I.__dict__["dropwhile"] = (
    lambda my_filter, my_list: "dropwhile replaced with patched"
)
output = list(mymodule.I.dropwhile(lambda x: x < 3, my_list))
print(
    boxen(
        str(output),
        title="=== patched dropwhile ===",
        subtitle="=== patched dropwhile ===",
        subtitle_alignment="left",
        color="green",
        padding=1,
    )
)
console.print(mymodule.I.dropwhile(lambda x: x < 3, my_list))

# was dropwhile replaced with patched?
# was dropwhile called with 2 arguments?


# what is blast radius?

from itertools import dropwhile

print("Reimporting dropwhile and run...")
output = list(mymodule.I.dropwhile(lambda x: x < 3, my_list))
print(
    boxen(
        str(output),
        title="=== restored dropwhile ===",
        subtitle="=== restored dropwhile ===",
        subtitle_alignment="left",
        color="green",
        padding=1,
    )
)
# console.print(list(dropwhile(lambda x: x < 3, (1, 2, 3, 4, 5))))


console.print(type(sys.modules))
# for n, m in sys.modules.items():
#     console.print((n, "==>", m))

print('mymodule.__dict__["reduce"]')
console.print(mymodule.__dict__["reduce"])
print("run...]")
console.print(mymodule.reduce(lambda acc, cur: acc + cur, [1, 2, 3, 4, 5]))
print("Patching reduce...")
setattr(mymodule, "reduce", lambda a, c: "reduce replace with patched")
print("run...]")
console.print(mymodule.reduce(lambda acc, cur: acc + cur, [1, 2, 3, 4, 5]))

from functools import reduce

console.print(
    "reverse monkeypatch -->", reduce(lambda acc, cur: acc + cur, [1, 2, 3, 4, 5])
)

# This time the import from the module cache brought back the original functionality. Why is that? It’s because the imported objects (variables, classes, functions) are not stored as references to the original module. Instead, they are directly added to the current namespace. In our example we have only modified mymodule.reduce(), but this change was not reflected back to the module cache, hence we were able to (re-)import the original reduce() function from functools in the module cache.


# So far we have patched objects that we have imported into our own module. “Is it even possible to patch the cache directly?”, you might be tempted to ask. Absolutely! Remember, it’s just a plain dictionary!

import sys
import pathlib as pl

print("Patchging Path.home()")
setattr(
    getattr(sys.modules["pathlib"], "Path"), "home", lambda: "Path changed to <new_dir>"
)
console.print(pl.Path.home())

# Summary
# sys.module is Python’s runtime module cache stored in memory
# modules are cached in sys.module, which is a mutable, plain dictionary mapping names to module objects
# importing entire modules creates references to the module cache in the local namespace
# objects of modules (variables, functions, classes) are directly added to the current namespace when imported
# local and global namespaces as well as the module cache are also just mutable plain dictionaries
