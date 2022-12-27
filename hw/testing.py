import unittest, time
from fibonacci import fibonacci


class TEST(unittest.TestCase):
    def test1(self):
        self.assertEqual(list(fibonacci(5)), [1, 1, 2, 3, 5])

    def test2(self):
        with self.assertRaises(ValueError):
            list(fibonacci(-1))

    def test3(self):
        start_time = time.time()
        fibonacci(10000)
        self.assertLess(time.time() - start_time, 1)


if __name__ == "__main__":
    unittest.main()
