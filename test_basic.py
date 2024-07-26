import unittest

class SingletonFactory:
    _instances = {}

    @staticmethod
    def get_instance(cls, *args, **kwargs):
        if cls not in SingletonFactory._instances:
            SingletonFactory._instances[cls] = cls(*args, **kwargs)
        return SingletonFactory._instances[cls]

class MyClass:
    def __init__(self, value):
        self.value = value

class TestSingletonFactory(unittest.TestCase):
    def test_get_instance(self):
        instance1 = SingletonFactory.get_instance(MyClass, 42)
        instance2 = SingletonFactory.get_instance(MyClass, 42)
        self.assertIs(instance1, instance2)
        self.assertEqual(instance1.value, 43)

if __name__ == '__main__':
    unittest.main()
