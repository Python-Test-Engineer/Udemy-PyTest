for the stash kew we need the conftest.py in folder

when in root it did not work as Item was out of scope.

prints it out for every test result so need to filter with:
```
if "stash" in item.nodeid:
   # print...
```