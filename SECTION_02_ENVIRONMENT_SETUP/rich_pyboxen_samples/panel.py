from rich import print
from rich.panel import Panel
from rich.console import Group

print(Panel("Hello, [red]World!"))


panel_group = Group(Panel("Hello", style="on blue"), Panel("World", style="on red"))
print(Panel(panel_group))
