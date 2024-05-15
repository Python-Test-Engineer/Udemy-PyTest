

### What does item.keywords give us?

```
  for test in items:
        all_keywords = [str(x) for x in test.keywords]
        all_keywords = (" - ").join(all_keywords)

        output = f"Test: {test.nodeid} \nKeywords: {all_keywords}"
        # keyword order is
        # test name - markers - module name - folder - parent folder/grandparent folder - root folder
```

When we run the above we see that we get:

Test: 

tests/tests_ex02_add_custom_markers/test_add_custom_markers.py 
::test_interface_complex  

Keywords: 

test_interface_complex - complex_marker - test_add_custom_markers.py - tests_ex02_add_custom_markers - tests - PyTest_07_HOOKS -  

Thus we get:

- test name: test_interface_complex
- markers: complex_marker
- file_name: test_add_custom_markers.py 
- parent folder:  tests_ex02_add_custom_markers 
- grandparent folder: tests and so on up to...
- root folder: PyTest_07_HOOKS

We can thus order tests by any of these keywords if we want. We can split the node and get the chose 'bit' and then do a sort based on that key.

https://docs.python.org/3/howto/sorting.html#key-functions