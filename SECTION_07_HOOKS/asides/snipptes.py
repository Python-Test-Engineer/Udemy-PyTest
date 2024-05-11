# EX01
def pytest_generate_tests(metafunc):
    if "fixture1" in metafunc.fixturenames:
        metafunc.parametrize(
            "fixture1",
            [
                metafunc.function.__name__,
                metafunc.module.__name__,
            ],
        )
    if "fixture2" in metafunc.fixturenames:
        metafunc.parametrize("fixture2", dir(metafunc.module))


def test_foobar(fixture1, fixture2):
    assert type(fixture1) == type(fixture2)


# check out https://github.com/dillonm197/pytest.percent

# EX02


# A pytest hook to for modifying collected items
def pytest_collection_modifyitems(items, config):
    # we can sort order of items (tests) as needed
    # can ber used to sort by fixtures used if one is say expensive in time
    # items.sort(key=lambda item: "expensive" in item.fixturenames)
    random.shuffle(items)
    output = ""
    for test in items:
        # print(f"Item: {item.nodeid}")
        keywords = [str(x) for x in test.keywords]
        all_keywords = ("|").join(keywords)
        output += f"TEST: {test.nodeid} \n\tKEYWORDS: {all_keywords}\n"
    print(
        boxen(
            output,
            title="Sorted order of tests randomly",
            subtitle="Sorted order of tests randomly",
            subtitle_alignment="left",
            color="green",
            padding=1,
        )
    )


def pytest_generate_tests(metafunc):
    metafunc.parametrize("y", [2])
    metafunc.parametrize("x", [1, 2], indirect=True)


def pytest_funcarg__x(request):
    return request.param * 10


def pytest_funcarg__y(request):
    return request.param


def test_simple(x, y):
    assert x in (10, 20)
    assert y == 2


result = testdir.runpytest("-v")
result.stdout.fnmatch_lines(
    [
        "*test_simple*1-2*",
        "*test_simple*2-2*",
        "*2 passed*",
    ]
)
# Change the test name
# Sometimes you want to change how the tests are shown so you can understand better what the test is doing. You can use the ids argument to pytest.mark.parametrize.
# https://lyz-code.github.io/blue-book/coding/python/pytest_parametrized_testing/

tasks_to_try = (
    Task("sleep", done=True),
    Task("wake", "brian"),
    Task("wake", "brian"),
    Task("breathe", "BRIAN", True),
    Task("exercise", "BrIaN", False),
)

task_ids = [f"Task({task.summary}, {task.owner}, {task.done})" for task in tasks_to_try]


@pytest.mark.parametrize("task", tasks_to_try, ids=task_ids)
def test_add_4(task):
    task_id = tasks.add(task)
    t_from_db = tasks.get(task_id)
    assert equivalent(t_from_db, task)


# pytest -v test_func.py::test_add_4
# ===================== test session starts ======================
# collected 5 items

# test_add_variety.py::test_add_4[Task(sleep,None,True)] PASSED
# test_add_variety.py::test_add_4[Task(wake,brian,False)0] PASSED
# test_add_variety.py::test_add_4[Task(wake,brian,False)1] PASSED
# test_add_variety.py::test_add_4[Task(breathe,BRIAN,True)] PASSED
# test_add_variety.py::test_add_4[Task(exercise,BrIaN,False)] PASSED

# =================== 5 passed in 0.04 seconds ===================


# https://github.com/adiralashiva8/pytest-email
