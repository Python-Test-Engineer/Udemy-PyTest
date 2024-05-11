# content of test_module.py

from pyboxen import boxen

from rich.console import Console

console = Console()


class TestHello:
    @classmethod
    def callme(cls):
        console.print("\tTestHello callme called!")

    def test_method1(self):
        console.print("\tTestHello::test_method1 run")

    def test_method2(self):
        console.print("\tTestHello::test_method2 run")


class TestOther:
    @classmethod
    def callme(cls):
        console.print("\tTestOther callme other called")

    def test_other(self):
        console.print("\tTestOther::test_other run")


# works with unittest as well ...
import unittest


class SomeTest(unittest.TestCase):
    @classmethod
    def callme(self):
        print("\tSomeTest callme called")

    def test_unit1(self):
        print("\tSomeTest::test_unit1 run")
