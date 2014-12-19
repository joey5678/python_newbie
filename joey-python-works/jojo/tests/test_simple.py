import sys
try:
    import unittest2 as unittest
except ImportError:
    import unittest


class TestKey(unittest.TestCase):
    def test_key(self):
        a = ['a', 'b']
        b = ['b', 'a']
        self.assertEqual(a, b)

    @unittest.skip('Do not run this')
    def test_fail(self):
        self.fail("This should not be run")


class TestMe(unittest.TestCase):
    def setUp(self):
        self.list = [1, 2, 3]

    def test_length(self):
        self.list.append(4)
        self.assertEqual(len(self.list), 4)

    def test_has_one(self):
        self.assertEqual(len(self.list), 3)
        self.assertIn(1, self.list)

# def test_True():
#     assert True
#
#
# def test_False():
#     assert False