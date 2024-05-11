import pytest

from rich.console import Console

console = Console()


@pytest.fixture(scope="session", autouse=True)
def callattr_ahead_of_all_tests(request):
    print("\n\ncallattr_ahead_of_all_tests called\n")
    seen = {
        None
    }  # needed to prevent AttributeError: 'dict' object has no attribute 'add'
    session = request.node
    for item in session.items:
        cls = item.getparent(pytest.Class)
        if cls not in seen:
            if hasattr(cls.obj, "callme"):
                cls.obj.callme()
            seen.add(cls)
        # we will print the dir of the item - there are 4 tests so we might skip 3 for clarity
        # nodeid,name,location,own_markers etc
        # console.print(dir(item))
        console.print("item.location", item.location)
