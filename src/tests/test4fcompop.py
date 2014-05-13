import fcompop
import unittest


class TestFunctor(unittest.TestCase):
    def test_rshift(self):
        def mul2(x):
            return x * 2
        func = str._ >> mul2 >> str.upper
        self.assertEqual(func(123), str.upper(mul2(str(123))))
        func = str.upper._ >> mul2
        self.assertEqual(func('abc'), mul2(str.upper('abc')))
        func = (lambda x: -x)._ >> mul2 >> str
        self.assertEqual(func(10), str(mul2(-10)))

    def test_lshift(self):
        def mul2(x):
            return x * 2
        func = str.upper._ << mul2 << str
        self.assertEqual(func(123), str.upper(mul2(str(123))))
        func = mul2._ << str.upper
        self.assertEqual(func('abc'), mul2(str.upper('abc')))
        func = str._ << mul2 << (lambda x: -x)
        self.assertEqual(func(10), str(mul2(-10)))

if __name__ == '__main__':
    unittest.main()
